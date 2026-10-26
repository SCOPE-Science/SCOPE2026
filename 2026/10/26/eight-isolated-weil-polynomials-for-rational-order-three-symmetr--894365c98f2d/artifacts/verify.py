import itertools,math,collections
p=3
M=[]
for a,b,c,d in itertools.product(range(p),repeat=4):
 if (a*d-b*c)%p:
  U=(a,b,c,d)
  if U not in M and tuple((2*t)%p for t in U) not in M: M.append(U)
print('PGL',len(M))

def mul(v,w):
 r=[0]*(len(v)+len(w)-1)
 for i,a in enumerate(v):
  for j,b in enumerate(w):r[i+j]=(r[i+j]+a*b)%3
 return r

def scale_trans(f,m):
 a,b,c,d=m
 x=[b,a];z=[d,c]
 xp=[[1]];zp=[[1]]
 for i in range(6): xp.append(mul(xp[-1],x));zp.append(mul(zp[-1],z))
 r=[0]*7
 for i,t in enumerate(f):
  term=mul(xp[i],zp[6-i]); assert len(term)==7
  for j in range(7):r[j]=(r[j]+t*term[j])%3
 return tuple(r)

# coefficients index x^i (z^{6-i})
forms={}
for c,a,b in itertools.product((1,2),range(3),range(3)):
 if (a*a-b)%3==0: continue
 f=[0]*7
 for i,t in [(6,1),(4,1),(2,1),(3,a),(1,-a),(0,b)]:f[i]=(f[i]+c*t)%3
 forms[(c,a,b)]=tuple(f)
print('models',len(forms))
for k,f in forms.items(): print(k,f)
orbits=[];seen=set()
for k,f in forms.items():
 if f in seen:continue
 o={scale_trans(f,m) for m in M}
 seen|=o
 hit=[key for key,v in forms.items() if v in o]
 stabilizer=24//len(o)
 orbits.append((k,len(o),stabilizer,hit))
print('ISOMORPHIC ORBITS:',len(orbits))
for r in orbits:print(r)

# for each model branch pattern, rational point count, automorphism order 3 normal subgroup? two fixed inf points when leading square
for (c,a,b),f in forms.items():
 P=lambda t:(t*t+a*t+b)%3
 roots=[t for t in range(3) if P(t)==0]
 if len(roots)==2:
  part=(1,1,1,3) if 0 in roots else (3,3)
 elif len(roots)==0:
  part=(2,2,2) if a==0 else (6,)
 else: raise AssertionError((c,a,b,roots))
 ninf=2 if c==1 else 0
 v=(c*b)%3
 nfinite=3*(1 if v==0 else (2 if v==1 else 0))
 print('profile', (c,a,b), 'branch',part,'N1',ninf+nfinite)
