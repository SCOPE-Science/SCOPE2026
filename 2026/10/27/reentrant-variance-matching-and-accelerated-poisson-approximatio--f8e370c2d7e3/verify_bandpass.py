from fractions import Fraction as F
from math import factorial

def exp_interval(x,N=90):
 assert x>=0
 s=sum((x**j)/factorial(j) for j in range(N+1))
 nxt=x**(N+1)/factorial(N+1)
 tail=nxt/(1-x/F(N+2))
 return s,s+tail

def negexp_interval(x):
 lo,hi=exp_interval(x)
 return (1/hi,1/lo)

def interval_mul(a,b):
 return min(a*b[0],a*b[1]), max(a*b[0],a*b[1])

def interval_add(a,b):return a[0]+b[0],a[1]+b[1]

def coeffs(t):
 A=t*t/F(2)+4*t+9
 B=t**6/F(2304)+7*t**5/F(384)+17*t**4/F(64)+79*t**3/F(48)+35*t*t/F(8)+11*t/F(2)
 C=-(t**7/F(36)+7*t**6/F(36)+11*t**5/F(12)+3*t**4+8*t**3+15*t*t+18*t+9)
 return A,B,C

def interval_I(t):
 t=F(t)
 x=(F(0),F(0))
 for coeff,power in zip(coeffs(t),[t,F(3,2)*t,2*t]):
  x=interval_add(x,interval_mul(coeff,negexp_interval(power)))
 return x

for t in [1,2,3,4,5]:
 a,b=interval_I(t)
 print(t,'low',float(a),'high',float(b),'width',float(b-a),'sign',a>0 or b<0)
assert interval_I(2)[0]>0
assert interval_I(3)[1]<0
assert interval_I(4)[0]>0


def p_add(p,q):
    out=p[:]
    if len(q)>len(out): out.extend([F(0)]*(len(q)-len(out)))
    for i,v in enumerate(q):out[i]+=v
    return out

def p_mul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out

def p_pow_shift(a,j):
    from math import comb
    return [F(comb(j,i))*a**(j-i)*(-1)**i for i in range(j+1)]

def Q(t,shift):
    out=[F(0)]
    for j in range(4-shift):
        low=max(0,1-shift-j)
        high=3-shift-j
        v=[F(0)]*low+[F(1,factorial(i)) for i in range(low,high+1)]
        out=p_add(out,[a/F(factorial(j)) for a in p_mul(p_pow_shift(t,j),p_mul(v,v))])
    return out

# Exact finite Poisson-sum polynomials independently reconstructed from Palm counts.
assert Q(F(2),1)==[F(5),F(3),F(5,2),F(0),F(1,4)] or False

def primitive_polynomial(p):
    # e^{-u} Q(u) has primitive -e^{-u} R(u), where R+? R-R'=Q.
    R=[F(0)]*len(p)
    for j,c in enumerate(p):
        for k in range(j+1):
            R[k]+=c*F(factorial(j),factorial(k))
    return R

def peval(p,u):
    return sum(c*u**j for j,c in enumerate(p))

# Three coefficient identities are polynomials in t of degree at most seven.
# Nine rational test parameters therefore prove the displayed identity identically.
for parameter in range(9):
    t=F(parameter)
    R1=primitive_polynomial(Q(t,1))
    R0=primitive_polynomial(Q(t,0))
    A,B,C=coeffs(t)
    S=t+t*t/F(2)+t**3/F(6)
    assert peval(R1,F(0))==A
    assert peval(R0,t/2)-peval(R1,t/2)==B
    assert -peval(R0,t)-t*S*S==C

# A nonzero Poisson--Charlier signed coefficient: k=0 equals p_alpha(0)>0.
# The sign intervals were constructed exclusively using exact Fractions.
assert interval_I(2)[0] > 0
assert interval_I(3)[1] < 0
assert interval_I(4)[0] > 0
print('All rational polynomial identities and signed exponential bounds passed.')
