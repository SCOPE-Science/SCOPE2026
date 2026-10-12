#!/usr/bin/env python3
"""Exact covariance sign-table verification for three-letter Bernoulli patterns.

Requires Python 3 and SymPy. All assertions use rational or symbolic arithmetic.
"""
from itertools import combinations, product
from sympy import Matrix, eye, zeros, ones, symbols, Rational, factor, fraction, sign, count_roots, Poly, gcd, sympify

WORDS = [''.join(t) for t in product('HT', repeat=3)]
p = symbols('p', real=True)

TABLE = {
    ('HHH', 'HHT'): ('-(p**4 + 2*p**3 + 3*p**2 - 2*p - 1)/p**4', 1),
    ('HHH', 'HTH'): ('-(p**4 - 2*p**3 - 4*p**2 - 2*p + 2)/(p**3*(p**2 - p - 1))', 1),
    ('HHH', 'HTT'): ('-(p**3 + 3*p**2 + 4*p - 1)/(p**2*(p**3 - p + 1))', 1),
    ('HHH', 'THH'): ('-(5*p**4 + 2*p**3 + 2*p**2 - 2*p - 1)/p**4', 1),
    ('HHH', 'THT'): ('(p + 1)*(p**3 - 2*p - 5)/(p*(p**2 - p + 1))', 0),
    ('HHH', 'TTH'): ('(p**4 - 3*p**3 - 6*p**2 - 2*p + 1)/(p**2*(p**3 - p + 1))', 1),
    ('HHH', 'TTT'): ('(p**4 - 2*p**3 + 2*p**2 - p + 12)/(p**4 - 2*p**3 - p**2 + 2*p - 1)', 0),
    ('HHT', 'HTH'): ('-(p**5 - 4*p**4 + 5*p**3 + 3*p**2 - 6*p + 2)/(p**3*(p - 2)*(p - 1)**2)', 0),
    ('HHT', 'HTT'): ('-(p**3 - 6*p**2 + 5*p - 1)/(p**2*(p - 1)**2*(p**2 - p + 1))', 2),
    ('HHT', 'THH'): ('(p**7 - 3*p**5 + 3*p**4 + 5*p**3 - 6*p**2 + 1)/(p**4*(p - 1)**2)', 0),
    ('HHT', 'THT'): ('-(5*p**3 - 7*p**2 - 3*p + 4)/(p*(p - 1)**2)', 1),
    ('HHT', 'TTH'): ('-(p**2 - p - 1)*(p**4 - 2*p**3 + 6*p**2 - 5*p + 1)/(p**2*(p - 1)**2*(p**2 - p + 1))', 2),
    ('HTH', 'HTT'): ('-(p**3 - 2*p**2 - 4*p + 1)/(p**2*(p - 1))', 1),
    ('HTH', 'THH'): ('-(2*p**5 - 6*p**4 + 6*p**3 + 3*p**2 - 6*p + 2)/(p**3*(p - 2)*(p - 1)**2)', 0),
    ('HTH', 'THT'): ('(p**6 - 3*p**5 + p**4 + 3*p**3 - p**2 - p + 1)/(p**2*(p - 1)**2*(p**2 - p + 1))', 0),
    ('HTT', 'THH'): ('-(p**4 - 2*p**3 - 4*p**2 + 5*p - 1)/(p**2*(p - 1)**2)', 2),
}

POSITIVE_DENOMINATORS = {
    ('HHH', 'HHT'): 'p**4',
    ('HHH', 'HTH'): '-p**3*(p**2 - p - 1)',
    ('HHH', 'HTT'): 'p**2*(p**3 - p + 1)',
    ('HHH', 'THH'): 'p**4',
    ('HHH', 'THT'): 'p*(p**2 - p + 1)',
    ('HHH', 'TTH'): 'p**2*(p**3 - p + 1)',
    ('HHH', 'TTT'): '-p**4 + 2*p**3 + p**2 - 2*p + 1',
    ('HHT', 'HTH'): '-p**3*(p - 2)*(p - 1)**2',
    ('HHT', 'HTT'): 'p**2*(p - 1)**2*(p**2 - p + 1)',
    ('HHT', 'THH'): 'p**4*(p - 1)**2',
    ('HHT', 'THT'): 'p*(p - 1)**2',
    ('HHT', 'TTH'): 'p**2*(p - 1)**2*(p**2 - p + 1)',
    ('HTH', 'HTT'): '-p**2*(p - 1)',
    ('HTH', 'THH'): '-p**3*(p - 2)*(p - 1)**2',
    ('HTH', 'THT'): 'p**2*(p - 1)**2*(p**2 - p + 1)',
    ('HTT', 'THH'): 'p**2*(p - 1)**2',
}

def automaton(targets):
    """Transient states are the proper prefixes of the specified words."""
    states = [''] + sorted({w[:i] for w in targets for i in (1, 2)})
    states = list(dict.fromkeys(states))
    trans = {}
    for s in states:
        for c in 'HT':
            t = s + c
            done = next((w for w in targets if t.endswith(w)), None)
            if done is None:
                trans[s, c] = max((u for u in states if t.endswith(u)), key=len)
            else:
                trans[s, c] = ('done', done)
    return states, trans


