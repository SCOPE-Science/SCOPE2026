"""p-rank and point counts on bidegree (2,3) genus-two forms over F2.
GF4 encoding 0,1,z,z+1 with z^2=z+1.
"""
from bideg23 import nsm,mons,smooth,count
from collections import Counter,defaultdict
mul=[[0]*4 for _ in range(4)]
for a in range(4):
 for b in range(4):
  p=0
  for i in range(2):
   for j in range(2):
    if (a>>i)&1 and (b>>j)&1:p ^= (1<<(i+j))
  if p&8:p^=0b1100
  if p&4:p^=0b111
  mul[a][b]=p
assert mul[2][2]==3

def powf(a,e):
 p=1
 for _ in range(e):p=mul[p][a]
 return p

def val(k,x,y):
 a,b=x; c,d=y
 z=0
 for n,(i,j) in enumerate(mons):
  if (k>>n)&1:
   m=mul[powf(a,2-i)][powf(b,i)]
   m=mul[m][powf(c,3-j)]
   m=mul[m][powf(d,j)]
   z ^= m
 return z
P=[(1,t) for t in range(4)]+[(0,1)]

def n2(k):return sum(val(k,x,y)==0 for x in P for y in P)

d=Counter(); pr=Counter(); sigs=defaultdict(list);details=[]
for mask,w,n1 in nsm:
 m=n2(mask);assert (m-5+(n1-3)**2)%2==0
 a1=n1-3;a2=(m-5+a1*a1)//2
 rank=2 if a2%2 else 1 if a1%2 else 0
 d[(n1,rank)]+=w;pr[rank]+=w
 sigs[(n1,m,rank)].append((mask,w));details.append((mask,w,n1,m,a1,a2,rank))
print('prank totals',dict(sorted(pr.items())))
print('joint table',dict(sorted(d.items())))
print('signatures',len(sigs), 'individual',dict(sorted(sigs.items())))
print('DETAILS',details)
