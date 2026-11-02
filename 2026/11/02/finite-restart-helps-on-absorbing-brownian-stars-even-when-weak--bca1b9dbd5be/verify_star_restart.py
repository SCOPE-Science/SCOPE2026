#!/usr/bin/env python3
"""Reproduce exact arithmetic and independent discrete-graph approximations for a resetting Brownian star."""
import math
from fractions import Fraction


def transform(q, z):
    """Laplace transform of the no-restart exit time at s=z*z (unit diffusion)."""
    def csch(x):
        t = math.exp(-x)
        return 2*t/(1-t*t)
    numerator = csch(z) + q*csch(q*z)
    def coth(x):
        t = math.exp(-2*x)
        return (1+t)/(1-t)
    denominator = coth(z) + q*coth(q*z)
    return numerator/denominator


def reset_mean(q, z):
    f = transform(q,z)
    return (1-f)/(z*z*f)


def bare_mean(q):
    return (1+q*q)/4


def bare_second_moment(q):
    return (1+q**4)/24 + (1+q*q)**2/12


def independent_chain_approximation(q, subdivision, z):
    """Solve a continuous-time absorbing random walk on the subdivided star.

    Interior edge rates are 1/h^2; central-to-each-edge rates are
    2/(degree*h^2). These generators converge to Kirchhoff Brownian motion.
    Computes both unreset mean exit and discounted absorption by sparse solves.
    """
    import numpy as np
    from scipy.sparse import lil_matrix, identity
    from scipy.sparse.linalg import spsolve

    n = subdivision
    length_counts = [n] + [q*n]*q
    n_states = 1 + sum(k-1 for k in length_counts)
    Q = lil_matrix((n_states,n_states), dtype=float)
    b = np.zeros(n_states)
    scale = float(n*n)
    d = len(length_counts)
    nxt = 1
    for M in length_counts:
        prev = 0
        for j in range(1,M+1):
            u = nxt if j<M else None
            if j<M:
                nxt += 1
                Q[prev,prev] -= (2.0/d if prev==0 else 1.0)*scale
                Q[prev,u] += (2.0/d if prev==0 else 1.0)*scale
                Q[u,u] -= scale
                Q[u,prev] += scale
            else:
                Q[prev,prev] -= (2.0/d if prev==0 else 1.0)*scale
                b[prev] += (2.0/d if prev==0 else 1.0)*scale
            prev = u
    assert nxt == n_states
    L = Q.tocsr()
    mfpt = spsolve(-L, np.ones(n_states))[0]
    discounted = spsolve(z*z*identity(n_states,format='csr')-L,b)[0]
    return mfpt, discounted


def main():
    # A strict, rational lower bound for (log 4)^2.
    # log(2)=2(1/3+1/(3*3^3)+...) > 56/81 > 69/100.
    assert Fraction(56,81)>Fraction(69,100)
    assert Fraction(69,50)**2>Fraction(17613,9250)
    assert Fraction(69,50)**2>Fraction(19,10)

    # q=4 has a separate exact rational calculation.
    q=4
    w=Fraction(4**q)
    numerator=Fraction(3,5)+q*(w-1)/(w+1)
    denominator=Fraction(8,15)+2*q*w/(w*w-1)
    assert numerator/denominator == Fraction(299421,37000)
    assert (numerator/denominator)/Fraction(17,4)==Fraction(17613,9250)

    # q>=5 follows from the polynomial comparison, strictly increasing thereafter.
    assert 19*5**2-75*5-26 > 0
    assert all(19*q*q-75*q-26>0 for q in range(5,501))
    z=math.log(4)
    print('q  CV^2  reset/no-reset  predicted asymptotic q*ratio')
    for q in (4,5,6,8,12,25,50,100,1000):
        cv2=1-4*q*q/(3*(1+q*q)**2)
        ratio=reset_mean(q,z)/bare_mean(q)
        assert cv2 < 1 and ratio < 1
        print(q, f'{cv2:.10f}', f'{ratio:.10f}', f'{q*ratio:.8f}')
    assert abs(1000*reset_mean(1000,z)/bare_mean(1000) - 15/(2*z*z)) < 0.01

    for q in (4,5,7):
        mu=bare_mean(q)
        var=bare_second_moment(q)-mu*mu
        assert abs((mu*mu-var)/2-q*q/24)<1e-9
        for r in (1.e-3,1.e-4):
            ratio=reset_mean(q,math.sqrt(r))-mu
            assert ratio>0
        print('local derivative q=',q,'=',q*q/24)

    # Independent discretized PDE: finite-state resolvent, rather than hyperbolic ratios.
    for q in (4,5):
        for n in (8,16,32):
            mfpt,discount=independent_chain_approximation(q,n,z)
            assert abs(mfpt-bare_mean(q))<1e-8
            assert abs(discount-transform(q,z)) < 2e-3
            print('discrete q',q,'steps/unit',n,'mean',mfpt,
                  'Laplace abs error',abs(discount-transform(q,z)))
    print('PASS: rational, moment, asymptotic, and independent resolvent tests')


if __name__=='__main__':
    main()
