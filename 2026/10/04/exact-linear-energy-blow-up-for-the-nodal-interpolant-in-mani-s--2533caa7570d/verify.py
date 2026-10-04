from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 90


def cbrt_int(n):
    if n == 0:
        return Decimal(0)
    a = Decimal(n)
    x = Decimal(str(float(n) ** (1.0 / 3.0)))
    for _ in range(18):
        x = (Decimal(2) * x + a / (x * x)) / Decimal(3)
    return x


def cell(j):
    a = cbrt_int(j)
    b = cbrt_int(j + 1)
    d = b - a
    A = Decimal(3) * a * a * d - Decimal(1)
    B = Decimal(3) * a * d * d
    D = d * d * d
    integ = (A*A/Decimal(3) + A*B/Decimal(2)
             + (B*B + Decimal(2)*A*D)/Decimal(5)
             + B*D/Decimal(3) + D*D/Decimal(7))
    return d**6 * integ

# Exact first cell: integral_0^1 (s^3-s)^2 ds.
c0_exact = Fraction(1, 7) - Fraction(2, 5) + Fraction(1, 3)
assert c0_exact == Fraction(8, 105)
assert abs(cell(0) - (Decimal(8) / Decimal(105))) < Decimal('1e-80')

# Numerical coefficient from a long positive partial sum; the omitted tail is tiny.
N = 5000
S = sum(cell(j) for j in range(N))
lo = Decimal('0.07619104142716667')
hi = Decimal('0.07619104142716670')
assert lo < S < hi

# Cell-tail coefficient.
target_cell = Decimal(1) / Decimal(196830)
r = cell(2000) * (Decimal(2000) ** 6)
assert abs(r / target_cell - Decimal(1)) < Decimal('0.002')

# Energy-tail coefficient using the long partial sum as a proxy for C.
def energy(n):
    return Decimal(n) * sum(cell(j) for j in range(n))

target_tail = Decimal(1) / Decimal(984150)
n = 150
scaled = (S * Decimal(n) - energy(n)) * (Decimal(n) ** 4)
assert abs(scaled / target_tail - Decimal(1)) < Decimal('0.02')

# Published rounded PLFOpt values are consistent with the exact interpolant energy.
for n, rounded in [(3, Decimal('0.229')), (5, Decimal('0.381')), (8, Decimal('0.610')),
                   (10, Decimal('0.762')), (15, Decimal('1.143')), (20, Decimal('1.524'))]:
    val = energy(n)
    assert abs(val - rounded) < Decimal('0.0006')

print('VERIFY_OK')
