from itertools import combinations

def calc(m,h):
 G=set(range(1,m))|set(range(2*m-h,2*m))
 S=(set(range(m,2*m-h))|{0})
 # every normalized I represented by mask of gaps
 reflex=[]; ideals=[]
 for mask in range(1<<len(G)):
  X={x for i,x in enumerate(sorted(G)) if mask>>i&1}
  I=S|X
  if any(a+b<2*m and a+b not in I for a in I for b in S):continue
  ideals.append(frozenset(I))
  H={z for z in S if all((z+x>=2*m or z+x in S) for x in I)}
  V={z for z in range(2*m) if all((z+x>=2*m or z+x in S) for x in H)}
  if I==V:reflex.append(frozenset(I))
 predicted={frozenset(S)}
 high=set(range(2*m-h,2*m))
 for t in range(1<<(m-1)):
  T={i+1 for i in range(m-1) if t>>i&1}
  word=[i not in T for i in range(1,m)]
  blocks=[];k=0
  while k<m-1:
   if word[k]:
    j=k
    while j<m-1 and word[j]:j+=1
    blocks.append(j-k); k=j
   else:k+=1
  if all(b>=h for b in blocks):predicted.add(frozenset(S|high|T))
 return len(ideals),len(reflex),len(predicted),set(reflex)==predicted
for m in range(2,9):
 for h in range(1,m):
  if m-1+h>13:continue
  a,b,c,d=calc(m,h)
  print(m,h,a,b,c,d)
  assert d
print('VERIFY_OK')
