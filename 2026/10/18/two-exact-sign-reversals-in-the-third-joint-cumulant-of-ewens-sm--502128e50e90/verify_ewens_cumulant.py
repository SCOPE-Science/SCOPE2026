"""Standalone exact checks for Ewens mixed cumulant; requires SymPy."""
import itertools
import math
from fractions import Fraction
import sympy as s

n,t=s.symbols('n t',integer=True,positive=True)
def w(k):
    return s.prod((n-i)/(t+n-1-i) for i in range(k))
Q=(5*n-10)*t**3+(8*n**2-53*n+60)*t**2+(n**3-29*n**2+128*n-110)*t-2*n**4+14*n**3-12*n**2-60*n+60
F=w(6)-w(3)**2-w(4)*w(2)-w(5)*w(1)+2*w(1)*w(2)*w(3)
D=(n+t-6)*(n+t-5)*(n+t-4)*(n+t-3)**2*(n+t-2)**2*(n+t-1)**3
assert s.cancel(F-6*n*(n-2)*(n-1)*(t-1)*Q/D)==0
assert s.factor(Q.subs(t,2))==-2*n*(n-4)*(n-3)*(n-1)
assert s.factor(Q.subs(t,3))==-n*(n-6)*(n-3)*(2*n+1)
assert s.simplify(Q.subs(t,0)+2*(n-1)*(n**3-6*n**2+30))==0
assert s.factor(s.diff(Q,t).subs(t,2))==n**3+3*n**2-24*n+10
c,d=s.symbols('c d')
assert s.factor(s.expand(Q.subs(t,c*n)).coeff(n,4))==(c+1)**2*(5*c-2)
assert s.simplify(s.expand(Q.subs(t,s.Rational(2,5)*n+d)).coeff(n,3))==s.Rational(49,5)*d-s.Rational(168,25)

# Independently enumerate partitions (cycle-count vectors) and Ewens weights.
def partitions_count(n_left,min_size=1):
    if n_left==0:
        yield ()
    else:
        for part in range(min_size,n_left+1):
            for rest in partitions_count(n_left-part,part):
                yield (part,)+rest

def exact_cumulant(N,theta):
    denominator=Fraction(math.prod(theta+i for i in range(N)),1)
    moments={mask:Fraction(0) for mask in range(8)}
    for parts in partitions_count(N):
        counts={j:parts.count(j) for j in set(parts)}
        weight=Fraction(math.factorial(N),1)*theta**len(parts)
        for j,v in counts.items():
            weight/=j**v * math.factorial(v)
        prob=weight/denominator
        for mask in range(8):
            prod=1
            for j in range(1,4):
                if mask>>(j-1)&1:
                    prod*=counts.get(j,0)
            moments[mask]+=prob*prod
    assert moments[0]==1
    mm=moments
    return mm[7]-mm[3]*mm[4]-mm[5]*mm[2]-mm[6]*mm[1]+2*mm[1]*mm[2]*mm[4]

ct=0
for N in range(6,13):
    for theta in [Fraction(1,2),Fraction(1),Fraction(2),Fraction(3),Fraction(5),Fraction(9),Fraction(20)]:
        actual=exact_cumulant(N,theta)
        predicted=Fraction(s.Rational(theta.numerator,theta.denominator)**3 / 6 * F.subs({n:N,t:s.Rational(theta.numerator,theta.denominator)}))
        assert actual==predicted,(N,theta,actual,predicted)
        ct+=1
print('PASS: symbolic factorization, three anchor factorizations, asymptotic expansion; independent partition enumeration',ct,'cases')
