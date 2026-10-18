#!/usr/bin/env python3
"""Standalone finite cellular checks for two unordered particles on prism graphs.

The all-parameter proof is mathematical. This script exhaustively tests specified finite
rim lengths; it does not infer arbitrary cases from the tested range.
"""
from itertools import combinations

def prism(n):
    assert n >= 4
    v = range(2*n)
    E = sorted({tuple(sorted((u,w))) for u,w in
        ([(i,(i+1)%n) for i in range(n)] +
         [(n+i,n+(i+1)%n) for i in range(n)] +
         [(i,n+i) for i in range(n)])})
    ed = {e:i for i,e in enumerate(E)}
    pairV = list(combinations(v,2))
    cell1 = [(i,u) for i,(a,b) in enumerate(E) for u in v if u not in (a,b)]
    cell2 = [(i,j) for i,j in combinations(range(len(E)),2) if set(E[i]).isdisjoint(E[j])]
    return E,ed,pairV,cell1,cell2

def rank_f2(vectors):
    piv = {}
    for c in vectors:
        while c:
            k=c.bit_length()-1
            if k in piv: c ^= piv[k]
            else: piv[k]=c; break
    return len(piv)

def act(n,k,a,b,v):
    i,t=v%n,v//n
    return (k+(-i if a else i))%n + n*(t^b)

def traces(n,k,a,b,E=None,cell2=None):
    if E is None: E,_,_,_,cell2=prism(n)
    A=lambda v:act(n,k,a,b,v)
    emap={e:i for i,e in enumerate(E)}
    eperm=[]; esign=[]
    for u,v in E:
        x,y=A(u),A(v)
        eperm.append(emap[tuple(sorted((x,y)))])
        esign.append(1 if x<y else -1)
    c0=sum((A(u)==u and A(v)==v) or (A(u)==v and A(v)==u)
           for u,v in combinations(range(2*n),2))
    c1=sum(esign[i] for i,(u,v) in enumerate(E) if eperm[i]==i
           for z in range(2*n) if z not in (u,v) and A(z)==z)
    c2=0
    for i,j in cell2:
        if (eperm[i],eperm[j]) == (i,j): c2+=esign[i]*esign[j]
        elif (eperm[i],eperm[j]) == (j,i): c2-=esign[i]*esign[j]
    return c0-c1+c2, (c0,c1,c2)

def theoretical(n,k,a,b):
    q=(n if k==0 else 0) if not a else sum((k-i-1)%n==i for i in range(n))
    h1=(-1)**(a+b)*(q+2*(b==0))
    if not a:
        if k==0:p=n*(n-3)//2
        elif n%2==0 and 2*k==n:p=-n//2
        else:p=0
    elif n%2: p=(3-n)//2
    else: p=(4-n)//2
    h2=(-1)**b+p
    return h1,h2

def cycles(n,E,emap):
    def cyc(vs):
        return {emap[tuple(sorted((a,b)))]:1 if a<b else -1
                for a,b in zip(vs,vs[1:]+vs[:1])}
    return ([cyc(list(range(n))),cyc([n+i for i in range(n)])]+
            [cyc([i,(i+1)%n,n+(i+1)%n,n+i]) for i in range(n)])

def test_tori(n,E,emap,cell1,cell2):
    cid={c:i for i,c in enumerate(cell1)}
    sid={c:i for i,c in enumerate(cell2)}
    faces=cycles(n,E,emap)
    facepairs=[(0,1)]+[(i+2,j+2) for i,j in combinations(range(n),2)
                            if j-i not in (1,n-1)]
    assert len(facepairs)==1+n*(n-3)//2
    top=[emap[tuple(sorted((i,(i+1)%n)))] for i in range(n)]
    bot=[emap[tuple(sorted((n+i,n+(i+1)%n)))] for i in range(n)]
    # An identity-sized minor proves primitivity of this cycle lattice
    pivotrows=[tuple(sorted((top[0],bot[0])))]+[
        tuple(sorted((top[i-2],top[j-2]))) for i,j in facepairs[1:]]
    for k,(i,j) in enumerate(facepairs):
        z={}
        for e,x in faces[i].items():
            for f,y in faces[j].items():
                a,b=sorted((e,f))
                z[(a,b)]=z.get((a,b),0)+x*y*(1 if e<f else -1)
        assert len(z)==len(faces[i])*len(faces[j])
        assert all(z.get(p,0)==(z[p] if r==k else 0) for r,p in enumerate(pivotrows))
        assert abs(z[pivotrows[k]])==1
        boundary={}
        for (e,f),v in z.items():
            u,w=E[e]; x,y=E[f]
            for c,sgn in [((f,w),1),((f,u),-1),((e,y),-1),((e,x),1)]:
                boundary[c]=boundary.get(c,0)+v*sgn
        assert all(t==0 for t in boundary.values())
    return len(facepairs)

def main():
    # Rigorous finite enumeration against closed formulas; unlimited n handled in proof.
    for n in range(4,19):
        E,ed,C0,C1,C2=prism(n)
        for a in range(2):
            for b in range(2):
                for k in range(n):
                    L,checks=traces(n,k,a,b,E,C2)
                    h1,h2=theoretical(n,k,a,b)
                    assert L==1-h1+h2,(n,k,a,b,L,h1,h2,checks)
        if n<=10:
            nt=test_tori(n,E,ed,C1,C2)
            row={c:i for i,c in enumerate(C1)}
            vectors=[]
            for e,f in C2:
                u,v=E[e];x,y=E[f]
                bits=0
                for c in ((f,u),(f,v),(e,x),(e,y)):bits^=1<<row[c]
                vectors.append(bits)
            r=rank_f2(vectors)
            assert len(C2)-r==nt,(n,len(C2),r,nt)
            assert len(C1)-(len(C0)-1)-r==n+2
    print('VERIFY_OK_PRISM_GRAPH_TWO_PARTICLE')
    print('ALL_SYMMETRIES_N4_TO18_SIGNED_CELLULAR_LEFSCHETZ')
    print('EXACT_TORUS_BOUNDARIES_AND_UNIMODULAR_MINOR_N4_TO10')
    print('MOD2_SECOND_BOUNDARY_RANKS_N4_TO10')
    print('H1_CHAR_SIGN_TWIST_FACES H2_SIGNED_NONADJACENT_PAIRS_PLUS_CAP_SWAP')

if __name__=='__main__':main()
