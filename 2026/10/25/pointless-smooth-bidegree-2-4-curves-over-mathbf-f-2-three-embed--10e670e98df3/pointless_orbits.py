"""Enumerate smooth pointless genus-3 (2,4) curves and factorwise PGL2(F2) orbits."""
from count_genus3 import smooth,rational_points,distinct_geometric_roots
from collections import Counter
import json

def matrices():
  return [(a,b,c,d) for a in range(2) for b in range(2) for c in range(2) for d in range(2) if (a*d^b*c)]
G=matrices(); assert len(G)==6
# evaluate polynomial substitution via exact monomial representation GF2
# Basis for first factor quadratic: s^0*t^2, s*t, s^2.
# Basis for second quartic: u^0*v^4, u*v^3,..., u^4.
# individual variables S,T,U,V represented as expanded term coefficients over GF2

def prod(f,g):
   out={}
   for (i,j),c in f.items():
    for (k,l),v in g.items():
     key=(i+k,j+l);out[key]=out.get(key,0)^(c&v)
   return {k:v for k,v in out.items() if v}

def pwr(f,k):
   ans={(0,0):1}
   for _ in range(k):ans=prod(ans,f)
   return ans

def btransform(q,deg,m):
   a,b,c,d=m
   L={(1,0):a,(0,1):b};M={(1,0):c,(0,1):d}
   ans={}
   for i in range(deg+1):
    if q>>i&1:
     for k,v in prod(pwr(L,i),pwr(M,deg-i)).items():
      ans[k]=ans.get(k,0)^v
   return sum(v<<k[0] for k,v in ans.items())

def transform(code,m1,m2):
    a,b,c=[code>>(5*i)&31 for i in range(3)]
    # base second factor quartics, new coefficient polynomials
    vals=[btransform(f,4,m2) for f in [c,b,a]]  # coefficient for s²,st,t²
    # apply first factor substitution: s -> a s+b t, t -> c s+d t
    m=m1
    aa,bb,cc,dd=m
    # each original monomial coefficient: s²,st,t²
    result=[0,0,0]
    # s² -> aa*s² + bb*t²
    if aa:result[2]^=vals[0]
    if bb:result[0]^=vals[0]
    # st -> aa cc s² +(aa dd + bb cc) st + bb dd t²
    if aa&cc:result[2]^=vals[1]
    if aa&dd^bb&cc:result[1]^=vals[1]
    if bb&dd:result[0]^=vals[1]
    # t² -> cc s²+dd t²
    if cc:result[2]^=vals[2]
    if dd:result[0]^=vals[2]
    return result[0] |result[1]<<5|result[2]<<10

def main():
  P={a|b<<5|c<<10 for a in range(32) for b in range(1,32) for c in range(32) if smooth(a,b,c) and rational_points(a,b,c)==0}
  assert len(P)==33
  orbits=[]
  while P:
    v=min(P); o={transform(v,m1,m2) for m1 in G for m2 in G}
    assert o<=P
    orbits.append((v,len(o),distinct_geometric_roots(v>>5&31)-1))
    P-=o
  print(json.dumps({'count':sum(x[1] for x in orbits),'orbits':[{'bits':x[0], 'size':x[1],'p_rank':x[2]} for x in sorted(orbits)],'group_order':36},indent=2))
if __name__=='__main__':main()
