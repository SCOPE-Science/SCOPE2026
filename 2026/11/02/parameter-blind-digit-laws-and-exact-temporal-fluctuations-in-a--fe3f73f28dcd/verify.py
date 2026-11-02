#!/usr/bin/env python3
"""Exact rational checks for a six-cell random interval transformation.

Requires Python 3 standard library only.  Checks finite algebra and branch geometry;
the accompanying proof supplies the infinite-time Markov and limit arguments.
"""
from fractions import Fraction as Q

Z = [Q(1, 3), Q(7, 18), Q(4, 9), Q(1, 2), Q(2, 3), Q(5, 6), Q(1)]
# Affine coefficients of the two maps on cells I_1,...,I_6.
MAPS = (
    ((-6, 3), (6, -2), (6, -2), (-2, 2), (2, -1), (2, -1)),
    ((-6, 3), (-6, 3), (6, -2), (-2, 2), (-2, 2), (2, -1)),
)
J = [(Q(2, 3), Q(1)), (Q(1, 3), Q(2, 3)),
     (Q(2, 3), Q(1)), (Q(2, 3), Q(1)),
     (Q(1, 3), Q(2, 3)), (Q(2, 3), Q(1))]

def matvec(M, v):
    return [sum(x*y for x, y in zip(row, v)) for row in M]

def rowmat(v, M):
    return [sum(v[i]*M[i][j] for i in range(len(v))) for j in range(len(M[0]))]

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def joint(pattern, P, pi):
    # Boolean pattern: 1 = digit 3, 0 = digit 2.
    weights = [pi[i] if (i < 3) == bool(pattern[0]) else Q(0) for i in range(6)]
    for b in pattern[1:]:
        weights = rowmat(weights, P)
        weights = [weights[i] if (i < 3) == bool(b) else Q(0) for i in range(6)]
    return sum(weights)

def main():
    assert all(Z[i] < Z[i+1] for i in range(6))
    for j, amap in enumerate(MAPS):
        for i, (a,b) in enumerate(amap):
            assert a != 0
            lo, hi = sorted([Q(a)*Z[i]+Q(b), Q(a)*Z[i+1]+Q(b)])
            assert (lo,hi) == J[i], (j,i,lo,hi)
            assert abs(a)*(Z[i+1]-Z[i]) == Q(1,3)
    P = []
    for i in range(6):
        row=[]
        for j in range(6):
            overlap=max(Q(0),min(J[i][1],Z[j+1])-max(J[i][0],Z[j]))
            row.append(3*overlap)
        assert sum(row)==1
        P.append(row)
    expected=[
        [0,0,0,0,Q(1,2),Q(1,2)],
        [Q(1,6),Q(1,6),Q(1,6),Q(1,2),0,0],
        [0,0,0,0,Q(1,2),Q(1,2)],
        [0,0,0,0,Q(1,2),Q(1,2)],
        [Q(1,6),Q(1,6),Q(1,6),Q(1,2),0,0],
        [0,0,0,0,Q(1,2),Q(1,2)],
    ]
    assert P==expected
    pi=[Q(t,16) for t in [1,1,1,3,5,5]]
    assert sum(pi)==1 and rowmat(pi,P)==pi
    assert [pi[i]/(Z[i+1]-Z[i]) for i in range(6)] == [Q(9,8)]*4+[Q(15,8)]*2
    f=[Q(int(i<3)) for i in range(6)]
    mu=dot(pi,f)
    assert mu==Q(3,16)
    g=[x-mu for x in f]
    Pg=matvec(P,g)
    P2g=matvec(P,Pg)
    assert all(P2g[i]==-Pg[i]/3 for i in range(6))
    C0=dot(pi,[x*x for x in g])
    C1=dot(pi,[g[i]*Pg[i] for i in range(6)])
    assert (C0,C1)==(Q(39,256),-Q(1,256))
    for n in range(0,70):
        c=dot(pi,[g[i]*matvec_power(P,g,n)[i] for i in range(6)])
        wanted=C0 if n==0 else Q(3,256)*Q(-1,3)**n
        assert c==wanted,(n,c,wanted)
    for N in range(1,100):
        v=N*C0+2*sum((N-k)*(Q(3,256)*Q(-1,3)**k) for k in range(1,N))
        formula=Q(75,512)*N+Q(9,2048)*(1-Q(-1,3)**N)
        assert v==formula,(N,v,formula)
    # Explicit observed-digit non-Markov witness.
    a=joint([1,0,1],P,pi)/joint([1,0],P,pi)
    b=joint([0,0,1],P,pi)/joint([0,0],P,pi)
    assert (a,b)==(Q(1,5),Q(4,21))
    assert Q(75,512)>0
    print('PASS: 12 affine branch images, 6 Markov rows, invariant density,')
    print('      correlations through lag 69, finite variances through N=99,')
    print('      and distinct non-Markov conditional probabilities.')
    print('Exact asymptotic variance: 75/512; p in [0,1] has no effect on the coding.')

def matvec_power(P,v,n):
    out=v
    for _ in range(n):out=matvec(P,out)
    return out

if __name__=='__main__':main()
