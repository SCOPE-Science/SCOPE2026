from gq_constructor import make_quad,shortest_paths
from collections import Counter

def basis(q,x,y,k):
 pts,lines,nbr=make_quad(q);d=shortest_paths(nbr);n=len(nbr)
 memo={}
 def getseq(v,steps,left):
  key=(v,steps,left)
  if key in memo:return memo[key]
  if steps==0:return ((v,),) if left==0 and v==y else ()
  arr=[]
  for w in range(n):
   if w==v or d[v][w]>left:continue
   for nxt in getseq(w,steps-1,left-d[v][w]):arr.append((v,)+nxt)
  memo[key]=tuple(arr)
  return memo[key]
 return getseq(x,k,5),d

def boundary(high,low,d):
 idx={t:i for i,t in enumerate(low)}
 cols=[]
 for tup in high:
  bits=0
  for j in range(1,len(tup)-1):
   if d[tup[j-1]][tup[j+1]]==d[tup[j-1]][tup[j]]+d[tup[j]][tup[j+1]]:
    bits^=1<<idx[tup[:j]+tup[j+1:]]
  cols.append(bits)
 return cols

def rank(cols):
 piv={}
 for c in cols:
  while c:
   b=c.bit_length()-1
   if b in piv:c^=piv[b]
   else:piv[b]=c;break
 return len(piv)

pts,lines,nbr=make_quad(3);p=len(pts)
for dist in (1,3):
 x=0;y=next(j for j in range(p,len(nbr)) if shortest_paths(nbr)[x][j]==dist)
 sets={};ds=None
 for k in (2,3,4):
  a,ds=basis(3,x,y,k);sets[k]=a
 print('distance',dist,'counts',{k:len(v) for k,v in sets.items()},flush=True)
 b3=boundary(sets[3],sets[2],ds);b4=boundary(sets[4],sets[3],ds)
 # Verify the chain condition independently of Gaussian elimination.
 for column in b4:
  composition=0
  while column:
   bit=column&-column;idx=bit.bit_length()-1
   composition^=b3[idx];column^=bit
  assert composition==0
 r3=rank(b3);r4=rank(b4)
 print('distance',dist,'rank3',r3,'rank4',r4,'H3',len(sets[3])-r3-r4,flush=True)
# All classes are represented: symplectic transvections generate an explicit transitive subgroup on nonincident point-line pairs.
from collections import deque
pts,lines,nbr=make_quad(3);p=len(pts);index={x:i for i,x in enumerate(pts)};lineindex={frozenset(z):j for j,z in enumerate(lines)}
def omega(a,b):return (a[0]*b[2]-a[2]*b[0]+a[1]*b[3]-a[3]*b[1])%3
gens=[]
for v in pts:
 perm=[]
 for x in pts:
  a=omega(x,v);z=tuple((x[i]+a*v[i])%3 for i in range(4));r=next(w for w in z if w);z=tuple((a*pow(r,-1,3))%3 for a in z)
  perm.append(index[z])
 lp=[lineindex[frozenset(perm[i] for i in ln)] for ln in lines]
 gens.append((tuple(perm),tuple(lp)))
for flag in (False,True):
 start=next((i,j) for i in range(p) for j,ln in enumerate(lines) if (i in ln)==flag)
 todo=[start];seen={start}
 for i,j in todo:
  for gp,gl in gens:
   pair=(gp[i],gl[j]);
   if pair not in seen:seen.add(pair);todo.append(pair)
 target=sum((i in ln)==flag for i in range(p) for ln in lines)
 assert len(seen)==target,(flag,len(seen),target)
 print('symplectic point-line orbit', 'incident' if flag else 'nonincident',len(seen))
print('GQ33_MAGNITUDE_EXACT_MOD2_VERIFIED')
