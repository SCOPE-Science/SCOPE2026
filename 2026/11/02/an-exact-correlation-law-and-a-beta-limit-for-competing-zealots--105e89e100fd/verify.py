"""Exact finite-state and moment checks for bipartite voter dynamics with opposing fixed zealots.

Standard library only. The infinite-system beta limit requires the analytic
stationary-generator argument presented in RESULT.md; finite checks do not prove it.
"""
from fractions import Fraction as F
from itertools import product


def analytical(a, b):
    assert a >= 2 and b >= 2
    nall = a + b
    d = (nall-1)*(3*nall-4)
    x = F(b-1, nall-1)
    y = F(b, nall-1)
    p_ab = F(b*(a+3*b-4), d)
    p_aa = F((b-1)*(a+3*b-4), d)
    p_bb = F(b*(a+3*b-2), d)
    return x, y, p_ab, p_aa, p_bb


def rate_dict(a, b, i, j):
    m, n = a-1, b-1
    rates = {}
    if i < m: rates[(i+1,j)] = F((m-i)*j, b)
    if i > 0: rates[(i-1,j)] = F(i*(b-j), b)
    if j < n: rates[(i,j+1)] = F((n-j)*(i+1), a)
    if j > 0: rates[(i,j-1)] = F(j*(a-1-i), a)
    return {s: v for s, v in rates.items() if v}


def independently_aggregate(a, b, i, j):
    """Enumerate individual copying events without using the count-rate formulas."""
    m, n = a-1, b-1
    abits = (1,)*i + (0,)*(m-i)
    bbits = (1,)*j + (0,)*(n-j)
    new = {}
    for bit in abits:
        # Each A agent copies a uniformly chosen B neighbor, one of whom is fixed at zero.
        t = (i-1 if bit else i+1, j)
        r = F((1 + sum(1-v for v in bbits)) if bit else sum(bbits), b)
        new[t] = new.get(t,F(0)) + r
    for bit in bbits:
        # Each B agent copies a uniformly chosen A neighbor, one of whom is fixed at one.
        t = (i,j-1 if bit else j+1)
        r = F(sum(1-v for v in abits) if bit else 1+sum(abits), a)
        new[t] = new.get(t,F(0)) + r
    return {s:v for s,v in new.items() if v}


def solve_exact(A, b):
    n = len(b)
    q = [list(A[k]) + [b[k]] for k in range(n)]
    for col in range(n):
        pivot = next((k for k in range(col,n) if q[k][col]),None)
        assert pivot is not None, (col,n)
        q[col], q[pivot] = q[pivot], q[col]
        inv = F(1)/q[col][col]
        for k in range(col,n+1): q[col][k] *= inv
        for row in range(n):
            if row == col or not q[row][col]: continue
            factor = q[row][col]
            for k in range(col,n+1): q[row][k] -= factor*q[col][k]
    return [q[i][-1] for i in range(n)]


def stationary(a,b):
    states=[(i,j) for i in range(a) for j in range(b)]
    lookup={state:k for k,state in enumerate(states)}
    d=len(states)
    A=[[F(0) for _ in range(d)] for _ in range(d)]
    for z,(i,j) in enumerate(states):
        rates=rate_dict(a,b,i,j)
        for s,r in rates.items():
            A[lookup[s]][z] += r
            A[z][z] -= r
    A[-1] = [F(1)]*d
    rhs=[F(0)]*(d-1)+[F(1)]
    p=solve_exact(A,rhs)
    assert all(q >= 0 for q in p) and sum(p)==1
    return states,p


def check():
    rate_cases=moment_cases=stationary_cases=0
    for a in range(2,21):
        for b in range(2,21):
            m,n=a-1,b-1
            x,y,c,u,v=analytical(a,b)
            I=m*x; J=n*y
            I2=m*(m-1)*u; J2=n*(n-1)*v; IJ=m*n*c
            assert F(m,b)*J-I == 0
            assert F(n,a)*(I+1)-J == 0
            assert 2*(F(m-1,b)*IJ-I2)==0
            assert 2*(F(n-1,a)*(IJ+J)-J2)==0
            assert F(m,b)*(J2+J)+F(n,a)*(I2+2*I)-2*IJ==0
            moment_cases+=1
            if a<=5 and b<=5:
                for i in range(a):
                    for j in range(b):
                        assert rate_dict(a,b,i,j)==independently_aggregate(a,b,i,j)
                        rate_cases+=1
                states,p=stationary(a,b)
                assert sum(z*i for z,(i,j) in zip(p,states))==I
                assert sum(z*j for z,(i,j) in zip(p,states))==J
                assert sum(z*i*j for z,(i,j) in zip(p,states))==IJ
                assert sum(z*i*(i-1) for z,(i,j) in zip(p,states))==I2
                assert sum(z*j*(j-1) for z,(i,j) in zip(p,states))==J2
                stationary_cases+=1
    print(f'PASS: {rate_cases} independent microevent rate checks; '
          f'{moment_cases} full five-equation rational stationary checks; '
          f'{stationary_cases} independent exact stationary distributions.')


if __name__ == '__main__': check()
