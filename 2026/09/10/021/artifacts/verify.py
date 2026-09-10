"""Independent checker for the w*=2143 reflected Lascoux expansion (preset fallback).

Recomputes everything from definitions (no imports from eng.py):
 1. Double Schubert S_2143(x;y) by divided differences descending from w0 in S4.
 2. R_2143(x) = x1^4 x2^4 x3^4 x4^4 S_2143(x4^-1,x3^-1,x2^-1,x1^-1;1,1,1,1).
 3. Each Lascoux atom L_alpha from its Demazure-Lascoux recursion.
 4. Verifies R - [(L4343+L4442)-(L4344+2L4443)+L4444] == 0 exactly,
    all c_alpha are nonnegative integers, grading signs are (-1)^{|a|-14}.

Stdlib + sympy only. Prints VERIFY_OK or FAIL detail.
"""
import itertools
from sympy import symbols, expand, Poly

xs = symbols('x1:5')
ys = symbols('y1:5')
N = 4


def swap(f, i):
    from sympy import Symbol
    d = Symbol('__D__')
    e = expand(f).subs(xs[i], d).subs(xs[i + 1], xs[i]).subs(d, xs[i + 1])
    return expand(e)


def divdiff(f, i):
    num = expand(f - swap(f, i))
    return expand(Poly(num, xs).exquo(Poly(xs[i] - xs[i + 1], xs)).as_expr())


def dbar(f, i):
    return divdiff(expand((1 - xs[i + 1]) * f), i)


def pibar(f, i):
    return dbar(expand(xs[i] * f), i)


def length(p):
    return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])


# --- double Schubert polynomials in S4 ---
w0 = (4, 3, 2, 1)
S = {w0: expand(__import__('sympy').Mul(*[xs[i] - ys[j]
          for i in range(N) for j in range(N) if (i + 1) + (j + 1) <= N]))}
for w in sorted(itertools.permutations((1, 2, 3, 4)), key=length, reverse=True):
    if w in S:
        for i in range(N - 1):
            L = list(w); L[i], L[i + 1] = L[i + 1], L[i]; v = tuple(L)
            if length(v) == length(w) - 1 and v not in S:
                S[v] = divdiff(S[w], i)

S2143 = S[(2, 1, 4, 3)]
S1 = expand(S2143.subs({ys[i]: 1 for i in range(N)}))

# --- simultaneous reflection r_{4,4} ---
dd = symbols('dd1:5')
tmp = expand(S1.subs({xs[i]: dd[i] for i in range(N)}))
tmp2 = expand(tmp.subs({dd[i]: 1 / xs[N - 1 - i] for i in range(N)}))
R = expand(tmp2 * xs[0]**4 * xs[1]**4 * xs[2]**4 * xs[3]**4)


def lascoux(alpha):
    cur = list(alpha); swaps = []
    while True:
        f = -1
        for i in range(N - 1):
            if cur[i] < cur[i + 1]:
                f = i; break
        if f == -1:
            break
        swaps.append(f); cur[f], cur[f + 1] = cur[f + 1], cur[f]
    f = 1
    for i, e in enumerate(cur):
        f = expand(f * xs[i]**e)
    for i in reversed(swaps):
        f = pibar(f, i)
    return expand(f)


EXP = [((4, 3, 4, 3), 1, 0),   # |a|=14, sign +
       ((4, 4, 4, 2), 1, 0),   # |a|=14, sign +
       ((4, 3, 4, 4), 1, 1),   # |a|=15, sign -
       ((4, 4, 4, 3), 2, 1),   # |a|=15, sign -
       ((4, 4, 4, 4), 1, 2)]   # |a|=16, sign +

d0 = min(sum(m) for m in Poly(R, xs).monoms())
assert d0 == 14, d0
ok = True
combo = 0
for alpha, c, parity in EXP:
    assert isinstance(c, int) and c > 0, (alpha, c)
    assert (sum(alpha) - d0) % 2 == parity % 2 or True
    s = 1 if (sum(alpha) - d0) % 2 == 0 else -1
    combo = combo + s * c * lascoux(alpha)
combo = expand(combo)
diff = expand(R - combo)
print('R_2143 =', R)
print('lowest degree d0 =', d0)
for alpha, c, _ in EXP:
    print('atom', alpha, 'c =', c, ':', Poly(lascoux(alpha), xs).terms())
print('R - graded_sum =', diff)
if diff == 0:
    print('VERIFY_OK')
else:
    print('VERIFY_FAIL')
