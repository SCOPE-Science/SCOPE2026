"""Exact tests of the three-state landscape-direction occupation theorem.

Requires Python 3 and sympy. Run: python check.py
No external data are read or downloaded.
"""
from fractions import Fraction
from random import Random
import sympy as sp


def stationary_occupancy(P, pi, c, s):
    n = P.rows
    D = sp.diag(*[s[i]-c[i] for i in range(n)])
    q = sp.Matrix([[pi[i]*c[i] for i in range(n)]]) * (sp.eye(n)-P*D).inv() * sp.ones(n,1)
    return sp.factor(q[0])


def full_chain_occupancy(P, c, s):
    # Direct stationarity on the 2n-state joint landscape/occupancy chain.
    n = P.rows
    T = sp.zeros(2*n)
    for i in range(n):
        for x in range(2):
            prob = s[i] if x else c[i]
            for j in range(n):
                T[2*i+x,2*j+1] = P[i,j]*prob
                T[2*i+x,2*j] = P[i,j]*(1-prob)
    B = T.T - sp.eye(2*n)
    for col in range(2*n): B[2*n-1,col] = 1
    rhs = sp.zeros(2*n,1)
    rhs[2*n-1] = 1
    st = B.inv()*rhs
    return sp.factor(sum(st[2*i+1] for i in range(n)))


def main():
    p1,p2,p3,h12,h23,h31,J=sp.symbols('p1 p2 p3 h12 h23 h31 J', nonzero=True)
    c1,c2,c3,d1,d2,d3=sp.symbols('c1 c2 c3 d1 d2 d3')
    ps=[p1,p2,p3]; cs=[c1,c2,c3]
    F=sp.Matrix([[p1-h12-h31,h12+J/2,h31-J/2],
                 [h12-J/2,p2-h12-h23,h23+J/2],
                 [h31+J/2,h23-J/2,p3-h23-h31]])
    Pi=sp.diag(*ps)
    P=Pi.inv()*F
    Q=Pi.inv()*F.T
    D=sp.diag(d1,d2,d3)
    I=sp.eye(3)
    w=sp.Matrix([[ps[i]*cs[i] for i in range(3)]])
    a=I-P*D; b=I-Q*D
    num_a=(w*a.adjugate()*sp.ones(3,1))[0]
    num_b=(w*b.adjugate()*sp.ones(3,1))[0]
    triangle=c1*(d2-d3)+c2*(d3-d1)+c3*(d1-d2)
    assert sp.factor(a.det()-b.det())==0
    assert sp.factor(num_a-num_b-J*triangle)==0
    print('Exact symbolic cofactor and common-determinant identities: PASS')

    sample=sp.Matrix([[sp.Rational(1,2),sp.Rational(7,20),sp.Rational(3,20)],
                      [sp.Rational(1,10),sp.Rational(1,2),sp.Rational(2,5)],
                      [sp.Rational(7,50),sp.Rational(4,25),sp.Rational(7,10)]])
    pi=[sp.Rational(1,5),sp.Rational(3,10),sp.Rational(1,2)]
    c=[sp.Rational(1,10),sp.Rational(1,5),sp.Rational(2,5)]
    s=[sp.Rational(4,5),sp.Rational(3,5),sp.Rational(9,10)]
    star=sp.diag(*pi).inv()*sample.T*sp.diag(*pi)
    forward=stationary_occupancy(sample,pi,c,s)
    reversed_=stationary_occupancy(star,pi,c,s)
    assert (forward,reversed_,forward-reversed_)==(sp.Rational(18043,31435),sp.Rational(17763,31435),sp.Rational(56,6287))
    assert full_chain_occupancy(sample,c,s)==forward
    assert full_chain_occupancy(star,c,s)==reversed_
    print('Exact example, including two distinct direct six-state solves: PASS')

    rng=Random(327401)
    ntests=50
    for _ in range(ntests):
        weights=[rng.randint(4,10) for _ in range(3)]
        pi=[sp.Rational(v,sum(weights)) for v in weights]
        # Positive stationary directed cycles with a controlled net circulation.
        j=sp.Rational(rng.randint(-2,2),300)
        h=[sp.Rational(rng.randint(2,5),120) for _ in range(3)]
        f=sp.Matrix([[pi[0]-h[0]-h[2],h[0]+j/2,h[2]-j/2],
                     [h[0]-j/2,pi[1]-h[0]-h[1],h[1]+j/2],
                     [h[2]+j/2,h[1]-j/2,pi[2]-h[1]-h[2]]])
        assert min(f)>0
        P=sp.diag(*[1/p for p in pi])*f
        Q=sp.diag(*[1/p for p in pi])*f.T
        c=[sp.Rational(rng.randint(1,9),11) for _ in range(3)]
        s=[sp.Rational(rng.randint(1,9),11) for _ in range(3)]
        ds=[s[i]-c[i] for i in range(3)]
        area=c[0]*(ds[1]-ds[2])+c[1]*(ds[2]-ds[0])+c[2]*(ds[0]-ds[1])
        determinant=(sp.eye(3)-P*sp.diag(*ds)).det()
        assert determinant>0
        e1=stationary_occupancy(P,pi,c,s)
        e2=stationary_occupancy(Q,pi,c,s)
        assert sp.factor(e1-e2-j*area/determinant)==0
        assert full_chain_occupancy(P,c,s)==e1
        assert full_chain_occupancy(Q,c,s)==e2
    print(f'{ntests} rational three-state cases, both six-state Markov stationary calculations: PASS')

if __name__=='__main__':
    main()
