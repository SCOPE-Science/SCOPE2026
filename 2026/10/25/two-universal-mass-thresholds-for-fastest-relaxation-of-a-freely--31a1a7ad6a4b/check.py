import numpy as np, sympy as sp, math, random
s,G,t=sp.symbols('s G t',real=True)
P=s**3+G*s**2+s+t*G
D=sp.factor(sp.discriminant(P,s))
assert sp.simplify(D-(-4*t*G**4+(1+18*t-27*t*t)*G**2-4))==0
# derive critical inequalities identities
u=sp.symbols('u',positive=True)
q=(1-3*t-sp.sqrt((1-t)*(1-9*t)))/2
assert sp.simplify(q*q-(1-3*t)*q+t)==0
R=sp.symbols('R',positive=True)
Cg=R*(R**2+1)/(R**2+t)
assert sp.simplify(sp.diff(Cg,R)-(R**4+(3*t-1)*R**2+t)/(R**2+t)**2)==0
assert sp.simplify((Cg-R)/2-R*(1-t)/(2*(R**2+t)))==0
def opt(t):
 if t < 1/9:
  u=(1-3*t-math.sqrt((1-t)*(1-9*t)))/2
  r=math.sqrt(u);g=(1+3*u)/(2*r); rate=r
 elif t <= 1/5:
  r=math.sqrt((1-3*t)/2);g=3*r;rate=r
 else:
  r=math.sqrt(t);g=(1+t)/(2*r);rate=(1-t)/(4*r)
 return g,rate
rng=random.Random(726526)
cases= [1e-4,.001,.01,.06,.1,1/9,.112,.14,.19,.2,.21,.4,.9,.999] + [10**rng.uniform(-4,-1.0) for _ in range(100)] + [rng.uniform(.112,1) for _ in range(100)]
num=0
for tt in cases:
 g,rat=opt(tt)
 if tt <1/9:
  roots=np.roots([1,g,1,g*tt]); obs=-max(x.real for x in roots)
  assert abs(obs-rat)<1e-5, (tt,g,rat,roots)
 elif tt == 1/9:
  assert abs(-max(x.real for x in np.roots([1,g,1,g*tt]))-rat)<1e-4
 else:
  roots=np.roots([1,g,1,g*tt]);obs=-max(x.real for x in roots)
  assert abs(obs-rat)<1e-7, (tt,g,rat,roots)
 for scale in [0.02,.1,.4,.7,.9,.97,1.03,1.1,1.5,2.5,5,25]:
  gg=g*scale;roots=np.roots([1,gg,1,gg*tt]);rate=-max(x.real for x in roots)
  assert rate<rat+5e-8,(tt,g,rat,scale,rate)
  num+=1
 for _ in range(3):
  m1=10**rng.uniform(-2,2);m2=m1*(1-tt)/tt;k=10**rng.uniform(-2,2)
  omega=(k/m1+k/m2)**.5; gamma=g*m1*omega
  mat=np.array([[0,0,1,0],[0,0,0,1],[-k/m1,k/m1,-gamma/m1,0],[k/m2,-k/m2,0,0]])
  ev=np.linalg.eigvals(mat); nz=ev[np.abs(ev)>1e-6]; r_phys=-max(e.real for e in nz)/omega
  if tt != 1/9:assert abs(r_phys-rat)<1e-5,(tt,r_phys,rat)
  num+=1
print('symbolic factor, 200+ formula/phase,',num,'comparisons passed')
for tt in [.01,.1,1/9,.14,.2,.3,.5,.9]:
 g,rat=opt(tt);print(f'theta {tt:.6f} gamma {g:.9f} rate {rat:.9f} roots',np.round(np.roots([1,g,1,g*tt]),7))
