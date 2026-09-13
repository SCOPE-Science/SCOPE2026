# T2 certificate: local weighted-order standard basis of Jac(f) over QQ.
# Order: leading term = lowest W=(42,35,30).dot(m), tie-break lex.
# Run: python3 local_buchberger_qq.py  (stdlib only)
from fractions import Fraction

def W(m):
    return 42 * m[0] + 35 * m[1] + 30 * m[2]

def key(m):
    return (-W(m), m)

def add(a, b):
    out = dict(a)
    for m, v in b.items():
        out[m] = out.get(m, 0) + v
        if out[m] == 0:
            del out[m]
    return out

def neg(a):
    return {m: -v for m, v in a.items()}

def mul_scalar(a, c):
    if c == 0:
        return {}
    return {m: v * c for m, v in a.items() if v * c != 0}

def mul_x(a, m2):
    return {(m[0] + m2[0], m[1] + m2[1], m[2] + m2[2]): v for m, v in a.items()}

def LM(a):
    return max(a.keys(), key=key)

def spoly(a, b):
    la, lb = LM(a), LM(b)
    L = (max(la[0], lb[0]), max(la[1], lb[1]), max(la[2], lb[2]))
    ca, cb = a[la], b[lb]
    t1 = mul_scalar(mul_x(a, (L[0] - la[0], L[1] - la[1], L[2] - la[2])), cb)
    t2 = mul_scalar(mul_x(b, (L[0] - lb[0], L[1] - lb[1], L[2] - lb[2])), ca)
    return add(t1, neg(t2)), L

def reduce_full(f, G):
    f = dict(f)
    steps = []
    while f:
        m = LM(f)
        hit = None
        hidx = None
        for i, g in enumerate(G):
            lg = LM(g)
            if m[0] >= lg[0] and m[1] >= lg[1] and m[2] >= lg[2]:
                hit = g
                hidx = i
                break
        if hit is None:
            break
        lg = LM(hit)
        q = (m[0] - lg[0], m[1] - lg[1], m[2] - lg[2])
        coef = f[m] / hit[lg]
        steps.append((m, lg, q, coef, hidx))
        f = add(f, neg(mul_scalar(mul_x(hit, q), coef)))
    return f, steps

fx = {(4, 0, 0): Fraction(5), (2, 2, 1): Fraction(3)}
fy = {(0, 5, 0): Fraction(6), (3, 1, 1): Fraction(2)}
fz = {(0, 0, 6): Fraction(7), (3, 2, 0): Fraction(1)}
names = ['fx', 'fy', 'fz']
G = [fx, fy, fz]
print('LMs:', [LM(g) for g in G])
ok = True
for i, j in [(0, 1), (0, 2), (1, 2)]:
    s, L = spoly(G[i], G[j])
    r, steps = reduce_full(s, G)
    print(f'S({names[i]},{names[j]}): LCM={L} remainder={r} nsteps={len(steps)}')
    for st in steps:
        print('   ', st)
    if r != {}:
        ok = False
print('ALL ZERO:', ok)
LMs = [LM(g) for g in G]
cnt = sum(1 for a in range(8) for b in range(8) for c in range(8)
          if not any(a >= L[0] and b >= L[1] and c >= L[2] for L in LMs))
print('local mu:', cnt)
assert ok and cnt == 120
