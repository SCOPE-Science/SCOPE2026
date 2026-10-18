import sympy as s
from collections import Counter
V=s.symbols('x0:5')
E=[(i,j) for i in range(5) for j in range(i+1,5)]
def q(mask):
 return sum(((mask>>i)&1)*V[i]**2 for i in range(5))+sum(((mask>>(5+k))&1)*V[i]*V[j] for k,(i,j) in enumerate(E))
def qeval(mask,x):
 z=(mask&x&31).bit_count()%2
 for k,(i,j) in enumerate(E):
  if mask>>(5+k)&1 and x>>i&1 and x>>j&1:z^=1
 return z

def smooth_h(a,b,h):
 p=next(i for i in range(5) if (h>>i)&1)
 rem=[i for i in range(5) if i!=p]
 sub={V[p]:sum(V[i] for i in rem if h>>i&1)}
 polys=[s.expand(q(m).subs(sub)) for m in [a,b]]
 for pivot in rem:
  vs=[V[i] for i in rem if i!=pivot]
  fs=[s.Poly(s.expand(f.subs({V[pivot]:1})),*vs,modulus=2).as_expr() for f in polys]
  minors=[]
  deriv=[[s.diff(f,x) for x in vs] for f in fs]
  for i in range(3):
   for j in range(i+1,3):minors.append(s.expand(deriv[0][i]*deriv[1][j]-deriv[0][j]*deriv[1][i]))
  gb=s.groebner(fs+minors,*vs,order='grevlex' if False else 'lex',modulus=2)
  if not (len(gb.polys)==1 and gb.polys[0].is_one):return False
 return True

if __name__=='__main__':
 for label,a,b in [('cycle5',4144,778),('cycle23_reduced',4144,792),('cycle23_twist',4144,793)]:
  pts=[x for x in range(1,32) if qeval(a,x)==qeval(b,x)==0]
  joint=Counter()
  for h in range(1,32):
   cnt=sum(((h&x).bit_count()%2)==0 for x in pts)
   sm=smooth_h(a,b,h)
   joint[(sm,cnt)]+=1
  print(label,'joint',sorted(joint.items()),'smooth',sum(v for (sm,c),v in joint.items() if sm), flush=True)
