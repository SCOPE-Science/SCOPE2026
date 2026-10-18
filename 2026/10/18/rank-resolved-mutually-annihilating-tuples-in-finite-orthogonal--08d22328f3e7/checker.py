"""Exact arithmetic checks for joint square-zero tuples in finite orthogonal Lie algebras.

Run: python3 checker.py. Only the Python standard library is required.
The exhaustive implementation uses prime fields; the theorem also covers prime powers.
"""
from collections import Counter
from itertools import product
from math import prod


def gaussian(n, r, q):
    if not 0 <= r <= n:
        return 0
    return prod(q**(n-i)-1 for i in range(r)) // prod(q**(r-i)-1 for i in range(r))


def isotropic(n, r, q, form='standard'):
    if r == 0:
        return 1
    m = n//2
    if n % 2:
        return gaussian(m,r,q)*prod(q**(m-i)+1 for i in range(r))
    split = (m%2==0 or q%4==1) if form=='standard' else form=='split'
    if split:
        return gaussian(m,r,q)*prod(q**(m-i-1)+1 for i in range(r))
    return gaussian(m-1,r,q)*prod(q**(m-i)+1 for i in range(r))


def spanning_alternating_tuples(r,k,q):
    return sum((-1)**(r-j)*q**((r-j)*(r-j-1)//2)*gaussian(r,j,q)*q**(k*j*(j-1)//2)
               for j in range(r+1))


def formula(n,q,k,form='standard'):
    out={}
    for r in range(n//2+1):
        v=isotropic(n,r,q,form)*spanning_alternating_tuples(r,k,q)
        if v:out[r]=v
    return out


def multiply(A,B,q):
    n=len(A)
    return tuple(tuple(sum(A[i][h]*B[h][j] for h in range(n))%q for j in range(n))
                 for i in range(n))


def rank(A,q):
    A=[list(row) for row in A]
    n=len(A);m=len(A[0]);d=0
    for col in range(m):
        p=next((i for i in range(d,n) if A[i][col]%q),None)
        if p is None:continue
        A[d],A[p]=A[p],A[d]
        inv=pow(A[d][col],-1,q)
        A[d]=[(x*inv)%q for x in A[d]]
        for i in range(n):
            if i!=d and A[i][col]%q:
                b=A[i][col]
                A[i]=[(x-b*y)%q for x,y in zip(A[i],A[d])]
        d+=1
        if d==n:break
    return d


def skew_square_zero(n,q):
    edge=[(i,j) for i in range(n) for j in range(i+1,n)]
    zero=tuple((0,)*n for _ in range(n))
    result=[]
    for values in product(range(q),repeat=len(edge)):
        A=[[0]*n for _ in range(n)]
        for (i,j),v in zip(edge,values):
            A[i][j]=v; A[j][i]=-v%q
        A=tuple(tuple(row) for row in A)
        if multiply(A,A,q)==zero:result.append(A)
    return result


def exhaustive(n,q,k):
    pool=skew_square_zero(n,q)
    zero=tuple((0,)*n for _ in range(n))
    counts=Counter()
    for matrices in product(pool,repeat=k):
        if any(multiply(A,B,q)!=zero for A in matrices for B in matrices):continue
        r=rank(tuple(tuple(entry for A in matrices for entry in A[i]) for i in range(n)),q)
        counts[r]+=1
    assert dict(counts)==formula(n,q,k), (n,q,k,dict(counts),formula(n,q,k))
    print('EXHAUSTIVE_OK',n,q,k,'squarezero_count',len(pool),'joint_ranks',sorted(counts.items()))


def odd_joint_rank_witness():
    q=3;d=3;n=6
    G=tuple(tuple(int((i<d and j==i+d) or (i>=d and j==i-d)) for j in range(n)) for i in range(n))
    S1=((0,1,0),(2,0,0),(0,0,0))
    S2=((0,0,0),(0,0,1),(0,2,0))
    def zero_extend(S):
        # With hyperbolic Gram matrix, the nonzero block is upper-right S.
        return tuple(tuple(S[i][j-d] if i<d and j>=d else 0 for j in range(n)) for i in range(n))
    X=(zero_extend(S1),zero_extend(S2))
    assert all(multiply(A,B,q)==tuple((0,)*n for _ in range(n)) for A in X for B in X)
    for A in X:
        GA=multiply(G,A,q)
        assert all((GA[i][j]+GA[j][i])%q==0 for i in range(n) for j in range(n))
    assert rank(tuple(tuple(entry for A in X for entry in A[i]) for i in range(n)),q)==3
    assert formula(6,3,2,'split')=={0:1,2:4160,3:49920}
    assert formula(6,3,2,'nonsplit')=={0:1,2:2240}
    print('ODD_JOINT_RANK_OK rank=3 form=hyperbolic n=6')


def main():
    for n,q,k in [(3,3,2),(4,3,1),(4,3,2),(4,5,2),(5,3,1),(5,3,2)]:
        exhaustive(n,q,k)
    odd_joint_rank_witness()
    for q in (3,5,7):
        for n in range(1,11):
            for k in (1,2,3):
                c=formula(n,q,k)
                assert c.get(0)==1 and 1 not in c
                assert all(x>0 for x in c.values())
    print('FORMULA_SANITY_OK')
    print('CHECKER_OK')

if __name__=='__main__':main()
