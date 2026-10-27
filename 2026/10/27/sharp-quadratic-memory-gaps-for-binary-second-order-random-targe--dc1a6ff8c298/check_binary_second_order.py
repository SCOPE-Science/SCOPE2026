"""Exact checks for stationary-target hitting times of binary second-order chains.

Independent stationary equations and four-state hitting-time linear systems are
solved with rational Gaussian elimination; no statistical simulation is used.
"""
from fractions import Fraction as F
from random import Random

STATES = [(0,0),(0,1),(1,0),(1,1)]

def solve(matrix, rhs):
    n = len(rhs)
    z = [list(map(F, row)) + [F(rhs[i])] for i,row in enumerate(matrix)]
    for i in range(n):
        pivot = next(k for k in range(i,n) if z[k][i] != 0)
        z[i],z[pivot] = z[pivot],z[i]
        v = z[i][i]
        z[i] = [a/v for a in z[i]]
        for k in range(n):
            if k != i:
                v = z[k][i]
                z[k] = [a-v*b for a,b in zip(z[k], z[i])]
    return [row[-1] for row in z]

def checks(a,b,c,d):
    p = {(0,0):a,(0,1):b,(1,0):c,(1,1):d}
    Q = [[F(0) for _ in STATES] for _ in STATES]
    for ix,(i,j) in enumerate(STATES):
        for k in (0,1):
            Q[ix][STATES.index((k,i))] += p[i,j] if k else 1-p[i,j]
    # Solve (Q^T-I) mu=0, sum mu=1, using independent equations.
    st = solve([[Q[row][col] - (col==row) for row in range(4)] for col in range(3)] + [[1]*4], [0,0,0,1])
    assert sum(st)==1 and all(x>0 for x in st)
    assert all(sum(st[row]*Q[row][col] for row in range(4))==st[col] for col in range(4))
    pi = [sum(st[ix] for ix,(i,j) in enumerate(STATES) if i==y) for y in (0,1)]
    assert sum(pi)==1
    h = {}
    for target in (0,1):
        M = [[F(int(row==col)) for col in range(4)] for row in range(4)]
        for row,(i,j) in enumerate(STATES):
            for k in (0,1):
                if k != target:
                    M[row][STATES.index((k,i))] -= Q[row][STATES.index((k,i))]
        x=solve(M,[1]*4)
        assert all(t>0 for t in x)
        assert all(x[row]==1+sum(Q[row][col]*x[col] for col,(k,l) in enumerate(STATES) if k!=target) for row in range(4))
        h[target] = x
    K = {pair:sum(pi[target]*h[target][ix] for target in (0,1)) for ix,pair in enumerate(STATES)}
    den=(1-b)*(1-d)+a*c+2*a*(1-d)
    assert den>0
    gap_zero=(a-b)**2*(1+c-d)/den
    gap_one=(c-d)**2*(1+a-b)/den
    assert K[0,0]-K[0,1]==gap_zero
    assert K[1,1]-K[1,0]==gap_one
    assert (len(set(K.values()))==1)==(a==b and c==d)
    return K,pi,gap_zero,gap_one

def main():
    rng=Random(20261024)
    tests=[]
    for _ in range(192):
        data=[F(rng.randrange(1,20),20) for i in range(4)]
        tests.append(tuple(data))
    for _ in range(24):
        a,c=F(rng.randrange(1,20),20),F(rng.randrange(1,20),20)
        tests.append((a,a,c,c))
        tests.append((a,F(rng.randrange(1,20),20),c,c))
        tests.append((a,a,c,F(rng.randrange(1,20),20)))
    tests += [
      (F(1,4),F(3,4),F(2,3),F(1,3)),
      (F(1,10),F(9,10),F(9,10),F(1,10)),
      (F(1,2),)*4,
      (F(2,3),F(2,3),F(1,4),F(1,4)),
    ]
    for a,b,c,d in tests:
        checks(a,b,c,d)
    print('Exact independently solved rational kernels:',len(tests))
    a,b,c,d=F(1,4),F(3,4),F(2,3),F(1,3)
    K,pi,d0,d1=checks(a,b,c,d)
    print('Witness a,b,c,d:',a,b,c,d)
    print('Marginal pi0,pi1:',pi)
    print('K00,K01,K10,K11:',*(K[s] for s in STATES))
    print('First quadratic gap K00-K01:',d0)
    print('Second quadratic gap K11-K10:',d1)
    print('All exact checks passed.')
if __name__=='__main__':main()
