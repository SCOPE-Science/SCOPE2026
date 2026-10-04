from collections import Counter,deque
E=((0,1),(0,2),(0,3),(0,4),(1,2),(2,3),(3,4),(4,1))
A=[]
for i,(u,v) in enumerate(E): A += [(u,v,i),(v,u,i)]
F=[]
def rec(s,C,T,U,S):
 F.append(tuple(C))
 for a in range(s,len(A)):
  u,v,e=A[a]
  if u in T or e in U: continue
  x=v; cyc=(x==u)
  while not cyc and x in S:
   x=S[x]; cyc=(x==u)
  if cyc: continue
  T.add(u);U.add(e);S[u]=v;C.append(a);rec(a+1,C,T,U,S);C.pop();del S[u];U.remove(e);T.remove(u)
rec(0,[],set(),set(),{})
M=[]
for f in F:
 m=0
 for a in f:m|=1<<a
 M.append(m)
assert len(M)==len(set(M))==576
fv=Counter(m.bit_count()-1 for m in M if m);assert fv==Counter({0:16,1:94,2:240,3:225})
O=(8,12,3,9,6,11,15,14,13,0,2,4,10,7,1,5)
U=set(M);U.remove(0);P={}
for v in O:
 for m in tuple(U):
  h=m|(1<<v)
  if not (m>>v)&1 and h in U:U.remove(m);U.remove(h);P[m]=h
assert len(P)==255 and Counter(m.bit_count()-1 for m in U)==Counter({3:64,0:1})
N=[m for m in M if m];adj={m:[] for m in N};rev={h:l for l,h in P.items()}
for h in N:
 b=h
 while b:
  z=b&-b;l=h^z;b^=z
  if l:
   (adj[l] if rev.get(h)==l else adj[h]).append(h if rev.get(h)==l else l)
ind={m:0 for m in N}
for x,vs in adj.items():
 for y in vs:ind[y]+=1
q=deque(x for x in N if ind[x]==0);n=0
while q:
 x=q.popleft();n+=1
 for y in adj[x]:
  ind[y]-=1
  if ind[y]==0:q.append(y)
assert n==575
print("VERIFY_OK")
