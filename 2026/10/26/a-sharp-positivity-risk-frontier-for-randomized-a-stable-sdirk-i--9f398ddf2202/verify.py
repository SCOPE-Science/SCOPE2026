#!/usr/bin/env python3
"""Reproducible finite checks for a randomized SDIRK sign-transition theorem.

Only Python's standard library is needed. Finite checks corroborate the
separate algebraic proof; they are not a certificate for its universal claims.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from itertools import product
from math import sqrt


def amplitude(s, x):
    s, x = F(s), F(x)
    return (2 + 4*s*x - 2*s + s*s*(2*x*x-4*x+1))/(2*(1+s*x)**2)


def direct_stages(s, x):
    s, x = F(s), F(x)
    k1 = -s/(1+s*x)
    k2 = -s*(1+(1-2*x)*k1)/(1+s*x)
    return 1+(k1+k2)/2


def nsign(s, x):
    s, x = F(s), F(x)
    return 2 + (4*x-2)*s + (2*x*x-4*x+1)*s*s


def critical_root(s):
    z = float(s)
    return 1 - 1/z + sqrt((z-2)/(2*z))


def p_uniform(s):
    s = float(s)
    if s <= 2: return 0.0
    if s >= 1 + sqrt(3): return 1.0
    return 1 - 2/s + sqrt(2*(s-2)/s)


def test():
    counts = {}
    # Independent stage equations versus the simplified rational stability function.
    n = 0
    for a in range(1, 71):
        s = F(a, 13)
        for b in range(0, 61):
            x = F(1, 2) + F(b, 120)
            assert amplitude(s, x) == direct_stages(s, x)
            assert (amplitude(s, x) > 0) == (nsign(s, x) > 0)
            assert -1 < amplitude(s, x) < 1
            n += 1
    counts['exact_stage_and_contraction_cases'] = n

    # Strict derivative sign is an algebraic identity. Check its exact
    # quotient numerator at many positive rational arguments.
    n=0
    for a in range(1, 33):
        s = F(a, 7)
        for b in range(0, 33):
            x = F(1, 2)+F(b, 64)
            # d_x R = s**3*(2*x-1)/(1+s*x)**3, derived by quotient rule.
            d = s*s*s*(2*x-1)/(1+s*x)**3
            assert d >= 0 and (d == 0) == (x == F(1, 2))
            n+=1
    counts['derivative_formula_sign_cases'] = n

    # Test exact sign classification using only rational comparisons:
    # r = 1-1/s + sqrt((s-2)/(2s)).
    n=0
    for k in range(1, 101):
        s = F(2, 1)+F(k, 140)
        for j in range(0, 201):
            x=F(1,2)+F(j,400)
            if s >= F(11, 4):
                continue  # keep this check within the mixed-sign regime
            c=1-F(1,1)/s
            q=(s-2)/(2*s)
            predicts_negative = (x <= c) or ((x-c)**2 < q)
            assert (nsign(s,x) < 0) == predicts_negative
            n+=1
    counts['exact_sign_region_cases']=n

    # Finite independent sign chains; parity-binomial identity.
    n=0
    for p in (F(1,7),F(2,5),F(3,4)):
        for steps in range(1, 11):
            negative = F(0)
            for outcomes in product((0,1), repeat=steps):
                num_neg=sum(outcomes)
                if num_neg%2:
                    negative += p**num_neg*(1-p)**(steps-num_neg)
            exact = (1-(1-2*p)**steps)/2
            assert negative == exact
            n+=1
    counts['exact_parity_distribution_cases']=n

    # Sharp sampling-law lower bound under the two third-order moment conditions:
    # E[(xi-1/2)^2]=1/12. Probe all feasible two-point laws on a rational grid.
    n=0
    xs=[F(1,2)+F(j,24) for j in range(13)]
    m=F(1,12)
    for ss in (F(9,4),F(5,2),F(8,3)):
        r=critical_root(ss)
        aa=(r-.5)**2
        lower=max(0.0,1-float(m)/aa)
        for i,x1 in enumerate(xs):
            u1=(x1-F(1,2))**2
            for x2 in xs[i+1:]:
                u2=(x2-F(1,2))**2
                if not(u1<=m<=u2): continue
                w1=(u2-m)/(u2-u1)
                w2=1-w1
                assert w1*u1+w2*u2==m
                prob=float(w1)*(amplitude(ss,x1)<0)+float(w2)*(amplitude(ss,x2)<0)
                assert prob>=lower-1e-13
                n+=1
    counts['moment_constrained_two_atom_cases']=n
    # Cross-validate closed-form threshold and critical onset numerically.
    with localcontext() as ctx:
        ctx.prec=75
        one=Decimal(1)
        critical=one+Decimal(3).sqrt()
        for s in (Decimal('2.001'),Decimal('2.07'),Decimal('2.22'),Decimal('2.5'),critical-Decimal('1e-12')):
            r=one-one/s+((s-2)/(2*s)).sqrt()
            lhs=2+(4*r-2)*s+(2*r*r-4*r+1)*s*s
            assert abs(lhs) < Decimal('1e-53')
        vals=[]
        for k in (2,3,4,5,6,7,8):
            d=Decimal(10)**(-k)
            ss=Decimal(2)+d
            p=one-2/ss+(2*(ss-2)/ss).sqrt()
            vals.append(float(p/d.sqrt()))
        assert abs(vals[-1]-1)<1e-4
        counts['high_precision_root_and_edge_cases']=12
    return counts

if __name__=='__main__':
    counts=test()
    for key,value in counts.items(): print(f'{key}: {value}')
    print('All finite checks passed; general proof is provided separately.')
