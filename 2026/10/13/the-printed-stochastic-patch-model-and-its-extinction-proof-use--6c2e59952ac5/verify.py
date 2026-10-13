#!/usr/bin/env python3
import sympy as sp

p,s1,s2 = sp.symbols("p s1 s2", positive=True)
vind_expr = sp.expand(s1**2*p**2 + s2**2*(1-p)**2)
pstar = sp.simplify(sp.solve(sp.diff(vind_expr,p),p)[0])
vind = sp.simplify(vind_expr.subs(p,pstar))
assert pstar == s2**2/(s1**2+s2**2)
assert vind == s1**2*s2**2/(s1**2+s2**2)

# Common-noise loading is affine in p; for positive intensities its square
# ranges between the squared endpoint intensities.
common = sp.expand((s1*p+s2*(1-p))**2)
assert sp.simplify(common.subs(p,0)-s2**2) == 0
assert sp.simplify(common.subs(p,1)-s1**2) == 0

# Equal-noise exact factor-two comparison.
sigma=sp.symbols("sigma", positive=True)
assert sp.simplify(vind.subs({s1:sigma,s2:sigma})-sigma**2/2) == 0
assert sp.simplify((sigma*p+sigma*(1-p))**2-sigma**2) == 0

# Exact symmetric witness.
r=sp.Rational(3,8)
d=sp.symbols("d", positive=True)
R1=R2=r-d
D12=D21=d
Lambda=sp.simplify(R1+R2+sp.sqrt((R1-R2)**2+4*D12*D21))
assert Lambda == sp.Rational(3,4)
vind_w=sp.Rational(1,2)
vcom_w=sp.Integer(1)
assert not (Lambda < vind_w)
assert Lambda < vcom_w

# Log-total drift before the negative competition correction.
assert r-sp.Rational(1,2) == -sp.Rational(1,8)

# Source Figure 2(b) noise comparison.
s1v=sp.Rational(7,10)
s2v=sp.Rational(8,10)
source_eff=sp.simplify(s1v**2*s2v**2/(s1v**2+s2v**2))
common_eff=min(s1v**2,s2v**2)
assert source_eff == sp.Rational(3136,11300)
assert common_eff == sp.Rational(49,100)
assert common_eff > source_eff

print("VERIFY_OK")
print("pstar_independent", pstar)
print("v_independent", vind)
print("equal_noise_v_independent", sigma**2/2)
print("equal_noise_v_common", sigma**2)
print("witness_Lambda", Lambda)
print("witness_log_rate_upper", r-sp.Rational(1,2))
print("figure2b_source_effective", source_eff, float(source_eff))
print("figure2b_common_effective", common_eff, float(common_eff))
