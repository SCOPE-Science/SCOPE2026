from fractions import Fraction
import cmath

def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def poly_coeffs(d, sign):
    # Ascending coefficients for (l+1)(l^2+2)(l^2 + sign*d*l + 3).
    return conv(conv([1,1],[2,0,1]),[3,sign*d,1])

def fiber_roots(d, sign):
    # l^2 + sign*d*l + 3 = 0; sign=+1 is printed minus-ds system.
    disc=d*d-12
    root=cmath.sqrt(complex(disc,0))
    return ((-sign*d+root)/2,(-sign*d-root)/2)

# Exact polynomial coefficients, ascending in lambda.
d=Fraction(7,5)
minus=poly_coeffs(d,1)
plus=poly_coeffs(d,-1)
assert minus == [6, 6+2*d, 5+2*d, 5+d, 1+d, 1]
assert plus  == [6, 6-2*d, 5-2*d, 5-d, 1-d, 1]

# Equilibrium residuals for x=+/-1 in the printed system.
for d in [Fraction(1,1000),Fraction(499,500),Fraction(7,5),Fraction(4,1)]:
    for x in [Fraction(1),Fraction(-1)]:
        y=x; z=Fraction(0); s=-x/Fraction(3); w=d*s
        residual=(y*z, x-y, 1-x*x, -3*s-x, w-d*s)
        assert residual == (0,0,0,0,0)

# Divergence identities.
d0=Fraction(499,500)
assert -1-d0 == Fraction(-999,500)
assert -1+d0 == Fraction(-1,500)

# Fiber signs across underdamped and overdamped regimes.
for q in [Fraction(1,1000),Fraction(499,500),Fraction(3),Fraction(4),Fraction(10)]:
    roots=fiber_roots(float(q),1)
    assert max(r.real for r in roots) < 0

minus_roots=fiber_roots(float(d0),1)
plus_roots=fiber_roots(float(d0),-1)
assert all(abs(r.real + 0.499) < 1e-12 for r in minus_roots)
assert all(abs(r.real - 0.499) < 1e-12 for r in plus_roots)

# Published finite-time exponent sum at d=0.998.
reported=[Fraction(4976,10000),Fraction(4942,10000),Fraction(1737,10000),Fraction(-2,10000),Fraction(-11673,10000)]
assert sum(reported,Fraction(0)) == Fraction(-1,500)

print('VERIFY_OK')
print('printed_divergence_at_d_0.998=-1.998')
print('plus_variant_divergence_at_d_0.998=-0.002')
print('printed_fiber_real_parts_at_d_0.998=-0.499,-0.499')
print('plus_variant_fiber_real_parts_at_d_0.998=0.499,0.499')
print('reported_finite_time_LE_sum=-0.002')
