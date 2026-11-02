"""Reproducibility checks for Ewens fixed-point occupation covariance."""
from fractions import Fraction
from math import exp, factorial, log1p, sqrt, log, isclose

checks = 0

def check(assertion, explanation):
    global checks
    checks += 1
    if not assertion:
        raise AssertionError(explanation)


def integral(theta, d, subdivisions=8000):
    """Independent composite Simpson quadrature for the explicit integral."""
    if subdivisions % 2:
        raise ValueError('subdivisions must be even')
    total = 0.0
    for k in range(subdivisions + 1):
        u = k / subdivisions
        value = 0.0 if k == subdivisions else exp(theta*u + d*log1p(-u))
        total += (1 if k == 0 or k == subdivisions else (4 if k%2 else 2))*value
    return total / (3*subdivisions)


def threshold(d):
    low, high = 0.0, 3*d+10.0
    for k in range(80):
        mid = (low + high) / 2
        if integral(mid,d) < 1.0:
            low = mid
        else:
            high = mid
    return (low+high)/2


def finite_exact(n, theta, d):
    """Exact rational dynamic programming for the two empirical counts."""
    theta = Fraction(theta)
    state = {1:(Fraction(1),Fraction(0),Fraction(1 if d==1 else 0),Fraction(0))}
    for j in range(1,n):
        new = {}
        for c, (p,a,b,ab) in state.items():
            transitions = ((c+1,theta/(theta+j)),(c-1,Fraction(c,1)/(theta+j)),(c,Fraction(j-c,1)/(theta+j)))
            for nxt, weight in transitions:
                if not weight:
                    continue
                t = 1 if nxt==0 else 0
                v = 1 if nxt==d else 0
                p2,a2,b2,ab2 = new.get(nxt,(Fraction(0),)*4)
                new[nxt] = (p2+weight*p,a2+weight*(a+t*p),b2+weight*(b+v*p),ab2+weight*(ab+a*v+b*t+p*t*v))
        state = new
        check(sum(entry[0] for entry in state.values())==1,'mass conservation')
    mean_a = sum(entry[1] for entry in state.values())/n
    mean_b = sum(entry[2] for entry in state.values())/n
    mixed = sum(entry[3] for entry in state.values())/n**2
    return mean_a,mean_b,mixed-mean_a*mean_b

# Boundary, normalization, state-exclusion and convergence checks.
for d in range(1,9):
    check(isclose(integral(0,d),1/(d+1),rel_tol=2e-7), 'zero-intensity integral')
    root = threshold(d)
    check(root>0,'positive root')
    check(abs(integral(root,d)-1)<1e-7,'root equation')
    check(integral(root*0.95,d)<1,'negative covariance phase')
    check(integral(root*1.05,d)>1,'positive covariance phase')
    if d>1:
        check(threshold(d)>threshold(d-1),'ordered thresholds')

check(abs(threshold(1)-1.79328213290076)<1e-7,'first root')
check(abs(threshold(2)-3.38363428285321)<1e-7,'second root')

for theta in (1,2,3):
    for d in (1,2):
        a,b,cov = finite_exact(25,theta,d)
        check(0<=a<=1 and 0<=b<=1,'occupation means')
        check(cov>=-Fraction(1,4) and cov<=Fraction(1,4),'occupation covariance bound')
        expected_a=exp(-theta)
        check(abs(float(a)-expected_a)<0.08,'derangement frequency mean')

# Strict asymptotic scale ratio approaches 1 (very slowly); check broad bounds.
for d in (100,500,1000):
    root=threshold(d)
    ratio=(root-d)/sqrt(d*log(d))
    check(0.75<ratio<1.15,'threshold transition scale')

print(f'PASS: {checks} independent exact/deterministic checks; theta1={threshold(1):.12f}; theta2={threshold(2):.12f}')
