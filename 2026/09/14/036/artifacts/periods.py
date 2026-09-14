"""Numerically confirm the rank-2 period lemma of DRAFT.md Sec.4:
on C_h: w^2 = 2h - x^6/3 at h=1/2, the period vectors of dx/w and x^3 dx/w
over independent loops encircling root pairs are linearly independent (det != 0).
"""
import mpmath as mp

mp.mp.dps = 60
h = mp.mpf('0.5')
roots = [(3*h)**(mp.mpf(1)/6)*mp.e**(1j*mp.pi*k/3) for k in range(6)]

def integrand(x, j):
    return x**j/mp.sqrt(2*h - x**6/3)

def pair_loop_integral(j, r1, r2):
    f = lambda s: integrand(r1+(r2-r1)*s, j)*(r2-r1)
    return 2*mp.quad(f, [0, 1])

print("roots:")
for r in roots:
    print("  ", r)
for j in (0, 3):
    print(f"--- j={j} ---")
    for k in range(3):
        print(f"pair {2*k},{2*k+1}: {pair_loop_integral(j, roots[2*k], roots[2*k+1])}")
pairs = [(0, 1), (1, 2)]
M = mp.matrix([[pair_loop_integral(0, roots[a], roots[b]),
                pair_loop_integral(3, roots[a], roots[b])] for (a, b) in pairs])
print("period matrix M =", M)
d = mp.det(M)
print("det(M) =", d)
print("|det| =", abs(d))
assert abs(d) > 1, "period determinant unexpectedly small"
print("RANK-2 PERIOD LEMMA NUMERICALLY CONFIRMED.")