# f9 a+b*u, u^2=2
V=[(a,b) for a in range(3) for b in range(3)]
add=lambda x,y:((x[0]+y[0])%3,(x[1]+y[1])%3)
mul9=lambda x,y:((x[0]*y[0]+2*x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
def pow9(v,e):
 z=(1,0)
 for _ in range(e):z=mul9(z,v)
 return z
squares={mul9(v,v) for v in V}
for (c,a,b),f in forms.items():
 n2=2
 for x in V:
  t=add(pow9(x,3),mul9((2,0),x))
  t2=mul9(t,t)
  y=add(add(t2,mul9((a,0),t)),(b,0))
  y=mul9((c,0),y)
  n2+=(1 if y==(0,0) else (2 if y in squares else 0))
 n1=3*(1 if c*b%3==0 else (2 if c*b%3==1 else 0))+(2 if c==1 else 0)
 a1=n1-4;a2=(n2-10+a1*a1)//2
 assert (n2-10+a1*a1)%2==0
 print('WEIL', (c,a,b),'N1',n1,'N2',n2,'a1,a2',a1,a2,'Jac',10+4*a1+a2,'ordinary?',a2%3!=0)

def gcdpoly(f,g):
 def trim(v):
  v=list(v)
  while v and v[-1]%3==0:v.pop()
  return v
 f=trim(f);g=trim(g)
 while g:
  r=f[:]
  while r and len(r)>=len(g):
   v=(r[-1]*pow(g[-1],-1,3))%3
   shift=len(r)-len(g)
   for i in range(len(g)):r[shift+i]=(r[shift+i]-v*g[i])%3
   r=trim(r)
  f,g=g,r
 return len(f)-1

def is_sf(f):
 d=max((i for i,c in enumerate(f) if c),default=-1)
 if d<5:return False
 deriv=tuple(i*f[i]%3 for i in range(1,7))
 return gcdpoly(f,deriv)==0

def matmul(s,t):
 a,b,c,d=s; e,f,g,h=t
 return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)

def norm(m):
 t=next(x for x in m if x)
 return tuple(v*pow(t,-1,3)%3 for v in m)
orders={}
for m in M:
 v=norm(m); z=v
 for n in range(1,25):
  if z==norm((1,0,0,1)):
   orders[m]=n;break
  z=norm(matmul(z,m))
print('PGL orders',collections.Counter(orders.values()))
three=[m for m,v in orders.items() if v==3]
print('eight order3',len(three))
allf=[]
for f in itertools.product(range(3),repeat=7):
 if not is_sf(f):continue
 if any(scale_trans(f,m)==f for m in three):allf.append(tuple(f))
print('full binary sextic locus:',len(allf),'expected',sum(q[1] for q in orbits))
assert len(allf)==sum(q[1] for q in orbits)
for f in allf:
 assert any(f in {scale_trans(forms[k],m) for m in M} for k,_,_,_ in orbits)
print('FULL_LOCUS_COVERED')

# The complete arithmetic genus-two isomorphism classification is the orbit
# space of geometrically squarefree binary sextics under PGL2(F3).
smooth=[tuple(f) for f in itertools.product(range(3),repeat=7) if is_sf(f)]
assert len(smooth)==1296
visited=set(); arithmetic_orbits=[]
for f in smooth:
 if f in visited: continue
 orbit={scale_trans(f,m) for m in M}
 assert len(orbit)==24//(24//len(orbit))
 assert all(is_sf(v) for v in orbit)
 visited|=orbit
 arithmetic_orbits.append((f,len(orbit)))
assert len(visited)==1296 and len(arithmetic_orbits)==69

def eval9(f,x):
 out=(0,0)
 for a in reversed(f):out=add(mul9(out,x),(a,0))
 return out

def weil_pair(f):
 leading=f[6]
 n1=(2 if leading==1 else (0 if leading==2 else 1))
 n2=(2 if leading else 1)
 for xx in range(3):
  z=sum(f[i]*pow(xx,i,3) for i in range(7))%3
  n1+=(1 if z==0 else (2 if z==1 else 0))
 for xx in V:
  z=eval9(f,xx)
  n2+=(1 if z==(0,0) else (2 if z in squares else 0))
 a=n1-4
 assert (n2-10+a*a)%2==0
 return (a,(n2-10+a*a)//2)

by_weil=collections.defaultdict(list)
order3_locus=[]
for f,size in arithmetic_orbits:
 pair=weil_pair(f)
 by_weil[pair].append((f,size))
 if (24//size)%3==0:
  assert any(scale_trans(f,m)==f for m in three)
  order3_locus.append((pair,f,size))
 else:
  assert all(scale_trans(f,m)!=f for m in three)
assert len(by_weil)==50
assert len(order3_locus)==8
wanted={(-4,10),(-2,7),(-2,1),(-1,-2),(1,-2),(2,1),(2,7),(4,10)}
assert {t[0] for t in order3_locus}==wanted
assert all(len(by_weil[ab])==1 for ab in wanted)
assert collections.Counter(size for _,_,size in order3_locus)=={1:2,4:2,8:4}
assert sorted(n for _,n in arithmetic_orbits if (24//n)%3==0)==[1,1,4,4,8,8,8,8]
print('GLOBAL: 1296 squarefree sextics; 69 arithmetic orbits; 50 Weil types')
for pair,f,size in sorted(order3_locus):
 print('UNIQUE',pair, 'orbit_size', size, 'representative', ''.join(map(str,f)))
print('EIGHT WEIL TYPES: each has exactly one genus-two isomorphism class')
print('PASS')
