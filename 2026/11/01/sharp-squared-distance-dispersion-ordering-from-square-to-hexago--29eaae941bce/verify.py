from fractions import Fraction as F
from math import isclose
# Independently integrate powers of q over the square and removed triangles using exact arithmetic.
def integrate_poly(poly):
    # polynomial dict exponent tuple -> coefficient, integral over rectangle [-1/2,1/2]^2
    def sym(e):
        return F(0) if e%2 else F(1,2**e*(e+1))
    return sum(v*sym(i)*sym(j) for (i,j),v in poly.items())
def multiply(a,b):
    r={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():r[(i+k,j+l)]=r.get((i+k,j+l),F(0))+x*y
    return r
# Independently compute exact corner integral by integrating monomials in (u,v)
# on u=-1/2+t, v=1/2-s, where t,s>=0 and t+s<=c.
from math import factorial
def tri_monom(i,j,c):
    from math import comb
    ans=F(0)
    for a in range(i+1):
        for b in range(j+1):
            coeff=comb(i,a)*comb(j,b)*F(-1,2)**(i-a)*F(1,2)**(j-b)*(-1)**b
            ans+=coeff*factorial(a)*factorial(b)*c**(a+b+2)/factorial(a+b+2)
    return ans
def calc(c,k):
    p={(2,0):F(1),(0,2):F(1),(1,1):-2*c};v={(0,0):F(1)}
    for _ in range(k):v=multiply(v,p)
    return (integrate_poly(v)-2*sum(coef*tri_monom(i,j,c) for (i,j),coef in v.items()))/(1-c*c)**(k+1)
for c in [F(0), F(1,9), F(1,5), F(1,3), F(1,2)]:
    m1=(1+c-c*c)/(6*(1+c))
    m2=(8*c**4-8*c**3-12*c*c+14*c+7)/(180*(1+c)**2)
    assert calc(c,1)==m1 and calc(c,2)==m2
    v=(3*c**4+2*c**3-7*c*c+4*c+2)/(180*(1+c)**2*(1-c*c))
    assert v==(m2-m1*m1)/(1-c*c)
assert F(3*F(1,2)**4+2*F(1,2)**3-7*F(1,2)**2+4*F(1,2)+2)/(180*(1-F(1,2))*(1+F(1,2))**3)==F(43,4860)
print('EXACT_RATIONAL_CORNER_INTEGRALS_PASSED')
print('SHARP_ENDPOINTS_PASSED')
print('ALL_CHECKS_PASSED')
