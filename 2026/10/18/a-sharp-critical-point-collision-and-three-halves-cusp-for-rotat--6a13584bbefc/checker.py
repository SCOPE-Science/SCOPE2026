import sympy as s, cmath, math
w,r,c=s.symbols('w r c',positive=True, real=True)
q=r**2
U=w*(w*w-2*r*c*w+r*r)
V=1-2*r*c*w+r*r*w*w
F=U/V
N=s.factor(s.diff(U,w)*V-U*s.diff(V,w))
assert s.expand(N - (q*(w**4+1)-4*r*c*(w**3+w)+(3+4*r*r*c*c-r**4)*w*w))==0
assert s.factor(N/w**2-(q*(w+1/w)**2-4*r*c*(w+1/w)+3+4*r*r*c*c-r**4-2*r*r))==0
cp=s.sqrt((3+r*r))/2
t=(s.sqrt(3+r*r)-s.sqrt(3*(1-r*r)))/(2*r)
assert s.simplify((w**2*N).subs({c:cp,w:t}))==0
assert s.simplify(N.subs(c,cp).subs(w,t))==0
assert s.simplify(s.diff(N,w).subs(c,cp).subs(w,t))==0
assert s.simplify((s.diff(N,w,2).subs(c,cp).subs(w,t))-(6*(1-r*r)))==0
assert s.simplify((s.diff(N,c).subs(c,cp).subs(w,t))+8*cp*(1-r*r)*t*t)==0
print('Symbolic derivative/critical collision identities all PASS')
for rv in [0.25,0.5,0.75]:
 qv=rv**2; cv=math.sqrt(3+qv)/2; tv=(math.sqrt(3+qv)-math.sqrt(3*(1-qv)))/(2*rv)
 kv=tv*math.sqrt(8*cv/3)
 Vv=1-2*rv*cv*tv+qv*tv**2
 K=(32/3)*cv*(1-qv)*tv*tv*kv/Vv**2
 def innerroot(u):
  roots=[(u+cmath.sqrt(u*u-4))/2,(u-cmath.sqrt(u*u-4))/2]
  return min(roots,key=abs)
 def critical_pair(cc):
  rad=cmath.sqrt((1-qv)*(4*cc**2-3-qv))
  return [innerroot((2*cc+sgn*rad)/rv) for sgn in (+1,-1)]
 def FV(z,cc): return z*(z*z-2*rv*cc*z+qv)/(1-2*rv*cc*z+qv*z*z)
 for d in [-1e-3,1e-3,1e-4]:
  crits=critical_pair(cv+d)
  gap=abs(FV(crits[0],cv+d)-FV(crits[1],cv+d))
  predicted=K*abs(d)**1.5
  print('r',rv,'delta',d,'criticals',crits,'gap ratio',gap/predicted)
  assert abs(gap/predicted-1)<0.1
print('All numerical branch checks PASS')
# Additional checks of chain-rule critical multiplicities in two sample lifts.
z=s.symbols('z')
for n in (1,2,3,5):
    Cz=s.cancel(F.subs(w,z**n).subs({r:s.Rational(1,2),c:s.Rational(4,5)}))
    Cprime=s.cancel(s.diff(F,w).subs(w,z**n).subs({r:s.Rational(1,2),c:s.Rational(4,5)}))
    assert s.cancel(s.diff(Cz,z)-n*z**(n-1)*Cprime)==0
print('All rational lift checks PASS')
