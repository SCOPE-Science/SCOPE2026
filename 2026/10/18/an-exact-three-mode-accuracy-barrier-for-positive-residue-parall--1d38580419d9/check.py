"""Reproduce the scalar identities for the positive-residue three-mode minimax theorem.

Uses only Python's standard library. This tests finite scalar cases; the theorem's
universal quantifiers follow from the analytical Jensen proof in RESULT.md.
"""
from decimal import Decimal, localcontext
from random import Random


def main():
    with localcontext() as ctx:
        ctx.prec = 80
        one = Decimal(1)
        two = Decimal(2)
        three = Decimal(3)
        q = one / three
        rt3 = three.sqrt()
        err = (two * rt3 - three) / Decimal(9)
        alpha = (rt3 - one) / two
        weight = two * rt3 / Decimal(9)
        tol = Decimal('1e-72')
        assert abs(Decimal(27) * err * err + Decimal(18) * err - one) < tol
        assert alpha > Decimal('0.25')
        for j in range(3):
            target = q ** j
            actual = weight / (Decimal(j) + alpha)
            assert abs(actual - target - ((-one) ** j) * err) < tol
        delta = one / Decimal(4)
        shift_weight = three ** (-delta) * weight
        for j in range(3):
            at_shift = shift_weight / (Decimal(j) + alpha)
            exact = three ** (-(delta + Decimal(j)))
            assert abs(at_shift - exact - ((-one) ** j) * three ** (-delta) * err) < tol
        for k in range(1, 1000):
            qk = Decimal(k) / Decimal(1000)
            b = three - two*qk + three*qk*qk
            ek = two*qk*(one-qk)**2 / ((b*b+Decimal(16)*qk*(one-qk)**2).sqrt()+b)
            assert ek > 0 and ek < qk
            assert abs(Decimal(4)*ek*ek + b*ek - qk*(one-qk)**2) < Decimal('1e-70')
            assert ek <= err + Decimal('1e-70')
        print('algebraic extremizer, shifted SPD matrix and 999 q-cases: PASS')

    rng = Random(347119)
    checks = 0
    for m in (1, 2, 5, 11):
        for _ in range(500):
            s = [10**rng.uniform(-3, 3) for _ in range(m)]
            w = [10**rng.uniform(-3, 3) for _ in range(m)]
            c = 10**rng.uniform(-5, 1) if rng.randrange(2) else 0.0
            v = [c+sum(wi/(x+si) for wi, si in zip(w,s)) for x in (0.0,1.0,2.0)]
            assert v[2] >= v[0]*v[1]/(2*v[0]-v[1]) - 5e-12*max(v)
            max_err=max(abs(v[j]-3.0**(-j)) for j in range(3))
            assert max_err >= float(err)-2e-12
            checks+=1
    print(f'{checks} independent positive-mixture checks: PASS')
    print('E_star = %.15f; shifted-SPD E_star = %.15f' % (float(err),3**(-.25)*float(err)))


if __name__ == '__main__':
    main()
