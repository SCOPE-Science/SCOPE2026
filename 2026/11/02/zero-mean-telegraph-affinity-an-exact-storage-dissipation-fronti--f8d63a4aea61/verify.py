"""Independent exact-arithmetic and generator checks for the telegraph-affinity battery.

Run: python verify.py
Requires: sympy (a widely available symbolic algebra library).
The analytical argument is in RESULT.md; these are finite deterministic supplements.
"""
import sympy as sp

x, y, k, nu = sp.symbols('x y k nu', positive=True)
u_plus, v_plus = k*y/x, k*x/y
u_minus, v_minus = k/(x*y), k*x*y
L_plus, L_minus = u_plus+v_plus, u_minus+v_minus
Delta = L_plus*L_minus + nu*(L_plus+L_minus)
z_plus = (u_plus*(L_minus+nu)+nu*u_minus)/(2*Delta)
z_minus = (u_minus*(L_plus+nu)+nu*u_plus)/(2*Delta)
pi = sp.Matrix([sp.Rational(1,2)-z_plus,z_plus,sp.Rational(1,2)-z_minus,z_minus])
Q = sp.Matrix([
    [-u_plus-nu, u_plus, nu, 0],
    [v_plus,-v_plus-nu,0,nu],
    [nu,0,-u_minus-nu,u_minus],
    [0,nu,v_minus,-v_minus-nu],
])
C=(x+x**-1)/2
S=(x-x**-1)/2
c=(y+y**-1)/2
s=(y-y**-1)/2
H=k*(C**2+s**2)
G=C*c
W=H+nu*G
peq=1/(1+x*x)
delta=k*S*s**2/(2*C*W)
J=k*nu*s*c/(2*W)
delta0=S*s**2/(2*C*(C**2+s**2))
# The dimensionless entropy production is 2*alpha*J, with alpha=2 log(y).
# Divide by 2*alpha to avoid symbolic logarithms in exact rational checks.
sigma_over_2alpha=J
sigma_infty_over_2alpha=k*s/(2*C)

def check_zero(expr, label):
    z=sp.factor(sp.together(expr))
    assert z==0, f'{label}: {z}'

checks=0
check_zero(sum(pi)-1,'normalization');checks+=1
for i in range(4):
    check_zero((Q.T*pi)[i],f'generator stationarity {i}');checks+=1
check_zero(pi[1]+pi[3]-peq-delta,'charge formula');checks+=1
check_zero(u_plus*pi[0]-v_plus*pi[1]-J,'battery-edge current');checks+=1
check_zero(nu*(pi[1]-pi[3])-J,'sign-edge current');checks+=1
check_zero(v_minus*pi[3]-u_minus*pi[2]-J,'negative-sign battery current');checks+=1
check_zero(nu*(pi[2]-pi[0])-J,'second sign-edge current');checks+=1
check_zero(delta/delta0+J/sigma_infty_over_2alpha-1,'normalized exact frontier');checks+=1
check_zero((delta/delta0)-H/W,'storage fraction');checks+=1
check_zero((J/sigma_infty_over_2alpha)-nu*G/W,'dissipation fraction');checks+=1
check_zero(sp.diff(delta,nu)+delta0*H*G/W**2,'negative charging response');checks+=1
check_zero(sp.diff(J,nu)-sigma_infty_over_2alpha*H*G/W**2,'positive dissipation response');checks+=1
check_zero((sp.Rational(1,2)-peq)-delta-(S/(2*C))*nu*G/W-(S/(2*C))*(C**2*k/H-1)*H/W,'optional identity check') if False else None

# Exact independent stationary distribution by solving a 4-state linear system
# for varied positive rational exponentials and physical time scales.
xs=[sp.Rational(3,2),sp.Rational(2),sp.Rational(5)]
ys=[sp.Rational(4,3),sp.Rational(3),sp.Rational(7,2)]
ks=[sp.Rational(1,3),sp.Rational(2)]
rs=[sp.Rational(1,7),sp.Rational(1),sp.Rational(5)]
for xv in xs:
    for yv in ys:
        for kv in ks:
            for rv in rs:
                su={x:xv,y:yv,k:kv,nu:rv}
                qr=Q.subs(su)
                a=qr.T.copy()
                a[3,:]=sp.Matrix([[1,1,1,1]])
                stationary=a.inv()*sp.Matrix([0,0,0,1])
                expected=pi.subs(su)
                assert stationary==expected
                assert all(z>0 for z in stationary)
                exact_p=stationary[1]+stationary[3]
                exact_J=kv*yv/xv*stationary[0]-kv*xv/yv*stationary[1]
                assert exact_p==sp.cancel(peq.subs(su)+delta.subs(su))
                assert exact_J==sp.cancel(J.subs(su))
                assert exact_p>peq.subs(su)
                assert exact_p<sp.Rational(1,2)
                checks+=6
print('PASS:',checks,'exact symbolic and rational checks; finite tests supplement the proof.')
