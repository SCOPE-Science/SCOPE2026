import math

worst_contact = 0.0
worst_majorant = 0.0
worst_poly = 0.0
cases = 0
for m in range(2, 201):
    delta = 2.0 * math.pi / (3.0 * m)
    u = math.cos(delta)
    A = 3.0 / (1.0 + 2.0 * u)
    q = 2.0 * A * math.sin(delta) / (m * math.sqrt(3.0))
    B = (2.0 * (A - 1.0) + q) / 3.0
    C = (A - 1.0 - q) / 3.0
    b = ((-1) ** m) * B
    c = C
    theta0 = math.pi - delta

    def P(t):
        return 1.0 + A * math.cos(t) + b * math.cos(m * t) + c * math.cos(2 * m * t)

    deriv0 = (-A * math.sin(theta0)
              - m * b * math.sin(m * theta0)
              - 2 * m * c * math.sin(2 * m * theta0))
    dual = P(math.pi) + 2.0 * P(theta0)
    worst_contact = max(worst_contact, abs(P(math.pi)), abs(P(theta0)), abs(deriv0), abs(dual))
    assert abs(P(math.pi)) < 2e-12
    assert abs(P(theta0)) < 2e-12
    assert abs(deriv0) < 2e-11
    assert abs(dual) < 4e-12

    def R(y):
        return 1.0 - C + B * y + 2.0 * C * y * y

    def g(y):
        yy = max(-1.0, min(1.0, y))
        return A * math.cos(math.acos(yy) / m)

    assert abs(R(1.0) - A) < 2e-12
    assert abs(R(-0.5) - A * u) < 2e-12
    assert abs((B - 2.0 * C) - q) < 2e-12

    for j in range(2001):
        y = -1.0 + 2.0 * j / 2000.0
        gap = R(y) - g(y)
        worst_majorant = min(worst_majorant, gap)
        assert gap > -4e-12

    for j in range(8001):
        t = 2.0 * math.pi * j / 8000.0
        val = P(t)
        worst_poly = min(worst_poly, val)
        assert val > -8e-12
    cases += 1

A,b,c,B,C,q,u,delta = (lambda m: (
    3/(1+2*math.cos(2*math.pi/(3*m))),
    ((-1)**m)*(2*(3/(1+2*math.cos(2*math.pi/(3*m)))-1)+2*(3/(1+2*math.cos(2*math.pi/(3*m))))*math.sin(2*math.pi/(3*m))/(m*math.sqrt(3)))/3,
    ((3/(1+2*math.cos(2*math.pi/(3*m)))-1)-2*(3/(1+2*math.cos(2*math.pi/(3*m))))*math.sin(2*math.pi/(3*m))/(m*math.sqrt(3)))/3,
    0,0,0,0,0))(2)
assert abs(A - 1.5) < 2e-15
assert abs(b - 7.0/12.0) < 2e-15
assert abs(c + 1.0/12.0) < 2e-15
print(f"VERIFY_OK m=2..200 cases={cases} worst_contact={worst_contact:.3e} worst_majorant={worst_majorant:.3e} worst_poly={worst_poly:.3e}")
