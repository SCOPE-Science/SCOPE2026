"""Independent finite EF-type recursion for sorted affine incidence structures."""
from itertools import product

def add(a,b,q):return a^b if q==4 else (a+b)%q

def mul(a,b,q):
 if q!=4:return (a*b)%q
 res=0
 while b:
  if b&1:res^=a
  b>>=1
  a<<=1
  if a&4:a^=7 # x^2+x+1
 return res

def plane(q):
 assert q in (2,3,4,5)
 points=list(product(range(q),repeat=2))
 lines=[('v',c) for c in range(q)]+[(m,c) for m in range(q) for c in range(q)]
 n=q*q+len(lines)
 adj=[set() for _ in range(n)]
 for i,(x,y) in enumerate(points):
  for j,(m,c) in enumerate(lines):
   test=x==c if m=='v' else y==add(mul(m,x,q),c,q)
   if test:
    adj[i].add(q*q+j);adj[q*q+j].add(i)
 assert all(len(adj[i])==q+1 for i in range(q*q))
 assert all(len(adj[i])==q for i in range(q*q,n))
 return adj,[0]*(q*q)+[1]*len(lines)

INTER=[{} for _ in range(5)]
def intern(r,s):
 dic=INTER[r]
 if s not in dic:dic[s]=len(dic)
 return dic[s]

def profile(q):
 A,sort=plane(q);n=len(A)
 mat=[[int(j in A[i]) for j in range(n)] for i in range(n)]
 t3={}
 for a in range(n):
  for b in range(n):
   for c in range(n):
    t=(a,b,c)
    atom=(tuple(sort[x] for x in t),tuple((t[i]==t[j],mat[t[i]][t[j]]) for i,j in ((0,1),(0,2),(1,2))))
    possible=0
    for x in range(n):
     if x==a or x==b or x==c:continue
     mask=(sort[x]<<3)+mat[x][a]+2*mat[x][b]+4*mat[x][c]
     possible|=(1<<mask)
    t3[t]=intern(1,(atom,possible))
 t2={(a,b):intern(2,frozenset(t3[a,b,c] for c in range(n))) for a in range(n) for b in range(n)}
 t1={a:intern(3,frozenset(t2[a,b] for b in range(n))) for a in range(n)}
 t0=intern(4,frozenset(t1.values()))
 return t0, [len(d) for d in INTER]

if __name__=='__main__':
 expected={2:0,3:1,4:2,5:2}
 for q in (2,3,4,5):
  typ,types=profile(q)
  print(f'order={q} vertices={q*q+q*(q+1)} type={typ} cumulative_types={types}',flush=True)
  assert typ==expected[q]
 print('VERIFY_OK')
