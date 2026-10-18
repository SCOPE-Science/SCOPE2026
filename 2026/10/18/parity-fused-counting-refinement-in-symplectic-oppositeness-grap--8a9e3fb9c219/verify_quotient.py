"""Independent q-binomial moment inversion and parity-refinement checks.
Run: python verify_quotient.py (standard library only)
"""
from functools import lru_cache
from collections import defaultdict
from itertools import product
from math import prod

@lru_cache(None)
def gaussian(n, k, q):
    if k<0 or k>n:return 0
    if k==0 or k==n:return 1
    return gaussian(n-1,k,q)+q**(n-k)*gaussian(n-1,k-1,q)


def quotient(n,q):
    N=n*(n+1)//2
    matrix=[]
    for s in range(n+1):
        moments=[q**(s*r)*gaussian(n-s,r,q)*q**((n-r)*(n-r+1)//2)
                 for r in range(n+1)]
        row=[]
        for t in range(n+1):
            p=sum((-1)**(r-t)*q**((r-t)*(r-t-1)//2)*
                  gaussian(r,t,q)*moments[r] for r in range(t,n+1))
            row.append(p)
        assert min(row)>=0 and sum(row)==q**N
        matrix.append(row)
    cardinality=[gaussian(n,s,q)*q**((n-s)*(n-s+1)//2) for s in range(n+1)]
    assert sum(cardinality)==prod(q**j+1 for j in range(1,n+1))
    for s in range(n+1):
        for t in range(n+1):
            assert cardinality[s]*matrix[s][t]==cardinality[t]*matrix[t][s]
    return matrix


def refine(mat):
    n=len(mat)-1
    colors=[1 if s==n else 0 for s in range(n+1)]
    groups=[]
    for step in range(1,n+3):
        cset=sorted(set(colors))
        sig=[(colors[s],tuple(sum(mat[s][t] for t in range(n+1) if colors[t]==c)
                         for c in cset)) for s in range(n+1)]
        dic={x:i for i,x in enumerate(sorted(set(sig)))}
        out=[dic[z] for z in sig]
        g=defaultdict(list)
        for s,c in enumerate(out):g[c].append(s)
        groups.append(tuple(sorted(tuple(v) for v in g.values())))
        if out==colors:break
        colors=out
    return groups


def expected(n):
    if n%2==0:
        return tuple((s,) for s in range(n+1))
    return tuple([(0,)]+[(s,s+1) for s in range(1,n-1,2)]+[(n,)])


def rank_mod_prime(rows,p):
    a=[list(x) for x in rows]
    h=len(a); r=0
    for j in range(h):
        pivot=next((i for i in range(r,h) if a[i][j]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,p)
        a[r]=[v*inv%p for v in a[r]]
        for i in range(h):
            if i==r:continue
            mul=a[i][j]
            if mul:a[i]=[(a[i][z]-mul*a[r][z])%p for z in range(h)]
        r+=1
    return r


def direct_symmetric_distribution(m,p):
    cells=[(i,j) for i in range(m) for j in range(i,m)]
    dist=[0]*(m+1)
    for vals in product(range(p),repeat=len(cells)):
        a=[[0]*m for _ in range(m)]
        for (i,j),x in zip(cells,vals):a[i][j]=a[j][i]=x
        dist[m-rank_mod_prime(a,p)]+=1
    return dist


def check():
    checked=0
    for q,limit in [(2,12),(3,10),(4,9),(5,8)]:
        for n in range(2,limit+1):
            mat=quotient(n,q)
            layers=refine(mat)
            assert layers[-1]==expected(n),(n,q,layers)
            if n==2:assert len(layers[0])==3
            if n%2==0 and n>=4:
                assert len(layers[1])<n+1 and len(layers[2])==n+1
            if n%2==1:
                assert len(layers[1])==(n+3)//2 and layers[-1]==layers[1]
            checked+=1
    for p,mmax in [(2,5),(3,4)]:
        for m in range(mmax+1):
            observed=direct_symmetric_distribution(m,p)
            assert observed==quotient(m,p)[0] if m>=1 else observed==[1]
    print('moment-inversion quotient cases=%d, q=2/3/4/5, ranks 2..12: PASS'%checked)
    print('direct symmetric-matrix rank distributions p=2 ranks0..5, p=3 ranks0..4: PASS')
    print('odd parity equitable fusion; even sharp round-three separation: PASS')
    print('QUOTIENT_VERIFICATION_PASS')

if __name__=='__main__':check()
