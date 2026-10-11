import sympy as s

n,p,alpha,h1,n0,kappa,sigma,E,bn,bn2,var = s.symbols(
    "n p alpha h1 n0 kappa sigma E bn bn2 var", positive=True
)

G = (1+alpha*p)*n/(1+h1*(1+alpha*p)*n)
prey_loss = n*(1+alpha*p)*p/(1+h1*(1+alpha*p)*n)
assert s.simplify(prey_loss-G*p) == 0

# E denotes exp(beta*tau) > 0. Integrated predator balance is avg(Gp)=E*bp.
bp = s.symbols("bp", positive=True)
from_prey = s.simplify((sigma*bn-sigma*bn2/kappa)/E)
expected = sigma/E*(bn-bn2/kappa)
assert s.simplify(from_prey-expected) == 0
assert s.simplify(expected.subs(bn2, bn**2+var) - sigma/E*(bn*(1-bn/kappa)-var/kappa)) == 0

Phi = p*(1+alpha*p)/(1+h1*n0*(1+alpha*p))
dPhi = s.factor(s.diff(Phi,p))
num = s.factor(s.together(dPhi).as_numer_denom()[0])
expected_num = (1+h1*n0)*(1+2*alpha*p)+h1*n0*alpha**2*p**2
assert s.expand(num-expected_num) == 0

handling_gap = s.simplify(1/h1-G)
assert s.simplify(handling_gap - 1/(h1*(1+h1*(1+alpha*p)*n))) == 0

# Logistic parabola identity giving the universal ceiling.
x = s.symbols("x", real=True)
assert s.expand(kappa/4 - x*(1-x/kappa) - (x-kappa/2)**2/kappa) == 0

print("VERIFY_OK")
