exec(open('verify_quadratic.py').read().split("print('orbit'")[0])
from collections import Counter,defaultdict
from itertools import combinations
N=15
mons=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
assert len(mons)==15
pow8=[[1]*5 for _ in range(8)]
for x in range(8):
 for i in range(1,5):pow8[x][i]=mul[pow8[x][i-1]][x]
def point_eval(P,mon):
 t=1
 for x,k in zip(P,mon):t=mult(t,pow8[x][k])
 return t
def f_eval(P,coefs):
 out=0
 for k,v in enumerate(mons):
  if coefs>>k&1:out^=point_eval(P,v)
 return out
# all 73 P2(F8) points: normalize first nonzero coordinate
allp={normal((x,y,z)) for x in range(8) for y in range(8) for z in range(8) if x or y or z}
assert len(allp)==73
def frob(P):return tuple(mul[x][x] for x in P)
orb=[];seen=set()
for p in sorted(allp):
 if p in seen:continue
 o=[];q=p
 while q not in o:o.append(q);seen.add(q);q=frob(q)
 if len(o)==3:orb.append(tuple(o))
assert len(orb)==22

def detmat(A):return invmat([list(p) for p in A]) is not None
Blist=[o for o in orb if detmat(o)]
print('orbits',len(orb),len(Blist))

def getrows(P,deriv=False):
 vals=[]
 for m in mons:
  if deriv:
   if (m[deriv-1]&1)==0:vals.append(0)
   else:
    mm=list(m);mm[deriv-1]-=1;vals.append(point_eval(P,mm))
  else:vals.append(point_eval(P,m))
 return [sum(((v>>bit)&1)<<i for i,v in enumerate(vals)) for bit in range(3)]

def ker(rows,n=15):
 rows=rows[:];piv=[];rr=0
 for j in range(n):
  t=next((i for i in range(rr,len(rows)) if rows[i]>>j&1),None)
  if t is None:continue
  rows[rr],rows[t]=rows[t],rows[rr]
  for k in range(len(rows)):
   if k!=rr and rows[k]>>j&1:rows[k]^=rows[rr]
  piv.append(j);rr+=1
  if rr==len(rows):break
 free=[j for j in range(n) if j not in piv]
 basis=[]
 for j in free:
  v=1<<j
  for i,p in enumerate(piv):
   if rows[i]>>j&1:v|=1<<p
  basis.append(v)
 return basis

def eval_binary(v,P):return f_eval(P,v)
import itertools
info=[];examples=defaultdict(list);count=Counter();dupes=set()
for B in Blist:
 b=B[0]; j=next(i for i in range(3) if b[i]);
 rows=getrows(b)+sum((getrows(b,i+1) for i in range(3) if i!=j),[])
 for C in orb:
  if C==B:continue
  cc=C[0];bas=ker(rows+getrows(cc))
  count['pairs']+=1
  count['dimensions '+str(len(bas))]+=1
  if len(bas)!=3:continue
  mappts=[];ok=True
  for p in pts:
   v=tuple(eval_binary(f,p) for f in bas)
   if v==(0,0,0):ok=False;break
   mappts.append(idx[v])
  if not ok or len(set(mappts))<7:
   count['not bijective']+=1;continue
  p=tuple(mappts)
  count['bijective']+=1
  typ=cyc(p);count[typ]+=1
  if p not in dupes:dupes.add(p);count['distinct base normalized']+=1
  examples[typ].append((B,C,bas,p))
print('stats',count)
for t,ex in sorted(examples.items()):
 B,C,bas,p=ex[0]
 print('type',t,'ex',len(ex),'B',B,'C',C,'coeffs',bas,'permutation',p)
trans=[tuple(j if k==i else i if k==j else k for k in range(7)) for i in range(7) for j in range(i+1,7)]
print('transposition achieved', sum(any(compose(g,p) in trans for g in G) for arr in examples.values() for _,_,_,p in arr))
for arr in examples.values():
 for B,C,bas,p in arr:
  for g in G:
   q=compose(g,p)
   if q in trans:
    print('TRANS', 'B',B,'C',C,'basis',bas,'g',g,'p',p,'q',q)
    quit()
assert count['pairs']==168 and count['dimensions 3']==168 and count['bijective']==112
assert all(sum(1 for i in range(7) for j in range(i+1,7) if p[i]>p[j])%2==0 for arr in examples.values() for _,_,_,p in arr)
print('quartic_proper_certificate PASS; 168 systems; 112 rational permutations, all even')
