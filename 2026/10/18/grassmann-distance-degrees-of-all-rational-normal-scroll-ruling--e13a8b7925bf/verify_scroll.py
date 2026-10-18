#!/usr/bin/env python3
"""Exact symbolic sample checks for the scroll ruling-curve GD calculation.

This checks valid block-diagonal orthogonal-projector data, not a proof of
any assertion for arbitrary degrees; the all-degree argument is in RESULT.md.
Requires Python 3 and SymPy.
"""
from sympy import symbols, Poly, lcm, gcd as pgcd, totient

t = symbols('t')


def check_case(name, blocks):
    s = []
    q = []
    g = []
    for w in blocks:
        n = len(w) - 1
        si = Poly(sum(t**(2*j) for j in range(n+1)), t, domain='QQ')
        qi = sum(c*c for c in w)
        gi = Poly(sum(c*t**j for j,c in enumerate(w)), t, domain='QQ')
        assert qi != 0
        s.append(si); q.append(qi); g.append(gi)
    L = s[0]
    for p in s[1:]:
        L = lcm(L,p)
    R = Poly(0,t,domain='QQ')
    for si,qi,gi in zip(s,q,g):
        R += (L.exquo(si)*gi*gi).quo_ground(qi)
    assert pgcd(L,R).degree()==0, f'pole cancellation for {name}'
    delta=L.degree()
    H = R.diff()*L-R*L.diff()
    assert H.degree()==2*delta-2, (name,'at-infinity ramification')
    assert pgcd(H,H.diff()).degree()==0, (name,'repeated critical root')
    cut=Poly(1,t,domain='QQ')
    for gi in g: cut *= gi
    assert pgcd(H,cut).degree()==0, (name,'critical point on algebraic cut locus')
    assert H.eval(0)!=0, (name,'critical point at 0 is allowed but excluded in this sample')
    expected=sum(int(totient(e)) for e in range(3,2*max(len(w) for w in blocks)+1)
                 if any(2*len(w)%e==0 for w in blocks))
    assert expected==delta, (name,expected,delta)
    print(f'{name}: multidegree={tuple(len(w)-1 for w in blocks)},'
          f' poles={delta}, distinct simple critical points={2*delta-2}')


if __name__=='__main__':
    cases=[
        ('equal blocks',[[1,2,3],[2,1,3]]),
        ('coprime block lengths',[[1,2,3],[2,1,3,1]]),
        ('shared cyclotomic poles',[[1,2,3],[2,1,3,1,2,1]]),
        ('three blocks',[[1,2,3],[2,1,3],[3,1,1]]),
        ('larger blocks',[[1,2,3,4],[2,1,3,1,2]]),
    ]
    for name,blocks in cases:
        check_case(name,blocks)
    print('All exact sample checks passed.')
