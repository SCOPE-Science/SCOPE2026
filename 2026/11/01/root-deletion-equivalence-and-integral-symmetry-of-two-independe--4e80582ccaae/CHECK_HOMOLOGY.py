from itertools import product

def complex_faces(q):
 m=len(q)
 total=1+m+sum(q)
 edges=[];j=1+m
 for i,k in enumerate(q):
  edges.append((0,i+1))
  for t in range(k):edges.append((i+1,j));j+=1
 faces=[[] for i in range(total+1)]
 for b in range(1<<total):
  adj=[[] for _ in range(total)]
  for a,c in edges:
   if b>>a&1 and b>>c&1:
    adj[a].append(c);adj[c].append(a)
  seen=set();valid=True
  for v in range(total):
   if b>>v&1 and v not in seen:
    st=[v];seen.add(v)
    for w in st:
     for z in adj[w]:
      if z not in seen:seen.add(z);st.append(z)
    if len(st)>2:valid=False;break
  if valid:faces[b.bit_count()].append(b)
 return faces

def rank_gf2(cols):
 piv={}
 for v in cols:
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 return len(piv)

def betti(q):
 fs=complex_faces(q)
 # boundaries C_k (face size k+1) to C_{k-1} (size k)
 rs=[]
 for k in range(len(fs)):
  if k==0:rs.append(0);continue
  face_idx={b:j for j,b in enumerate(fs[k-1])}
  columns=[]
  for b in fs[k]:
   x=0
   for v in range(b.bit_length()):
    if b>>v&1:
     x^=1<<face_idx[b^(1<<v)]
   columns.append(x)
  rs.append(rank_gf2(columns))
 bs={k-1:len(fs[k])-rs[k]-(rs[k+1] if k+1<len(rs) else 0) for k in range(1,len(fs))}
 bs={k:v for k,v in bs.items() if v}
 return [len(x) for x in fs],bs
for q in [(2,2),(2,3),(3,3),(2,2,2),(1,3,2),(1,1),(3,3,2)]:
 try:
  ff,b=betti(q)
  rank=__import__('math').prod(z-1 for z in q)
  assert b==({2*len(q)-1:rank} if rank else {}),(q,b,rank)
  print(q, 'mod-two reduced Betti ranks',b,'facecounts',ff)
 except Exception as e: print(type(e).__name__,e)
