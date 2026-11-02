"""Standalone exact check for a two-agent binary-chore lottery criterion.
All allocation patterns and both strong WEFX inequalities are tested.
"""
from fractions import Fraction
from itertools import product
from math import comb

def test_instance(a,b,c,d,p):
    q=1-p
    tasks=[(1,0)]*a+[(0,1)]*b+[(1,1)]*c+[(0,0)]*d
    feasible_ef=0
    supports=[]
    for assignments in product((0,1),repeat=len(tasks)):
        bundles=[[],[]]
        for k,owner in enumerate(assignments): bundles[owner].append(k)
        own=[sum(tasks[k][i] for k in bundles[i]) for i in (0,1)]
        social=sum(own)
        # Independently check fractional PO via minimum possible total cost.
        if social!=sum(min(pair) for pair in tasks):continue
        cross=[sum(tasks[k][i] for k in bundles[1-i]) for i in (0,1)]
        exact_ef=q*own[0]<=p*cross[0] and p*own[1]<=q*cross[1]
        if exact_ef: feasible_ef+=1
        def max_after(i):
            return max((own[i]-tasks[k][i] for k in bundles[i]),default=0)
        wefx=q*max_after(0)<=p*cross[0] and p*max_after(1)<=q*cross[1]
        if wefx:
            supports.append((own[0],cross[0],own[1],cross[1]))
    # Ex-ante WEF is a pair of affine inequalities. Under fPO the
    # only variable is x = number of shared-cost chores given to agent 1.
    # Convex hull of projection is interval [min x,max x].
    criterion=(feasible_ef>0)
    if supports:
        xs=[v[0] for v in supports]
        # Expected x lies in [lower,upper].
        lottery=(min(xs)<=p*(a+c) and max(xs)>=p*c-q*b)
    else: lottery=False
    count_formula=(2**d)*sum(comb(c,x) for x in range(c+1) if p*c-q*b<=x<=p*(a+c))
    assert feasible_ef==count_formula,(a,b,c,d,p,feasible_ef,count_formula)
    assert criterion==lottery,(a,b,c,d,p,criterion,lottery,supports)
    return len(supports)

cases=0; allocations=0; wefx=0
for size in range(9):
 for a in range(size+1):
  for b in range(size-a+1):
   if a+b==0:continue
   for c in range(size-a-b+1):
    d=size-a-b-c
    for B in range(2,10):
     for A in range(1,B):
      cases+=1;allocations+=2**size
      wefx+=test_instance(a,b,c,d,Fraction(A,B))
print(f'VERIFY_OK cases={cases} allocations={allocations} wefx_supports={wefx}')
