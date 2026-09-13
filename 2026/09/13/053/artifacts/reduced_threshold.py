"""Threshold check for reduced S^2 problem (Hopf-invariant class).

Reduced equation (derived in DRAFT): -Delta_{S^2(1/2)} v + 2 v = nu v^3.
Eigenvalues of -Delta on S^2(1/2): 4k(k+1): 0,8,24,48,...
Linearized at constant v=c (nu c^2 = 2): -Delta - 4 on mean-zero.
Gap = 8-4 = 4 > 0. First bifurcation where coeff 2*mu coeff hits 8,
i.e. threshold constant 8 vs our 4. Confirm margin factor 2.
Also confirm anti-diagonal S1 gap from previous script (8 in CR units).
"""
eigs = [4*k*(k+1) for k in range(6)]
print("S^2(1/2) eigenvalues:", eigs)
coeff = 4.0
print("linearized shift:", coeff)
print("gap to first nonzero eig:", eigs[1]-coeff)
print("threshold ratio (eig1/coeff):", eigs[1]/coeff)
# perturbed Rossi: operators move O(|t|); bound operator shift <= C|t|
# with C ~ 8 (Levi/torsion coefficients bounded for |t|<=1/2).
# Gap persists while C|t| < gap -> |t| < 4/8 = 1/2. Consistent with delta<1/2.
C = 8.0
print("max |t| preserving positivity:", (eigs[1]-coeff)/C)
# IFT radius estimate: quadratic nonlinearity N(z)=6z^2+2z^3 (per unit vol).
# Lipschitz of DN on ball radius r: <= 12r+6r^2 (sup norm, H^2 algebra with
# Sobolev constant S for S^2(1/2), S~1). Inverse bound M=1/gap=1/4.
# Newton-Kantorovich radius r0 ~ 1/(2*M*L2) with L2=12 -> r0 ~ 1/6.
# Take conservative r0 = 0.05 in H^2. Uniform Schauder gives
# ||u - c|| <= K|t| trapping; choose delta = 1/10 safely inside.
M = 1/4
L2 = 12.0
print("IFT radius estimate:", 1/(2*M*L2))
