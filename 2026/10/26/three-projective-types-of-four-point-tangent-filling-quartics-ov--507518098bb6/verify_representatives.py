"""Independent finite-field verification of three extremal quartic representatives."""
from itertools import product
MON = [(i,j,4-i-j) for i in range(5) for j in range(5-i)]
REPS = [
 (0,1,0,2,0,0,0,0,0,0,0,0,0,0,1),
 (0,1,0,2,0,0,0,0,0,0,0,1,0,0,1),
 (0,1,0,2,0,0,0,0,0,0,0,1,0,1,2),
]
POINTS = [p for p in product(range(3), repeat=3) if any(p) and next(t for t in p if t)==1]
assert len(POINTS)==13

def normalize(v):
 k=next(t for t in v if t)
 return tuple(t*(1 if k==1 else 2)%3 for t in v)

def f(v,p):
 return sum(co*pow(p[0],i)*pow(p[1],j)*pow(p[2],k) for co,(i,j,k) in zip(v,MON))%3

def grad(v,p):
 return tuple(sum(co*e[t]*pow(p[0],e[0]-int(t==0))*pow(p[1],e[1]-int(t==1))*pow(p[2],e[2]-int(t==2))
 for co,e in zip(v,MON) if e[t])%3 for t in range(3))

def collinear(points):
 return [line for line in POINTS if all(sum(a*b for a,b in zip(line,p))%3==0 for p in points)]

for i,v in enumerate(REPS,1):
 q=[p for p in POINTS if f(v,p)==0]
 assert len(q)==4 and len(collinear(q))==1
 lines=[]
 for p in q:
  g=grad(v,p)
  assert any(g)
  lines.append(normalize(g))
 assert len(set(lines))==4
 assert all(any(sum(x*y for x,y in zip(l,p))%3==0 for l in lines) for p in POINTS)
 assert all(l[0]==0 for l in lines)
 assert (1,0,0) not in q
 print('representative',i,'rational points',q,'tangent lines',lines,'point line',collinear(q))
print('THREE REPRESENTATIVES VERIFIED')
