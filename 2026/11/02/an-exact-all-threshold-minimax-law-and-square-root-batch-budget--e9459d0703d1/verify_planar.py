"""Standalone reproducibility checks for planar Gaussian random-line minimization.

The universal theorem is established analytically in RESULT.md.  These checks
independently test the line-energy identity, angular density, finite CDF,
minimax ordering, batch confidence and the large-condition-number limit.
No online resources and no third-party packages are needed.
"""
from fractions import Fraction
import math
import random

pi = math.pi
checks = 0

def check(ok, msg):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(msg)

def simpson(f, a, b, n=4096):
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for j in range(1, n):
        s += (4 if j % 2 else 2) * f(a+j*h)
    return s * h / 3

def pdens(phi, K):
    return math.sqrt(K) / (pi*(K*math.cos(phi)**2 + math.sin(phi)**2))

def fail(K, t):
    return 2 / pi * math.atan(math.sqrt(K*t / (1-t)))

# 1. Exact rational arithmetic independently reconstructs one-line minimization.
for K in (Fraction(1), Fraction(2), Fraction(9), Fraction(100)):
    for x1 in (Fraction(-3,5), Fraction(1), Fraction(7,3)):
      for x2 in (Fraction(-2), Fraction(1,4), Fraction(11,7)):
       for u1 in (Fraction(0), Fraction(1,3), Fraction(-4,3)):
        for u2 in (Fraction(0), Fraction(5,4), Fraction(-2,3)):
         if u1==u2==0:continue
         E=x1*x1+K*x2*x2
         a=(u1*x1+K*u2*x2)/(u1*u1+K*u2*u2)
         after=(x1-a*u1)**2+K*(x2-a*u2)**2
         p=(u1*x1+K*u2*x2)**2/((u1*u1+K*u2*u2)*E)
         check(E-after == E*p, 'exact fraction energy identity')
         check(0<=p<=1, 'progress bounded')

# 2. Angular distribution, exact derivative formula, symmetry and minimizer.
for K in (1, 2, 9, 100):
    check(abs(simpson(lambda ph:pdens(ph,K),0,pi,16384)-1)<2e-10,
          'angular density normalization')
    for t in (.07, .25, .5, .8, .97):
      r=math.acos(math.sqrt(t))
      success=simpson(lambda ph:pdens(ph,K),-r,r,8192)
      check(abs(success-(1-fail(K,t)))<2e-9,'Cauchy exact threshold probability')
      vals=[simpson(lambda ph:pdens(ph,K),j*pi/32-r,j*pi/32+r,2048)
            for j in range(17)]
      check(all(vals[j] <= vals[j+1]+1e-11 for j in range(16)),
            'orientation stochastic minimax')
      for th in (.04,.2,.65,1.1):
        D=lambda ph: K*math.cos(ph)**2+math.sin(ph)**2
        diff=pdens(th+r,K)-pdens(th-r,K)
        identity=math.sqrt(K)*(K-1)*math.sin(2*th)*math.sin(2*r)/(pi*D(th+r)*D(th-r))
        check(abs(diff-identity)<1e-10, 'angular derivative identity')

# 3. Exact single-probe mean and median at the hard orientation.
for K in (1, 2, 9, 100, 10000):
    mean=simpson(lambda ang:math.cos(ang)**2/
                 (math.cos(ang)**2 + K*math.sin(ang)**2),0,pi/2,16384)*2/pi
    check(abs(mean-1/(1+math.sqrt(K)))<2e-10,'mean line gain')
    check(abs(fail(K,1/(1+K))-.5)<1e-12,'median line gain')

# 4. Batch confidence, unique isotropic minimax, whitening calibration.
for K in (1,2,9,100,10000):
    for t in (.1,.5,.9):
      check(fail(K,t)>=fail(1,t)-1e-13,'whitening improves worst case')
      if K>1:check(fail(K,t)>fail(1,t),'strict covariance minimax')
      for delta in (.1,.05,.01):
        m=math.ceil(math.log(delta)/math.log(fail(K,t)))
        check(fail(K,t)**m<=delta+1e-13,'batch count suffices')
        check(fail(K,t)**(m-1)>delta-1e-13,'batch count minimal')

# 5. Independent Gaussian simulation checks exact finite CDF, including rotation.
rng=random.Random(20261031)
N=60000
K=9
for angle in (0, pi/6, pi/3, pi/2):
    n_fail=0
    for _ in range(N):
        v1=rng.gauss(0,1);v2=math.sqrt(K)*rng.gauss(0,1)
        norm2=v1*v1+v2*v2
        progress=(v1*math.cos(angle)+v2*math.sin(angle))**2/norm2
        n_fail+=(progress<.5)
    rate=n_fail/N
    check(rate<=fail(K,.5)+.012,'empirical stochastic minimax')
    if angle==0:check(abs(rate-fail(K,.5))<.012,'empirical hard-axis CDF')
    if angle==pi/2:check(rate<fail(K,.5)-.3,'easy axis strict separation')

# 6. Full batch CDF and diffusive sqrt condition-number scaling.
for m in (1,2,5,10):
    n_fail=0
    for _ in range(30000):
        good=False
        for __ in range(m):
            g1=rng.gauss(0,1);g2=rng.gauss(0,1)
            good = good or (g1*g1/(g1*g1+K*g2*g2)>=.5)
            # Continue drawing to preserve fixed batch size in all cases.
        n_fail += not good
    check(abs(n_fail/30000-fail(K,.5)**m)<.018,'batch distribution')

for c in (.25,1,2,4):
    Klarge=1000000
    m=round(c*math.sqrt(Klarge))
    for t in (.2,.5,.8):
        q=fail(Klarge,t)**m
        limiting=math.exp(-2*c/pi*math.sqrt((1-t)/t))
        check(abs(q-limiting)<.002,'sqrt condition scaling limit')

print(f'PASS: {checks} independent deterministic assertions; exact-arithmetic line identity,')
print('angular minimax, finite CDF, batch law, whitening and asymptotic limit.')
