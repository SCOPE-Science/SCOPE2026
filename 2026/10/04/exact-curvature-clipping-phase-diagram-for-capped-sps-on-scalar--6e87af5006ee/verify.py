from fractions import Fraction
from itertools import product

def parameters(a, b, c, gamma):
    q = Fraction(1,1)/(2*c)
    r = [min(q, ai*gamma) for ai in a]
    sr = sum(r, Fraction(0))
    m = sum(ri*bi for ri,bi in zip(r,b))/sr
    V = (
        sum(ri*ri*(bi-m)*(bi-m) for ri,bi in zip(r,b))
        /
        (2*sr-sum(ri*ri for ri in r))
    )
    xstar = sum(ai*bi for ai,bi in zip(a,b))/sum(a)
    return q, r, m, V, xstar

# General exact invariant-moment identities.
a = [Fraction(5,2), Fraction(3,2), Fraction(1,2)]
b = [Fraction(2), Fraction(-1), Fraction(4)]
c = Fraction(3,4)
for gamma in (Fraction(1,10), Fraction(1,3), Fraction(2)):
    q,r,m,V,xstar = parameters(a,b,c,gamma)
    n = len(a)
    assert all(Fraction(0) < ri <= 1 for ri in r)
    mean_rhs = sum((1-ri)*m + ri*bi for ri,bi in zip(r,b))/n
    assert mean_rhs == m
    var_rhs = sum((1-ri)**2*V + ri**2*(bi-m)**2 for ri,bi in zip(r,b))/n
    assert var_rhs == V

# All-capped regime: target is the true curvature-weighted minimizer.
a = [Fraction(4), Fraction(2), Fraction(1)]
b = [Fraction(3), Fraction(-2), Fraction(5)]
c = Fraction(1,2)
q = Fraction(1)
gamma = Fraction(1,8)  # <= q / max(a) = 1/4
q,r,m,V,xstar = parameters(a,b,c,gamma)
assert r == [ai*gamma for ai in a]
assert m == xstar
V_capped = gamma * sum(ai*ai*(bi-xstar)**2 for ai,bi in zip(a,b)) / (
    2*sum(a)-gamma*sum(ai*ai for ai in a)
)
assert V == V_capped

# All-uncapped regime: curvature disappears exactly.
gamma = Fraction(2)
q,r,m,V,xstar = parameters(a,b,c,gamma)
assert r == [q,q,q]
bbar = sum(b)/len(b)
assert m == bbar
var_b = sum((bi-bbar)**2 for bi in b)/len(b)
assert V == q*var_b/(2-q)

# Exact two-component phase diagram.
a = [Fraction(2), Fraction(1)]
b = [Fraction(1), Fraction(-1)]
c = Fraction(1,2)
q = Fraction(1)
xstar = Fraction(1,3)

for gamma, expected_m in [
    (Fraction(1,4), xstar),
    (Fraction(1,2), xstar),
    (Fraction(3,4), Fraction(1,7)),
    (Fraction(1), Fraction(0)),
    (Fraction(2), Fraction(0)),
]:
    _, r, m, V, xs = parameters(a,b,c,gamma)
    assert xs == xstar
    assert m == expected_m
    assert V >= 0

# Finite-depth exact mean/variance recursion agrees with enumeration.
a = [Fraction(2), Fraction(1)]
b = [Fraction(1), Fraction(-1)]
c = Fraction(1,2)
gamma = Fraction(3,4)
q,r,mstar,Vstar,xstar = parameters(a,b,c,gamma)

mean = Fraction(5,2)
second = mean*mean
for depth in range(1,7):
    # Moment recursion.
    mean_new = sum((1-ri)*mean + ri*bi for ri,bi in zip(r,b))/2
    second_new = sum(
        (1-ri)**2*second + 2*(1-ri)*ri*bi*mean + ri*ri*bi*bi
        for ri,bi in zip(r,b)
    )/2

    # Enumeration from deterministic x0.
    vals = []
    for seq in product(range(2), repeat=depth):
        x = Fraction(5,2)
        for idx in seq:
            x = (1-r[idx])*x + r[idx]*b[idx]
        vals.append(x)
    enum_mean = sum(vals)/len(vals)
    enum_second = sum(x*x for x in vals)/len(vals)
    assert mean_new == enum_mean
    assert second_new == enum_second
    mean, second = mean_new, second_new

# Uniform pathwise contraction coefficient is strictly below one.
assert max(1-ri for ri in r) < 1

print("verification passed")
