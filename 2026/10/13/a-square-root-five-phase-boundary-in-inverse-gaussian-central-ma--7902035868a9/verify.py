from fractions import Fraction as F
from math import exp, sqrt, pi, erf

# Polynomial dictionaries: exponent -> rational coefficient.
def add(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}

def scale(a,s): return {k:v*s for k,v in a.items() if v*s}
def mul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items(): c[i+j]=c.get(i+j,F(0))+x*y
    return {k:v for k,v in c.items() if v}
def deriv(a): return {k-1:F(k)*v for k,v in a.items() if k>0}
def shift(a,j): return {k+j:v for k,v in a.items()}

def L(j):
    # coefficient of e^j in -3/2 log(1+ez) + z^2/2*(1-1/(1+ez))
    s = F((-1)**(j+1),1)
    return add({j:-F(3,2)*s/F(j)}, {j+2:F(1,2)*s})

# Exponential-series recurrence R_n=(1/n) sum_{j=1}^n j L_j R_{n-j}.
R=[{0:F(1)}]
for n in range(1,7):
    acc={}
    for j in range(1,n+1):
        acc=add(acc, scale(mul(L(j),R[n-j]),F(j)))
    R.append(scale(acc,F(1,n)))

A2={6:F(1,8),4:-F(5,4),2:F(15,8)}
A4={12:F(1,384),10:-F(3,32),8:F(63,64),6:-F(105,32),4:F(315,128)}
assert R[2]==A2
assert R[4]==A4
# Parity: coefficient R_n has only powers with parity n.
for n,p in enumerate(R):
    assert all(k%2==n%2 for k in p)

# If Q is odd, integral_{-c}^c (Q'-zQ)phi = 2 Q(c)phi(c).
Q2={3:F(5,8),5:-F(1,8)}
assert add(deriv(Q2),scale(shift(Q2,1),F(-1)))==A2
# Q4 corresponds to half of the stated boundary coefficient.
# -z^5(z^2-7)(z^4-18z^2+27)/384
qbase=mul({5:F(1)},mul({2:F(1),0:F(-7)},{4:F(1),2:F(-18),0:F(27)}))
Q4=scale(qbase,-F(1,384))
assert add(deriv(Q4),scale(shift(Q4,1),F(-1)))==A4

# Boundary substitutions.
# c=1: I2/phi=1, I4/phi=5/16.
def i2_over_phi(c): return c**3*(5-c*c)/4
def i4_over_phi(c): return -c**5*(c*c-7)*(c**4-18*c*c+27)/192
assert abs(i2_over_phi(1.0)-1.0)<1e-15
assert abs(i4_over_phi(1.0)-5/16)<1e-15
c=sqrt(5.0)
assert abs(i2_over_phi(c))<1e-12
assert i4_over_phi(c)<0

# Supplementary Simpson quadrature regression.
def phi(z): return exp(-z*z/2)/sqrt(2*pi)
def density(z,k):
    e=1/sqrt(k)
    return phi(z)*(1+e*z)**(-1.5)*exp(z*z/2-z*z/(2*(1+e*z)))
def simpson(f,a,b,n=20000):
    if n%2: n+=1
    h=(b-a)/n
    s=f(a)+f(b)
    s+=4*sum(f(a+(2*j-1)*h) for j in range(1,n//2+1))
    s+=2*sum(f(a+2*j*h) for j in range(1,n//2))
    return s*h/3
def approx(c,k):
    base=erf(c/sqrt(2))
    p=phi(c)
    return base+p*i2_over_phi(c)/k+p*i4_over_phi(c)/(k*k)

for c in (1.0,2.0,sqrt(5.0),2.5,3.0):
    k=1000.0
    exact=simpson(lambda z:density(z,k),-c,c,12000)
    ap=approx(c,k)
    assert abs(exact-ap)<3e-8
print('VERIFY_OK series_order=6 primitive_A2=exact primitive_A4=exact quadrature_cases=5')
