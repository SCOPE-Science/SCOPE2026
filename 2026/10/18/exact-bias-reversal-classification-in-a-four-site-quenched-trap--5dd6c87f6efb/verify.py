"""Independent checks of the four-site, one-vacancy trap-ASEP current law.

Usage: python verify.py
Dependencies: sympy, numpy.
"""
import itertools
import numpy as np
import sympy as sp


def exact_tree_test():
    a, b, c, d, eps = sp.symbols('a b c d eps')
    w = [a, b, c, d]
    p, q = (1 + eps) / 2, (1 - eps) / 2
    right = lambda i: q * w[(i + 1) % 4]
    left = lambda i: p * w[(i - 1) % 4]
    tau = []
    for i in range(4):
        j, k, m = ((i + h) % 4 for h in (1, 2, 3))
        tau.append(sp.expand(right(j)*right(k)*right(m)
                             +left(j)*right(k)*right(m)
                             +left(j)*left(k)*right(m)
                             +left(j)*left(k)*left(m)))
    direct = (p*a*tau[1] - q*b*tau[0]) / sum(tau)
    U, V = a+c, b+d
    x, y = a-c, b-d
    delta = x*y*(U-V)
    H = U*V*(U+V) - 2*(V*x*x + U*y*y)
    E = U*V*(U+V) + eps**2*H
    P = E + eps*(1-eps**2)*delta
    formula = 4*a*b*c*d*eps*(1+eps**2)/P
    assert sp.cancel(direct - formula) == 0
    leading = 4*a*b*c*d/(U*V*(U+V))
    quadratic = -4*a*b*c*d*delta/(U**2*V**2*(U+V)**2)
    assert sp.simplify(sp.limit(formula/eps,eps,0)-leading) == 0
    assert sp.simplify(sp.limit((formula-leading*eps)/eps**2,eps,0)-quadratic) == 0
    parity_numerator = sp.cancel((formula+formula.subs(eps,-eps))*(E**2-(eps*(1-eps**2)*delta)**2))
    assert sp.expand(parity_numerator +8*a*b*c*d*eps**2*(1+eps**2)*(1-eps**2)*delta) == 0
    print('Symbolic identities: stationary current, first two response coefficients, rectification sign: PASS')


def linear_stationarity(rates, eps):
    n = len(rates)
    G = np.zeros((n,n))
    p, q = (1+eps)/2, (1-eps)/2
    for i in range(n):
        for j, rate in [((i+1)%n,q*rates[(i+1)%n]),
                        ((i-1)%n,p*rates[(i-1)%n])]:
            G[j,i] += rate
            G[i,i] -= rate
    A=G.copy(); A[-1,:] = 1
    rhs=np.zeros(n);rhs[-1]=1
    state=np.linalg.solve(A,rhs)
    assert min(state)>0 and abs(sum(state)-1)<1e-12
    return p*rates[0]*state[1]-q*rates[1]*state[0]


def three_site_exact_test():
    a,b,c,eps=sp.symbols('a b c eps')
    w=[a,b,c];p=(1+eps)/2;q=(1-eps)/2
    r=lambda i:q*w[(i+1)%3]
    ell=lambda i:p*w[(i-1)%3]
    tau=[]
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        tau.append(sp.expand(r(j)*r(k)+ell(j)*r(k)+ell(j)*ell(k)))
    actual=(p*a*tau[1]-q*b*tau[0])/sum(tau)
    target=a*b*c*eps*(3+eps**2)/((a+b+c)**2-eps**2*((a+b+c)**2-4*(a*b+b*c+a*c)))
    assert sp.cancel(actual-target)==0
    assert sp.cancel(target+target.subs(eps,-eps))==0
    print('Three-site exact one-vacancy formula and parity: PASS')


def numeric_test():
    for rates in ((1,2,4,3),(1,2,4,5),(1,2,3,4),(5,2,4,3),(1,5,1,2),(3,4,5,4)):
        a,b,c,d=map(float,rates)
        U,V=a+c,b+d
        H=U*V*(U+V)-2*(V*(a-c)**2+U*(b-d)**2)
        delta=(a-c)*(b-d)*(U-V)
        for eps in (-.9,-.7,-.25,-.001, .001,.25,.7,.9):
            P=U*V*(U+V)+eps**2*H+eps*(1-eps**2)*delta
            proposed=4*a*b*c*d*eps*(1+eps**2)/P
            actual=linear_stationarity(rates,eps)
            assert abs(proposed-actual)<1e-11*(1+abs(proposed)), (rates,eps,proposed,actual)
        symmetric=abs(delta)<1e-10
        parity_error=linear_stationarity(rates,.7)+linear_stationarity(rates,-.7)
        assert (abs(parity_error)<1e-12)==symmetric
        if not symmetric:
            assert np.sign(parity_error)==-np.sign(delta)
    # Three sites with two particles: an odd current for arbitrary positive site rates.
    for rates in ((1,2,4),(3,5,7),(1,1,4)):
        for eps in (.01,.4,.8):
            assert abs(linear_stationarity(rates,eps)+linear_stationarity(rates,-eps))<1e-12
    print('Numeric Markov-generator solves: 48 four-site tests, six parity cases, nine three-site tests: PASS')


if __name__=='__main__':
    exact_tree_test()
    three_site_exact_test()
    numeric_test()
