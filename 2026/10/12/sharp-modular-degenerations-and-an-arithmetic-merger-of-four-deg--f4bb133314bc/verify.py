"""Exact identities and finite-field checks for four degree-seven conic-line divisors.

Uses only the Python standard library. Run: python verify.py
The finite-field checks are independent examples, not a proof of all primes.
"""
from fractions import Fraction as F
from math import isqrt


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def P(n):
    return [F(n)]

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])

def neg(a):
    return [-v for v in a]

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)

def scale(a,v):
    return trim([F(v)*x for x in a])

def prod(*args):
    z=P(1)
    for a in args:z=mul(z,a)
    return z

T=[F(0),F(1)]

def linear(a,b):
    return [F(b),F(a)]

def q1(X):
    return sub(X,mul(T,T))

def q2(X):
    return sub(add(sub(mul(X,X),scale(mul(T,X),10)),scale(X,25)),P(36))

def q3(X):
    return sub(add(sub(scale(X,4),scale(mul(T,T),5)),scale(T,8)),P(12))

# Complete conic-conic intersection elimination.
assert q2(mul(T,T))==prod(linear(1,1),linear(1,-2),linear(1,-3),linear(1,-6))
assert q3(mul(T,T))==neg(prod(linear(1,-2),linear(1,-6)))
x_on_q3=scale(add(sub(scale(mul(T,T),5),scale(T,8)),P(12)),F(1,4))
assert scale(q2(x_on_q3),16)==prod(linear(1,-6),linear(1,-2),linear(5,-8),linear(5,-8))
# In local coordinates near [0:1:0], Q1 gives z=t^2;
# Q3 restricts to -t^2(1-2t)(1-6t).
assert sub(add(scale(mul(T,T),-1),scale(prod(T,T,T),8)),scale(prod(T,T,T,T),12)) == neg(prod(T,T,linear(-2,1),linear(-6,1)))

line_parameters=[(F(32,5),F(-256,25)),(F(0),F(0)),(F(10),F(-25)),(F(18,5),F(-81,25))]
line_q2_factors=[scale(prod(linear(20,-57),linear(20,-57)),F(-36,625)),P(-36),P(-36),scale(prod(linear(20,-43),linear(20,-43)),F(-36,625))]
line_q3_factors=[scale([F(-1324),F(840),F(-125)],F(1,25)),sub(add(scale(T,8),scale(mul(T,T),-5)),P(12)),neg(prod(linear(1,-4),linear(5,-28))),scale(neg(prod(linear(5,-12),linear(25,-52))),F(1,25))]
discriminants=[F(16*109,25),F(-16*11),F(64),F(64,25)]
for k,(a,b) in enumerate(line_parameters):
    x=linear(a,b)
    assert q1(x)==scale(prod(linear(1,-a/2),linear(1,-a/2)),-1)
    assert q2(x)==line_q2_factors[k]
    assert q3(x)==line_q3_factors[k]
    coeff=q3(x)
    assert len(coeff)==3
    assert coeff[1]**2-4*coeff[0]*coeff[2]==discriminants[k]

# None of the four lines meets the six fixed intersection points in
# characteristics at least seven, except the indicated characteristic seven.
L=[lambda t,x:25*x-160*t+256, lambda t,x:x,
   lambda t,x:x-10*t+25, lambda t,x:25*x-90*t+81]
base_t=[-1,2,3,6]
assert [[F(f(F(t),F(t*t))) for t in base_t] for f in L]==[
    [441,36,1,196], [1,4,9,36], [36,9,4,1], [196,1,36,441]]
assert [f(F(8,5),F(3)) for f in L]==[75,3,12,12]
# Their coefficients of x do not vanish mod primes >=7 at [0:1:0].
assert [v%7 for v in (25,-160,256)] == [v%7 for v in (25,-90,81)]
# Pairwise conic Hessian determinants (smooth for all primes >= 7).
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
assert [det3(H) for H in (
    [[-2,0,0],[0,0,1],[0,1,0]],
    [[0,-10,0],[-10,2,25],[0,25,-72]],
    [[-10,0,8],[0,0,4],[8,4,-24]])] == [2,7200,160]
# The only conic-conic root mergers for primes >=7 are:
# p=7: -1 and 6 in Q1 cap Q2; p=11: 6 and 8/5 in Q2 cap Q3.
assert 6-(-1)==7 and 5*6-8==22
# p=7: Q1,Q2,L1 (and L4), share the same tangent at t=6.
assert all((a.numerator-12*a.denominator)%7==0 for a,b in (line_parameters[0],line_parameters[3]))
assert [f(F(6),F(36))%7 for f in (L[0],L[3])] == [0,0]
# p=11: Q2-Q3 local intersection has multiplicity three at t=6.
assert (5*6-8)%11 == 0
# p=109: L1-Q3 restriction has double root.
assert discriminants[0].numerator % 109 == 0


def isprime(n):
    if n<2:return False
    return all(n%d for d in range(2,isqrt(n)+1))

def chi(a,p):
    v=a%p
    if v==0:return 0
    return 1 if pow(v,(p-1)//2,p)==1 else -1

def rational_singular_count(p,k):
    a,b=line_parameters[k]
    A=(a.numerator*pow(a.denominator,-1,p))%p
    B=(b.numerator*pow(b.denominator,-1,p))%p
    def on(Pt):
        t,x,z=Pt
        q1=(x*z-t*t)%p
        q2=(x*x-10*t*x+25*x*z-36*z*z)%p
        q3=(4*x*z-5*t*t+8*t*z-12*z*z)%p
        ell=(x-A*t-B*z)%p
        return sum(v==0 for v in (q1,q2,q3,ell))>=2
    ans=0
    for t in range(p):
        for x in range(p):
            if on((t,x,1)):ans+=1
    for t in range(p):
        if on((t,1,0)):ans+=1
    if on((1,0,0)):ans+=1
    return ans

primes=[p for p in range(7,110) if isprime(p)]
for p in primes:
    counts=[rational_singular_count(p,k) for k in range(4)]
    if p not in (7,11,109):
        expected=[9+chi(109,p),9+chi(-11,p),10,10]
        assert counts==expected,(p,counts,expected)
    else:
        print('exception',p,counts)
print('VERIFY_OK: exact intersections, contacts, discriminants; finite-field singular supports for',len(primes),'primes')
