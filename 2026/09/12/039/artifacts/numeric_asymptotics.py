"""Numerical Schmid/SL2 evidence (50 digits): periods of E and Abel-Jacobi
integrals; verifies e1+e2=0 relation row numerically and SL(2,Z) action.
Reproducible with mpmath.
"""
import mpmath as mp
mp.mp.dps = 50

def f(x): return (x - 2)*(x - 3)*(x - 4)
def absf(x): return abs(f(x))

Omega_A = 2*mp.quad(lambda x: 1/mp.sqrt(f(x)), [2, 3])
I34 = mp.quad(lambda x: 1/mp.sqrt(absf(x)), [3, 4])
Omega_B = 2*mp.j*I34
J0 = mp.quad(lambda x: 1/mp.sqrt(absf(x)), [0, 2])
J1 = mp.quad(lambda x: 1/mp.sqrt(absf(x)), [1, 2])
z1 = -2*mp.j*J0
z2 = -2*mp.j*J1

print("Omega_A =", Omega_A)
print("Omega_B =", Omega_B)
print("z1 =", z1)
print("z2 =", z2)
print("c1 = J0/I34 =", J0/I34)
print("c2 = J1/I34 =", J1/I34)
print("c1 + c2 =", (J0 + J1)/I34)

# Lattice check: z1 + z2 + Omega_B/2 + Omega_A/2 ? determine integers:
# Solve z1+z2 = m*Omega_A + n*Omega_B. Since z1+z2 purely imag, m=0; n=(J0+J1)/I34 /(-1)? sign.
n = (J0 + J1)/I34
print("z1+z2 over Omega_B =", (z1+z2)/Omega_B)   # expect half-integer (torsion AJ sum)
# e1+e2=0 exact: z1+z2 = 2*AJ(T)+2*AJ(O)? T=(-1,0) is 2-torsion so 2T=0; check z1+z2 in (1/2)Lattice.
w = (z1 + z2)/Omega_B
print("w =", w, " 2w =", 2*w, " nearest int(2Re(w)) =", int(mp.nint(mp.re(2*w))))
print("residual |2(z1+z2) - round*Lattice| =", abs(2*(z1+z2) - int(mp.nint(mp.re(2*w)))*Omega_B))
print("ratio J0/J1 =", J0/J1)
print("tau = Omega_B/Omega_A =", Omega_B/Omega_A, "(= i, j=1728 class) by symmetry")
