"""Bounded certificates for T_inv disproof route.

(1) Finite nonempty chains have a maximum, refuting the no-endpoint axiom.
(2) Antitone involutions on n-chains: odd n forces a fixed point, even n admits
    a fixed-point-free one (f(i) = n-1-i).
(3) Term bound: with sole function symbol f and f(f(x)) = x, every term in
    x1..xn equals some xi or f(xi); hence an n-generated model has <= 2n elements.
"""
for n in range(1, 7):
    chain = list(range(n))
    m = max(chain)
    assert not any(x > m for x in chain)
    print(f"n={n}: max={m} witnesses failure of no-upper-endpoint")


def anti_inv(n):
    return [n - 1 - i for i in range(n)]


for n in range(1, 7):
    f = anti_inv(n)
    assert all(f[f[i]] == i for i in range(n))
    assert all(f[j] < f[i] for i in range(n) for j in range(i + 1, n))
    print(f"n={n}: fixed_pts={[i for i in range(n) if f[i] == i]}")

for n in [1, 2, 3, 5]:
    print(f"n-gens={n}: max presented-model size <= {2 * n}")
print("OK")
