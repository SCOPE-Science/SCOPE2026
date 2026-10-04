from fractions import Fraction
import sympy as sp
S,E,I,V1,V2,R = sp.symbols("S E I V1 V2 R", positive=True)
Lam,beta,psi,mu,omegav,phi,phi1,gamma,kappa,omega = sp.symbols("Lam beta psi mu omegav phi phi1 gamma kappa omega", positive=True)
N = S+E+I+V1+V2+R
bS = Lam-beta*S*I/N-(psi+mu)*S+omegav*V1
bE = beta*S*I/N-(mu+phi)*E
bI = phi*E-(mu+gamma+phi1)*I
bV1 = psi*S-(mu+omegav+kappa)*V1
bV2 = kappa*V1-(mu+omega)*V2
bR = gamma*I+omega*V2-mu*R
target = sp.simplify(bS+bE+bI+bV1+bV2+bR)
expected_target = Lam-mu*N-phi1*I
assert sp.simplify(target-expected_target) == 0
printed_I = bI-beta*S*I/N
assert sp.simplify(printed_I-bI + beta*S*I/N) == 0
printed_total = sp.simplify(bS+bE+printed_I+bV1+bV2+bR)
assert sp.simplify(printed_total-(expected_target-beta*S*I/N)) == 0
assert sp.simplify(printed_total-target + beta*S*I/N) == 0
assert -Fraction(1,20)*Fraction(1,1)*Fraction(1,1)/Fraction(2,1) == Fraction(-1,40)
print("VERIFY_OK")
