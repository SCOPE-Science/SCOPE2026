"""Exact symbolic reproduction-matrix check for a published 15-compartment co-infection ODE."""
from sympy import Matrix, symbols, Rational, simplify, sqrt

# Linear infected coordinates: E_C, E_M, E_CM, I_C, I_M, I_CM, E_r, I_r.
(beta_a,beta_m,beta_b,beta_r, theta_C,theta_M,theta_CM,theta_r,
 phi_C,phi_M,a,b,c,d,e,u,g,h)=symbols(
 'beta_a beta_m beta_b beta_r theta_C theta_M theta_CM theta_r '
 'phi_C phi_M a b c d e u g h', positive=True)

V=Matrix.diag(a,b,c,d,e,u,g,h)
V[2,0]=-phi_C;V[2,1]=-phi_M
V[3,0]=-theta_C;V[4,1]=-theta_M;V[5,2]=-theta_CM;V[7,6]=-theta_r
F=Matrix.zeros(8)
F[0,3]=beta_a;F[0,5]=beta_a
F[1,4]=beta_m;F[1,5]=beta_m;F[1,7]=beta_b
F[6,7]=beta_r
indices=(0,1,6)
G=(F*V.inv()).extract(indices,indices).applyfunc(simplify)
w=theta_CM/(c*u)
expected=Matrix([
 [beta_a*(theta_C/d+phi_C*w)/a, beta_a*phi_M*w/b, 0],
 [beta_m*phi_C*w/a, beta_m*(theta_M/e+phi_M*w)/b, beta_b*theta_r/(g*h)],
 [0,0,beta_r*theta_r/(g*h)]
])
assert all(simplify(v)==0 for v in (G-expected)), (G,expected)
# Strictly positive model parameter assignment: mu_h=mu_r=1,
# theta_C=theta_M=theta_r=1, theta_CM=4, phi_C=phi_M=1,
# rho_C=rho_M=2, delta_C=delta_M=1, rho_CM=delta_CM=1/4,
# delta_r=1; beta_a=7 and beta_m=beta_b=beta_r=1.
vals={beta_a:7,beta_m:1,beta_b:1,beta_r:1,
 theta_C:1,theta_M:1,theta_CM:4,theta_r:1,phi_C:1,phi_M:1,
 a:3,b:3,c:5,d:4,e:4,u:Rational(3,2),g:2,h:2}
G0=G.subs(vals)
assert G0==Matrix([[Rational(329,180),Rational(56,45),0],
                  [Rational(8,45),Rational(47,180),Rational(1,4)],
                  [0,0,Rational(1,4)]])
H=G0[:2,:2]
trace=H.trace();delta=simplify(trace**2-4*H.det())
rho_h=simplify((trace+sqrt(delta))/2)
assert simplify(rho_h-Rational(329,180)).is_positive
assert Rational(7,8)<1 and Rational(1,8)<1 and Rational(1,4)<1
# Positive transfer out of the putative COVID-only invariant face.
assert vals[phi_C]>0 and vals[phi_M]>0
print('VERIFY_OK')
print('G0=', G0)
print('rho_h=',rho_h, 'float=',rho_h.evalf(15))
print('published_max=',Rational(7,8))
