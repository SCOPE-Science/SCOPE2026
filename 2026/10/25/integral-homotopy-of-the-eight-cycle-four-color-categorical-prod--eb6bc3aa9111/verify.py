import collections,time,sys
n=8;q=4;N=n*q
E=[];nbr=[0]*N
for i in range(n):
 for a in range(q):
  x=i*q+a
  for d in (-1,1):
   for b in range(q):
    if b!=a: nbr[x]|=1<<(((i+d)%n)*q+b)
faces=[0]
t=time.monotonic()
# independent faces recursively increasing
stack=[(0,(1<<N)-1)]
while stack:
 f,available=stack.pop()
 while available:
  z=available&-available;available-=z
  x=z.bit_length()-1;g=f|z
  faces.append(g)
  nxt=available & ~nbr[x]
  if nxt:stack.append((g,nxt))
print('generated faces',len(faces),'seconds',time.monotonic()-t,flush=True)
print('fvector', dict(sorted(collections.Counter(f.bit_count() for f in faces).items())),flush=True)
S=set(faces[1:]);match=[];t=time.monotonic()
for v in range(N):
 bit=1<<v
 pairs=[]
 for f in list(S):
  if f&bit: continue
  g=f|bit
  if g in S:pairs.append((f,g))
 for f,g in pairs:S.remove(f);S.remove(g)
 match+=pairs
 print(v,'remaining',len(S),'elapsed',time.monotonic()-t,flush=True)
crit=collections.Counter(f.bit_count()-1 for f in S)
print('critical',crit,flush=True)
from collections import deque
print('verifying acyclic',flush=True)
M={a:b for a,b in match}; RI={b:a for a,b in match}; face_set=set(faces[1:]); indegree={f:0 for f in face_set}; outgoing=collections.defaultdict(list); cover_count=0
for f in face_set:
 s=f
 while s:
  b=s&-s;s-=b
  lower=f^b
  if lower==0:continue
  if M.get(lower)==f:
   a,z=lower,f
  else:a,z=f,lower
  outgoing[a].append(z);indegree[z]+=1;cover_count+=1
queue=deque(f for f in face_set if indegree[f]==0); num=0
while queue:
 v=queue.popleft();num+=1
 for w in outgoing[v]:
  indegree[w]-=1
  if not indegree[w]:queue.append(w)
print('Kahn',num,len(face_set),'cover',cover_count,flush=True)
assert num==len(face_set)
critical=sorted(S, key=lambda f:(f.bit_count(),f)); print('critical faces', [hex(f) for f in critical],flush=True)
crit4=sorted(f for f in S if f.bit_count()==5)
crit5=sorted(f for f in S if f.bit_count()==6)
cache={}
def sign(g, deleted):
 return -1 if (g & (deleted-1)).bit_count()%2 else 1
# gradient projection of dimension-four face into critical 4-chain
def project4(f):
 if f in cache:return cache[f]
 if f in S:res={f:1}
 elif f in M:
  g=M[f];removed=g^f; coeff=-sign(g,removed)
  res=collections.defaultdict(int)
  bits=g
  while bits:
   b=bits&-bits;bits-=b
   if b==removed:continue
   for h,v in project4(g^b).items():res[h]+=coeff*sign(g,b)*v
  res={h:v for h,v in res.items() if v}
 else:res={}
 cache[f]=res;return res
B=[]
for c in crit5:
 r=collections.Counter();s=c
 while s:
  b=s&-s;s-=b
  for h,v in project4(c^b).items():r[h]+=sign(c,b)*v
 B.append([r[h] for h in crit4])
# Compare the full signed gradient-path boundary with the separately stored certificate.
import json
from pathlib import Path
cert=json.loads(Path(__file__).with_name('morse_boundary.json').read_text(encoding='utf-8'))
assert n==8 and q==4 and N==32
assert len(faces)==196227 and len(face_set)==196226
assert cover_count==1457216 and num==196226
assert len(match)==98087
assert collections.Counter(f.bit_count()-1 for f in S)=={0:1,4:24,5:27}
assert [hex(f) for f in sorted(S) if f.bit_count()==1]==cert['critical_0_faces']
assert [hex(f) for f in crit4]==cert['critical_4_faces']
assert [hex(f) for f in crit5]==cert['critical_5_faces']
assert B==cert['morse_boundary_5_to_4']

# Unimodular row and column operations diagonalize the integer Morse differential.
# At each step the pivot must be a unit (+1 or -1); there are no divisions.
A=[row[:] for row in B];rows=len(A);cols=len(A[0]);pivot=0
while pivot<min(rows,cols):
    choices=[(sum(v!=0 for v in A[i])+sum(A[t][j]!=0 for t in range(pivot,rows)),i,j)
             for i in range(pivot,rows) for j in range(pivot,cols) if abs(A[i][j])==1]
    if not choices:
        break
    _,i,j=min(choices)
    A[pivot],A[i]=A[i],A[pivot]
    for row in A:
        row[pivot],row[j]=row[j],row[pivot]
    if A[pivot][pivot]<0:
        A[pivot]=[-v for v in A[pivot]]
    for i in range(rows):
        if i!=pivot and A[i][pivot]:
            factor=A[i][pivot]
            A[i]=[x-factor*y for x,y in zip(A[i],A[pivot])]
    for j in range(cols):
        if j!=pivot and A[pivot][j]:
            factor=A[pivot][j]
            for row in A:
                row[j]-=factor*row[pivot]
    assert A[pivot][pivot]==1
    pivot+=1
assert pivot==21
assert all(A[i][j]==0 for i in range(pivot,rows) for j in range(pivot,cols))
assert cert['integral_smith_unit_count']==21
assert cert['integral_smith_zero_count']==3
# Reduced Euler characteristic = 24-27 = -3, and after 21 cancellations = 3-6.
assert sum((-1)**(f.bit_count()-1) for f in face_set)==-2
print('CERTIFICATE_C8_TENSOR_K4_MATCHING_ACYCLIC',num,cover_count)
print('CERTIFICATE_C8_TENSOR_K4_SMITH_21_UNIT_PIVOTS')
print('C8_TENSOR_K4_WEDGE_3S4_AND_6S5_VERIFIED')

