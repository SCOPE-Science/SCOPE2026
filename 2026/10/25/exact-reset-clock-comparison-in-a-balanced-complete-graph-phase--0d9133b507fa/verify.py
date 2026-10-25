"""Exact rational independent reconstruction of reset-network stationary moments.

Requires Python 3 standard library only. This script checks finite parameter samples;
the analytic proof separately establishes the all-parameter statements.
"""
from fractions import Fraction as F
from itertools import product


def solve(A,b):
    A=[list(row)+[rhs] for row,rhs in zip(A,b)]
    n=len(A)
    for c in range(n):
        p=next((p for p in range(c,n) if A[p][c]),None)
        assert p is not None, ('singular',c)
        A[c],A[p]=A[p],A[c]
        k=A[c][c]
        A[c]=[v/k for v in A[c]]
        for i in range(n):
            if i != c:
                q=A[i][c]
                if q: A[i]=[u-q*v for u,v in zip(A[i],A[c])]
    return [r[-1] for r in A]


def covariance_from_full_generator(N,rate,damping,freq,kind):
    # Unknown is each entry of the symmetric second-moment matrix.
    pairs=[(i,j) for i in range(N) for j in range(i,N)]
    midx={p:k for k,p in enumerate(pairs)}
    def idx(i,j): return midx[(min(i,j),max(i,j))]
    first=[w/(rate+damping) for w in freq]
    rows=[]; rhs=[]
    for i,j in pairs:
        coefficients=[F(0)]*len(pairs)
        coefficients[idx(i,j)] += 2*damping + (rate if kind=='shared' else rate*(1+(i!=j)))
        for a in range(N):
            coefficients[idx(a,j)] -= damping/F(N)
            coefficients[idx(i,a)] -= damping/F(N)
        rows.append(coefficients)
        rhs.append(freq[i]*first[j]+freq[j]*first[i])
    x=solve(rows,rhs)
    M=[[x[idx(i,j)] for j in range(N)] for i in range(N)]
    return M


def trial(N,r,g,omega):
    A=sum(w*w for w in omega)
    assert sum(omega)==0
    n=F(N)
    ms=omega
    Ds=2*A/((r+g)*(r+2*g))
    Di=A*(2*n-1)/((r+g)*(n*r+(2*n-1)*g))
    H=A/(n*(r+g)*(n*r+(2*n-1)*g))
    assert Ds-Di==A*r/((r+g)*(r+2*g)*(n*r+(2*n-1)*g))
    assert Di < Ds
    assert H>0
    for kind in ('shared','independent'):
        M=covariance_from_full_generator(N,r,g,omega,kind)
        U=sum(M[i][i] for i in range(N))
        S2=sum(M[i][j] for i in range(N) for j in range(N))
        D=U-S2/n
        assert D==(Ds if kind=='shared' else Di),(kind,N,r,g,D)
        assert S2/(n*n)==(F(0) if kind=='shared' else H)
        cvar=D-A/((r+g)*(r+g))
        expected=(A*r/((r+g)**2*(r+2*g)) if kind=='shared'
                  else A*(n-1)*r/((r+g)**2*(n*r+(2*n-1)*g)))
        assert cvar==expected
    return True

if __name__=='__main__':
    ct=0
    for N,r,g in product(range(2,7),[F(1,3),F(1),F(4)],[F(1,2),F(2),F(5)]):
        # Asymmetric, nonconstant, balanced natural frequencies.
        omega=[F(i+1) for i in range(N-1)]
        omega.append(-sum(omega))
        assert trial(N,r,g,omega)
        ct+=1
    print('PASS:',ct,'exact-rational all-generator scenarios; 2 protocols each')
