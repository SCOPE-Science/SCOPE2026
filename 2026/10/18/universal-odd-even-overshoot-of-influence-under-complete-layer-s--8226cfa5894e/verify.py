"""Exact rational checks of a parity interlacing result for periodic graph averaging.

This program checks finite examples and algebraic matrix identities only. The
universal and asymptotic claims rely on the accompanying mathematical proof.
"""
from fractions import Fraction as F
from itertools import combinations


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def matpow(A, k):
    R = eye(len(A))
    while k:
        if k & 1:
            R = matmul(R, A)
        k //= 2
        if k:
            A = matmul(A, A)
    return R


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def rowmul(v, A):
    return [sum(v[i]*A[i][j] for i in range(len(v))) for j in range(len(v))]


def solve(T, b):
    """Solve exact rational linear system T x = b by pivoted elimination."""
    n=len(T)
    a=[list(T[i])+[b[i]] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        scale=a[j][j]
        a[j]=[v/scale for v in a[j]]
        for i in range(n):
            if i!=j:
                s=a[i][j]
                a[i]=[a[i][v]-s*a[j][v] for v in range(n+1)]
    return [a[i][-1] for i in range(n)]


def weighted_B(n, edges):
    W=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j,w in edges:
        w=F(w)
        W[i][j]=W[j][i]=w
    d=[sum(row) for row in W]
    assert all(sum(x>0 for x in row)>=2 for row in W)
    B=[[W[i][j]/d[i] for j in range(n)] for i in range(n)]
    return B,d


def run_example(n, edges, desc):
    B,d=weighted_B(n, edges)
    total=sum(d)
    pi=[v/total for v in d]
    A=[[F(int(i!=j),n-1) for j in range(n)] for i in range(n)]
    u=[F(1,n) for _ in range(n)]
    x=[min(d)/v for v in d]
    c_B=dot(pi,x)
    c_A=dot(u,x)
    assert c_A>c_B
    assert rowmul(pi,B)==pi
    past_odd=None
    past_even=None
    chi_A=sum((u[i]-pi[i])**2/pi[i] for i in range(n))
    assert chi_A>0
    past_chi_odd=None
    past_chi_even=None
    examples={}
    for k in range(1,13):
        t=F(-1,n-1)**k
        C=matmul(B,matpow(A,k))
        exact=[[F(1-t,n)+t*B[i][j] for j in range(n)] for i in range(n)]
        assert C==exact
        assert all(v>0 for row in C for v in row)
        # Solve (I-tB)^T nu = (1-t)u, then check stationary directly.
        T=[[F(int(i==j))-t*B[j][i] for j in range(n)] for i in range(n)]
        nu=solve(T,[(1-t)*ui for ui in u])
        assert sum(nu)==1
        assert rowmul(nu,C)==nu
        assert all(z>0 for z in nu)
        val=dot(nu,x)
        chi=sum((nu[i]-pi[i])**2/pi[i] for i in range(n))
        if k%2:
            assert val>c_A and chi>chi_A
            if past_chi_odd is not None:
                assert chi<past_chi_odd
            past_chi_odd=chi
            if past_odd is not None:
                assert val<past_odd
            past_odd=val
        else:
            assert c_B<val<c_A and 0<chi<chi_A
            if past_chi_even is not None:
                assert chi>past_chi_even
            past_chi_even=chi
            if past_even is not None:
                assert val>past_even
            past_even=val
        examples[k]=val
        # quotient eigen identity in the stronger vector form C(v)-C(w) centered:
        # row stochastic C has same differences as t B on vectors.
        for vec in ([F(i%3-1) for i in range(n)],
                    [F((i+1)**2) for i in range(n)]):
            cvec=[dot(row,vec) for row in C]
            bvec=[dot(row,vec) for row in B]
            for j in range(1,n):
                assert cvec[j]-cvec[0]==t*(bvec[j]-bvec[0])
    print(desc, 'n=',n,'c_B=',c_B,'c_A=',c_A,'k1=',examples[1],
          'k2=',examples[2], 'k3=',examples[3], 'k4=',examples[4], 'chi_A=', chi_A)
    return examples


def main():
    # Weighted triangles, sparse and dense irregular graphs, all with odd cycles.
    examples=[
      (3, [(0,1,2),(0,2,1),(1,2,1)],'weighted triangle'),
      (4, [(0,2,1),(0,3,1),(1,2,1),(1,3,1),(2,3,1)],'four-node five-edge graph'),
      (5, [(0,1,1),(1,2,1),(2,0,1),(2,3,2),(3,4,2),(4,0,1),(1,4,1)],'five-node graph'),
      (6, [(0,1,1),(1,2,2),(2,0,1),(2,3,1),(3,4,3),(4,5,1),(5,3,1),(5,0,2),(1,4,1)],'six-node graph'),
    ]
    for n,edges,desc in examples:
        run_example(n,edges,desc)
    print('PASS: 4 graphs x 12 switching lengths, positivity, stationary equations, strict odd/even interlacing, and 2 quotient identities per period')

if __name__=='__main__':
    main()
