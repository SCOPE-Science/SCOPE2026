"""Reproducible finite checks for the ell-one Rips complex of K_{m,n}.
Uses independent exhaustive shortest Hamiltonian path lengths and GF(2) boundary ranks.
The universal homotopy conclusion is proved mathematically, not by this finite check.
"""
from itertools import combinations, permutations
from math import comb


def C(n,k):
    return comb(n,k) if 0<=k<=n else 0


def proposed_weight(a,b):
    k=a+b
    return max(k-1,2*max(a,b)-2) if k else 0


def actual_weight(vertices,m):
    if len(vertices)<2:return 0
    best=10**6
    for p in permutations(vertices):
        val=sum(1 if (x<m)!=(y<m) else 2 for x,y in zip(p,p[1:]))
        best=min(best,val)
    return best


def simplices(m,n,r):
    out={}
    for k in range(1,m+n+1):
        out[k-1]=[]
        for s in combinations(range(m+n),k):
            a=sum(v<m for v in s)
            if proposed_weight(a,k-a)<=r:
                out[k-1].append(s)
    return {k:v for k,v in out.items() if v}


def rank2(columns):
    pivots={}
    rank=0
    for vector in columns:
        while vector:
            p=vector.bit_length()-1
            if p not in pivots:
                pivots[p]=vector;rank+=1;break
            vector ^=pivots[p]
    return rank


def bettis(simp):
    dimensions=sorted(simp)
    dmax=max(dimensions)
    ranks={0:1} # augmentation map C_0 -> Z/2, as vertices always present
    for d in range(1,dmax+1):
        faces={s:i for i,s in enumerate(simp.get(d-1,[]))}
        columns=[]
        for sig in simp.get(d,[]):
            v=0
            for i in range(len(sig)):
                v ^= 1<<faces[sig[:i]+sig[i+1:]]
            columns.append(v)
        ranks[d]=rank2(columns)
    ranks[dmax+1]=0
    return {d:len(simp.get(d,[]))-ranks[d]-ranks[d+1] for d in dimensions if len(simp.get(d,[]))-ranks[d]-ranks[d+1]}


def predicted(m,n,r):
    s=r//2
    if r%2:
        val=C(m-1,s+1)*C(n-1,s+1)
    else:
        val=C(m,s+1)*C(n,s+1)-C(m-1,s+1)*C(n-1,s+1)
    return {r:val} if val else {}


def run():
    brute=0;homology=0
    for m in range(1,4):
        for n in range(1,4):
            for k in range(1,m+n+1):
                for v in combinations(range(m+n),k):
                    a=sum(i<m for i in v)
                    observed=actual_weight(v,m)
                    expect=proposed_weight(a,k-a)
                    assert observed==expect,(m,n,v,observed,expect)
                    brute+=1
    for m in range(1,5):
        for n in range(1,5):
            for r in range(0,2*min(m,n)+2):
                actual=bettis(simplices(m,n,r))
                expect=predicted(m,n,r)
                assert actual==expect,(m,n,r,actual,expect)
                homology+=1
    print('PASS: exhaustive path weights',brute,'and independent binary homology stages',homology)
    for m,n in [(2,2),(3,3),(3,4),(4,4)]:
        print((m,n),[predicted(m,n,r) for r in range(2*min(m,n))])

if __name__=='__main__':run()
