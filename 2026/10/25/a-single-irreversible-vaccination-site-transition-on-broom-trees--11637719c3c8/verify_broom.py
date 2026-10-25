"""Exact arithmetic independent epidemic and candidate tests for single-vertex protection on broom trees."""
from fractions import Fraction
from itertools import product
from math import comb

def broom(k,L):
    n=1+k+L
    edges=[(0,i) for i in range(1,k+1)]
    edges+=[(0,k+1)]+[(k+i,k+i+1) for i in range(1,L)]
    return n,edges

def pair_score(n,edges,v,p):
    adj=[[] for _ in range(n)]
    for x,y in edges: adj[x].append(y);adj[y].append(x)
    ans=Fraction(0)
    for x in range(n):
      if x==v:continue
      stack=[(x,-1,0)]
      for a,b,d in stack:
        ans+=p**d
        for c in adj[a]:
          if c!=b and c!=v:stack.append((c,a,d+1))
    return ans

def edge_score(n,edges,v,p):
    # Independently sum all percolation outcomes and all potential seed vertices.
    keep=[(x,y) for x,y in edges if x!=v and y!=v]
    s=Fraction(0)
    for mask in range(1<<len(keep)):
      adj=[[] for _ in range(n)]
      cnt=mask.bit_count()
      weight=p**cnt*(1-p)**(len(keep)-cnt)
      for j,(x,y) in enumerate(keep):
        if mask>>j & 1:adj[x].append(y);adj[y].append(x)
      total=0;seen=set()
      for x in range(n):
        if x==v or x in seen:continue
        st=[x];seen.add(x);size=0
        for y in st:
          size+=1
          for z in adj[y]:
            if z not in seen:seen.add(z);st.append(z)
        total+=size*size
      s+=weight*total
    return s

def formula(k,L,t,p):
    C=Fraction(k*(k-1),2)
    c=1-k*(1-p)
    return 2*p*(1-p**t)*(p**(L-t)-c)/(1-p)**2 + 2*C*p*p

def optimal_gap(k,L,p):
    n,es=broom(k,L)
    sc=[pair_score(n,es,i,p) for i in range(n)]
    best=min(sc)
    return [i for i,v in enumerate(sc) if v==best]

def run():
  checked=0;identities=0
  for k in range(2,5):
    for L in range(2,8):
      n,edges=broom(k,L)
      for p in (Fraction(1,3),Fraction(2,3)):
        ps=[pair_score(n,edges,v,p) for v in range(n)]
        for v in range(n):
          assert ps[v]==edge_score(n,edges,v,p),(k,L,p,v,ps[v])
          checked+=1
        for t in range(1,L):
          assert ps[k+t]-ps[0]==formula(k,L,t,p)
          identities+=1
        assert all(ps[v]>ps[0] for v in range(1,k+1))
        assert ps[n-1]>ps[n-2]
  # A critical benchmark: (k,L)=(2,5), t=1 always dominates other path vertices.
  k,L=2,5
  for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(4,5),Fraction(9,10),Fraction(99,100)):
    best=optimal_gap(k,L,p)
    assert best==([0] if p*p+p*p*p<1 else [k+1]),(p,best)
  # Separate empirical check of strict decrease of critical p as the handle length grows.
  for k in (2,3,4,5):
    for L in range(3,26):
      d=L-k
      switch=(d>=2 and 2*(d*d//4)>k*(k-1))
      at1=[k*(k-1)+2*t*(t+k-L) for t in range(1,L)]
      assert (min(at1)<0)==switch
  print('PASS',checked,'independent exact enumerations; ',identities,'difference identities; threshold and benchmark checks PASS')
if __name__=='__main__':run()
