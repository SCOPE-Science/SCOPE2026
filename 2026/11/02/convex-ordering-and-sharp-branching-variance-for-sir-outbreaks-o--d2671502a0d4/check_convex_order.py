"""Exact stop-loss (convex-order) checks on all labelled rooted trees through n=6."""
from itertools import product
from fractions import Fraction as F
from verify_tree_variance import adj_from_prufer,pgf

def stoploss(poly,k):return sum(max(0,i-k)*x for i,x in enumerate(poly))

def run():
  tested=0; strict=0
  families=[
    [[(F(1,2),F(1))],[(F(1,4),F(1,2)),(F(3,4),F(1,2))],[(F(0),F(1,2)),(F(1),F(1,2))]],
    [[(F(2,5),F(1))],[(F(1,5),F(2,3)),(F(4,5),F(1,3))],[(F(0),F(3,5)),(F(1),F(2,5))]],
  ]
  for n in range(2,7):
    for code in product(range(n),repeat=n-2):
      adj=adj_from_prufer(code)
      for r in range(n):
        for fam in families:
          poly=[pgf(adj,r,law) for law in fam]
          assert len(set(sum(F(i)*q for i,q in enumerate(a)) for a in poly))==1
          for k in range(n+1):
            vals=[stoploss(a,k) for a in poly]
            assert vals==sorted(vals),(n,code,r,k,vals)
            tested+=1
            if vals[0]<vals[-1]: strict+=1
    print('n=',n, 'cases=',tested)
  print('CONVEX_ORDER_PASS', tested, 'stop-loss triplet checks; strict cases',strict)
if __name__=='__main__':run()
