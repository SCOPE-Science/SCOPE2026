import random
from functools import lru_cache
W=range(4)
Val={'p':1<<2,'q':1<<3,'r':0}
F=[frozenset([1,14]),frozenset([1,5,14])]
def sub(s):
 return (t for t in range(16) if t&s==t)
@lru_cache(maxsize=None)
def support(m,s,formula):
 op=formula[0]
 if op=='atom':return (s & ~Val[formula[1]])==0
 if op=='bot':return s==0
 if op=='and':return support(m,s,formula[1]) and support(m,s,formula[2])
 if op=='inq':return support(m,s,formula[1]) or support(m,s,formula[2])
 if op=='imp':return all(not support(m,t,formula[1]) or support(m,t,formula[2]) for t in sub(s))
 if op in ('E','A'):
  def at(w):
   cond=[support(m,t,formula[1]) for t in F[m]]
   return any(cond) if op=='E' else all(cond)
  return all(at(w) for w in W if (1<<w)&s)
 assert False,formula
rnd=random.Random(1134)
def form(depth):
 if depth==0:return rnd.choice([('atom','p'),('atom','q'),('atom','r'),('bot',)])
 op=rnd.choice(['atom','bot','and','inq','imp','E','A'])
 if op=='atom': return ('atom',rnd.choice(list(Val)))
 if op=='bot':return ('bot',)
 if op in ('E','A'):return(op,form(depth-1))
 return(op,form(depth-1),form(depth-1))
for k in range(2500):
 x=form(rnd.choice([1,2,3,4]))
 for s in range(16):
  assert support(0,s,x)==support(1,s,x),(k,s,x)
print('DIRECT_SEMANTICS_OK',2500,'formulas',40000,'paired state comparisons')
