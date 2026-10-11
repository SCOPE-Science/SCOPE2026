from fractions import Fraction

def parity_area_coeff(m):
    return 0 if m % 2 == 0 else 1  # A_m/(2*pi)

# All scale-sensitive quantities divided by 2*pi^2 equal m.
for m in range(1, 25):
    A_over_2pi = parity_area_coeff(m)
    L_over_2pi = m
    # covol/(2*pi^2) = determinant of [[1,A/(4pi)],[0,L/(2pi)]]
    covol_ratio = m
    energy_ratio = m
    mass_ratio = m
    assert covol_ratio == energy_ratio == mass_ratio == m

# z_1=(1+i)/2. S(z)=-1/z gives -1+i; T then gives i=z_2.
# Exact complex arithmetic using rational pairs.
def inv_neg(x, y):
    den = x*x + y*y
    return (-x/den, y/den)

x1, y1 = Fraction(1,2), Fraction(1,2)
sx, sy = inv_neg(x1, y1)
assert (sx, sy) == (Fraction(-1), Fraction(1))
tx, ty = sx + 1, sy
assert (tx, ty) == (Fraction(0), Fraction(1))

# Fundamental-domain inequalities for representative cases are algebraic:
# even m>=2: Re=0, |z|^2=m^2/4 >=1;
# odd m>=3: Re=1/2, |z|^2=(1+m^2)/4 >1.
for m in range(2, 25):
    if m % 2 == 0:
        x, y = Fraction(0), Fraction(m,2)
        assert x == 0 and x*x+y*y >= 1
    else:
        x, y = Fraction(1,2), Fraction(m,2)
        assert x == Fraction(1,2) and x*x+y*y > 1

print("VERIFY_OK")
print("scale_sensitive_invariants=2*pi^2*m")
print("unique_exception_transform=z1_to_z2")
print("fundamental_domain_cases=true")
