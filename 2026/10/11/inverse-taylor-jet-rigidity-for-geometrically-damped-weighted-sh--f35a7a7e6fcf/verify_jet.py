#!/usr/bin/env python3
"""Finite Jacobi tests for the analytic inverse-germ theorem; not a proof."""
from decimal import Decimal, localcontext

def largest_eigenvalue(weights, q):
    # Symmetric tridiagonal Jacobi matrix, with first edge 1/2 and
    # remaining edges (weights[j-1] q**j)/2.
    edges = [Decimal(1)] + [Decimal(v) * q**j for j, v in enumerate(weights, 1)]
    def characteristic(x):
        before, at = Decimal(1), x
        for w in edges:
            before, at = at, x*at - (w / 2)**2 * before
        return at
    low, high = Decimal('0.5'), Decimal('2')
    assert characteristic(low) < 0 < characteristic(high)
    for _ in range(350):
        mid = (low + high) / 2
        if characteristic(mid) < 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2

def run():
    with localcontext() as ctx:
        ctx.prec = 100
        original = [2, 1, 3, 1, 2, 1, 3, 2]
        for k in range(1, 5):
            modified = original.copy()
            modified[k-1] += 1
            target = Decimal(modified[k-1]**2 - original[k-1]**2) / 4
            for j in range(k-1):
                target *= original[j]**2
            deviations = []
            for s in ('0.05', '0.025'):
                q = Decimal(s)
                lhs = largest_eigenvalue(modified, q) - largest_eigenvalue(original, q)
                ratio = lhs / q**(k*(k+1))
                assert lhs > 0
                assert abs(ratio/target - 1) < Decimal('0.06'), (k, s, ratio, target)
                deviations.append(abs(ratio/target - 1))
            assert deviations[1] < deviations[0], (k, deviations)
        print('INVERSE_JET_FINITE_TRIDIAGONAL_CHECK_OK')

if __name__ == '__main__':
    run()
