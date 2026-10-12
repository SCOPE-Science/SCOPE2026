"""Exact tests for the torus singularity of polygonal universal adjoints.

Run with Python 3 and SymPy: python verify_cycle.py
All checks use exact integer/rational linear algebra.
"""
import sympy as sp


def cycle_hessian(coeff):
    n = len(coeff)
    h = sp.zeros(n)
    for i, a in enumerate(coeff):
        j = (i + 1) % n
        h[i, j] += a
        h[j, i] += a
    return h


for n in (4, 5, 6, 8, 10, 12):
    h = cycle_hessian([1] * n)
    assert h.rank() == (n - 2 if n % 4 == 0 else n)
    print(f"n={n} constant weights: rank={h.rank()}")

w_balanced = [2, 3, 3, 2, 5, 7, 7, 5]
w_unbalanced = [2, 3, 3, 2, 5, 7, 7, 6]
assert sp.prod(w_balanced[::2]) == sp.prod(w_balanced[1::2])
assert cycle_hessian(w_balanced).rank() == 6
assert cycle_hessian(w_unbalanced).rank() == 8
print('weighted n=8: balanced rank=6, unbalanced rank=8')

n = 8
x = sp.symbols(f'x0:{n}')
f = sum(sp.prod(x[j] for j in range(n) if j not in {i, (i+1) % n}) for i in range(n))
point = [-2, -3, 2, 3, -2, -3, 2, 3]
substitution = dict(zip(x, point))
assert f.subs(substitution) == 0
assert all(sp.diff(f, a).subs(substitution) == 0 for a in x)
assert sp.hessian(f, x).subs(substitution).rank() == 6
print('n=8 universal adjoint: direct gradient zero, Hessian rank=6 at torus point')
print('VERIFY_OK')
