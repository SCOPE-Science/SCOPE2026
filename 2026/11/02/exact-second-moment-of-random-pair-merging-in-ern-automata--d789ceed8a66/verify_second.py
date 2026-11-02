"""Exact checks for the second moment of random pair merging in cyclic automata.

Uses no non-standard packages; this finite test supplements an all-n algebraic proof.
"""
from fractions import Fraction
from itertools import combinations
from verify_random import canon_pairs, predicted, move, independent_linear


def X(n, r):
    return 2*(n-1)**2+(r-1)*(4*n*n-12*n+4)-(r-1)*(r-2)*(4*n-2)


def D(n, r):
    return 4*n*n-12*n+4-(r-1)*(8*n-4)


def J(n, r):
    k=n//2
    return D(n,r)//2 if r<k else (n-1 if n%2 else 0)


def B(n, r, s):
    return s*(4*X(n,r)-2)+4*s*(s+1)+4*J(n,r)*max(0,s-r+1)


def second_moments(n):
    k=n//2
    m=lambda r: k if n%2==0 and r==k else n
    K={k: B(n,k,n-1)-B(n,k,k) if n%2 else 0}
    d={}
    if k>=2:
        d[k-1]=2*(4*X(n,k)-2+B(n,k-1,n-1)+B(n,k,m(k)-1)+K[k]+(2*k-3)*D(n,k-1))
        for r in range(k-2,0,-1):
            A=4*X(n,r+1)-2+B(n,r,n-1)+B(n,r+1,n-1)
            d[r]=d[r+1]+2*A+2*(2*r-1)*D(n,r)+2*(2*r+1)*D(n,r+1)
        for r in range(1,k):
            assert d[r]%2==0
            K[r]=d[r]//2+(2*r-1)*D(n,r)
    Y={1:4*X(n,1)-2+B(n,1,m(1)-1)+K[1]}
    for r in range(1,k):
        Y[r+1]=Y[r]+d[r]
    res={}
    for (r,s),pair in canon_pairs(n).items():
        res[pair]=Y[r]+B(n,r,s)+(K[r] if s>=r else 0)
    return res


def solve_exact_second(n, pairs, means):
    """Independent Fraction Gaussian elimination on second-moment Bellman equations."""
    states=list(pairs.values());index={p:i for i,p in enumerate(states)}
    N=len(states)
    A=[[Fraction(0)]*(N+1) for _ in range(N)]
    for i,p in enumerate(states):
        A[i][i]=Fraction(2)
        A[i][-1]=Fraction(4*means[p]-2)
        for letter in 'ab':
            nxt=move(n,p,letter)
            if len(nxt)==2:
                A[i][index[nxt]]-=1
    for col in range(N):
        pivot=next(i for i in range(col,N) if A[i][col])
        A[col],A[pivot]=A[pivot],A[col]
        scale=A[col][col]
        A[col]=[v/scale for v in A[col]]
        for row in range(col+1,N):
            factor=A[row][col]
            if factor:
                A[row]=[x-factor*y for x,y in zip(A[row],A[col])]
    sol=[Fraction(0)]*N
    for i in range(N-1,-1,-1):
        sol[i]=A[i][-1]-sum(A[i][j]*sol[j] for j in range(i+1,N))
    return dict(zip(states,sol))


def run():
    checked=0;independent=0
    for n in range(2,81):
        pairs=canon_pairs(n)
        means={p:predicted(n,r,s) for (r,s),p in pairs.items()}
        seconds=second_moments(n)
        assert set(seconds)==set(pairs.values())
        for p, v in seconds.items():
            rhs=4*means[p]-2
            for letter in 'ab':
                nxt=move(n,p,letter)
                rhs+=seconds.get(nxt,0) if len(nxt)==2 else 0
            assert 2*v==rhs,(n,p,v,rhs)
            checked+=1
        expected=Fraction(16*n**6-32*n**5-16*n**4+66*n**3-15*n*n-87*n+52,15)
        assert Fraction(sum(seconds.values()),len(seconds))==expected,(n,expected)
        if n<=11:
            solved=solve_exact_second(n,pairs,means)
            for p,v in solved.items():
                assert seconds[p]==v
                independent+=1
    print('VERIFY_SECOND_OK', 'n=2..80', 'Bellman_states='+str(checked), 'independent_states='+str(independent))

if __name__=='__main__':
    run()
