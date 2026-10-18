from collections import defaultdict,Counter
from itertools import combinations
D=defaultdict(list)
for line in open('canonical_dags.txt'):
 n,c=map(int,line.split());D[n].append(c)
def graph(n,c):
 ins=[[] for _ in range(n)];outs=[[] for _ in range(n)];k=0
 for i in range(n):
  for j in range(n):
   if i!=j:
    if c>>k&1:outs[i].append(j);ins[j].append(i)
    k+=1
 return ins,outs
for n,C in D.items():
 GG=[graph(n,c) for c in C];colors=[[0]*n for _ in C]
 for r in range(n+2):
  keys=[(colors[g][i],tuple(sorted(colors[g][j] for j in ins[i])),tuple(sorted(colors[g][j] for j in outs[i]))) for g,(ins,outs) in enumerate(GG) for i in range(n)]
  lut={key:v for v,key in enumerate(sorted(set(keys)))}
  new=[[lut[keys[g*n+i]] for i in range(n)] for g in range(len(C))]
  if new==colors:break
  colors=new
 assert new==colors, 'refinement did not stabilize'
 group=defaultdict(list)
 for c,row in zip(C,colors):group[tuple(sorted(row))].append(c)
 ambiguous=[v for v in group.values() if len(v)>1]
 print('n',n,'types',len(C),'C2classes',len(group),'ambiguities',len(ambiguous),'class sizes',Counter(map(len,ambiguous)),'rounds',r)
 for cls in sorted(ambiguous,key=len,reverse=True)[:4]:print('examples:',cls[:8])

assert [len(D[n]) for n in range(1,7)] == [1,2,6,31,302,5984]
assert len(group)==5983 and len(ambiguous)==1 and len(ambiguous[0])==2
print("VERIFIED")
