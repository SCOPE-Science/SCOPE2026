from itertools import product

def gfops(q):
 if q in (2,3,5,7,11):
  return (lambda a,b:(a+b)%q),(lambda a,b:(a*b)%q)
 if q==4:
  # bit polynomial basis GF2[t]/(t^2+t+1)
  def mul(a,b):
   z=0
   while b:
    if b&1: z^=a
    b>>=1; a<<=1
    if a&4: a^=7
   return z
  return (lambda a,b:a^b),mul
 raise ValueError(q)

def plane(q):
 add,mul=gfops(q)
 vecs=list(product(range(q),repeat=3))
 def firstnonzero_norm(v):
  for c in v:
   if c:
    inv=next(t for t in range(1,q) if mul(c,t)==1)
    return tuple(mul(t,inv) for t in v)
 points=sorted({firstnonzero_norm(v) for v in vecs if any(v)})
 n=len(points)
 inc=[]
 for p in points:
  inc.append(tuple((add(add(mul(p[0],l[0]),mul(p[1],l[1])),mul(p[2],l[2]))==0) for l in points))
 return n,inc

def sigbuilder(q):
 n,inc=plane(q)
 N=2*n
 def incobj(x,y):
  if x<n and y>=n:return inc[x][y-n]
  if y<n and x>=n:return inc[y][x-n]
  return False
 def concurrency(x,y,z):
  if x<n and y<n and z<n:
   if len({x,y,z})<3:return 0
   return int(any(inc[x][l] and inc[y][l] and inc[z][l] for l in range(n)))
  if x>=n and y>=n and z>=n:
   if len({x,y,z})<3:return 0
   return int(any(inc[p][x-n] and inc[p][y-n] and inc[p][z-n] for p in range(n)))
  return 0
 def signature(v):
  k=len(v)
  out=[tuple(x<n for x in v),tuple(v[i]==v[j] for i in range(k) for j in range(i+1,k)),tuple(int(incobj(v[i],v[j])) for i in range(k) for j in range(i+1,k)),tuple(concurrency(v[i],v[j],v[l]) for i in range(k) for j in range(i+1,k) for l in range(j+1,k))]
  return tuple(out)
 return N,signature

def do(q,alltr=False):
 N,signature=sigbuilder(q)
 rep={};support={}; disagreement=[]
 # for every triple up to N^3
 for a in range(N):
  for b in range(N):
   for c in range(N):
    t=(a,b,c)
    s=signature(t)
    if s in support and not alltr: continue
    ext={signature(t+(x,)) for x in range(N)}
    if s in support and ext!=support[s]:
     disagreement.append((s,t,rep[s],len(ext),len(support[s])))
     return support,disagreement
    else:
     rep[s]=t; support[s]=ext
 print('q',q,'N',N,'three_types',len(support),'extension_patterns',sum(map(len,support.values())),'consistency_failures',len(disagreement),flush=True)
 return support,disagreement

if __name__=='__main__':
 res={}
 for q in [2,3,4,5,7]:
  s,b=do(q,alltr=(q<=4))
  res[q]=s
  if b:print('BAD',b);break
 for a,b in zip(list(res),list(res)[1:]):
  d=[(k, len(res[a].get(k,set())-res[b].get(k,set())),len(res[b].get(k,set())-res[a].get(k,set()))) for k in set(res[a])|set(res[b]) if res[a].get(k,set())!=res[b].get(k,set())]
  print('comparison',a,b,'different_three_types',len(d),'lost_extension_patterns',sum(x[1] for x in d),'gained_extension_patterns',sum(x[2] for x in d),flush=True)

