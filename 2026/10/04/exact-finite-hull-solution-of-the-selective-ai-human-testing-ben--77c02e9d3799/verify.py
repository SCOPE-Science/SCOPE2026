from fractions import Fraction as F


def lower_hull(points):
    # Keep the cheapest point at each information coordinate.
    best = {}
    for k, c, name in points:
        if k not in best or c < best[k][0]:
            best[k] = (c, name)
    pts = sorted((k, c, name) for k, (c, name) in best.items())
    hull = []
    for p in pts:
        while len(hull) >= 2:
            k0, c0, _ = hull[-2]
            k1, c1, _ = hull[-1]
            k2, c2, _ = p
            # Remove a middle point if the new slope is not larger.
            if (c1-c0)*(k2-k1) >= (c2-c1)*(k1-k0):
                hull.pop()
            else:
                break
        hull.append(p)
    return hull


def eval_hull(hull, x):
    assert hull[0][0] <= x <= hull[-1][0]
    for i in range(len(hull)-1):
        k0, c0, _ = hull[i]
        k1, c1, _ = hull[i+1]
        if k0 <= x <= k1:
            if x == k0:
                return c0
            return c0 + (c1-c0)*(x-k0)/(k1-k0)
    return hull[-1][1]


def make_direction(g, d, I, c_ai, c_h):
    W = [F(0)]
    D = [F(0)]
    for gj, dj in zip(g, d):
        W.append(W[-1] + gj)
        D.append(D[-1] + gj*dj)
    J = I + D[-1]
    pts = [(F(0), F(0), 'idle')]
    for q in range(len(W)):
        pts.append((I+D[q], c_ai+c_h*W[q], f'ai{q}'))
    pts.append((J, c_h, 'human'))
    return W, D, J, lower_hull(pts)


def psi_at(s, W, D, d):
    if s == 0:
        return F(0)
    for q in range(1, len(W)):
        if s <= W[q]:
            return D[q-1] + d[q-1]*(s-W[q-1])
    raise AssertionError('s out of range')

# Direction 1: a three-report exact example.
g1 = [F(1,4), F(1,4), F(1,2)]
d1 = [F(4), F(2), F(1)]
I1, c_ai, c_h = F(1), F(1), F(5)
W1, D1, J1, H1 = make_direction(g1, d1, I1, c_ai, c_h)
assert W1 == [F(0), F(1,4), F(1,2), F(1)]
assert D1 == [F(0), F(1), F(3,2), F(2)]
assert J1 == F(3)
# Full AI escalation has the same information as human but costs more.
assert c_ai + c_h > c_h
# At s=3/10 the frontier is inside the second breakpoint segment.
s = F(3,10)
psi = psi_at(s, W1, D1, d1)
assert psi == F(11,10)
N, T = F(10), F(21)
original_cost = N*c_ai + c_h*(N*s)
original_info = N*(I1 + psi)
assert original_info == T
assert original_cost == F(25)
# The hull formula gives exactly the same value.
assert eval_hull(H1, T/N) == F(5,2)
assert N*eval_hull(H1, T/N) == F(25)
# It is the 4/5--1/5 mixture of adjacent q=1 and q=2 AI modes.
assert F(4,5)*(I1+D1[1]) + F(1,5)*(I1+D1[2]) == T/N
assert F(4,5)*(c_ai+c_h*W1[1]) + F(1,5)*(c_ai+c_h*W1[2]) == F(5,2)
# Selective escalation beats the AI-human chord exactly in this threshold regime.
Dm = J1-I1
assert c_ai/c_h < 1-Dm/d1[0]
Kq1 = I1 + D1[1]
Cq1 = c_ai + c_h*W1[1]
chord_q1 = c_ai + (c_h-c_ai)*(Kq1-I1)/(J1-I1)
assert Cq1 < chord_q1

# Direction 0 for an outer-benchmark check.
g0 = [F(1,2), F(1,2)]
d0 = [F(2), F(1)]
I0 = F(1,2)
W0, D0, J0, H0 = make_direction(g0, d0, I0, c_ai, c_h)
T1, T0 = F(21), F(9)
c_data = F(1,10)
Nmin = 7  # max(ceil(T1/J1), ceil(T0/J0))

def gamma(T, N, hull):
    x = T/F(N)
    if x > hull[-1][0]:
        return None
    return F(N)*eval_hull(hull, x)

def outer(N):
    a = gamma(T1, N, H1)
    b = gamma(T0, N, H0)
    if a is None or b is None:
        return None
    return F(N)*c_data + max(a,b)

brute = [(outer(n), n) for n in range(Nmin, 101)]
brute = [x for x in brute if x[0] is not None]
best_val, best_n = min(brute)

# Build a superset of all real outer breakpoints/crossings from hull segments.
def pieces(T, hull):
    out = []
    for i in range(len(hull)-1):
        k0,c0,_ = hull[i]
        k1,c1,_ = hull[i+1]
        a = (c1-c0)/(k1-k0)
        b = c0-a*k0
        lo = T/k1
        hi = None if k0 == 0 else T/k0
        out.append((lo,hi,a*T,b))  # gamma(N)=const+b*N
    return out

candidates = {F(Nmin)}
P1, P0 = pieces(T1,H1), pieces(T0,H0)
for lo,hi,_,_ in P1+P0:
    candidates.add(lo)
    if hi is not None:
        candidates.add(hi)
for lo1,hi1,A1,B1 in P1:
    for lo0,hi0,A0,B0 in P0:
        lo = max(lo1,lo0,F(Nmin))
        his = [x for x in (hi1,hi0) if x is not None]
        hi = min(his) if his else None
        if hi is not None and lo > hi:
            continue
        candidates.add(lo)
        if hi is not None:
            candidates.add(hi)
        if B1 != B0:
            x = (A0-A1)/(B1-B0)
            if x >= lo and (hi is None or x <= hi):
                candidates.add(x)

integer_candidates = set()
for x in candidates:
    if x < Nmin:
        continue
    f = x.numerator // x.denominator
    for n in (f, f+1):
        if n >= Nmin:
            integer_candidates.add(n)
finite = [(outer(n),n) for n in integer_candidates if outer(n) is not None]
finite_best = min(finite)
assert finite_best == (best_val,best_n)

print('VERIFY_OK')
print('inner_gamma=', original_cost)
print('outer_min_N=', best_n)
print('outer_min_cost=', best_val)
