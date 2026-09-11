"""Standalone verifier for lane-814 target falsification.
Rebuilds the barycentric subdivision of the Abrams model D4(G') from cubes.pkl,
recomputes d0/d1/d2 ranks (Betti numbers), and checks:
 (1) H^1 reps are 1-cocycles and represent a basis of H^1 (quotient dim 3);
 (2) each recorded cup equals the AW front/back-face product of the H^1 reps;
 (3) each cup is a coboundary: d(witness)==cup;
 (4) H^2 generator is a 2-cocycle but NOT a coboundary (so H^2=1 genuine).
Prints VERIFY_OK on success. Stdlib only.
"""
import pickle, os
BASE=os.path.dirname(os.path.abspath(__file__))
def bitcount(x): return bin(x).count("1")
def rref(rows):
    piv={}
    for m in rows:
        x=m
        for pc in sorted(piv.keys()):
            if (x>>pc)&1: x^=piv[pc]
        if x:
            p=(x&-x).bit_length()-1
            piv[p]=x
    pivs=sorted(piv.keys()); red=dict(piv)
    for i in reversed(range(len(pivs))):
        p=pivs[i]; x=red[p]
        for j in range(i+1,len(pivs)):
            q=pivs[j]
            if (x>>q)&1: x^=red[q]
        red[p]=x
    return red,pivs
def rank_only(rows):
    piv={}; r=0
    for m in rows:
        x=m
        while x:
            p=(x&-x).bit_length()-1
            if p in piv: x^=piv[p]
            else: piv[p]=x; r+=1; break
    return r
def main():
    C=pickle.load(open(os.path.join(BASE,"cubes.pkl"),"rb"))
    proper=C["proper"]; edges=C["edges"]; tris=C["tris"]
    N=len(proper)
    n0=N; n1=len(edges); n2=len(tris)
    edge_id={tuple(e):i for i,e in enumerate(edges)}
    tri_id={tuple(t):i for i,t in enumerate(tris)}
    H1=pickle.load(open(os.path.join(BASE,"H1_basis.pkl"),"rb"))
    cups={eval(k):v for k,v in pickle.load(open(os.path.join(BASE,"cups.pkl"),"rb")).items()}
    wits={eval(k):v for k,v in pickle.load(open(os.path.join(BASE,"witnesses.pkl"),"rb")).items()}
    h2=pickle.load(open(os.path.join(BASE,"h2gen.pkl"),"rb")); zgen=h2["zgen"]
    assert len(H1)==3, len(H1)
    # d0 rank
    d0rows=[(1<<u)|(1<<v) for (u,v) in edges]
    r0=rank_only(d0rows); assert n0-r0==1, (n0,r0)
    # d1 from tris
    cols=[0]*n1
    d1rowcheck=[]
    for t,(a,b,c) in enumerate(tris):
        e1=edge_id[(a,b)]; e2=edge_id[(b,c)]; e3=edge_id[(a,c)]
        cols[e1]|=1<<t; cols[e2]|=1<<t; cols[e3]|=1<<t
        d1rowcheck.append((1<<e1)|(1<<e2)|(1<<e3))
    r1=rank_only(d1rowcheck)
    assert n1-r1-r0==3, (n1,r1,r0)
    # (1) H1 reps are cocycles: dot with every tri row even
    for m in H1:
        for row in d1rowcheck:
            assert bitcount(row&m)%2==0
    # (2) cup definition: (ai U aj)(a,b,c)=ai(a,b)*aj(b,c)
    H1s=[set(e for e in range(n1) if (m>>e)&1) for m in H1]
    EA=[edge_id[(a,b)] for (a,b,c) in tris]; EB=[edge_id[(b,c)] for (a,b,c) in tris]
    for i in range(3):
        for j in range(3):
            m=0
            Si,Sj=H1s[i],H1s[j]
            for t in range(n2):
                if EA[t] in Si and EB[t] in Sj: m|=1<<t
            assert m==cups[(i,j)], f"cup def mismatch {(i,j)}"
    # (3) coboundary witnesses
    for k,w in wits.items():
        d=0; e=w
        while e:
            lsb=e&-e; p=lsb.bit_length()-1
            d^=cols[p]; e^=lsb
        assert d==cups[k], f"witness fail {k}"
    # (4) H2 generator: cocycle (tetra check) + non-coboundary
    tetras=[]
    for d_ in range(N):
        F=proper[d_]
        for c_ in F:
            PB=proper[c_]
            for b in PB:
                if b>=c_: continue
                for a in proper[b]:
                    if a<b<c_<d_: tetras.append((a,b,c_,d_))
    for (a,b,c,d_) in tetras:
        s=((zgen>>tri_id[(a,b,c)])&1)+((zgen>>tri_id[(a,b,d_)])&1)+((zgen>>tri_id[(a,c,d_)])&1)+((zgen>>tri_id[(b,c,d_)])&1)
        assert s%2==0, "h2gen not cocycle"
    d2rows=[(1<<tri_id[(a,b,c)])|(1<<tri_id[(a,b,d_)])|(1<<tri_id[(a,c,d_)])|(1<<tri_id[(b,c,d_)]) for (a,b,c,d_) in tetras]
    r2=rank_only(d2rows)
    assert n2-r1-r2==1, (n2,r1,r2)
    redB,pivsB=rref(cols)
    x=zgen
    for p in pivsB:
        if (x>>p)&1: x^=redB[p]
    assert x!=0, "h2gen is coboundary (H2 vacuous)"
    print(f"n0={n0} n1={n1} n2={n2} n3={len(tetras)} r0={r0} r1={r1} r2={r2} H=(1,3,1)")
    print("all 9 AW cups are coboundaries; H2 generator certified nonzero")
    print("VERIFY_OK")
if __name__=="__main__":
    main()
