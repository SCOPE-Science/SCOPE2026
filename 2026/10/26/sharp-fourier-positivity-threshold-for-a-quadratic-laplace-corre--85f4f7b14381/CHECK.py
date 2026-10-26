import sympy as S
u,v,a,c=S.symbols('u v a c', real=True)
F=8*a**2/((a**2+u)*(a**2+v))
T=S.factor(F+c*S.diff(F,a,2))
D=(1+u)**3*(1+v)**3
N=S.factor((T.subs(a,1))*D/8)
s,p=S.symbols('s p',real=True)
E=S.expand(N)
E2=S.Poly(E,u,v)
print('N raw=',E)
claim=s**2+(2-6*c)*p*s+(1+2*c)*p**2+(2-24*c)*p+(2-2*c)*s+1+6*c
assert S.factor(E-claim.subs({s:u+v,p:u*v}))==0
print('boundary:',S.factor(claim.subs(c,S.Rational(6,13))*13))
x,t=S.symbols('x t',real=True)
B=S.factor(13*claim.subs(c,S.Rational(6,13)).subs({p:x**2,s:2*x+t}))
print('B=',B)
assert S.factor(B-(13*t**2+(52*x-10*x**2+14)*t+(x+1)**2*(5*x-7)**2))==0
print('disc=',S.factor(S.discriminant(B,t)))
print('boundary at critical point=',S.factor(claim.subs({s:S.Rational(14,5),p:S.Rational(49,25)})))
print('c=1/2=',S.factor(claim.subs({s:S.Rational(14,5),p:S.Rational(49,25),c:S.Rational(1,2)})))
print('all checks PASSED')
import mpmath as m
m.mp.dps=35
pairs=[(m.mpf("0.3"),m.mpf("0.8")),(m.mpf("2.7"),m.mpf("3.1")),(m.sqrt(m.mpf(7)/5),0),(0,m.mpf("1.8")),(m.mpf("5.0"),m.mpf("0.2")),(m.mpf("7.5"),m.mpf("3.3"))]
for cc in [m.mpf(0),m.mpf(6)/13,m.mpf(1)/2]:
    for xi,eta in pairs:
        ff=lambda r: m.e**(-r)*(-1+cc*(2*r-r**2))
        integral=m.quad(lambda r: -4*ff(r)*(m.sin(xi*r)/xi if xi else r)*(m.sin(eta*r)/eta if eta else r),[0,m.inf])
        X=(xi-eta)**2;Y=(xi+eta)**2; ss=X+Y; pp=X*Y
        nn=ss**2+(2-6*cc)*pp*ss+(1+2*cc)*pp**2+(2-24*cc)*pp+(2-2*cc)*ss+1+6*cc
        rhs=8*nn/((1+X)**3*(1+Y)**3)
        assert abs(integral-rhs)<m.mpf('2e-11'),(cc,xi,eta,integral,rhs)
print('18 independent integral comparisons PASSED')
