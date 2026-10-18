from itertools import combinations, product
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

def formula(sizes):
    return max(Fraction(s+1,s//2+1) for s in sizes)

def solve_direct_fractional_cover(sizes):
    n=1+sum(sizes)
    assert n<=11
    adj=[set() for _ in range(n)]
    groups=[];k=1
    for s in sizes:
        block=list(range(k,k+s));groups.append(block)
        for v in block:
            adj[v].add(0); adj[0].add(v)
            for w in block:
                if v!=w: adj[v].add(w)
        k+=s
    stable=[]
    for mask in range(1<<n):
        selected=[v for v in range(n) if mask>>v&1]
        if all(2*sum(w in adj[v] for w in selected)<=len(adj[v]) for v in selected):
            stable.append(mask)
    # compress orbit profiles to save LP vars
    reps={}
    for mask in stable:
        profile=(int(mask&1),)+tuple(sum(mask>>v&1 for v in block) for block in groups)
        reps[profile]=mask
    cols=[]
    for (hub,*counts) in reps:
        cols.append([hub]+[c/s for c,s in zip(counts,sizes)])
    A=np.array(cols,dtype=float).T
    res=linprog(np.ones(len(cols)),A_ub=-A,b_ub=-np.ones(1+len(sizes)),bounds=(0,None),method='highs')
    assert res.success,res.message
    return res.fun,len(stable),len(reps),n

checks=0;states=0
for t in range(1,5):
 for sizes in product(range(1,5),repeat=t):
  if 1+sum(sizes)>11:continue
  value,st,num,n=solve_direct_fractional_cover(sizes)
  expected=float(formula(sizes))
  assert abs(value-expected)<1e-8,(sizes,value,expected)
  checks+=1;states+=(1<<n)
print('verified_profiles',checks,'subset_states_enumerated',states)
for sizes in [(2,), (3,), (2,2), (2,4), (2,3),(1,4),(4,4),(2,2,2),(2,4,4)]:
 print(sizes,'=',formula(sizes))
