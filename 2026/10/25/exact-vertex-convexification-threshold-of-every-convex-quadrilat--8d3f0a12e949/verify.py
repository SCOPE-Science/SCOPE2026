"""Exact rational checks for the quadrilateral vertex-convexification formula.
Finite checks supplement, but do not prove, the universal symbolic argument.
"""
from fractions import Fraction as F
from itertools import product

def gauge(t,r):
    return t if t>=0 else -t/r

def closest(x,r):
    return min(x+r,(1-x)/r)

def score(x,y,p,q):
    return min(closest(x,p)+gauge(y,q), gauge(x,p)+closest(y,q))

def maximize(p,q):
    xs=sorted(set((-p,F(0),1-p,F(1))))
    ys=sorted(set((-q,F(0),1-q,F(1))))
    best=F(-100)
    for xl,xr in zip(xs,xs[1:]):
      for yl,yr in zip(ys,ys[1:]):
        corners=[(xl,yl),(xl,yr),(xr,yl),(xr,yr)]
        pts=list(corners)
        def diff(x,y):
          return closest(x,p)+gauge(y,q)-gauge(x,p)-closest(y,q)
        for a,b in [(corners[0],corners[1]),(corners[0],corners[2]),(corners[1],corners[3]),(corners[2],corners[3])]:
          da,db=diff(*a),diff(*b)
          if da*db<0:
            t=da/(da-db)
            pts.append((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])))
        best=max(best,*(score(x,y,p,q) for x,y in pts))
    return best

if __name__=='__main__':
    rs=[F(1),F(1,2),F(1,3),F(1,5),F(2,3),F(3,4)]
    count=0
    for p,q in product(rs,repeat=2):
      target=1+(1-p*q)/(1+max(p,q))
      observed=maximize(p,q)
      assert observed==target,(p,q,observed,target)
      count+=1
    print(f'PASS: {count} affine-shape pairs checked using exact rational polyhedral subdivision.')
