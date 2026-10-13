import mpmath as mp

mp.mp.dps = 80

def xi_of(y):
    y = mp.mpf(y)
    return y/(1-y)

def survival_x(u, theta):
    u = mp.mpf(u)
    theta = mp.mpf(theta)
    return (1 + theta*u + theta**2*u**2/(2*(1+theta))) * mp.e**(-theta*u)

def numerator_direct(y, theta):
    y = mp.mpf(y)
    theta = mp.mpf(theta)
    xi = xi_of(y)
    return mp.quad(lambda u: survival_x(u,theta)/(1+u)**2, [xi, mp.inf])

def numerator_closed(y, theta):
    y = mp.mpf(y)
    theta = mp.mpf(theta)
    xi = xi_of(y)
    return (
        mp.e**(-theta*xi)/(2*(1+theta)) *
        (theta + (2-theta**2)*(1-y))
        + theta**3*mp.e**theta/(2*(1+theta)) *
        mp.e1(theta/(1-y))
    )

def mrl(y, theta):
    xi = xi_of(y)
    return numerator_closed(y,theta)/survival_x(xi,theta)

def source_term(k, y, theta):
    y = mp.mpf(y)
    theta = mp.mpf(theta)
    xi = xi_of(y)
    z = theta*xi
    bracket = (
        mp.gammainc(k+1, z, mp.inf)
        + mp.gammainc(k+2, z, mp.inf)
        + mp.gammainc(k+3, z, mp.inf)/(2*(1+theta))
    )
    return (k+1)*((-1)**k)*bracket/theta**(k+1)

tests = [
    (mp.mpf("0.1"), mp.mpf("0.2")),
    (mp.mpf("0.4"), mp.mpf("1")),
    (mp.mpf("0.8"), mp.mpf("2")),
    (mp.mpf("0.6"), mp.mpf("5")),
]
for y,theta in tests:
    d = numerator_direct(y,theta)
    c = numerator_closed(y,theta)
    assert abs(d-c) < mp.mpf("1e-60")
    assert c > 0

# Concrete MRL value.
value = mrl(mp.mpf("0.4"), mp.mpf("1"))
assert abs(value-mp.mpf("0.283322188636721124655020084629")) < mp.mpf("1e-29")

# Source terms grow rapidly at a representative point.
terms = [abs(source_term(k, mp.mpf("0.4"), mp.mpf("1"))) for k in range(8)]
for i in range(2, len(terms)-1):
    assert terms[i+1] > terms[i]
assert terms[-1] > mp.mpf("1e6")

# Check the analytic lower bound on large k at additional parameter points.
for y,theta in [
    (mp.mpf("0.2"),mp.mpf("0.7")),
    (mp.mpf("0.8"),mp.mpf("2")),
    (mp.mpf("0.5"),mp.mpf("6")),
]:
    xi = xi_of(y)
    for k in [40, 60]:
        if k+2 > theta*xi:
            lower = (
                (k+1)/(2*(1+theta)*theta**(k+1))
                * (k+2)**(k+2)*mp.e**(-(k+3))
            )
            assert abs(source_term(k,y,theta)) >= lower

print("VERIFY_OK")
print("mrl_theta1_y04", mp.nstr(value, 45))
print("source_term_magnitudes_theta1_y04",
      [mp.nstr(v, 14) for v in terms])
for y,theta in tests:
    print("quadrature_match", mp.nstr(theta,8), mp.nstr(y,8),
          mp.nstr(numerator_direct(y,theta)-numerator_closed(y,theta), 8))
