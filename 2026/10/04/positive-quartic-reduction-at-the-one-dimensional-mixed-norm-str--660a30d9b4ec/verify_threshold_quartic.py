from fractions import Fraction as F
from math import prod

# Polynomials in x represented by {degree: rational coefficient}.
def mul(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items():
            out[i+j]=out.get(i+j,F(0))+a*b
    return {k:v for k,v in out.items() if v}

def scale(p,c):
    return {k:v*c for k,v in p.items() if v*c}

def gp_even(n):
    # normalized moment for density proportional to exp(-5 x^2)
    if n%2: return F(0)
    m=n//2
    if m==0: return F(1)
    odd=prod(range(1,2*m,2))
    return F(odd,10**m)

def expect(p):
    return sum((c*gp_even(k) for k,c in p.items()),F(0))

# P3^2, where P3=(2x^3-3x)/sqrt(3).
p2={6:F(4,3),4:F(-4),2:F(3)}
p4=mul(p2,p2)
# P6 = sqrt(5)*Q6.
q6={6:F(2,15),4:F(-1),2:F(3,2),0:F(-1,4)}

E_p2=expect(p2)
E_p4=expect(p4)
E_q_coeff=expect(q6)                 # E[P6]=sqrt(5)*this
E_q2=5*expect(mul(q6,q6))            # E[P6^2]
E_p2q_coeff=expect(mul(p2,q6))       # E[P3^2 P6]=sqrt(5)*this

assert E_p2 == F(1,5)
assert E_p4 == F(249,3125)
assert E_q_coeff == F(-16,125)
assert E_q2 == F(2841,15625)
assert E_p2q_coeff == F(22,15625)

# The exact Taylor calculation gives normalized deficit coefficient
# C(a)=Rcoef*|a|^2 + Lcoef*sqrt(5)*Re(a) + C0.
Rcoef=F(462,625)
Lcoef=F(-444,625)
C0=F(252,125)
assert Rcoef == F(6*77,625)
assert Lcoef == F(6*(-74),625)
assert C0 == F(6*210,625)

# Completing the square:
# 77(|a|^2)-74 sqrt(5) Re(a)+210
# =77((Re(a)-37sqrt(5)/77)^2+(Im(a))^2)+9325/77.
amin_sq_rational=F(37*37*5,77*77)
recovered_constant=77*amin_sq_rational + F(9325,77)
assert recovered_constant == 210
min_coeff=F(6,625)*F(9325,77)
assert min_coeff == F(2238,1925)
assert min_coeff > 0

print('VERIFY_OK')
print('E_P3_sq', E_p2)
print('E_P3_4', E_p4)
print('E_P6_sqrt5_coeff', E_q_coeff)
print('E_P6_sq', E_q2)
print('E_P3_sq_P6_sqrt5_coeff', E_p2q_coeff)
print('quartic_Rcoef', Rcoef)
print('quartic_sqrt5_Rea_coef', Lcoef)
print('quartic_constant', C0)
print('quartic_min', min_coeff)
