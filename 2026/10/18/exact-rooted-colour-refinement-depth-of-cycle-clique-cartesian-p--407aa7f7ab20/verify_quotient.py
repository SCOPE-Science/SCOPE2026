"""Independent orbit-quotient test using neighbour multiplicities, stdlib only."""
from collections import Counter

def refine(colors):
    signatures={}
    for a in colors:
        counts=Counter()
        for b,v in adjacency[a].items():
            if v:counts[colors[b]]+=v
        signatures[a]=(colors[a],tuple(sorted(counts.items())))
    labels={x:i for i,x in enumerate(sorted(set(signatures.values())))}
    return {a:labels[s] for a,s in signatures.items()}

pairs=0
states=0
for n in range(5,101):
 for m in range(2,11):
  d=n//2
  types=[(j,b) for j in range(d+1) for b in (0,1)]
  adjacency={}
  for j,b in types:
   row=Counter()
   for x in ((j-1)%n,(j+1)%n):row[(min(x,n-x),b)]+=1
   if b==0:row[(j,1)]+=m-1
   else:
    row[(j,0)]+=1
    row[(j,1)]+=m-2
   adjacency[(j,b)]=row
  color={a:int(a==(0,0)) for a in types}
  for t in range(2*(d+1)+2):
   if len(set(color.values()))==len(types):break
   color=refine(color)
  else:raise AssertionError((n,m,'not discrete'))
  assert t==d+int(n==5 and m==2),(n,m,t)
  pairs+=1
  states+=len(types)
print(f'QUOTIENT_PASS pairs={pairs} states={states} n=5..100 m=2..10')
