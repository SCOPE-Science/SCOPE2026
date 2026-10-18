"""Independent double-counting and exact orbit-size tests; no graph-refinement code."""
from itertools import combinations
from math import comb
from collections import Counter

def C(n,r):
    return comb(n,r) if 0 <= r <= n else 0

def check(n,k,b):
    A=frozenset(range(k))
    B=frozenset(list(range(b))+list(range(k,k+k-b)))
    vertices=[frozenset(v) for v in combinations(range(n),k)]
    class_freq=Counter()
    for X in vertices:
        s=len(X&A);t=len(X&B);r=len(X&A&B)
        class_freq[(r,s-r,t-r,k-s-t+r)]+=1
        observed=sum(len(Y&A)*len(Y&B) for Y in vertices if X.isdisjoint(Y))
        expected=(k-s)*(k-t)*C(n-k-2,k-2)+(b-r)*C(n-k-2,k-1)
        assert observed==expected,(n,k,b,X,observed,expected)
        recovered=b-(observed-(k-s)*(k-t)*C(n-k-2,k-2))//C(n-k-2,k-1)
        assert recovered==r
    ranges=(b,k-b,k-b,n-2*k+b)
    feasible=[]
    for a in range(ranges[0]+1):
      for d in range(ranges[1]+1):
       for e in range(ranges[2]+1):
        f=k-a-d-e
        if 0<=f<=ranges[3]:
         tup=(a,d,e,f)
         feasible.append(tup)
         expected=C(ranges[0],a)*C(ranges[1],d)*C(ranges[2],e)*C(ranges[3],f)
         assert class_freq[tup]==expected,(n,k,b,tup)
    assert len(class_freq)==len(feasible)
    assert sum(class_freq.values())==C(n,k)
    return len(vertices)

def main():
  cases=0;instances=0
  for k in range(2,5):
    for n in range(3*k-1,min(3*k+3,13)):
      for b in range(k):
        instances+=check(n,k,b);cases+=1
  A={0,1,2};B={0,3,4}
  for X, expected in [({0,5,6},12),({1,3,5},15)]:
    observed=sum(len(set(Y)&A)*len(set(Y)&B) for Y in combinations(range(8),3) if not (set(Y)&X))
    assert observed==expected
  print('PASS: moment and orbit-size configurations=',cases,'total vertex-instances=',instances)
  print('SHARPNESS KG(8,3): weighted neighborhood moments = 12 and 15')

if __name__=='__main__':main()
