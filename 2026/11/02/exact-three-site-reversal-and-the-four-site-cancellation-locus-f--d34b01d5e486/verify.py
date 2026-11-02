"""Exact symbolic and independent finite-state checks for trap-rate ASEP current formulas.

Requires sympy >=1.13. Execute: python verify.py
All symbolic coefficients are rational; no floating-point evidence is used.
The finite samples corroborate, but do not prove, the all-parameter statements.
"""
from itertools import combinations
from random import Random
import sympy as sp

COUNT = 0

def check(condition, message):
    global COUNT
    if condition is not True and condition != sp.true:
        raise AssertionError(message)
    COUNT += 1


def generator_hole(rates, e):
    """Q row generator for the single vacancy in the cyclic site-trap ASEP."""
    l = len(rates)
    p, q = (1 + e)/2, (1 - e)/2
    Q = sp.zeros(l)
    for i in range(l):
        for j, rate in [((i + 1) % l, q * rates[(i + 1) % l]),
                        ((i - 1) % l, p * rates[(i - 1) % l])]:
            Q[i, j] += rate
            Q[i, i] -= rate
    return Q


def current_full_exclusion(rates, e, particles):
    """Independent exact master equation for all N-particle occupation patterns."""
    l = len(rates)
    states = list(combinations(range(l), particles))
    index = {st:i for i, st in enumerate(states)}
    Q = sp.zeros(len(states)); p, q = (1 + e)/2, (1 - e)/2
    for i, st in enumerate(states):
        stset = set(st)
        for u in st:
            for v, rate in [((u+1)%l, p*rates[u]),
                            ((u-1)%l, q*rates[u])]:
                if v not in stset:
                    dst = tuple(sorted(stset - {u} | {v}))
                    j = index[dst]
                    Q[i,j] += rate
                    Q[i,i] -= rate
    lhs = Q.T.copy()
    for j in range(len(states)):
        lhs[len(states)-1,j] = 1
    rhs = sp.zeros(len(states),1)
    rhs[len(states)-1,0] = 1
    sol = lhs.inv()*rhs
    flux = 0
    for i,st in enumerate(states):
        stset=set(st)
        if 0 in stset and 1 not in stset:
            flux += p*rates[0]*sol[i]
        if 1 in stset and 0 not in stset:
            flux -= q*rates[1]*sol[i]
    return sp.factor(flux), sol, states


def tree_flux(rates,e):
    Q = generator_hole(rates,e)
    t = [sp.factor((-Q).minor_submatrix(i,i).det(method='berkowitz'))
         for i in range(len(rates))]
    p,q=(1+e)/2,(1-e)/2
    return sp.factor(p*rates[0]*t[1]-q*rates[1]*t[0]), sp.factor(sum(t))


def three_formula(rates,e):
    a,b,c = rates
    den=(a+b+c)**2-e**2*(a*a+b*b+c*c-2*(a*b+a*c+b*c))
    return a*b*c*e*(3+e*e)/den


def four_formula(rates,e):
    a,b,c,d=rates
    X,Y,U,V=a+c,b+d,a-c,b-d
    H=X*Y*(X+Y)*(1+e**2)-2*e**2*(U**2*Y+V**2*X)+e*(1-e**2)*U*V*(X-Y)
    return 4*a*b*c*d*e*(1+e**2)/H


