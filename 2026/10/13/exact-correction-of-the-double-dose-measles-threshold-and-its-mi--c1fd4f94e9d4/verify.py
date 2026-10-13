import sympy as sp
mu,kappa,omegav,psiv,omega,phi,gamma,phi1,beta,Lam,c=sp.symbols('mu kappa omegav psiv omega phi gamma phi1 beta Lam c', positive=True)
k1=phi+mu; k2=gamma+phi1+mu; k3=omegav+kappa+mu; k4=omega+mu
D=mu*k3+psiv*(kappa+mu); Q=k3*k4+psiv*(k4+kappa)
S=Lam*k3/D; V1=psiv*Lam/D; V2=kappa*V1/k4; R=omega*V2/mu
N=sp.simplify(S+V1+V2+R)
assert sp.simplify(N-Lam/mu)==0
Rtot=sp.simplify(beta*phi*S/(N*k1*k2))
assert sp.simplify(Rtot-beta*phi*mu*k3/(k1*k2*D))==0
R24=beta*phi*k3*k4/(k1*k2*Q)
R26=beta*phi*k4/(k1*k2*Q)
assert sp.simplify(R24-k3*R26)==0
assert sp.simplify(S/(S+V1+V2)-k3*k4/Q)==0
gap=beta*phi*k3*psiv*kappa*omega/(k1*k2*D*Q)
assert sp.simplify(R24-Rtot-gap)==0
rates={mu:c*mu,kappa:c*kappa,omegav:c*omegav,psiv:c*psiv,omega:c*omega,phi:c*phi,gamma:c*gamma,phi1:c*phi1,beta:c*beta}
assert sp.simplify(Rtot.xreplace(rates)-Rtot)==0
assert sp.simplify(R24.xreplace(rates)-R24)==0
assert sp.simplify(R26.xreplace(rates)-R26/c)==0
vals={mu:1,kappa:1,omegav:1,psiv:1,omega:1,phi:1,gamma:1,phi1:0,beta:sp.Rational(31,5)}
assert sp.simplify(Rtot.subs(vals))==sp.Rational(93,100)
assert sp.simplify(R24.subs(vals))==sp.Rational(31,30)
print('VERIFY_OK')
