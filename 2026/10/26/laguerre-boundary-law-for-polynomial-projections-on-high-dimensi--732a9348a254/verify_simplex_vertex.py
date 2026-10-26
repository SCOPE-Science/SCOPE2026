"""Exact-moment and high-precision checks of simplex-vertex projection formulas.

The infinite-dimensional conclusions require the analytic proof in RESULT.md.
"""
import math
import sympy as S
import mpmath as M

M.mp.dps=55

def beta_moment(d,j):
    return S.factorial(j)/S.prod(d+1+k for k in range(j))

def kernel_coeffs(d,m):
    H=S.Matrix(m+1,m+1,lambda i,j: beta_moment(d,i+j))
    return list(H.inv()*S.ones(m+1,1))

def laguerre(m,z):
    return sum((-1)**j*S.binomial(m,j)*z**j/S.factorial(j) for j in range(m+1))

for d in range(1,10):
    for m in range(1,6):
        coeff=kernel_coeffs(d,m)
        for j in range(m+1):
            assert S.simplify(sum(coeff[i]*beta_moment(d,i+j) for i in range(m+1))-1)==0
        assert S.simplify(sum(coeff[i] for i in range(m+1))-S.binomial(d+m,m)**2)==0
        if m==2:
            A=S.Rational(1,4)*(d+1)*(d+2)*(d+3)*(d+4)
            B=-(d+1)*(d+2)*(d+3)
            C=S.Rational(1,2)*(d+1)*(d+2)
            assert [A,B,C] == [coeff[2],coeff[1],coeff[0]]
print('PASS: 45 exact moment systems, normalization, and endpoint L2 diagonals')

for d in [1,2,3,5,10,50,200,2000]:
    dd=M.mpf(d)
    ra=(2-M.sqrt(2*(dd+2)/(dd+3)))/(dd+4)
    rb=(2+M.sqrt(2*(dd+2)/(dd+3)))/(dd+4)
    def k(t): return (dd+1)*(dd+2)*((dd+3)*(dd+4)*t*t/4-(dd+3)*t+M.mpf('0.5'))
    exact=M.mpf(1)+2*(-M.quad(lambda t:dd*(1-t)**(dd-1)*k(t),[ra,rb]))
    def Q(t):return 1-dd**2*(dd+3)*t/2+dd*(dd+1)*(dd+3)*(dd+4)*t*t/4
    algebraic=1+2*((1-rb)**dd*Q(rb)-(1-ra)**dd*Q(ra))
    assert abs(exact-algebraic)<M.mpf('2e-40')
    print('d=',d,'vertex_norm=',M.nstr(exact,16),'scaled=',M.nstr(exact/dd**2,12))

a=2-M.sqrt(2);b=2+M.sqrt(2)
c=(a*M.exp(-a)+b*M.exp(-b))/M.sqrt(2)
integral=M.quad(lambda s:M.exp(-s)*abs((s*s-4*s+2)/4),[0,a,b,M.inf])
assert abs(c-integral)<M.mpf('1e-48')
print('PASS: exact degree-two beta integrals and Laguerre constant=',M.nstr(c,30))
for m in [2,3,4]:
    d=300
    co=kernel_coeffs(d,m)
    z=S.symbols('z')
    poly=S.expand(sum(co[i]*z**i/S.Integer(d)**(m+i) for i in range(m+1)))
    target=S.expand((-1)**m*laguerre(m,z)/S.factorial(m))
    err=max(abs(float(S.expand(poly-target).coeff(z,j))) for j in range(m+1))
    assert err<0.08
    print('m=',m,'d=',d,'largest coefficient discrepancy=',err)
print('ALL CHECKS PASS')
