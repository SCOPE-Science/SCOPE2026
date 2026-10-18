from itertools import permutations
n=4; N=16; UN=-1
ord=sorted(range(N),key=lambda a:(-a.bit_count(),a))
SUBS=[[b for b in range(N) if (b&a)==b] for a in range(N)]
INT={(a,b):tuple(c for c in range(N) if (b&c)==b and (c&a)==c) for a in range(N) for b in SUBS[a]}
pres=[(0,1,2,3),(1,0,2,3),(1,0,3,2),(1,2,0,3),(1,2,3,0)]
def transform(p,a):return sum(1<<p[i] for i in range(n) if (a>>i)&1)
permmasks=[list(map(lambda a:transform(p,a),range(N))) for p in pres]
counts=[0]*5;pcounts=[0]*5;total=0;Ptot=0

def rec(f):
 global total,Ptot
 A=next((a for a in ord if f[a]==UN),None)
 if A is None:
  total+=1
  passed=all((f[a|b]& ~(f[a]|f[b]))==0 for a in range(N) for b in range(N))
  Ptot+=passed
  for i,mapping in enumerate(permmasks):
   if all(f[mapping[a]]==mapping[f[a]] for a in range(N)):
    counts[i]+=1
    pcounts[i]+=passed
  return
 for B in SUBS[A]:
  ints=INT[A,B]
  if all(f[C] in (UN,B) for C in ints):
   g=f.copy()
   for C in ints:g[C]=B
   rec(g)
rec([UN]*N)
print(total,Ptot,counts,pcounts)
assert (total,Ptot,counts,pcounts)==(336852,596,[336852,3312,484,141,20],[596,56,16,8,2])
