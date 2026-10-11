"""Symbolic coefficient checks for a cubic electrochemical slow-fast flow."""
import sympy as s
u,k,e,d,r=s.symbols('u k e d r', positive=True, finite=True)
H=e+k*(1+1/d)
A=-3*r/H
S=1+2/d+2/d**2
B=(-1+2*k*A**2*S)/H
a=-(1+1/d)*A
c=-(1+2/d)*A
b=s.simplify((e*B+1)/k)
q=s.simplify(b-(B+2*c*A)/d)
v=u+a*u**2+b*u**3
w=u+c*u**2+q*u**3
f=s.expand((k*(v-u)-3*r*u**2-u**3)/e)
g=s.expand(u-2*v+w)
h=s.expand(d*(v-w))
checks={
'fast_coefficient_u2':s.simplify(f.coeff(u,2)-A),
'fast_coefficient_u3':s.simplify(f.coeff(u,3)-B),
'y_invariance_u2':s.simplify(s.expand(s.diff(v,u)*f-g).coeff(u,2)),
'y_invariance_u3':s.simplify(s.expand(s.diff(v,u)*f-g).coeff(u,3)),
'z_invariance_u2':s.simplify(s.expand(s.diff(w,u)*f-h).coeff(u,2)),
'z_invariance_u3':s.simplify(s.expand(s.diff(w,u)*f-h).coeff(u,3)),
'log_coefficient':s.simplify(B/A - (1/(3*r)-6*k*r*S/H**2)),
}
for name,residual in checks.items():
 print(name,'=',residual)
 assert residual==0
print('H=',H)
print('A=',A)
print('B=',s.factor(B))
print('B/A=',s.factor(B/A))
print('a=',a,'b=',s.factor(b),'c=',c,'q=',s.factor(q))
