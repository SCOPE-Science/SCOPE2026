"""Independent finite-precision diagnostic of a two-sided Mallows displacement identity.

Requires only the Python standard library.  The mathematical theorem rests on
an infinite-series proof; finite decimal checks do not certify an infinite claim.
"""
from decimal import Decimal, localcontext


def pochhammer_prefixes(q, length):
    pref = [Decimal(1)]
    for k in range(1, length + 1):
        pref.append(pref[-1] * (1 - q ** k))
    return pref


def compare(q_string, cutoff):
    with localcontext() as ctx:
        ctx.prec = 72
        q = Decimal(q_string)
        pref = pochhammer_prefixes(q, cutoff)
        c = (1 - q) * pref[-1]
        total = Decimal(0)
        signed = Decimal(0)
        for r in range(cutoff + 1):
            coefficient = c * q ** r / pref[r]
            base = q ** (r + 1)
            power = Decimal(1)
            for s in range(cutoff + 1):
                weight = coefficient * power / pref[s]
                total += weight
                signed += weight if (r + s) % 2 == 0 else -weight
                power *= base
        product = Decimal(1)
        for k in range(1, cutoff + 1):
            product *= ((1 - q ** k) / (1 + q ** k)) ** 2
        # Bounds: mass beyond r,s<=N under the *exact* law is <=2q^(N+1),
        # while truncating (q;q)_infty introduces relative error at most
        # q^(N+1)/(1-q) by the elementary infinite-product union bound.
        tail_bound = 2 * q ** (cutoff + 1) + q ** (cutoff + 1) / (1 - q)
        # Truncated sign-product error from omitted factors is <=
        # 4 q^(N+1)/(1-q) by 1-(1-x)^2 <=2x and 1-product <=sum.
        product_tail_bound = 4 * q ** (cutoff + 1) / (1 - q)
        conservative_bound = tail_bound + product_tail_bound + Decimal('1e-54')
        error = abs(signed - product)
        assert error <= conservative_bound, (q_string, error, conservative_bound)
        assert abs(total - 1) <= tail_bound + Decimal('1e-54')
        assert 0 < product < 1
        assert signed > 0
        assert 0 < (1 - product) / 2 < Decimal('0.5')
        return q, signed, product, error, conservative_bound


def main():
    previous = Decimal(2)
    checks = 0
    for qstr, cutoff in [('0.1', 55), ('0.2', 70), ('0.5', 130), ('0.7', 205), ('0.8', 275)]:
        q, signed, product, error, bound = compare(qstr, cutoff)
        assert product < previous
        previous = product
        checks += 6
        print('q=', q, 'product=', str(product)[:40], 'error=', f'{error:.3E}',
              'bound=', f'{bound:.3E}')
    print('PASS:', checks, 'decimal identity, tail-bound and ordering checks')

if __name__ == '__main__':
    main()
