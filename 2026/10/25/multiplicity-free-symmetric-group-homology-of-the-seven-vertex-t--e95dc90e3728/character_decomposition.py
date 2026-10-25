import itertools, math,functools,collections,re,ast
from pathlib import Path

def parts(n,m=None):
 if not n:yield ()
 else:
  for i in range(min(n,m if m is not None else n),0,-1):
   for tail in parts(n-i,i):yield(i,)+tail

def cells(p):return {(r,c) for r,length in enumerate(p) for c in range(length)}
def is_shape(C):
 if not C:return True
 for r,c in C:
  for j in range(c):
   if (r,j) not in C:return False
  if r and (r-1,c) not in C:return False
 return True

def is_rim(S):
 if not S:return False
 if any({(r,c),(r+1,c),(r,c+1),(r+1,c+1)}<=S for r,c in S):return False
 todo={next(iter(S))};seen=set()
 while todo:
  x=todo.pop();seen.add(x)
  r,c=x
  todo.update({(r+1,c),(r-1,c),(r,c+1),(r,c-1)}&S-seen)
 return len(seen)==len(S)

def shape_of(C):
 return tuple(len([1 for r,c in C if r==i]) for i in range(max((r for r,c in C),default=-1)+1))
@functools.lru_cache(None)
def chi(lam,mu):
 if not mu:return int(not lam)
 k=mu[0];C=cells(lam);val=0
 for combo in itertools.combinations(C,k):
  S=set(combo)
  if not is_rim(S) or not is_shape(C-S):continue
  new=shape_of(C-S)
  val+=(-1)**(len({r for r,c in S})-1)*chi(new,mu[1:])
 return val

ss=list(parts(7))
chars={lam:[chi(lam,mu) for mu in ss] for lam in ss}
classes={mu:math.factorial(7)//math.prod(j**v*math.factorial(v) for j,v in collections.Counter(mu).items()) for mu in ss}
for la in ss:
 for lb in ss:
  orth=sum(classes[mu]*a*b for mu,a,b in zip(ss,chars[la],chars[lb]))//5040
  assert orth==(1 if la==lb else 0),(la,lb,orth)
vals={}
for line in (Path(__file__).parent/'equivariant_output.txt').open():
 if line.startswith('CHARACTER'):
  match=re.match(r'CHARACTER (\([^)]*\)) (\{.*\})',line)
  p=ast.literal_eval(match.group(1));d=ast.literal_eval(match.group(2));vals[p]=d
assert len(vals)==15
for d in (5,7,8):
 decomp={lam:sum(classes[mu]*vals[mu][d]*c for mu,c in zip(ss,chars[lam]))//5040 for lam in ss}
 assert all(v>=0 for v in decomp.values()),decomp
 dimension=sum(v*chars[k][-1] for k,v in decomp.items())
 assert dimension=={5:7,7:55,8:1}[d]
 assert all(sum(decomp[la]*chars[la][j] for la in ss)==vals[mu][d] for j,mu in enumerate(ss))
 print('DECOMP',d,{str(k):v for k,v in decomp.items() if v},'DIM',dimension)
print('ALL_CHARACTERS',chars)
