import json
j=json.load(open('hyperflex_flags.json'));M=[tuple(m) for m in j['monomials']];idx={m:i for i,m in enumerate(M)}
G=[[[0,1,0],[1,0,0],[0,0,1]],[[1,0,0],[0,0,1],[0,1,0]],[[1,1,0],[0,1,0],[0,0,1]],[[2,0,0],[0,1,0],[0,0,1]]]

def mul(p,line):
 q={}
 for m,c in p.items():
  for i,a in enumerate(line):
   if a:
    n=tuple(m[k]+(i==k) for k in range(3));q[n]=(q.get(n,0)+c*a)%3
 return q
T=[]
for g in G:
 cols=[]
 for m in M:
  p={(0,0,0):1}
  for i,k in enumerate(m):
   for _ in range(k):p=mul(p,g[i])
  cols.append([p.get(k,0) for k in M])
 T.append(cols)
open('hyperflex_actions.json','w').write(json.dumps(T))
