"""Exact reproduction checks for optimal noise-free leader placements on clique windmills.

Requires Python >=3.10, SymPy >=1.10.  Run `python verify.py`.
"""
from fractions import Fraction
from math import comb
import itertools
import random
import sympy as sp

K,S=sp.symbols('k s', positive=True, integer=True)
T=sp.symbols('t', real=True)
f=(S-T-1)/(S+1)+1/(T+1)
h=T/(T+1)
g=(S-T)/(T+1)**2
assert sp.factor(sp.diff(f,T,2))==2/(T+1)**3
assert sp.factor(sp.diff(h,T,2))==-2/(T+1)**3
assert sp.simplify(sp.diff(g,T,2)-(6*S-2*T+4)/(T+1)**4)==0

# Fractions encode the proof's Schur-complement costs independently of floating point.
def ft(s,t): return Fraction(s-t-1,s+1)+Fraction(1,t+1)
def gt(s,t): return Fraction(s-t,(t+1)**2)
def ht(t): return Fraction(t,t+1)
def balanced(k,m):
    a,r=divmod(m,k)
    return [a]*(k-r)+[a+1]*r

def cost_profile(k,s,counts,hub):
    assert len(counts)==k and all(0<=t<=s for t in counts)
    base=sum((ft(s,t) for t in counts),Fraction())
    if hub:return base
    denom=(s+1)*sum((ht(t) for t in counts),Fraction())
    assert denom>0
    return base+(1+sum((gt(s,t) for t in counts),Fraction()))/denom

def optimum(k,s,m):
    assert 1<=m<=k*s
    H=cost_profile(k,s,balanced(k,m-1),True)
    N=cost_profile(k,s,balanced(k,m),False)
    return min(H,N), ('both' if H==N else ('hub' if H<N else 'peripheral')),H,N

# All occupancy profiles for small systems: find every conditional minimizer.
profile_checks=0
for k in range(2,6):
  for s in range(2,6):
    for m in range(1,k*s+1):
      for hub in (False,True):
        tcount=m-int(hub)
        ideal=cost_profile(k,s,balanced(k,tcount),hub)
        for counts in itertools.product(range(s+1),repeat=k):
          if sum(counts)!=tcount:continue
          value=cost_profile(k,s,counts,hub)
          assert value>=ideal,(k,s,m,hub,counts,value,ideal)
          assert (value==ideal)==(max(counts)-min(counts)<=1),(k,s,m,hub,counts)
          profile_checks+=1

# Verify complete analytic three-leader phase classification and ties.
three_checks=0
for k in range(2,12):
  for s in range(2,15):
    val,which,H,N=optimum(k,s,3)
    expected=('peripheral' if (k==2 and s<=4) or k==3 else
              'both' if (k==2 and s==5) or (k==4 and s==2) else 'hub')
    assert which==expected,(k,s,which,expected)
    three_checks+=1

# Independent exact inversion of the actual unweighted combinatorial Laplacian.
def build(k,s):
    n=1+k*s; L=sp.zeros(n)
    def edge(i,j):
        L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    for b in range(k):
        v=tuple(range(1+b*s,1+(b+1)*s))
        for i in v:edge(0,i)
        for i,j in itertools.combinations(v,2):edge(i,j)
    return L

def trace_inverse(L,leaders):
    followers=[i for i in range(L.rows) if i not in leaders]
    return sp.trace(L.extract(followers,followers).inv())

rng=random.Random(20261021)
inverse_checks=0
for k,s in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(5,3),(6,2)]:
  L=build(k,s)
  n=L.rows
  checks=[]
  for m in range(1,n):
    x=range(1,n)
    # Both hub and no-hub representatives, varying budgets.
    if m-1<=len(x):
        checks.append((0,)+tuple(rng.sample(list(x),m-1)))
    if m<=len(x):checks.append(tuple(rng.sample(list(x),m)))
  for leaders in checks:
    profile=[0]*k
    for i in leaders:
      if i:profile[(i-1)//s]+=1
    actual=trace_inverse(L,leaders)
    formula=cost_profile(k,s,profile,0 in leaders)
    assert actual==sp.Rational(formula.numerator,formula.denominator),(k,s,leaders,actual,formula)
    inverse_checks+=1

# Exhaustive 3-leader optimizer counts from independent principal-minor inverses.
exhaustive_checks=0
count_checks=0
for k,s in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3)]:
    L=build(k,s)
    optimal_value,_,H,N=optimum(k,s,3)
    hits=0
    for tri in itertools.combinations(range(L.rows),3):
        actual=trace_inverse(L,tri)
        assert actual>=sp.Rational(optimal_value.numerator,optimal_value.denominator)
        hits+=actual==sp.Rational(optimal_value.numerator,optimal_value.denominator)
        exhaustive_checks+=1
    # Each balanced leader occupancy contributes product binomials, with hub as needed.
    def nprofiles(m,hub):
        a,r=divmod(m,k)
        return comb(k,r)*(comb(s,a)**(k-r))*(comb(s,a+1)**r)
    count=(nprofiles(2,True) if H==optimal_value else 0)+(nprofiles(3,False) if N==optimal_value else 0)
    assert hits==count,(k,s,hits,count)
    count_checks+=1

print('VERIFY_OK symbolic_derivatives=3 occupancy_profiles=%d triple_phase_cases=%d exact_grounded_inverses=%d exhaustive_three_leader_inverses=%d optimizer_count_checks=%d'%(profile_checks,three_checks,inverse_checks,exhaustive_checks,count_checks))
