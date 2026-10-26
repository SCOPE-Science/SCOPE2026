"""Exact examples for the coordinate-incidence matroid of two maximal isotropics."""
from fractions import Fraction
from itertools import combinations

def rref(rows,n):
    a=[[Fraction(x) for x in r] for r in rows]
    rank=0; piv=[]
    for col in range(n):
        pivot=next((t for t in range(rank,len(a)) if a[t][col]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        v=a[rank][col];a[rank]=[x/v for x in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][col]:
                c=a[i][col];a[i]=[a[i][j]-c*a[rank][j] for j in range(n)]
        piv.append(col); rank+=1
    return a,tuple(piv)

def kernel(a):
    n=len(a)
    reduced,piv=rref(a,n)
    free=[j for j in range(n) if j not in piv]
    return [[-reduced[piv.index(l)][j] if l in piv else (Fraction(1) if l==j else Fraction(0)) for l in range(n)] for j in free]

def rank(rows,n): return len(rref(rows,n)[1])

def check(a):
    m=len(a)
    assert all(a[i][i]==0 and a[i][j]==-a[j][i] for i in range(m) for j in range(m))
    d=m-rank(a,m); B=kernel(a)
    assert len(B)==d and (m-d)%2==0
    sizes=[]
    for k in range(m+1):
        indices=list(combinations(range(m),k))
        allowable=[I for I in indices if rank([[b[i] for i in I] for b in B],k)==k]
        if allowable: assert k<=d
        sizes.append(len(allowable))
    assert sizes[d]>0 and all(x==0 for x in sizes[d+1:])
    return d,tuple(sizes)

if __name__=='__main__':
    cases=[
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,1,1,1],[-1,0,1,1],[-1,-1,0,1],[-1,-1,-1,0]],
    [[0,1,1,0],[-1,0,0,0],[-1,0,0,0],[0,0,0,0]],
    [[0,1,0,0,0],[-1,0,0,0,0],[0,0,0,1,1],[0,0,-1,0,1],[0,0,-1,-1,0]],
    ]
    out=[check(A) for A in cases]
    assert out[0]==(4,(1,4,6,4,1))
    assert out[1][0]==0
    assert out[2][0]==2
    assert out[3][0]==1
    print('VERIFY_OK: 4 exact skew-matrix profiles; (nullity, compatible subsets by size)=',out)
