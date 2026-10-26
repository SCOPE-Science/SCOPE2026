"""Independent finite checks for constrained planar Gaussian-minimum completion.
All theorem-scale assertions are proved analytically in RESULT.md; this code checks exact
rational interval certificates and numerical identities at selected configurations.
"""
import math
from fractions import Fraction as Q
from itertools import product

def sine_upper(x):
    x = Q(x)
    return sum((-1)**k*x**(2*k+1)/math.factorial(2*k+1) for k in range(5))

def sine_lower(x):
    x = Q(x)
    return sum((-1)**k*x**(2*k+1)/math.factorial(2*k+1) for k in range(6))

# Classical elementary enclosures for pi, with rational arithmetic only.
PI_LO = Q(314159265, 100000000)
PI_HI = Q(314159266, 100000000)
def arctan_bound(z,terms):
    z=Q(z)
    partial=sum((-1)**k*z**(2*k+1)/Q(2*k+1) for k in range(terms))
    next_term=z**(2*terms+1)/Q(2*terms+1)
    return (partial,partial+next_term) if terms%2==0 else (partial-next_term,partial)
# Use independent exact arithmetic and Machin's identity for the pi enclosure.
a_lo,a_hi=arctan_bound(Q(1,5),10)
b_lo,b_hi=arctan_bound(Q(1,239),6)
pi_lower=16*a_lo-4*b_hi
pi_upper=16*a_hi-4*b_lo
assert PI_LO < pi_lower <= pi_upper < PI_HI
assert pi_lower < Q(22,7) and Q(3,1)<pi_lower

def bound_sine_pi(a, b):
    lo,hi=Q(a,b)*PI_LO, Q(a,b)*PI_HI
    assert 0 <= lo <= hi <= Q(21,10)
    # Sine is 1-Lipschitz, so these enclosures remain valid past pi/2.
    return sine_lower(lo)-(hi-lo), sine_upper(lo)+(hi-lo)

# Strictly positive lower bound of the proposed moment gap between A and B.
terms=((3,13,60),(1,7,20),(-2,13,40),(-2,7,40))
lower=Q(0)
upper=Q(0)
for coeff,a,b in terms:
    lo,hi=bound_sine_pi(a,b)
    lower += coeff * (lo if coeff>0 else hi)
    upper += coeff * (hi if coeff>0 else lo)
assert lower > Q(28,1000), (float(lower),float(upper))
assert upper < Q(30,1000)
# A also beats the allocation C = (1,3).
termsC=((3,13,60),(1,7,20),(-1,13,20),(-3,7,60))
lowerC=Q(0)
for coeff,a,b in termsC:
    lo,hi=bound_sine_pi(a,b)
    lowerC += coeff * (lo if coeff>0 else hi)
assert lowerC > Q(4,5)

L=13*math.pi/20
S=7*math.pi/20
A=(L/3, L/3, L/3, S)
B=(L/2,L/2,S/2,S/2)
C=(L,S/3,S/3,S/3)
assert math.isclose(sum(A),math.pi)
assert math.isclose(sum(B),math.pi)
assert max(A)>max(B)

def second_moment(gaps):
    return 1-sum(math.sin(x) for x in gaps)/math.pi
assert second_moment(A)<second_moment(B)<second_moment(C)

def tail(gaps,t,steps=1200):
    # Angular integral integrated against the Rayleigh survival function.
    total=0.0
    for d in gaps:
        h=d/2
        du=h/steps
        ss=0.0
        for k in range(steps+1):
            angle=k*du
            vv=0 if k==0 else math.exp(-(t*t)/(2*math.sin(angle)**2))
            ss+=(1 if k==0 or k==steps else 4 if k%2 else 2)*vv
        total+=du*ss/3
    return (2/math.pi)*total

# Second moment from the survival integral, separately checked via finite angular quadrature.
for gapset in (A,B,C):
    r=second_moment(gapset)
    # Direct angular integration of 2 sin^2(D), not the sine-sum identity.
    val=0.0
    for d in gapset:
        N=1000
        dx=(d/2)/N
        val+= (4/math.pi)*dx/3 * sum((1 if i in (0,N) else 4 if i%2 else 2)*math.sin(i*dx)**2 for i in range(N+1))
    assert abs(val-r)<2e-10,(val,r)

for t in (0.1,0.5,1,2,4,8,14):
    pa,pb=tail(A,t),tail(B,t)
    assert 0<pa<1 and 0<pb<1
    if t>=8:
        assert pb<pa,(t,pb,pa)

# One-insertion convexity at sampled gaps: bisect the largest gap.
checks=0
for widths in ((math.pi/2,math.pi/2),(.65*math.pi,.35*math.pi),(.28*math.pi,.22*math.pi,.5*math.pi)):
    for t in (0.1,0.7,2,5):
        for j,d in enumerate(widths):
            for frac in (.1,.25,.5,.75,.9):
                new=list(widths[:j])+[d*frac,d*(1-frac)]+list(widths[j+1:])
                best_gap=max(widths)
                best=list(widths); best.remove(best_gap)
                best.extend((best_gap/2,best_gap/2))
                assert tail(best,t,400) <= tail(new,t,400)+2e-12
                checks+=1

print('Rational sine certificate: A-B in (%.9f, %.9f), A-C > %.9f' % (float(lower),float(upper),float(lowerC)))
print('Second moments: A %.12f, B %.12f, C %.12f'%(second_moment(A),second_moment(B),second_moment(C)))
for t in (2,8,14):
    print('Tail at %.0f: A %.12g, B %.12g'%(t,tail(A,t),tail(B,t)))
print('One-insertion finite comparison checks:',checks)
print('PASS: rational interval, exact gap identity, asymptotic ordering diagnostics')
