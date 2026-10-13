"""Exact-rational consistency checks for diagonal potential–interaction Wasserstein coordinate descent."""
from fractions import Fraction as Q
from itertools import product
from math import comb, log, exp


def r2(a, b):
    return ((b-a)/(b+a))**2

def delta(a, b):
    return 4*a*b/(a+b)**2

def step(a, b):
    return 2/(a+b)

def terms(a, b, m, v):
    return a*m*m/Q(2) + b*v/Q(2)

def after(a, b, m, v, eta):
    return terms(a, b, (1-eta*a)*m, (1-eta*b)**2*v)

checks = 0
for a in range(1,9):
  for b in range(a+1,12):
    a,b=Q(a),Q(b)
    eta=step(a,b)
    t=r2(a,b)
    d=delta(a,b)
    assert d==1-t
    for m,v in product([Q(-2),Q(-1,2),Q(0),Q(3)], [Q(0),Q(1,5),Q(1),Q(3)]):
      assert after(a,b,m,v,eta)==t*terms(a,b,m,v)
      checks+=1
    for eta_test in [Q(1,10*b),Q(1,2*b),Q(1,b),Q(3,2*b),Q(2,b),Q(4,b)]:
      tt=max((1-eta_test*a)**2,(1-eta_test*b)**2)
      assert tt>=t
      checks+=1

# Exact finite-time expectation formula checked via counting two-coordinate sampling paths.
for a1,b1,a2,b2 in [(Q(1),Q(2),Q(1),Q(3)),(Q(2),Q(7),Q(3),Q(8)),(Q(2),Q(3),Q(4),Q(5))]:
  eta1,eta2=step(a1,b1),step(a2,b2)
  p=Q(2,5)
  z1,z2=terms(a1,b1,Q(3),Q(2)),terms(a2,b2,Q(-2),Q(4))
  t1,t2=r2(a1,b1),r2(a2,b2)
  for k in range(1,10):
    enum=sum(Q(comb(k,j))*p**j*(1-p)**(k-j)*(z1*t1**j+z2*t2**(k-j)) for j in range(k+1))
    closed=z1*(1-p*(1-t1))**k + z2*(1-(1-p)*(1-t2))**k
    assert enum==closed
    checks+=1

# Exact annealed minmax value and equalized coordinate multipliers.
a1,b1,a2,b2=Q(1),Q(2),Q(1),Q(3)
d1,d2=delta(a1,b1),delta(a2,b2)
pa1=(1/d1)/(1/d1+1/d2)
pa2=1-pa1
assert pa1*d1==pa2*d2
assert max(1-pa1*d1,1-pa2*d2)==1-1/(1/d1+1/d2)

# The optimal almost-sure logarithmic weights differ except under equal t_i.
c1,c2=-log(float(r2(a1,b1))),-log(float(r2(a2,b2)))
pq1=(1/c1)/(1/c1+1/c2)
pq2=1-pq1
assert abs(pq1*c1-pq2*c2)<1e-12
assert abs(float(pa1)-pq1)>0.01

# A sharp adverse limit: almost-sure-optimized probabilities starve a nearly
# noninteracting coordinate, while annealed-optimal contraction stays bounded.
for z in [Q(1,10),Q(1,100),Q(1,10000),Q(1,1000000), Q(1,10**100)]:
    aa,bb=Q(1),Q(1)+z/Q(2)
    t_small=float(r2(aa,bb))
    t_fixed=0.25
    ca,cb=-log(t_small),-log(t_fixed)
    pq_first=(1/ca)/(1/ca+1/cb)
    annealed_quenched=max(1-pq_first*(1-t_small),1-(1-pq_first)*(1-t_fixed))
    annealed_opt=1-1/(1/(1-t_small)+1/(1-t_fixed))
    assert annealed_quenched>annealed_opt
    checks+=1
assert annealed_quenched>0.99
assert abs(annealed_opt - 4/7)<1e-6

# Independently calculate the original pairwise energy of particle laws,
# rather than only its variance-reduced representation.
def energy_atoms(points, aa, bb):
    n=Q(len(points))
    dimension=len(aa)
    pot=sum(sum(aa[i]*x[i]*x[i] for i in range(dimension)) for x in points)/(2*n)
    inter=sum(sum(bb[i]*(x[i]-y[i])**2 for i in range(dimension)) for x in points for y in points)/(8*n*n)
    return pot+inter

for aa in [(Q(1),Q(2)),(Q(2),Q(3)),(Q(5),Q(1))]:
    bb=(Q(2),Q(4))
    points=[(Q(1),Q(-3)),(Q(4),Q(1)),(Q(-2),Q(2))]
    n=Q(len(points))
    means=[sum(x[i] for x in points)/n for i in range(2)]
    variances=[sum((x[i]-means[i])**2 for x in points)/n for i in range(2)]
    a_modes=[aa[i]+bb[i]/2 for i in range(2)]
    assert energy_atoms(points,aa,bb)==sum(terms(aa[i],a_modes[i],means[i],variances[i]) for i in range(2))
    checks+=1
    for i in range(2):
        for eta in [Q(1,9),Q(2)/(aa[i]+a_modes[i]),Q(3,7)]:
            updated=[]
            for x in points:
                y=list(x)
                grad=aa[i]*means[i]+a_modes[i]*(x[i]-means[i])
                y[i]=x[i]-eta*grad
                updated.append(tuple(y))
            expected=after(aa[i],a_modes[i],means[i],variances[i],eta)+sum(terms(aa[j],a_modes[j],means[j],variances[j]) for j in range(2) if j!=i)
            assert energy_atoms(updated,aa,bb)==expected
            checks+=1

print('VERIFY_OK',checks,'exact-rational checks and limiting-regime numerical cross-checks')