def symbolic_identities():
    e=sp.symbols('e');a,b,c,d=sp.symbols('a b c d')
    n3,s3=tree_flux([a,b,c],e)
    check(sp.cancel(n3/s3-three_formula([a,b,c],e))==0,
          'three-site current symbolic identity')
    check(sp.factor(n3-a*b*c*e*(3+e**2)/4)==0,
          'three-site cofactor current numerator')
    den3=(a+b+c)**2-e**2*(a*a+b*b+c*c-2*(a*b+a*c+b*c))
    check(sp.factor(s3-den3/4)==0, 'three-site cofactor normalization')
    check(sp.factor(three_formula([a,b,c],e)+three_formula([a,b,c],-e))==0,
          'three-site all-parameter odd symmetry')
    n4,s4=tree_flux([a,b,c,d],e)
    check(sp.cancel(n4/s4-four_formula([a,b,c,d],e))==0,
          'four-site current symbolic identity')
    check(sp.factor(n4-a*b*c*d*e*(1+e**2)/2)==0,
          'four-site cofactor current numerator')
    X,Y,U,V=a+c,b+d,a-c,b-d
    H4=X*Y*(X+Y)*(1+e**2)-2*e**2*(U**2*Y+V**2*X)+e*(1-e**2)*U*V*(X-Y)
    check(sp.factor(s4-H4/8)==0, 'four-site cofactor normalization')
    X,Y,U,V=a+c,b+d,a-c,b-d
    K=U*V*(X-Y)
    H0=X*Y*(X+Y)*(1+e**2)-2*e**2*(U*U*Y+V*V*X)
    E=-4*a*b*c*d*e**2*(1-e**2)*(1+e**2)*K/(H0**2-e**2*(1-e**2)**2*K**2)
    check(sp.cancel((four_formula([a,b,c,d],e)+four_formula([a,b,c,d],-e))/2-E)==0,
          'exact even response formula')
    check(sp.factor(sp.diff(four_formula([a,b,c,d],e),e,2).subs(e,0)/2+
          4*a*b*c*d*K/(X**2*Y**2*(X+Y)**2))==0,
          'sharp quadratic rectification coefficient')
    for k,vals in enumerate([(1,2,3,4),(1,2,4,3),(1,2,3,5),
                             (1,2,4,3),(1,2,3,4)]):
        e0=sp.Rational(1,2)
        r=[sp.Integer(v) for v in vals]
        check(sp.cancel(four_formula(r,e0)+four_formula(r,-e0))==0
              if (r[0]-r[2])*(r[1]-r[3])*(r[0]+r[2]-r[1]-r[3])==0
              else sp.cancel(four_formula(r,e0)+four_formula(r,-e0))!=0,
              'four-site symmetry classifier %d' % k)


def independent_full_chain_tests():
    rng=Random(172901)
    count=0
    for length, n in [(3,1),(3,2),(4,3)]:
        for _ in range(40):
            w=[sp.Rational(rng.randint(1,9),rng.randint(1,5)) for i in range(length)]
            e=sp.Rational(rng.randint(-6,6),7)
            measured, sol, states=current_full_exclusion(w,e,n)
            if length==3 and n==1:
                predicted=e/sum(1/z for z in w)
            elif length==3:
                predicted=three_formula(w,e)
            else:
                predicted=four_formula(w,e)
            check(sp.cancel(measured-predicted)==0, f'independent chain L={length}, N={n}')
            check(sp.factor(sum(sol)-1)==0, 'probabilities normalize')
            check(all(z>=0 for z in sol),'probabilities nonnegative')
            count+=1
    # a non-geometric exact-reversal four-site example, with all four rates distinct
    w=list(map(sp.Integer,[1,2,4,3]));e=sp.Rational(3,5)
    check(sp.cancel(four_formula(w,e)+four_formula(w,-e))==0,
          'balanced alternating sums reverse symmetrically')
    # A fully asymmetric sample with a nonzero current even-part.
    w=list(map(sp.Integer,[1,2,3,5]));e=sp.Rational(1,2)
    expect=sp.Rational(3240,398603)
    check(sp.cancel(four_formula(w,e)+four_formula(w,-e)-expect)==0,
          'sample full current even-part')
    check(sp.cancel(four_formula(w,e)-sp.Rational(60,277))==0,
          'positive half-bias sample')
    check(sp.cancel(four_formula(w,-e)+sp.Rational(300,1439))==0,
          'negative half-bias sample')
    return count

if __name__=='__main__':
    symbolic_identities()
    n=independent_full_chain_tests()
    print(f'PASS: {COUNT} exact assertions; {n} independent full-configuration stationary systems. All arithmetic rational/symbolic.')
