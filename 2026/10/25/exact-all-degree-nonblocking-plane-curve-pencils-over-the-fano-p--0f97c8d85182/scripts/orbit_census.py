# independent enumeration from all 1023 binary cubic forms and all pairs
from itertools import product,combinations
from collections import Counter
mon3=[(a,b,3-a-b) for a in range(4) for b in range(4-a)]
mon4=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
mon2=[(a,b,2-a-b) for a in range(3) for b in range(3-a)]
index4={v:i for i,v in enumerate(mon4)}
pts=[p for p in product(range(2),repeat=3) if any(p)]
lines=[frozenset(i for i,p in enumerate(pts) if sum(u*v for u,v in zip(p,l))%2==0) for l in pts]

def vector(f):
 return sum((1<<i) if sum(((f>>j)&1)*int(all((k==0 or x!=0) for k,x in zip(m,p))) for j,m in enumerate(mon3))%2 else 0 for i,p in enumerate(pts))

def nb(vec): return any(all((vec>>i)&1 for i in set(l)) for l in lines)

# Macaulay rank
partials=[]
for j in range(10):
 mono=mon3[j]
 par=[]
 for k in range(3):
  if mono[k]%2:
   ee=list(mono);ee[k]-=1
   par.append(tuple(ee))
  else:par.append(None)
 partials.append(par)

def geo_smooth(f):
 q=[set() for k in range(3)]
 for j in range(10):
  if (f>>j)&1:
   for k in range(3):
    ee=partials[j][k]
    if ee is not None:
     if ee in q[k]:q[k].remove(ee)
     else:q[k].add(ee)
 columns=[]
 for part in q:
  for m in mon2:
   v=0
   for v2 in part:
    v^=1<<index4[tuple(x+y for x,y in zip(m,v2))]
   columns.append(v)
 span={}
 for v in columns:
  while v:
   k=v.bit_length()-1
   if k in span:v^=span[k]
   else:span[k]=v;break
 return len(span)==15

E=[vector(f) for f in range(1024)]
NB={f for f in range(1,1024) if nb(E[f])}
print('nonblocking cubic equations',len(NB))
pencils={tuple(sorted((f,g,f^g))) for f in NB for g in NB if f<g and (f^g) in NB}
print('all-nonblocking cubic pencils',len(pencils))
print('image multiplicities',Counter(tuple(sorted(E[f] for f in p)) for p in pencils).most_common(5))
smooth=[geo_smooth(f) for f in range(1024)]
print('all smooth cubic equations',sum(smooth))
print('smooth member distribution',Counter(sum(smooth[f] for f in p) for p in pencils))
print('point profiles',Counter(tuple(sorted(7-E[f].bit_count() for f in p)) for p in pencils))
print('rational basepoints',Counter(7-(E[p[0]]|E[p[1]]|E[p[2]]).bit_count() for p in pencils))

# polynomial arithmetic (monomial coefficient subsets)
D0={(0,0,0):1}
def mul(A,B):
 C={}
 for a,ai in A.items():
  for b,bj in B.items():
   k=tuple(x+y for x,y in zip(a,b))
   C[k]=C.get(k,0)^(ai&bj)
 return {k:v for k,v in C.items() if v}

def pow_poly(a,n):
 out=D0
 for k in range(n):out=mul(out,a)
 return out
idx3={m:i for i,m in enumerate(mon3)}
def det3(M):
 return (M[0][0]*((M[1][1]*M[2][2])^(M[1][2]*M[2][1])) ^M[0][1]*((M[1][0]*M[2][2])^(M[1][2]*M[2][0])) ^M[0][2]*((M[1][0]*M[2][1])^(M[1][1]*M[2][0])))&1

def perm_form(M):
 lin=[]
 for i in range(3):lin.append({tuple(1 if k==j else 0 for k in range(3)):1 for j in range(3) if M[i][j]})
 v=[]
 for a,b,c in mon3:
  p=mul(mul(pow_poly(lin[0],a),pow_poly(lin[1],b)),pow_poly(lin[2],c))
  v.append(sum(1<<idx3[k] for k in p))
 return v

mats=[]
for s in range(512):
 M=[[(s>>(3*i+j))&1 for j in range(3)] for i in range(3)]
 if det3(M):mats.append(M)
assert len(mats)==168
maps=[perm_form(M) for M in mats]

def act(f,t):
 ans=0
 for j in range(10):
  if (f>>j)&1:ans^=t[j]
 return ans

def actpen(P,t):return tuple(sorted(act(f,t) for f in P))

allpen=set(pencils);orbits=[]
while allpen:
 rep=min(allpen)
 orbit={actpen(rep,t) for t in maps}
 assert orbit <= pencils,(len(orbit), len(orbit-pencils))
 allpen-=orbit
 orbits.append((rep,len(orbit),sum(smooth[f] for f in rep),tuple(sorted(7-E[f].bit_count() for f in rep))))
print('orbit count',len(orbits),'orbit size',Counter(x[1] for x in orbits))
print('joint orbit table',Counter((x[1],x[2],x[3]) for x in orbits))
print('orbits',orbits)

# Exact finite coverage and orbit consistency checks.
assert len(NB)==512 and len(pencils)==18368 and len(orbits)==112
assert Counter(z[1] for z in orbits)=={168:108,56:4}
assert Counter(sum(smooth[f] for f in p) for p in pencils)=={0:4816,1:9408,2:3360,3:784}
assert Counter(7-(E[p[0]]|E[p[1]]|E[p[2]]).bit_count() for p in pencils)=={0:9408,1:8960}
assert len(maps)==168 and sum(z[1] for z in orbits)==len(pencils)
