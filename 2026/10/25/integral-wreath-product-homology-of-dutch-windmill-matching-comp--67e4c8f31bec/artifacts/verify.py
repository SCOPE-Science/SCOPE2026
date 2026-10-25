"""Independent finite checks of oriented matching homology for windmill graphs.

Uses exact fixed-orbit Lefschetz sums and mod-two simplicial boundary ranks.
"""
from itertools import permutations,product
from collections import defaultdict

def edges(n,m):
    E=[]
    for i in range(n):
        for t in range(m):
            v1=('c',) if t==0 else (i,t)
            v2=('c',) if t==m-1 else (i,t+1)
            E.append((v1,v2))
    return E

def orbit_matching_lefschetz(n,m,pi,flips):
    E=edges(n,m); N=len(E)
    def perm_edge(i):
        petal,t=divmod(i,m)
        return m*pi[petal]+(m-1-t if flips[petal] else t)
    p=[perm_edge(i) for i in range(N)]
    seen=set(); orbit_masks=[]
    for e in range(N):
        if e in seen:continue
        orb=[];x=e
        while x not in seen:
            seen.add(x);orb.append(x);x=p[x]
        verts=set(); valid=True
        for a in orb:
            for v in E[a]:
                if v in verts:valid=False
                verts.add(v)
        if valid:orbit_masks.append(frozenset(verts))
    # sum sign across independent sets of edge orbits
    def rec(i,used):
        if i==len(orbit_masks):return 1
        val=rec(i+1,used)
        if used.isdisjoint(orbit_masks[i]):
            val-=rec(i+1,used|orbit_masks[i])
        return val
    F=rec(0,frozenset())
    return -F # reduced Lefschetz

def sgn(pi):
    return -1 if sum(pi[i]>pi[j] for i in range(len(pi)) for j in range(i+1,len(pi)))%2 else 1

def predicted_character(n,m,pi,flips):
    residue=m%3
    if residue==0:return 0
    k=(m-1)//3 if residue==1 else (m-2)//3
    flip_sign=(-1)**((k+1)//2) if residue==1 else (-1)**(k//2)
    eta=(sgn(pi)**k)*(flip_sign**sum(flips))
    if residue==1:return eta
    fixed_spokes=sum(1 for i in range(n) if pi[i]==i and flips[i]==0)*2
    return eta*(fixed_spokes-1)

def all_faces(n,m):
    E=edges(n,m); faces=[(frozenset(),())];
    f_by_dim=defaultdict(list)
    f_by_dim[-1]=[()]
    def rec(at,chosen,used):
        for e in range(at,len(E)):
            a,b=E[e]
            if a not in used and b not in used:
                nxt=chosen+(e,)
                f_by_dim[len(nxt)-1].append(nxt)
                rec(e+1,nxt,used|{a,b})
    rec(0,(),set())
    return f_by_dim

def gf2rank(columns):
    pivots={}
    for c in columns:
        while c:
            i=c.bit_length()-1
            if i in pivots:c^=pivots[i]
            else:
                pivots[i]=c;break
    return len(pivots)

def homology_mod2(n,m):
    f=all_faces(n,m)
    dims=sorted(f)
    ranks={}
    for d in dims:
        if d==-1:continue
        basis={s:i for i,s in enumerate(f[d-1])}
        cols=[]
        for s in f[d]:
            col=0
            for j in range(len(s)):
                face=s[:j]+s[j+1:]
                col^=1<<basis[face]
            cols.append(col)
        ranks[d]=gf2rank(cols)
    betti={d:len(f[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in dims if d>=0}
    # reduced chain: augmented -1 -> trivial H0 subtraction through rank d=0
    return len(sum((f[d] for d in dims if d>=0),[])), {d:b for d,b in betti.items() if b}

def main():
    evaluations=0
    cases=[(2,3),(3,3),(2,4),(3,4),(4,4),(2,5),(3,5),(4,5),
           (2,6),(3,6),(2,7),(3,7),(2,8),(3,8),(2,9),(2,10),(2,11)]
    for n,m in cases:
        k=m//3 if m%3==0 else ((m-1)//3 if m%3==1 else (m-2)//3)
        degree=n*k-1 if m%3==1 else n*k
        for pi in permutations(range(n)):
            for fl in product((0,1),repeat=n):
                actual=(-1)**degree*orbit_matching_lefschetz(n,m,pi,fl)
                expected=predicted_character(n,m,pi,fl)
                assert actual==expected,(n,m,pi,fl,actual,expected)
                evaluations+=1
        print('CHAR_OK',n,m)
    for n,m in [(2,3),(3,3),(2,4),(3,4),(2,5),(3,5),(4,5),
                (2,6),(3,6),(2,7),(3,7),(2,8),(3,8)]:
        nf,hom=homology_mod2(n,m)
        if m%3==0: expected={}
        elif m%3==1:expected={n*((m-1)//3)-1:1}
        else:expected={n*((m-2)//3):2*n-1}
        assert hom==expected,(n,m,nf,hom,expected)
        print('HOMOLOGY_MOD2_OK',n,m,nf,hom)
    quotient_cases=0
    for n in range(2,6):
        for k in range(1,11):
            for residue in (0,1,2):
                m=3*k+residue
                if m<3:continue
                elements=[(pi,fl) for pi in permutations(range(n)) for fl in product((0,1),repeat=n)]
                total=sum(predicted_character(n,m,pi,fl) for pi,fl in elements)
                assert total%len(elements)==0
                invariant=total//len(elements)
                expected=((1 if k%4==0 else 0) if residue==1 else
                          (1 if n==2 and k%4==1 else 0) if residue==2 else 0)
                assert invariant==expected,(n,m,invariant,expected)
                reflect_total=sum(predicted_character(n,m,tuple(range(n)),fl) for fl in product((0,1),repeat=n))
                assert reflect_total%(2**n)==0
                reflect_invariant=reflect_total//(2**n)
                expected_ref= ((1 if k%4 in (0,3) else 0) if residue==1 else
                               (n-1 if k%4 in (0,1) else 0) if residue==2 else 0)
                assert reflect_invariant==expected_ref,(n,m,reflect_invariant,expected_ref)
                quotient_cases+=1
    print('WINDMILL_QUOTIENT_PREDICTIONS_VERIFIED',quotient_cases)
    print('WINDMILL_FULL_WREATH_CHARACTER_VERIFIED',evaluations)

if __name__=='__main__':main()
