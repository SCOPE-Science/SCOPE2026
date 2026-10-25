"""Verify signed cellular traces of half-graph matching complexes.

Method A enumerates matchings and applies the graph reflection with exact
orientation signs. Method B uses an independent recursion on reversal-pair
blocks. All calculations use Python integers; the checks are finite examples,
not the proof of the all-parameter identities.
"""

from math import comb
from collections import defaultdict

def polyadd(x,y,mult=1):
 for k,v in y.items():x[k]=x.get(k,0)+mult*v
 return {k:v for k,v in x.items() if v}

def polyscale(x,m):return {k:v*m for k,v in x.items() if v*m}

def pmul(x,y):
 z={}
 for k,a in x.items():
  for j,b in y.items():z[k+j]=z.get(k+j,0)+a*b
 return {k:v for k,v in z.items() if v}

def gen(n):
 m=(n+1)//2
 E=[{0:1}]
 for j in range(1,m+1):
  r={}
  for t in range(1,j+1):
   w=(-1)**(t-1)
   f={2*t-1:w, 2*t-2: 2**(t-1)*w}
   polyadd(r,pmul(f,E[j-t]),comb(j-1,t-1))
  E.append(r)
 if n%2: return E[m]
 r={}
 for t in range(m+1): polyadd(r,pmul({2*t:(-1)**t},E[m-t]),comb(m,t))
 return r

def brute(n):
 B=[(i,j) for i in range(1,n+1) for j in range(i,n+1)]
 perm={v:B.index((n+1-j,n+1-i)) for v,(i,j) in enumerate(B)}
 P=defaultdict(int)
 def visit(k,rows,cols,chosen):
  img=[perm[v] for v in chosen]
  if set(img)==set(chosen):
   sgn=(-1)**sum(img[a]>img[b] for a in range(len(img)) for b in range(a+1,len(img)))
   P[len(chosen)]+=sgn
  for i in range(k,len(B)):
   a,b=B[i]
   if not (rows>>(a-1)&1 or cols>>(b-1)&1): visit(i+1,rows|1<<(a-1),cols|1<<(b-1),chosen+(i,))
 visit(0,0,0,())
 return dict(P)
if __name__=='__main__':
 for n in range(1,10):
  e=gen(n)
  b=brute(n)
  assert e==b,(n,e,b)
  print(n, sum(b.values()),sum(v*(-1)**j for j,v in b.items()),e,flush=True)
 print('HALFGRAPH_REFLECTION_GRADED_TRACE_VERIFIED n=1..9')