def remaining(target, probability, suffix):
    states, trans = automaton([target]); k = len(states)
    index = {s: i for i, s in enumerate(states)}; Q = zeros(k)
    for s in states:
        for c, prob in (('H', probability), ('T', 1-probability)):
            nxt = trans[s, c]
            if isinstance(nxt, str): Q[index[s], index[nxt]] += prob
    m = (eye(k)-Q).inv() * ones(k, 1)
    start = max((v for v in states if suffix.endswith(v)), key=len)
    return m[index[start]]


def via_first_occurrence(a, b, probability):
    states, trans = automaton([a, b]); k = len(states)
    index = {s: i for i, s in enumerate(states)}
    Q=zeros(k); ra=zeros(k, 1); rb=zeros(k, 1)
    for s in states:
        for c, prob in (('H', probability), ('T', 1-probability)):
            nxt = trans[s, c]
            if isinstance(nxt, tuple):
                if nxt[1] == a: ra[index[s]] += prob
                else: rb[index[s]] += prob
            else: Q[index[s], index[nxt]] += prob
    N=(eye(k)-Q).inv(); m=N*ones(k, 1)
    s=(2*N-eye(k))*m
    wa=N*ra;wb=N*rb
    e_ta=N*wa;e_tb=N*wb
    ua=remaining(a, probability, b)
    ub=remaining(b, probability, a)
    E_ab=s[0]+ub*e_ta[0]+ua*e_tb[0]
    E_a=m[0]+ua*wb[0]
    E_b=m[0]+ub*wa[0]
    return factor(E_ab-E_a*E_b)


def via_joint_reward(a, b, probability):
    """Independent Markov reward computation keeping two observed-pattern flags."""
    start=('', False, False);states=[start];index={start:0}
    for tail, seen_a, seen_b in states:
        for c in 'HT':
            t=tail+c;fa=seen_a or t.endswith(a);fb=seen_b or t.endswith(b)
            if fa and fb:continue
            v=(t[-2:],fa,fb)
            if v not in index:index[v]=len(states);states.append(v)
    k=len(states);Q=zeros(k);ca=zeros(k,1);cb=zeros(k,1)
    for state in states:
        tail,fa,fb=state;i=index[state]
        ca[i]=int(not fa);cb[i]=int(not fb)
        for c,pr in (('H',probability),('T',1-probability)):
            t=tail+c;na=fa or t.endswith(a);nb=fb or t.endswith(b)
            if not (na and nb):Q[i,index[(t[-2:],na,nb)]]+=pr
    N=(eye(k)-Q).inv();ua=N*ca;ub=N*cb
    cross=N*(ca.multiply_elementwise(cb)+ca.multiply_elementwise(Q*ub)+cb.multiply_elementwise(Q*ua))
    return factor(cross[0]-ua[0]*ub[0])


def main():
    # One representative for each complement orbit; the other member uses p -> 1-p.
    allpairs=list(combinations(WORDS,2))
    assert len(allpairs)==28 and len(TABLE)==16
    seen=set(); roots_total=0
    for (a,b),(expression,number_roots) in TABLE.items():
        seen.add((a,b))
        complement=lambda w:w.translate(str.maketrans('HT','TH'))
        seen.add(tuple(sorted([complement(a),complement(b)])))
        actual=via_first_occurrence(a,b,p)
        assert factor(actual-sympify(expression, locals={'p':p}))==0,(a,b,actual)
        assert factor(actual-via_joint_reward(a,b,p))==0,(a,b,'independent symbolic recurrence')
        numerator,denominator=fraction(actual)
        Dsign=sign(denominator.subs(p,Rational(1,2)))
        D=factor(Dsign*denominator);P=factor(Dsign*numerator)
        assert Dsign in (1,-1)
        # Symbolic factor identity. All factors are strictly positive for 0<p<1:
        # p, 1-p, 2-p, 1+p-p**2, 1-p+p**3, p**2-p+1,
        # and 1-2p(1-p)-[p(1-p)]**2 (at least 7/16).
        asserted_den=sympify(POSITIVE_DENOMINATORS[a,b],locals={'p':p})
        assert factor(D-asserted_den)==0
        assert P.subs(p,0)!=0 and P.subs(p,1)!=0
        assert count_roots(P,0,1)==number_roots,(a,b,'root count')
        assert gcd(Poly(P,p), Poly(P.diff(p),p)).degree()==0,(a,b,'multiple root')
        roots_total+=number_roots
    assert len(seen)==28 and all(x in seen for x in allpairs)
    # Independent rational comparisons also check the complement cases.
    rational_tests=0
    for a,b in allpairs:
        for prob in (Rational(1,5),Rational(1,2),Rational(4,5)):
            assert via_first_occurrence(a,b,prob)==via_joint_reward(a,b,prob)
            rational_tests+=1
    # Explicit double-crossover illustration.
    x=factor(via_first_occurrence('HHT','HTT',p))
    assert factor(x+(p**3-6*p**2+5*p-1)/(p**2*(1-p)**2*(p**2-p+1)))==0
    assert count_roots(p**3-6*p**2+5*p-1,0,1)==2
    print('VERIFY_OK', 'pair_orbits=16','all_pairs=28',
          'symbolic_cross_checks=16','rational_cross_checks='+str(rational_tests),
          'representative_interior_zeros='+str(roots_total),
          'sturm_certificates=16')

if __name__=='__main__': main()
