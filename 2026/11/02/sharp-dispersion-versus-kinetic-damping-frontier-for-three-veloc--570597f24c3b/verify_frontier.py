"""Reproducibility checks for a sharp relaxation/dispersion frontier.

Only standard-library arithmetic is required; tests supplement the proof.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from random import Random


def stability_polynomial(a, b):
    return 8*a*a*b + 4*a*b*b - a - b


def residual_vw(a, b):
    v = (1-2*a)/(1+2*a)
    w = (1-2*b)/(1+2*b)
    return (v*v-6*v+1)*(w*w-1)+4*(1-v*v)*w


def sharp_bound(q):
    with localcontext() as ctx:
        ctx.prec = 75
        q = Decimal(q.numerator)/Decimal(q.denominator)
        l = (1-q)/(2*(1+q))
        pcrit = (1-4*l*l + (1+24*l*l+16*l**4).sqrt())/16
        return max(l*l, pcrit), l, pcrit


def check():
    random = Random(20261023)
    count_identity = 0
    for _ in range(720):
        a = F(random.randint(1, 45), random.randint(1, 45))
        b = F(random.randint(1, 45), random.randint(1, 45))
        lhs = residual_vw(a,b)
        rhs = -32*stability_polynomial(a,b)/((2*a+1)**2*(2*b+1)**2)
        assert lhs == rhs
        count_identity += 1

    count_grid = 0
    count_stable = 0
    # Exact rational points on and in the allowed relaxation square.
    for k in range(21):
        q = F(k,20)
        if q == 1:
            continue
        lower = F(1-q,2*(1+q))
        upper = F(1+q,2*(1-q))
        for i in range(31):
            for j in range(31):
                a = lower+(upper-lower)*F(i,30)
                b = lower+(upper-lower)*F(j,30)
                p = a*b
                count_grid += 1
                if stability_polynomial(a,b) >= 0:
                    count_stable += 1
                    assert p >= lower*lower
                    # This inequality is equivalent to p >= the positive
                    # root pcrit(lower) when p < 1/4. Use rational arithmetic.
                    if p < F(1,4):
                        assert 8*p*p+(4*lower*lower-1)*p-lower*lower >= 0
                    else:
                        assert p >= F(1,4)

    # Independently compare the polynomial criterion with the published
    # radical boundary, for a grid including both sides of that boundary.
    boundary_checks = 0
    with localcontext() as ctx:
        ctx.prec = 75
        for i in range(1,100):
            sv = Decimal(i)/50
            v = sv-1
            aa = v*v-6*v+1
            bb = 1-v*v
            swstar = 1+aa/((aa*aa+4*bb*bb).sqrt()+2*bb)
            assert abs((v*v-6*v+1)*((swstar-1)**2-1)+4*(1-v*v)*(swstar-1)) < Decimal('1e-67')
            for j in range(1,100):
                sw = Decimal(j)/50
                x = 1/sv-Decimal('0.5')
                y = 1/sw-Decimal('0.5')
                assert (stability_polynomial(x,y)>=0) == (sw<=swstar)
                boundary_checks += 1

    with localcontext() as ctx:
        ctx.prec = 75
        one = Decimal(1)
        count_extreme = 0
        q_values = [F(i,100) for i in range(100)] + [F(1,1000),F(101,1000),F(9999,10000)]
        for q in q_values:
            p, l, pcrit = sharp_bound(q)
            q_dec = Decimal(q.numerator)/Decimal(q.denominator)
            h = (1+q_dec)/(2*(1-q_dec))
            if l*l >= pcrit:
                a, b = l, l
            else:
                a, b = p/l, l
            assert l-Decimal('1e-65') <= a <= h+Decimal('1e-65')
            assert l-Decimal('1e-65') <= b <= h+Decimal('1e-65')
            assert abs(a*b-p) < Decimal('1e-65')
            assert stability_polynomial(a,b) > -Decimal('1e-63')
            if l*l < pcrit:
                assert abs(stability_polynomial(a,b)) < Decimal('1e-63')
            count_extreme += 1
        assert abs(sharp_bound(F(999999,1000000))[0] - Decimal(1)/8) < Decimal('1e-6')
        qstar = 5-2*Decimal(6).sqrt()
        bstar = (1-qstar)/(2*(1+qstar))
        assert abs(6*bstar*bstar-1) < Decimal('1e-65')

    print('PASS exact rational identity:', count_identity)
    print('PASS exact rational grid points:', count_grid, 'stable subset:', count_stable)
    print('PASS high precision published-boundary equivalences:', boundary_checks)
    print('PASS high precision sharp extremizers:', count_extreme)
    print('q crossover ~', qstar)
    for q in [F(0),F(1,10),F(1,5),F(1,2),F(4,5),F(99,100)]:
        print('q =', q, 'minimal magic =',sharp_bound(q)[0])


if __name__=='__main__':
    check()
