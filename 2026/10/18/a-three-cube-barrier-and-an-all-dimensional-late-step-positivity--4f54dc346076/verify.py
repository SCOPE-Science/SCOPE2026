"""Exact checks for fourth-order Gauss positivity on the hypercube."""
import sympy as s
h=s.symbols('h', real=True)
def rat(k):
    return (1-k*h+s.Rational(1,3)*k*k*h*h)/(1+k*h+s.Rational(1,3)*k*k*h*h)
def kraw(d,j,k):
    return sum((-1)**v*s.binomial(j,v)*s.binomial(d-j,k-v) for v in range(k+1))
def shell(d,j):
    return s.factor(sum(kraw(d,j,k)*rat(k) for k in range(d+1))/2**d)
D=2*(h*h+3*h+3)*(3*h*h+3*h+1)*(4*h*h+6*h+3)
P=h**4-6*h**3-20*h**2-18*h-6
expected=[(24*h**6+45*h**5+44*h**4+36*h**3+66*h*h+54*h+18)/D,
          -3*h*P/D,
          3*h*h*(7*h**3+18*h*h+18*h+6)/D,
          3*h**3*(11*h*h+18*h+6)/D]
checks=0
for j,v in enumerate(expected):
    assert s.cancel(shell(3,j)-v)==0
    checks+=1
for d in range(1,7):
    for j in range(d+1):
        f=s.cancel(shell(d,j))
        assert s.cancel(sum(s.binomial(d,j)*shell(d,j) for j in range(d+1))-1)==0
        checks+=1
        for step in [s.Rational(1,20),s.Rational(1),s.Rational(10),s.Rational(100)]:
            v=f.subs(h,step)
            if d<=2:assert v>=0
            checks+=1
for d in range(2,50):
    F=lambda n: sum(s.binomial(n,k)/k for k in range(1,n+1))-s.Rational(2,n)*(2**n-1)
    assert s.factor(F(d+1)-F(d))==s.Rational(2**(d+1)-d-2,d*(d+1))
    checks+=1
assert P.subs(h,8)<0 and P.subs(h,9)>0
assert shell(3,1).subs(h,9)<0 and shell(3,1).subs(h,8)>0
checks+=4
print('VERIFY_OK',checks,'exact symbolic/rational assertions')
