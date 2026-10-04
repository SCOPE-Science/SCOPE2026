from math import sqrt, isclose

def two_facet_value(n):
    return n + sqrt(2*(n**3 - 2*n**2 + 2)/(n+1))

def candidate(n):
    # Quadratic form Q(s,c) = A s^2 + D c^2 + q s c.
    A = 1/n
    D = (n-1)/n
    q = sqrt((n-1)/(n+1))
    off = q/2
    disc = (A-D)**2 + 4*off**2
    lam = (1 + sqrt(disc))/2
    # Positive unit eigenvector for the largest eigenvalue.
    r = off/(lam-A)  # s/c
    c = 1/sqrt(1+r*r)
    s = r*c
    b = sqrt((n+1)/(2*n))
    gamma = sqrt((n-1)/(2*n))
    a = sqrt(n/(2*(n+1)))
    x = b*s + gamma*c
    t = b*c - gamma*s
    y = s
    return lam, s, c, x, t, y, a, b, gamma

for n in range(3, 401):
    lam,s,c,x,t,y,a,b,gamma = candidate(n)
    assert s > 0 and c > 0 and t > 0
    assert abs(x*x + t*t - 1) < 2e-13
    # Lower endpoint equality from the spherical-angle bound.
    assert abs(y - (b*x - gamma*t)) < 2e-13
    # Strict visibility of the second upper facet.
    assert y < a*x
    # Every other facet is non-upper for the constructed normal.
    y_other = b*x + t/sqrt(2*n*(n-1))
    assert y_other > b*x > a*x
    # Published k=2 volume bracket.
    f = (2/n)*y*y - sqrt(2/(n*(n+1)))*(n+2)*x*y + 2*x*x
    assert abs(f-lam) < 5e-13
    assert abs(2*n*f - two_facet_value(n)) < 1e-10
    # The competing upper-endpoint branch is smaller.
    assert lam > 1 - 1/(n*n)

# Published five-dimensional value.
assert abs(two_facet_value(5) - (5 + sqrt(77/3))) < 1e-14

# Threshold: the two-facet benchmark beats 2n iff n>=5 among n>=3.
for n in range(3, 100):
    assert (two_facet_value(n) > 2*n) == (n >= 5)

# Asymptotic ratio tends to 1+sqrt(2).
target = 1 + sqrt(2)
for n in (10_000, 100_000, 1_000_000):
    assert abs(two_facet_value(n)/n - target) < 4/n

print("VERIFY_OK reflected simplex two-upper-facet benchmark")
