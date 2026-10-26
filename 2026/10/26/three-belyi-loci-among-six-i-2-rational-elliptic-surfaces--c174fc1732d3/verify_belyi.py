from sympy import symbols, sqrt, Poly, simplify, gcd
T=symbols('T')
ep=(1+sqrt(-3))/2
em=(1-sqrt(-3))/2
cases={'EE':(ep,em),'HH':(-1,2),'EH':(-1,ep)}

def part(f,d=12):
 f=Poly(f,T,extension=sqrt(-3))
 ans=[int(m) for fac,mul in f.sqf_list()[1] for m in [mul]*fac.degree()]
 if d>f.degree(): ans+=[d-f.degree()]
 return sorted(ans,reverse=True)
for key,(u,v) in cases.items():
 D=T**2+1; N=u*T**2+v; A=Poly(D**2-D*N+N**2,T,extension=sqrt(-3)); B=Poly(D*N*(D-N),T,extension=sqrt(-3))
 assert B.degree()==6
 assert gcd(A,B).degree()==0
 for p,q in [(D,N),(D,D-N),(N,D-N)]:
  assert gcd(Poly(p,T,extension=sqrt(-3)),Poly(q,T,extension=sqrt(-3))).degree()==0
 JN=256*A.as_expr()**3; JD=B.as_expr()**2
 JL=JN-1728*JD
 Q=(D+N)*(2*D-N)*(D-2*N)
 assert simplify(JL-64*Q**2)==0
 got=(part(JN),part(JL),part(JD))
 want={
  'EE':([6,6],[2]*6,[2]*6),
  'HH':([3]*4,[4,4,2,2],[2]*6),
  'EH':([6,3,3],[4,2,2,2,2],[2]*6)
 }[key]
 assert got==want,(key,got,want)
 # all polynomials finite roots disjoint and pairwise distinct except indicated multiplicities
 assert gcd(Poly(JN,T,extension=sqrt(-3)),Poly(JD,T,extension=sqrt(-3))).degree()==0
 assert gcd(Poly(JL,T,extension=sqrt(-3)),Poly(JD,T,extension=sqrt(-3))).degree()==0
 assert 12-len(got[0])+12-len(got[1])+12-len(got[2])==22
 print(key,got,'PASS')
print('VERIFY_OK')
