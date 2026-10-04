from fractions import Fraction

x0 = Fraction(1, 1)
q = Fraction(1, 2)
delta0 = Fraction(1, 4)
x = x0
delta = delta0
x_inf = x0 - delta0 / (1 - q)
assert x_inf == Fraction(1, 2)
for k in range(20):
    assert 0 < delta < x
    s = -delta
    f_before = x*x/2
    f_after = (x+s)*(x+s)/2
    predicted = f_before - f_after
    actual = f_before - f_after
    assert predicted > 0
    assert actual / predicted == 1
    closed = x0 - delta0 * (1 - q**k) / (1 - q)
    assert x == closed
    x = x + s
    delta = q * delta
assert x > x_inf
assert x_inf > 0
print("VERIFY_OK")
