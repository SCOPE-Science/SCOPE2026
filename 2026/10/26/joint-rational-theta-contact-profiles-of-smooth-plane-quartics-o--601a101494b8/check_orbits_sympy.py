import json,itertools,time
from sympy import symbols,Poly,groebner,expand,diff
X,Y,Z,s,t=symbols('X Y Z s t')
f=str(__import__('pathlib').Path(__file__).resolve().with_name('quartic_profiles.json'));data=json.load(open(f));terms=data['terms']

def expr(mask):return sum(X**a*Y**b*Z**c for i,(a,b,c) in enumerate(terms) if (mask>>i)&1)
start=time.time()
for n,row in enumerate(data['orbits']):
 F=expr(row['rep'])
 for sub,vars in [({X:1},(Y,Z)),({Y:1},(X,Z)),({Z:1},(X,Y))]:
  if not vars:continue
  G=expand(F.subs(sub));du=diff(G,vars[0]);dv=diff(G,vars[1]) if len(vars)>1 else 0
  J=groebner([G,du,dv],*vars,modulus=2)
  assert J.is_zero_dimensional or J.polys==[Poly(1,*vars,modulus=2)]
  if J.polys!=[Poly(1,*vars,modulus=2)]:
   print('BAD',row['rep'],sub, J);raise SystemExit(1)
 # independent contact (sympy factor) on F2-lines
 roots=[0,0,0]
 bit=[]
 for i,L in enumerate(data['lines']):
  A,B=L['points'][:2]
  Fs=Poly(expand(F.subs({X:A[0]*s+B[0]*t,Y:A[1]*s+B[1]*t,Z:A[2]*s+B[2]*t},simultaneous=True)),s,t,modulus=2)
  co=[int(Fs.coeff_monomial(s**(4-j)*t**j)) for j in range(5)]
  if co[1]==co[3]==0:
   assert co[0]+co[2]+co[4]>0
   Q=Poly(co[0]*s**2+co[2]*s*t+co[4]*t**2,s,t,modulus=2)
   count=sum(int(Q.eval({s:a,t:b})%2==0) for a,b in [(1,0),(0,1),(1,1)])
   roots[count]+=1;bit.append(i)
 assert roots==row['contact'],(row['rep'],roots,row['contact'])
 if n%10==0:print('validated',n+1,'elapsed',round(time.time()-start,2),flush=True)
print('PASS',len(data['orbits']),'elapsed',round(time.time()-start,3))
