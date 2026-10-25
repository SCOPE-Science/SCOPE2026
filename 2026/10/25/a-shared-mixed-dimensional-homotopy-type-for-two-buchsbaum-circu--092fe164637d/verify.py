"""Reproduce the finite homotopy certificates using the Python standard library."""
from collections import Counter,deque

CASES=[((1,2,3,8),(5,7,2,12,9,1,4,11,13,3,6,14,8,10,15,0)),((1,4,7,8),(2,3,11,10,8,1,5,4,7,15,9,12,6,13,14,0))]

def compute_faces(steps):
 adj=[0]*16
 for i in range(16):
  for s in steps:
   adj[i]|=1<<((i+s)%16)
   adj[i]|=1<<((i-s)%16)
 valid=bytearray(65536);valid[0]=1
 faces=[[],[],[]]
 for m in range(1,65536):
  lo=m&-m;v=lo.bit_length()-1
  if valid[m^lo] and not adj[v]&(m^lo):
   valid[m]=1;faces[m.bit_count()-1].append(m)
 return adj,faces

def check(steps,order):
 adj,face_groups=compute_faces(steps)
 assert list(map(len,face_groups))==[16,64,64]
 base=set().union(*map(set,face_groups));unmatched=set(base);pairs=[]
 for v in order:
  bit=1<<v
  for lo in sorted(unmatched):
   hi=lo|bit
   if lo&bit==0 and hi in unmatched:
    unmatched.remove(lo);unmatched.remove(hi);pairs.append((lo,hi))
 assert len(pairs)==63 and Counter(m.bit_count()-1 for m in unmatched)==Counter({0:1,1:1,2:16})
 partner={}
 for lo,hi in pairs:
  assert lo in base and hi in base and (hi^lo).bit_count()==1 and (lo&hi)==lo
  assert lo not in partner and hi not in partner
  partner[lo]=hi;partner[hi]=lo
 assert base==set(partner)|unmatched
 outgoing={m:[] for m in base};indeg={m:0 for m in base};edges=0
 for hi in base:
  x=hi
  while x:
   b=x&-x;x-=b;lo=hi^b
   if lo not in base:continue
   a,c=(lo,hi) if partner.get(lo)==hi else (hi,lo)
   outgoing[a].append(c);indeg[c]+=1;edges+=1
 assert edges==320
 queue=deque(m for m in base if indeg[m]==0);seen=0
 while queue:
  m=queue.popleft();seen+=1
  for n in outgoing[m]:
   indeg[n]-=1
   if indeg[n]==0:queue.append(n)
 assert seen==144
 # Show the graphs are not isomorphic: edge common-neighbor counts differ.
 histogram=Counter((adj[i]&adj[j]).bit_count() for i in range(16) for j in range(i+1,16) if adj[i]>>j&1)
 # A connected one-skeleton has 15 tree edges; quotient C1 has 49 generators.
 edges1=sorted(tuple(j for j in range(16) if m>>j&1) for m in face_groups[1]);known={0};tree=[]
 while len(known)<16:
  candidates=[e for e in edges1 if (e[0]in known) != (e[1]in known)]
  e=min(candidates);tree.append(e);known.update(e)
 chords=[e for e in edges1 if e not in tree];position={e:i for i,e in enumerate(chords)}
 assert len(chords)==49
 # Signed triangle boundary in C1 modulo the spanning tree.
 M=[[0]*64 for _ in range(49)]
 for j,m in enumerate(face_groups[2]):
  a,b,c=(i for i in range(16) if m>>i&1)
  for e,coef in (((a,b),1),((a,c),-1),((b,c),1)):
   if e in position:M[position[e]][j]=coef
 # Integer elimination by exactly unimodular row/column operations.
 rows,cols=len(M),len(M[0]);k=0
 while k<min(rows,cols):
  candidates=[(sum(1 for v in M[i][k:] if v),sum(1 for i2 in range(k,rows) if M[i2][j]),i,j)
              for i in range(k,rows) for j in range(k,cols) if abs(M[i][j])==1]
  if not candidates:break
  _,_,ri,cj=min(candidates)
  M[k],M[ri]=M[ri],M[k]
  for row in M:row[k],row[cj]=row[cj],row[k]
  if M[k][k]==-1:M[k]=[-x for x in M[k]]
  for i in range(rows):
   if i!=k and M[i][k]:
    coeff=M[i][k];M[i]=[x-coeff*y for x,y in zip(M[i],M[k])]
  for j in range(cols):
   if j!=k and M[k][j]:
    coeff=M[k][j]
    for i in range(rows):M[i][j]-=coeff*M[i][k]
  assert M[k][k]==1 and all(M[i][k]==0 for i in range(rows) if i!=k)
  assert all(M[k][j]==0 for j in range(cols) if j!=k)
  k+=1
 assert k==48 and all(M[i][j]==0 for i in range(k,rows) for j in range(k,cols)),(k,Counter(x for row in M for x in row if x))
 # H1=Z follows from a 49-by-64 relation matrix with Smith normal form (1^48,0).
 # Critical Morse 1-skeleton has one vertex and one edge. Since H1 has rank 1,
 # its sixteen critical 2-cells have attaching maps S1->S1 of degree zero,
 # hence nullhomotopic. The Morse CW type is S1 wedge 16 S2.
 print('STEPS',steps,'FACE_VECTOR',(16,64,64),'MATCHED_PAIRS',63,'CRITICAL',(1,1,16),'HASSE',edges,
       'UNIMODULAR_SMITH_PIVOTS',k,'EDGE_TRIANGLE_COUNTS',sorted(histogram.items()),'VERIFY_OK')
 return histogram

if __name__=='__main__':
 h1,h2=(check(*case) for case in CASES)
 assert h1!=h2,'The base circulants must be distinguished by an invariant.'
 print('BOTH_GRAPHS_NONISOMORPHIC_AND_HOMOTOPY_EQUIVALENT_OK')
