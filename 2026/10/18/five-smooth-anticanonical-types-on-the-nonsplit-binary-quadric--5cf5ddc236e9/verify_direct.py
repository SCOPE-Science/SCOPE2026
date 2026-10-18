"""Direct check of all 511 anticanonical divisors on a nonsplit quadric in characteristic 2."""
import itertools, collections, sympy as sp
v=sp.symbols('x0 x1 x2 x3')
# independent descending lex monomial order
terms=[tuple([int(i==j)+int(i==k) for i in range(4)]) for j in range(4) for k in range(j,4)]
M={a:i for i,a in enumerate(terms)}
def b(i,j):return 1<<M[tuple(int(k==i)+int(k==j) for k in range(4))]
Q=b(0,1)^b(2,2)^b(2,3)^b(3,3)
assert Q>0
highest=1<<(Q.bit_length()-1)
polys=[sum(sp.prod(v[i]**a[i] for i in range(4)) for k,a in enumerate(terms) if z>>k&1) for z in range(1024)]
q=polys[Q];dq=[sp.diff(q,x) for x in v]
points=[t for t in range(1,16) if q.subs({v[i]:(t>>i)&1 for i in range(4)})%2==0]
assert len(points)==5
hist=collections.Counter();smooth_masks=[]
for t in range(1,1024):
 if t&highest:continue
 f=polys[t];df=[sp.diff(f,x) for x in v]
 jac=[sp.expand(dq[i]*df[j]+dq[j]*df[i]) for i in range(4) for j in range(i+1,4)]
 ok=True
 for i in range(4):
  eq=[sp.Poly(e.subs(v[i],1),*[v[j] for j in range(4) if i!=j],modulus=2).as_expr() for e in [q,f]+jac]
  gb=sp.groebner(eq,*[v[j] for j in range(4) if i!=j],order='lex',modulus=2)
  if len(gb.polys)!=1 or gb.polys[0].as_expr()!=1:
   ok=False;break
 if ok:
  smooth_masks.append(t)
  n=sum(f.subs({v[i]:(p>>i)&1 for i in range(4)})%2==0 for p in points)
  hist[n]+=1
assert dict(hist)=={1:60,2:90,3:60,4:30},hist
assert len(smooth_masks)==240
print('direct (lex) smooth count',len(smooth_masks),'histogram',dict(sorted(hist.items())))
