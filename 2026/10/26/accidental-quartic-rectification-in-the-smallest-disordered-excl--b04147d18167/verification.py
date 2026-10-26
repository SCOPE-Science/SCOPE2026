#!/usr/bin/env python3
"""Exact finite-state verification of a disordered four-site exclusion current.

Dependencies: Python 3 and SymPy. No remote data or precomputed files are needed.
"""
import itertools
import sympy as sp


def generator_and_current(rates, particles, eps):
    L = len(rates)
    states = list(itertools.combinations(range(L), particles))
    index = {state: k for k, state in enumerate(states)}
    Q = sp.zeros(len(states))
    current = sp.zeros(len(states), 1)
    for col, state in enumerate(states):
        occupied = set(state)
        for i in state:
            for direction in (-1, 1):
                j = (i + direction) % L
                if j not in occupied:
                    rate = rates[i] * (1 + direction * eps) / 2
                    new_state = tuple(sorted((occupied - {i}) | {j}))
                    Q[index[new_state], col] += rate
                    Q[col, col] -= rate
                    current[col] += direction * rate / L
    return Q, current


def exact_current(rates, particles, eps):
    Q, c = generator_and_current(rates, particles, eps)
    M = Q.copy()
    M[-1, :] = sp.ones(1, Q.rows)
    b = sp.zeros(Q.rows, 1)
    b[-1] = 1
    pi = M.inv() * b
    return sp.factor((c.T * pi)[0])


def four_site_schur_current(rates, eps):
    """Independent elimination of adjacent states, leaving two opposite-pair states."""
    a, b, c, d = rates
    alpha, beta = (1 + eps) / 2, (1 - eps) / 2
    # columns: A_i -> B0, A_i -> B1, B0 -> A_i, B1 -> A_i
    table = [
        (alpha*b, beta*a, beta*c, alpha*d),
        (beta*b, alpha*c, alpha*a, beta*d),
        (alpha*d, beta*c, beta*a, alpha*b),
        (beta*d, alpha*a, alpha*c, beta*b),
    ]
    outgoing = [x[0] + x[1] for x in table]
    u = [sp.cancel(table[i][2] / outgoing[i]) for i in range(4)]
    v = [sp.cancel(table[i][3] / outgoing[i]) for i in range(4)]
    r01 = sum(u[i] * table[i][1] for i in range(4))
    r10 = sum(v[i] * table[i][0] for i in range(4))
    x, y = r10, r01  # unnormalized B0, B1 probabilities
    w = [u[i] * x + v[i] * y for i in range(4)]
    # current increments for adjacent pairs, and opposite pairs, per bond
    # A0 (0,1), A1 (1,2), A2 (2,3), A3 (3,0)
    cj = [
        (alpha*b-beta*a)/4,
        (alpha*c-beta*b)/4,
        (alpha*d-beta*c)/4,
        (alpha*a-beta*d)/4,
    ]
    # B0 (0,2) and B1 (1,3): all four moves permitted
    cj0 = (alpha*(a+c)-beta*(a+c))/4
    cj1 = (alpha*(b+d)-beta*(b+d))/4
    return sp.factor((sum(w[i]*cj[i] for i in range(4)) + x*cj0 + y*cj1)/(x+y+sum(w)))


def run():
    e,t = sp.symbols('e t')
    # The direct stationary linear system is not used in the Schur derivation.
    a,b,c,d = sp.symbols('a b c d', positive=True)
    Rgeneral = four_site_schur_current((a,b,c,d),e)
    S=a*b+a*c+a*d+b*c+b*d+c*d
    X,Y,U,V=a+c,b+d,a-c,b-d
    factorized= a*b*c*d*U*V*((Y-X)*(X**2+Y**2)+U**2*(X+3*Y)-V**2*(3*X+Y))/(S**2*(S+a*c+b*d)**2)
    assert sp.cancel(sp.diff(Rgeneral,e,2).subs(e,0)/2-factorized)==0
    R = four_site_schur_current((sp.Integer(2),sp.Integer(3),sp.Integer(4),t),e)
    C2 = sp.factor(sp.diff(R,e,2).subs(e,0)/2)
    expected_C2 = -144*t*(t-11)*(t-3)*(t-2)/((6*t+17)**2*(9*t+26)**2)
    assert sp.cancel(C2-expected_C2) == 0, (C2, expected_C2)

    R11 = sp.factor(R.subs(t,11))
    E=sp.Integer(51875)+38190*e**2-7025*e**4
    O=688*e**3*(e**2-1)
    N=2112*e*(25-4*e**2)*(1+e**2)
    expected_R11=N/(E+O)
    assert sp.cancel(R11-expected_R11)==0
    even=sp.factor((R11+R11.subs(e,-e))/2)
    expected_even=sp.Integer(1453056)*e**4*(25-4*e**2)*(1-e**4)/(E**2-O**2)
    assert sp.cancel(even-expected_even)==0
    c4=sp.factor(sp.diff(even,e,4).subs(e,0)/24)
    assert c4 == sp.Rational(1453056,107640625)
    assert sp.factor(C2.subs(t,2)) == 0
    assert sp.factor(C2.subs(t,3)) == 0
    assert sp.factor(C2.subs(t,11)) == 0
    assert sp.factor(C2.subs(t,4)) != 0
    assert sp.factor((R.subs(t,3)+R.subs({t:3,e:-e}))) == 0
    # No reflectively symmetric four-cycle can have these four distinct rates.
    assert len({2,3,4,11}) == 4

    for rates in [(2,3,4,11),(2,3,4,2),(2,3,4,3),(2,3,4,5)]:
        for eps in [sp.Rational(1,5),sp.Rational(1,2),sp.Rational(3,4)]:
            direct = exact_current(tuple(map(sp.Integer,rates)),2,eps)
            formula = sp.cancel(R.subs({t:rates[3],e:eps}))
            assert sp.cancel(direct-formula) == 0
    # Three-site two-particle case has an explicitly even denominator.
    a,b,c=sp.symbols('a b c',positive=True)
    j3=exact_current((a,b,c),2,e)
    predicted = a*b*c*e*(3+e**2)/((a+b+c)**2-e**2*(a*a+b*b+c*c-2*a*b-2*a*c-2*b*c))
    assert sp.cancel(j3-predicted)==0
    assert sp.cancel(j3+j3.subs(e,-e))==0
    # One-particle currents are bias odd for any site rates.
    j1=exact_current((a,b,c),1,e)
    assert sp.cancel(j1 - e/(1/a+1/b+1/c))==0
    print('PASS: symbolic Schur/current, general quadratic coefficient, exact quartic response,')
    print('      twelve independent rational generator solves, and three-site parity identities.')


if __name__ == '__main__':
    run()
