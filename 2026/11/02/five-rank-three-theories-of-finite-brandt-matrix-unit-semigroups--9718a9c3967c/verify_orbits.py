from functools import lru_cache
from itertools import product
ZERO=(-1,-1)

def norm(xs):
 d={};out=[]
 for v in xs:
  if v==ZERO:out.append(ZERO);continue
  a=[]
  for z in v:
   if z not in d:d[z]=len(d)
   a.append(d[z])
  out.append(tuple(a))
 return tuple(out)

def mult(a,b):
 if a==ZERO or b==ZERO:return ZERO
 return (a[0],b[1]) if a[1]==b[0] else ZERO

@lru_cache(None)
def atoms(x):
 xs=(ZERO,)+x
 return (tuple(a==b for a,b in product(xs,repeat=2)),tuple(mult(a,b)==c for a,b,c in product(xs,repeat=3)))

def extensions(x,n):
 used=1+max([z for p in x if p!=ZERO for z in p],default=-1)
 indices=range(min(n,used+2))
 return {norm(x+(v,)) for v in [ZERO]+list(product(indices,repeat=2))}

intern={};counts={}
def intern_type(sig):
 if sig not in intern:intern[sig]=len(intern)
 return intern[sig]

def root(n,r):
 @lru_cache(None)
 def ty(x,t):
  if t==0:return intern_type(('a',atoms(x)))
  ex=tuple(sorted({ty(y,t-1) for y in extensions(x,n)}))
  return intern_type(('e',ex))
 root_type=ty((),r)
 return root_type,ty.cache_info().currsize
if __name__=='__main__':
 for r in [1,2,3,4]:
  print('r',r,flush=True);last=None
  for n in range(1,15):
   ans,states=root(n,r)
   print(n,'type',ans,'states',states,'eq prev',ans==last,flush=True)
   last=ans
