from fractions import Fraction as F


def eaie(H):
    # Two factors, d=(2,1), coordinates (1,1),(1,2),(2,1).
    psi11 = H[(1,0)] - H[(0,0)]
    psi12 = H[(2,0)] - H[(1,0)]
    psi21 = H[(0,1)] - H[(0,0)]
    c = (H[(2,1)] - psi12 - psi21) / F(2)
    return {(1,1): psi11+c, (1,2): psi12+c, (2,1): psi21+c}


def excess_top(H, x, m):
    if m == 1:
        return H[(2,0)] - H[(1,0)] - x[(1,2)]
    if m == 2:
        return H[(0,1)] - H[(0,0)] - x[(2,1)]
    raise ValueError(m)


def step(H, x, alpha):
    e1, e2 = excess_top(H,x,1), excess_top(H,x,2)
    y = dict(x)
    c1 = alpha*(e1-e2)
    c2 = alpha*(e2-e1)
    y[(1,1)] += c1
    y[(1,2)] += c1
    y[(2,1)] += c2
    return y


def pcomr(H, x):
    return (
        x[(1,1)] + x[(2,1)] == H[(1,1)] and
        x[(1,2)] + x[(2,1)] == H[(2,1)] and
        x[(2,1)] + x[(1,2)] == H[(2,1)]
    )

# Minimal counterexample.
H = {
    (0,0):F(0), (1,0):F(0), (2,0):F(0),
    (0,1):F(0), (1,1):F(1), (2,1):F(0),
}
x0 = {(1,1):F(1), (1,2):F(0), (2,1):F(0)}
assert pcomr(H,x0)
psi = eaie(H)
assert psi == {(1,1):F(0),(1,2):F(0),(2,1):F(0)}
assert excess_top(H,x0,1) == 0
assert excess_top(H,x0,2) == 0
for a in [F(1,10), F(1,4), F(1,2), F(9,10)]:  # all lie in (0,1)= (0,2/|F|)
    x = dict(x0)
    for _ in range(8):
        x = step(H,x,a)
    assert x == x0
    assert x != psi

# Independent nonstationary example: grade gaps are invariant exactly.
H2 = {
    (0,0):F(0), (1,0):F(2), (2,0):F(5),
    (0,1):F(-1), (1,1):F(4), (2,1):F(7),
}
x = {(1,1):F(11,3), (1,2):F(7,3), (2,1):F(14,3)}
# Top coordinates sum to H2(2,1)=7, so x is in X.
assert x[(1,2)] + x[(2,1)] == H2[(2,1)]
for a in [F(1,7), F(2,5)]:
    y = step(H2,x,a)
    assert y[(1,1)] - y[(1,2)] == x[(1,1)] - x[(1,2)]
    assert y != x

print('VERIFY_OK')
