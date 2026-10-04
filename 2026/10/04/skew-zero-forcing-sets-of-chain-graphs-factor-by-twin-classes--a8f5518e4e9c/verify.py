from itertools import combinations_with_replacement
from collections import Counter

def build_chain(m,n,degs):
    # A=0..m-1, B=m..m+n-1; N(a_i)={B_0,...,B_{d_i-1}}
    N=m+n
    adj=[set() for _ in range(N)]
    for i,d in enumerate(degs):
        for j in range(d):
            u=i; v=m+j
            adj[u].add(v); adj[v].add(u)
    return adj

def twin_classes(adj):
    groups={}
    for v,a in enumerate(adj):
        key=tuple(sorted(a))
        groups.setdefault(key,[]).append(v)
    return list(groups.values())

def skew_forces(adj, blue_mask):
    N=len(adj); blue=[bool(blue_mask>>v &1) for v in range(N)]
    while True:
        changed=False
        # any vertex, blue or white, with exactly one white neighbor forces it
        for u in range(N):
            whites=[v for v in adj[u] if not blue[v]]
            if len(whites)==1:
                blue[whites[0]]=True
                changed=True
                break
        if not changed: break
    return all(blue)

def predicted(classes,N,mask):
    for T in classes:
        w=sum(1 for v in T if not (mask>>v)&1)
        if w>1: return False
    return True

def poly_product(classes):
    # coefficients exponent -> count of S; each class factor x^t + t*x^(t-1)
    c={0:1}
    for T in classes:
        t=len(T); d={t:1,t-1:t}
        z={}
        for a,x in c.items():
            for b,y in d.items(): z[a+b]=z.get(a+b,0)+x*y
        c=z
    return c

graphs=subset_checks=coefficient_checks=0
max_order=10
for total in range(2,max_order+1):
  for m in range(1,total):
    n=total-m
    # connected: every A degree >=1 and max degree n; sorted nondecreasing
    # canonical profiles: first m-1 may range 1..n, last fixed n
    for pref in combinations_with_replacement(range(1,n+1),m-1):
      degs=tuple(pref)+(n,)
      adj=build_chain(m,n,degs)
      classes=twin_classes(adj)
      actual=Counter()
      for mask in range(1<<total):
        a=skew_forces(adj,mask)
        p=predicted(classes,total,mask)
        subset_checks+=1
        if a!=p:
          raise AssertionError((m,n,degs,classes,mask,a,p))
        if a: actual[mask.bit_count()]+=1
      formula=poly_product(classes)
      for k in range(total+1):
        coefficient_checks+=1
        if actual.get(k,0)!=formula.get(k,0):
          raise AssertionError(('poly',m,n,degs,k,actual.get(k,0),formula.get(k,0),classes))
      # min exponent and count
      z=min(actual) if actual else None
      expected=total-len(classes)
      if z!=expected: raise AssertionError(('min',m,n,degs,z,expected))
      mincount=actual[z]
      prod=1
      for T in classes: prod*=len(T)
      if mincount!=prod: raise AssertionError(('count',m,n,degs,mincount,prod))
      graphs+=1
print(f'VERIFY_OK graph_profiles={graphs} subset_checks={subset_checks} coefficient_checks={coefficient_checks} max_order={max_order}')
