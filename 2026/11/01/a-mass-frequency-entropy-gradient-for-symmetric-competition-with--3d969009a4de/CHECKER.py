"""Exact, finite rational checks for the mass-frequency Lyapunov identities.

Run: python CHECKER.py.  Requires Python >=3.9, no extra dependencies.
The analytic all-time convergence theorem is proved separately.
"""
from fractions import Fraction as Q
from itertools import product


def vector_field(A, mu, x):
    n = len(x)
    s = sum(x)
    return [x[i] * (1-sum(A[i][j]*x[j] for j in range(n)))
            +mu*(s-n*x[i]) for i in range(n)]


def check(A, mu, p, S):
    n = len(p)
    assert sum(p) == 1 and min(p) > 0 and S > 0
    assert all(A[i][j] == A[j][i] and A[i][j] > 0
               for i in range(n) for j in range(n))
    x = [S*z for z in p]
    f = vector_field(A, mu, x)
    Sd = sum(f)
    pd = [(f[i]-p[i]*Sd)/S for i in range(n)]
    q = sum(p[i]*A[i][j]*p[j] for i in range(n) for j in range(n))
    ap = [sum(A[i][j]*p[j] for j in range(n)) for i in range(n)]
    assert Sd == S - S*S*q
    assert all(pd[i] == -S*p[i]*(ap[i]-q)+mu*(1-n*p[i]) for i in range(n))
    phis = 1/S-q
    phi_p = [-2*S*ap[i]+2*mu/p[i] for i in range(n)]
    mean_phi_p = sum(p[i]*phi_p[i] for i in range(n))
    assert Sd == S*S*phis
    assert all(pd[i] == p[i]*(phi_p[i]-mean_phi_p)/2 for i in range(n))
    chain = phis*Sd +sum(phi_p[i]*pd[i] for i in range(n))
    dissip = (Sd/S)**2 +2*sum(pd[i]**2/p[i] for i in range(n))
    assert chain == dissip >= 0
    return chain


def main():
    grids = [
       [[Q(1), Q(13,10), Q(13,10)],
        [Q(13,10), Q(1), Q(13,10)],
        [Q(13,10), Q(13,10), Q(1)]],
       [[Q(2), Q(1,3), Q(5,7)],
        [Q(1,3), Q(3), Q(4,5)],
        [Q(5,7), Q(4,5), Q(6,5)]],
    ]
    test_p = [[Q(1,3)]*3, [Q(1,2),Q(1,3),Q(1,6)],
              [Q(2,5),Q(2,5),Q(1,5)], [Q(1,10),Q(3,10),Q(6,10)]]
    checks = 0
    strict = 0
    for A,mu,p,S in product(grids,[Q(3,100),Q(1,4)],test_p,[Q(7,5),Q(13,10)]):
        v=check(A,mu,p,S)
        strict += (v>0)
        checks += 1
    # Exact multistable example: a=13/10, mu=3/100 has two
    # positive nonsymmetric ratio roots, neither equal to one.
    a=Q(13,10); mu=Q(3,100)
    # mu r^2 + (4a mu -a+1)r +2(a+1)mu =0.
    B=4*a*mu-(a-1)
    C=2*(a+1)*mu
    disc=B**2-4*mu*C
    assert disc>0 and B<0
    L=(a-1)-4*a*mu
    assert L>0 and L*L>8*mu*mu*(a+1)
    # Discriminant positivity together with negative sum and positive
    # product gives two positive roots; r=1 is not a root.
    assert (mu+B+C) != 0
    # Contrasts with type-blind competition, where no seven-equilibrium phase exists.
    assert checks==32 and strict>0
    print('PASS: 32 exact rational gradient/dissipation checks; fold ratio discriminant > 0.')

if __name__ == '__main__':
    main()
