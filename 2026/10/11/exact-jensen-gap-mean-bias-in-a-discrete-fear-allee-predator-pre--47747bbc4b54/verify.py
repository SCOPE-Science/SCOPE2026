#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp

N, theta, m, f, h, eps, Jp, Jn, barN, barP, Q = sp.symbols(
    "N theta m f h eps Jp Jn barN barP Q", positive=True
)

# Positive equilibrium algebra.
gm = (1-m)*(m-theta)
Pstar = (-1 + sp.sqrt(1 + 4*f*gm))/(2*f)
assert sp.simplify(Pstar*(1+f*Pstar)-gm) == 0

# Predator-growth Jensen-gap rearrangement.
expr = sp.solve(sp.Eq(sp.exp(Jp), 1+h*(barN-m)), barN)[0]
assert sp.simplify(expr - (m + (sp.exp(Jp)-1)/h)) == 0

# Prey-growth Jensen-gap rearrangement. Q denotes E[g(N)/(1+fP)].
sol = sp.solve(sp.Eq(sp.exp(Jn), 1 + h/eps*(Q-barP)), barP)[0]
assert sp.simplify(sol - (Q - eps/h*(sp.exp(Jn)-1))) == 0

# Completed square controlling the predator mean.
g = (1-N)*(N-theta)
gmax = (1-theta)**2/4
center = (1+theta)/2
assert sp.expand(g - (gmax-(N-center)**2)) == 0

# Source specializations.
ceil1 = (Fraction(1,1)-Fraction(1,10))**2/Fraction(4,1)
ceil2 = (Fraction(1,1)-Fraction(61,100))**2/Fraction(4,1)
assert ceil1 == Fraction(81,400)          # 0.2025
assert ceil2 == Fraction(1521,40000)      # 0.038025
assert float(ceil1) == 0.2025
assert float(ceil2) == 0.038025

print("VERIFY_OK")
