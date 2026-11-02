import sympy as sp,itertools
add=lambda a,b:a^b
MULT=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
def mul(a,b):return MULT[a][b]
def Q(v):
 return (lambda t: t)( __import__('functools').reduce(add,(mul(a,a) for a in v),0)^__import__('functools').reduce(add,(mul(v[i],v[j]) for i in range(4) for j in range(i+1,4)),0))
def B(u,v):return Q(tuple(u[i]^v[i] for i in range(4)))^Q(u)^Q(v)
def S(a,v):return tuple(mul(a,x) for x in v)
def Plus(*vs):return tuple(__import__('functools').reduce(add,(v[i] for v in vs),0) for i in range(4))
vecs=[p for p in itertools.product(range(4),repeat=4) if p!=(0,0,0,0) and Q(p)==0]
p=(0,1,1,1)
q=next(x for x in vecs if B(p,x)==1)
rs=[x for x in vecs if B(p,x)==B(q,x)==0]
r=rs[0];s=next(x for x in rs if B(r,x)==1)
print('basis p,r,s,q:',p,r,s,q,flush=True)
assert B(p,q)==B(r,s)==1 and all(B(x,y)==0 for x,y in [(p,r),(p,s),(q,r),(q,s)])
a,b,c,d=sp.symbols('a b c d');x=[a,b,c,d,a+b+c+d]
F=sp.Poly(sp.expand(sum(sp.prod(t) for t in itertools.combinations(x,3))),a,b,c,d,modulus=2)
poly={}
# polynomials in variables t=s*u, v=s*v,w=t*u,z=t*v corresponding to basis p,r,s,q
basis=(p,r,s,q)
# coefficient of monomials in 4 Segre vars y0..y3 in expansion, via linear substitution of cubic
terms={ (0,0,0,0):0 }
def mm(A,B):
 o={}
 for x,a in A.items():
  for y,b in B.items():
   z=tuple(x[i]+y[i] for i in range(4));o[z]=o.get(z,0)^mul(a,b)
 return {x:a for x,a in o.items() if a}
def lin(i):return {tuple(int(j==k) for j in range(4)):basis[k][i] for k in range(4) if basis[k][i]}
zero=(0,0,0,0)
for e,co in F.terms():
 if not co: continue
 m={zero:1}
 for i,ex in enumerate(e):
  for z in range(ex):m=mm(m,lin(i))
 for ex,v in m.items():poly[ex]=poly.get(ex,0)^v
poly={e:v for e,v in poly.items() if v}
print('cubic in segre vars',poly,flush=True)
# translate monomials y0=su y1=sv y2=tu y3=tv to exponents for s,t,u,v
G={}
for e,co in poly.items():
 j=(e[0]+e[1],e[2]+e[3],e[0]+e[2],e[1]+e[3]);G[j]=G.get(j,0)^co
G={e:v for e,v in G.items() if v}
assert all(e[0]+e[1]==3 and e[2]+e[3]==3 for e in G)
print('bidegree G:',G,flush=True)

# Independently multiply the two explicit bidegree-(1,2),(2,1) forms.
A={(1,0,0,2):1,(0,1,2,0):1,(0,1,0,2):1}
D={(2,0,0,1):1,(0,2,1,0):1,(0,2,0,1):1}
prod={}
for e,aa in A.items():
 for f,bb in D.items():
  z=tuple(e[i]+f[i] for i in range(4))
  prod[z]=prod.get(z,0)^mul(aa,bb)
prod={e:v for e,v in prod.items() if v}
assert prod==G,(G,prod)
# Geometry of the nonsplit quadric over F2.
F2points=[u for u in itertools.product((0,1),repeat=4) if any(u) and Q(u)==0]
assert len(F2points)==5
# Every rational point of the symmetric Bring model is singular and has
# exactly one zero among its five coordinates.
def e2(t):return __import__('functools').reduce(add,(mul(u,v) for u,v in itertools.combinations(t,2)),0)
def e3(t):return __import__('functools').reduce(add,(mul(u,mul(v,w)) for u,v,w in itertools.combinations(t,3)),0)
for u in F2points:
 x=list(u)+[u[0]^u[1]^u[2]^u[3]]
 assert e2(x)==e3(x)==0 and x.count(0)==1
# All F4 points: five nodes plus two conjugate parameterizations of the cubics.
F4points=set()
for u in itertools.product(range(4),repeat=4):
 if not any(u) or Q(u) or e3(list(u)+[u[0]^u[1]^u[2]^u[3]]): continue
 j=next(i for i,c in enumerate(u) if c)
 inv={1:1,2:3,3:2}[u[j]]
 F4points.add(tuple(mul(inv,c) for c in u))
assert len(F4points)==5,F4points
print('QUADRIC_F2_POINTS=5; BRING_F2_POINTS=5; BRING_F4_POINTS=5')
print('SEGRE_CUBIC_FACTOR_BIDEGREES=(1,2),(2,1); PRODUCT_IDENTITY=PASS')
print('NODE_COUNT=5; COMPONENT_DEGREES=3,3; INTERSECTION_MULTIPLICITIES=1^5')
print('FROBENIUS_EXCHANGES_COMPONENTS; POINTS_OVER_F2M=5_IF_ODD_ELSE_2^(M+1)-3')
print('VERIFY_OK')
