#!/usr/bin/env python3
"""Finite arithmetic consistency tests for the stated symbolic HN filtration.

This does not certify existence of bundles or all genera; those are proved by
normal and evaluation exact sequences in RESULT.md.
"""

def verify(g):
    assert isinstance(g, int) and g >= 3
    deg_L, deg_A = g + 4, 2
    steps = (2*deg_L + (g-2)*deg_A,
             2*deg_L - deg_A,
             deg_L + 2*deg_A)
    assert steps == (4*g + 4, 2*g + 6, g + 8)
    assert steps[0] > steps[1] > steps[2]
    # Tensor-product determinant identity: L^(2+2+1) A^(g-2-1+2).
    assert 2+2+1 == 5 and (g-2)-1+2 == g-1
    assert sum(steps) == 5*deg_L + (g-1)*deg_A
    # Adjunction: deg(N) = 5 deg(C) + deg(K_C).
    assert sum(steps) == 5*(g+4) + 2*g-2
    # Normal-scroll rank two quotient consistency.
    assert sum(steps[1:]) == 3*deg_L + deg_A

if __name__ == '__main__':
    for g in range(3, 10004):
        verify(g)
    print('VERIFY_OK: degree, strict HN gaps and determinant checks for g=3..10003')
