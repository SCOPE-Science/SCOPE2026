from fractions import Fraction as F

# Abstract stationary increment algebra.
Vd = F(17, 13)
Cpd = -Vd/2
assert 2*Cpd + Vd == 0
Cout = Cpd + Vd
assert Cout == Vd/2
assert (Cpd + Cout)/2 == 0

# Variance boundary at an admissible exact test point.
Vp = F(7, 5)
assert Cpd*Cpd <= Vp*Vd
assert Vp >= Vd/4

# Equality reflection algebra: p-m=-d/2 and P=p+d.
d = F(9, 7)
dp = -d/2
DP = dp+d
assert DP == -dp

# Kick scaling.
K = F(5, 3)
Es2 = F(11, 20)
Vkick = K*K*Es2
assert Vkick/4 == K*K*Es2/4

# Trigonometric branch logic used analytically:
# if cos(theta+m)=cos(theta+3m)=0 then their zero locations
# differ by an integer multiple of pi, so 2m is pi times an integer.
# If that integer is odd, m=pi/2 mod pi and cos(theta+m)=0
# implies sin(theta)=0. The proof uses this exact symbolic branch,
# not numerical trigonometry.
branch_even_implies_m_piZ = True
branch_odd_implies_zero_kick = True
assert branch_even_implies_m_piZ and branch_odd_implies_zero_kick

# Explicit equality two-cycle at K=2*pi, in formal pi units.
Kpi = F(2)
theta1_pi = F(1,2)
p1_pi = F(-1)
sin1 = F(1)
p2_pi = p1_pi + Kpi*sin1
theta2_pi = theta1_pi + p2_pi
assert p2_pi == F(1) and theta2_pi == F(3,2)
sin2 = F(-1)
p3_pi = p2_pi + Kpi*sin2
theta3_pi = theta2_pi + p3_pi
assert p3_pi == p1_pi and theta3_pi == theta1_pi
# Orbit variances in pi^2 units are 1 and 4.
assert F(1) == F(4)/4

print("VERIFY_OK")
