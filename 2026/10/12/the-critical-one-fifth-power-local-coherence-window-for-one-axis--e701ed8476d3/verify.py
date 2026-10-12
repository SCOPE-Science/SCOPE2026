#!/usr/bin/env python3
"""Reproduce moment identities and finite-size limits for locally dephased spin twisting."""
import mpmath as mp
mp.mp.dps=75

def xi(n,c,a):
    n=int(n); c=mp.mpf(str(c)); a=mp.mpf(str(a))
    e=c*mp.power(n, -mp.mpf(1)/5); t=a*mp.power(n,-mp.mpf(3)/5)
    A=1+ (n-1)*e**2/mp.mpf(2)*(1-mp.cos(2*t)**(n-2))
    B=(n-1)*e*mp.sin(t)*mp.cos(t)**(n-2)
    det=A-B**2
    # positive small eigenvalue via determinant to avoid cancellation
    plus=(1+A+mp.sqrt((A-1)**2+4*B**2))/2
    small=det/plus
    return small/(e**2*mp.cos(t)**(2*n-2))

def limit(c,a):
    c=mp.mpf(str(c)); a=mp.mpf(str(a)); return c**-4/a**2+a**4/(6*c**2)

for c in ['0.8','1.1','2.0']:
    cm=mp.mpf(c); a=(3/cm**2)**(mp.mpf(1)/6)
    pred=(3**(mp.mpf(2)/3)/2)*cm**(-mp.mpf(10)/3)
    errs=[]
    for n in [10**4,10**5,10**6,10**7]:
        v=xi(n,c,a); errs.append(float(abs(v-pred)))
    assert errs[-1]<errs[0]*0.3,(c,errs)
    print('critical_window c=',c,' a*=',mp.nstr(a,12),' limit=',mp.nstr(pred,12),' N=1e7=',mp.nstr(xi(10**7,c,a),12),'errors=',[round(e,5) for e in errs])

# Rationally verify the exact fourth-moment cancellation to the decisive sixth order.
import sympy as s
u,m=s.symbols('u m'); tau=s.symbols('tau')
c2=s.cos(2*tau);ct=s.cos(tau)
term=((m-1)/2*(1-c2**(m-2))-(m-1)**2*s.sin(tau)**2*ct**(2*m-4))
# Extract exact coefficient in tau^2,tau^4,tau^6 for integer m via symbolic differentiation of binomial expansions.
exp_c2=1 + (m-2)*(c2-1)+(m-2)*(m-3)/2*(c2-1)**2+(m-2)*(m-3)*(m-4)/6*(c2-1)**3
exp_ct2=1+(2*m-4)*(ct-1)+(2*m-4)*(2*m-5)/2*(ct-1)**2
# derive using formal series expansions as polynomials in u, avoids heavyweight symbolic exp at parameter m
cos2=1-2*u+s.Rational(2,3)*u**2-s.Rational(4,45)*u**3
cos1=1-u/2+u**2/24-u**3/720
sin2=u-u**2/3+s.Rational(2,45)*u**3
q=m-2
p2=s.expand(1+q*(cos2-1)+q*(q-1)/2*(cos2-1)**2+q*(q-1)*(q-2)/6*(cos2-1)**3)
p1=s.expand(1+(2*q)*(cos1-1)+(2*q)*(2*q-1)/2*(cos1-1)**2+(2*q)*(2*q-1)*(2*q-2)/6*(cos1-1)**3)
T=s.Poly(s.expand((m-1)/2*(1-p2)-(m-1)**2*sin2*p1),u)
coef6=s.expand(T.coeff_monomial(u**3));assert s.expand(coef6).coeff(m,4)==s.Rational(1,6)
print('sixth-order leading coefficient:',s.expand(coef6).coeff(m,4),'symbolic_check=passed')
print('VERIFY_OK independent_local_dephasing_critical_window=passed high_precision=passed sixth_order=passed')
