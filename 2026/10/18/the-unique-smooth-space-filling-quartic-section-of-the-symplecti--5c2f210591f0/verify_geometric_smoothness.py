import time
from sympy import symbols,groebner,Poly
x=symbols('x0:4')
M0=[(0,1,2,1),(0,2,0,2),(0,2,1,1),(0,2,2,0),(0,3,0,1),(0,3,1,0),(1,0,0,3),(1,0,3,0),(1,1,2,0),(1,2,1,0),(2,0,0,2),(3,0,1,0)]
M1=[(0,1,2,1),(0,2,0,2),(0,2,1,1),(0,2,2,0),(0,3,0,1),(0,3,1,0),(1,0,0,3),(1,0,3,0),(1,1,0,2),(1,1,2,0),(1,2,0,1),(1,2,1,0),(2,0,2,0),(3,0,0,1)]
g=x[0]**2*x[1]+x[0]*x[1]**2+x[2]**2*x[3]+x[2]*x[3]**2
for h,mons in enumerate((M0,M1)):
 f=sum(__import__('math').prod(x[i]**m[i] for i in range(4)) for m in mons)
 jacg=[g.diff(v) for v in x];jacf=[f.diff(v) for v in x]
 minors=[jacg[i]*jacf[j]-jacg[j]*jacf[i] for i in range(4) for j in range(i+1,4)]
 for chart in range(4):
  sub={x[chart]:1};vars=[x[j] for j in range(4) if j!=chart]
  polys=[u.subs(sub) for u in [g,f]+minors]
  t=time.perf_counter();b=groebner(polys,*vars,modulus=2,order='grevlex');unit=len(b.polys)==1 and b.polys[0].as_expr()==1
  print('rep',h,'chart',chart,'unit',unit,'basis length',len(b.polys),'elapsed',round(time.perf_counter()-t,3),flush=True)
