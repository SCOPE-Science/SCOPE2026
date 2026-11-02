V=[(1,0),(0,1),(1,1),(1,-1),(1,2),(2,1)]
from math import gcd
from fractions import Fraction as F
w=(2,2,2,1,1,1)
def check(n,verbose=True):
  lines=[(a,b,t) for (a,b),m in zip(V,w) for t in range(-m*n,m*n+1)]
  d=len(lines); pts={}
  for i,(a,b,t) in enumerate(lines):
   for j in range(i+1,d):
    c,e,s=lines[j];det=a*e-b*c
    if not det:continue
    x=t*e-b*s;y=a*s-c*t
    g=gcd(gcd(abs(x),abs(y)),abs(det));x//=g;y//=g;z=det//g
    if z<0:x=-x;y=-y;z=-z
    key=(x,y,z);pts[key]=pts.get(key,0)|(1<<i)|(1<<j)
  hist={}
  for mask in pts.values():
   r=mask.bit_count();hist[r]=hist.get(r,0)+1
  N=sum((3*r-4)*c for r,c in hist.items());D=sum((r-1)*c for r,c in hist.items());
  C1=N-2*d-15;C2=D-d-3
  if verbose:print('n',n,'d',d,'hist',hist,'N',N,'D',D,'c1',C1,'c2',C2,'ratio',C1/C2)
  return C1,C2

if __name__ == '__main__':
    from math import comb
    for n in (6,12):
        nlines=18*n+6
        got=check(n,True)
        assert got == (197*n*n+95*n-13,81*n*n+36*n-4)
        expected={2:23*n*n+17*n,3:14*n*n+8*n,4:7*n*n+4*n,5:n*n+n,6:n*n+n+1}
        all_pairs=sum(comb(r,2)*num for r,num in expected.items())+3*comb(4*n+1,2)+3*comb(2*n+1,2)
        assert all_pairs==comb(nlines,2)
    print('INDEPENDENT_PROJECTIVE_INCIDENCE_OK')
