"""verify_order5.py — independent second kill via rho = sigma^3 (stdlib only).

rho has type 5-(9;3): nine 5-cycles + three fixed points.
Fixed-subcode dim = 12/2 = 6; remainder 24-6 = 18.
Orbit count: 5 | (2^18 - 1) would be needed; 2^18-1 = 262143 = 3 mod 5.
Also checks irreducibility of x^4+x^3+x^2+x+1 over F2 (block GF(16)):
  no linear factor (f(0)=f(1)=1) and no quadratic factor (nonzero at both
  GF(4) roots w, w^2 of x^2+x+1).
"""


def compose(p, q):
    return [p[q[i]] for i in range(len(p))]


def power(p, e):
    n = len(p)
    r = list(range(n))
    for _ in range(e):
        r = compose(p, r)
    return r


def cycle_type(p):
    n = len(p)
    seen = [False] * n
    lens = []
    for i in range(n):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                L += 1
            lens.append(L)
    lens.sort()
    return lens


sigma = [0] * 48
for b in (0, 15, 30):
    for t in range(15):
        sigma[b + t] = b + (t + 1) % 15
for f in (45, 46, 47):
    sigma[f] = f
rho = power(sigma, 3)
ct = cycle_type(rho)
assert ct == [1, 1, 1] + [5] * 9, ct
q = rho
order = 1
while q != list(range(48)):
    q = compose(rho, q)
    order += 1
assert order == 5, order
assert sorted(i for i in range(48) if rho[i] == i) == [45, 46, 47]
print("rho=sigma^3 type 5-(9;3) OK, order 5, fix=3 OK")

# projector e = 1+r+r^2+r^3+r^4: e^2=e since each residue count 25/5=5=1 mod 2
counts = {}
for i in range(5):
    for j in range(5):
        counts[(i + j) % 5] = counts.get((i + j) % 5, 0) + 1
assert counts == {k: 5 for k in range(5)}, counts
print("projector e^2=e exponent counts OK:", counts)

n_orb = 9 + 3
assert n_orb == 12 and n_orb % 2 == 0
d_fix = n_orb // 2
assert d_fix == 6
rem = 24 - d_fix
assert rem == 18
r = (2 ** 18 - 1) % 5
assert r == 3, r
print(f"fixed dim={d_fix}, remainder={rem}, 2^18-1 mod 5 = {r} != 0 => kill OK")

# irreducibility of degree-4 cyclotomic over F2
f5 = 0b11111
assert bin(f5).count("1") % 2 == 1, "f5(1)=1: no linear factor at 1"
# f5(0) = constant term = 1: no linear factor at 0


def g4_mul(a, b):
    c0 = (a[0] & b[0]) ^ (a[1] & b[1])
    c1 = (a[0] & b[1]) ^ (a[1] & b[0]) ^ (a[1] & b[1])
    return (c0, c1)


def g4_add(a, b):
    return (a[0] ^ b[0], a[1] ^ b[1])


def g4_pow(a, k):
    r_ = (1, 0)
    for _ in range(k):
        r_ = g4_mul(r_, a)
    return r_


w = (0, 1)
assert g4_pow(w, 3) == (1, 0)
w2 = g4_pow(w, 2)


def g4_f5(a):
    r_ = (0, 0)
    for k in range(5):
        r_ = g4_add(r_, g4_pow(a, k))
    return r_


assert g4_f5(w) != (0, 0) and g4_f5(w2) != (0, 0), "no quadratic factor"
print("x^4+x^3+x^2+x+1 irreducible over F2 (block GF(16)); 18 not mult of 4 OK")
print("VERIFY_OK")
