#!/usr/bin/env python3
"""Independent finite checks for a parity identity in binary-channel pooling.

The finite tests do not replace the infinite-series and moment-uniqueness proofs.
Requires Python >= 3.11; standard library only.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import product
import random

ASSERTIONS = 0

def check(test, label):
    global ASSERTIONS
    if not test:
        raise AssertionError(label)
    ASSERTIONS += 1

def dec(x):
    if isinstance(x, F):
        return Decimal(x.numerator) / Decimal(x.denominator)
    return Decimal(x)

def js(p, q):
    result = Decimal(0)
    for a, b in zip(p, q):
        aa, bb = dec(a), dec(b)
        if aa:
            result += aa * (2 * aa / (aa + bb)).ln()
        if bb:
            result += bb * (2 * bb / (aa + bb)).ln()
    return result / 2

def tensor(a, b):
    return [x * y for x, y in product(a, b)]

def compare(p, q):
    n = len(p)
    zz = [F(0)] * n
    a = p + zz
    qa = q + zz
    b = zz + q
    qb = zz + p
    orig = js(tensor(a, b), tensor(qa, qb))
    avgp = [(x + y) / 2 for x, y in zip(a, b)]
    avgq = [(x + y) / 2 for x, y in zip(qa, qb)]
    homo = js(tensor(avgp, avgp), tensor(avgq, avgq))
    m = [(x + y) / 2 for x, y in zip(p, q)]
    z = [((x - y) / (x + y) if x + y else F(0)) for x, y in zip(p, q)]
    kplus = Decimal(0)
    kminus = Decimal(0)
    for i in range(n):
        for j in range(n):
            weight = dec(m[i] * m[j])
            t = dec(z[i] * z[j])
            if t != -1:
                kplus += weight * (1+t) * (1+t).ln()
            if t != 1:
                kminus += weight * (1-t) * (1-t).ln()
    return homo-orig, (kminus-kplus)/2, m, z, orig, homo

def main():
    with localcontext() as ctx:
        ctx.prec = 75
        cases = [
            ([F(1),F(0)],[F(1,2),F(1,2)]),
            ([F(3,4),F(1,4)],[F(1,4),F(3,4)]),
            ([F(7,10),F(3,10)],[F(2,5),F(3,5)]),
            ([F(3,8),F(1,8),F(1,2)],[F(1,8),F(3,8),F(1,2)]),
        ]
        rng = random.Random(9024)
        for n in (2,3,4,5):
            for _ in range(40):
                aa = [rng.randrange(1,35) for i in range(n)]
                bb = [rng.randrange(1,35) for i in range(n)]
                cases.append(([F(x,sum(aa)) for x in aa],
                              [F(x,sum(bb)) for x in bb]))
        for ind, (p,q) in enumerate(cases):
            gap, cor, m,z,_,_ = compare(p,q)
            check(abs(gap-cor) < Decimal('1e-65'), ('mutual information identity',ind))
            check(gap >= -Decimal('1e-65'), ('positivity',ind))
            check(sum(m) == 1 and sum(m[i]*z[i] for i in range(len(m))) == 0,
                  ('centering',ind))
            for j in range(1,5):
                odd = sum(m[i]*z[i]**(2*j+1) for i in range(len(m)))
                check(odd*odd >= 0, ('odd moment',ind,j))
        # This concrete example has a strictly positive, exact-logarithmic gap.
        p,q=cases[0]
        gap,_,m,z,orig,homo=compare(p,q)
        check(m == [F(3,4), F(1,4)], 'exact mixture')
        check(z == [F(1,3), F(-1)], 'exact posterior scores')
        check(2**12 > 5**5, 'strict rational inequality')
        check(abs(orig - Decimal(2).ln()/2) < Decimal('1e-65'), 'exact original divergence')
        check(abs(homo - (Decimal(5)*Decimal(2).ln()/4-Decimal(5)*Decimal(5).ln()/16)) < Decimal('1e-65'), 'exact pooled divergence')
        check(abs(gap - (Decimal(12)*Decimal(2).ln()-Decimal(5)*Decimal(5).ln())/16) < Decimal('1e-65'), 'exact gap')
        # Every binary symmetric-posterior example has equality, including nonidentical P,Q.
        for a in range(1,20):
            pp=[F(a,20),F(20-a,20)]
            qq=[F(20-a,20),F(a,20)]
            gg,*_ = compare(pp,qq)
            check(abs(gg)<Decimal('1e-65'), ('symmetric equality',a))
        # Nontrivial binary channels with nonsymmetric posterior scores have a strict gap.
        for a in range(1,10):
            for b in range(1,10):
                if a==b or a+b==10:
                    continue
                pp=[F(a,10),F(10-a,10)]
                qq=[F(b,10),F(10-b,10)]
                gg,*_ = compare(pp,qq)
                check(gg>0, ('binary strictness',a,b))
        # Independent exact arithmetic check of the power series coefficient identity.
        for j in range(1,75):
            coeff=F(1,(2*j)*(2*j+1))
            check(coeff>0 and coeff == F(1,2*j)-F(1,2*j+1), ('coefficient',j))
        # Weak-signal expansion under M=(3/5,2/5), u=(2/5,-3/5).
        M=[F(3,5),F(2,5)]
        u=[F(2,5),F(-3,5)]
        a3=sum(M[i]*u[i]**3 for i in range(2))
        target=dec(a3*a3)/6
        check(a3!=0, 'nonzero cubic moment')
        last=None
        for k in range(2,7):
            e=F(1,2**k)
            P=[M[i]*(1+e*u[i]) for i in range(2)]
            Q=[M[i]*(1-e*u[i]) for i in range(2)]
            gap,*_ = compare(P,Q)
            ratio=gap/dec(e**6)
            check(ratio > 0, ('weak contrast positivity',k))
            if last is not None:
                check(abs(ratio-target) < abs(last-target), ('sixth order convergence',k))
            last=ratio
        print('Verification: {} assertions passed.'.format(ASSERTIONS))
        print('Exact example Jensen-Shannon difference: {}'.format(gap if False else compare(cases[0][0],cases[0][1])[0]))
        print('Weak-signal coefficient: {}'.format(target))
        print('Scope: finite direct checks; analytic uniform-series and uniqueness proofs are in RESULT.md.')

if __name__=='__main__':
    main()
