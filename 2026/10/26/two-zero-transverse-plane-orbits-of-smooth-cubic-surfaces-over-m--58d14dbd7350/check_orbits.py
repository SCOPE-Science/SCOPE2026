from collections import deque
m=[]
for a in range(4):
 for b in range(4-a):
  for c in range(4-a-b):m.append((a,b,c,3-a-b-c))
assert len(m)==20
mon_index={tuple(v):i for i,v in enumerate(m)}
def mult(p,q):
 r={}
 for u,a in p.items():
  for v,b in q.items():
   w=tuple(u[i]+v[i] for i in range(4))
   r[w]=r.get(w,0)^(a&b)
 return {k:v for k,v in r.items() if v}
def substitution(i,j,kind):
 # x_i -> x_i+x_j (shear), or x_i <-> x_j (swap)
 subs=[]
 for k in range(4):
  if kind=='shear' and k==i:
   subs.append({tuple(1 if s==i else 0 for s in range(4)):1,tuple(1 if s==j else 0 for s in range(4)):1})
  else:
   t=(j if k==i else i) if kind=='swap' and k in (i,j) else k
   subs.append({tuple(1 if s==t else 0 for s in range(4)):1})
 lookup=[]
 for e in m:
  p={(0,0,0,0):1}
  for k,ek in enumerate(e):
   for _ in range(ek):p=mult(p,subs[k])
  code=0
  for a in p:code^=1<<mon_index[a]
  lookup.append(code)
 return lookup
Ts=[substitution(i,j,'shear') for i in range(4) for j in range(4) if i!=j]+[substitution(i,i+1,'swap') for i in range(3)]
def move(a,T):
 v=0
 while a:
  t=a&-a; v^=T[t.bit_length()-1];a-=t
 return v
zero={int(x) for x in open('zero_cubics.txt')};print('total zero',len(zero));print('Fermat in zeros',524809 in zero)
orbs=[]
while zero:
 x=min(zero);S={x};Q=deque([x]);
 while Q:
  a=Q.popleft()
  for t in Ts:
   b=move(a,t)
   if b not in S:S.add(b);Q.append(b)
 assert S<=zero,(len(S),len(S-zero))
 zero-=S
 orbs.append((len(S),min(S),S))
 print('orbit',len(S),'rep',min(S),'example',x,'Fermat?',524809 in S)
print('orbit sizes',[x[0] for x in orbs]);print('Fermat orbit?',[x[0] for x in orbs if 524809 in x[2]])
for cnt,rep,S in orbs:
 print('representative',rep,'terms', [''.join('xyzw'[i]*(e[i]) for i in range(4)) for k,e in enumerate(m) if rep>>k&1])
