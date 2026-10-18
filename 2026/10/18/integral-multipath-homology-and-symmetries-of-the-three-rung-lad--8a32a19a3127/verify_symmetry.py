from verify_morse import ARCS,ORDER,faces,match,bd,topo
from collections import Counter

F=faces(); pairs,crit=match(F)
D={f:bd(f) for f in F}
steps=[]
for s,t in pairs:
 c=D[t][s];assert abs(c)==1
 other={y:a for y,a in D[t].items() if y!=s}
 row={x:col[s] for x,col in D.items() if x not in (s,t) and s in col}
 steps.append((s,t,c,other,row))
 for x,a in row.items():
  for y,v in other.items():
   q=D[x].get(y,0)-a*v//c
   if q:D[x][y]=q
   else:D[x].pop(y,None)
  D[x].pop(s)
 del D[s];del D[t]
 for x in D:D[x].pop(t,None)
assert set(D)==crit and not any(D.values())

def project(z):
 z=z.copy()
 for s,t,c,other,row in steps:
  a=z.pop(s,0);z.pop(t,None)
  if a:
   for y,v in other.items():
    m=z.get(y,0)-a*v//c
    if m:z[y]=m
    else:z.pop(y,None)
 assert all(x in crit for x in z)
 return z

def lift(z):
 z=z.copy()
 for s,t,c,other,row in reversed(steps):
  a=-sum(z.get(x,0)*v for x,v in row.items())//c
  if a:z[t]=a
 return z

def boundary(z):
 out=Counter()
 for x,coeff in z.items():
  for y,v in bd(x).items():out[y]+=coeff*v
 return {x:v for x,v in out.items() if v}

for c in crit:
 vec=lift({c:1})
 assert not boundary(vec),(c,boundary(vec))
 assert project(vec)=={c:1}

id=list(range(6));row=[3,4,5,0,1,2];col=[2,1,0,5,4,3];both=[row[x] for x in col]
perms=[id,row,col,both];names=['identity','row_swap','column_reversal','half_turn']
Aindex={a:i for i,a in enumerate(ARCS)}

def action(p,z):
 out=Counter()
 for m,a in z.items():
  inds=[Aindex[(p[u],p[v])] for j,(u,v) in enumerate(ARCS) if m>>j&1]
  inversions=sum(inds[i]>inds[k] for i in range(len(inds)) for k in range(i+1,len(inds)))
  target=sum(1<<j for j in inds)
  out[target]+=a*(-1 if inversions%2 else 1)
 return {x:v for x,v in out.items() if v}

critby={d:sorted(x for x in crit if F[x]==d) for d in sorted(set(F[c] for c in crit))}
for name,p in zip(names,perms):
 traces={}
 for d,cs in critby.items():
  M=[]
  for c in cs:
   im=project(action(p,lift({c:1})))
   M.append([im.get(y,0) for y in cs])
  tr=sum(M[i][i] for i in range(len(cs)))
  traces[d]=tr
  # print matrix as columns
 print('action',name,'traces',traces,'reduced_lefschetz',sum((-1)**d*tr for d,tr in traces.items())-1)

for d in (2,3,4):
 print('degree',d,'four rational character multiplicities')
 # traces for each auto computed again
 trs=[]
 for p in perms:
  cs=critby[d]
  trs.append(sum(project(action(p,lift({c:1}))).get(c,0) for c in cs))
 for r in (0,1):
  for k in (0,1):
   mult=(trs[0]+(-1)**r*trs[1]+(-1)**k*trs[2]+(-1)**(r+k)*trs[3])//4
   assert 4*mult==(trs[0]+(-1)**r*trs[1]+(-1)**k*trs[2]+(-1)**(r+k)*trs[3])
   print((r,k,mult),end=' ')
 print()

def mat(g,d):
 cs=critby[d];p=perms[g]
 return [[project(action(p,lift({c:1}))).get(y,0) for y in cs] for c in cs]

def multiply(a,b):
 n=len(a)
 return [[sum(a[k][i]*b[j][k] for k in range(n)) for i in range(n)] for j in range(n)]

for d in (2,3,4):
 a,b,c=mat(1,d),mat(2,d),mat(3,d)
 identity=mat(0,d)
 assert multiply(a,a)==identity
 assert multiply(b,b)==identity
 assert multiply(a,b)==c==multiply(b,a)
 print('group_relations_verified',d,'dim',len(a))
