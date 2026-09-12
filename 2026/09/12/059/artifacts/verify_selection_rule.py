"""Verify reflection selection-rule obstruction for two-input sphere system.
r: (x,y,z) -> (x,-y,z), i.e. phi -> -phi. Potentials V1=z=cos t, V2=x=sin t cos p even.
Target odd mode eta ~ y = sin t sin p is odd. Checks:
 (1) pointwise even/odd symmetries of x,y,z on grid
 (2) L2 norms and orthogonality <c0,eta>=0 by quadrature
 (3) H3 closeness of normalized targets psi_f to c0
 (4) L2 lower bound dist(even subspace, psi_f) = eps/sqrt(1+eps^2)
"""
import numpy as np

# Gauss-Legendre in cos(theta) x uniform phi
Nt, Np = 200, 256
zs, wz = np.polynomial.legendre.leggauss(Nt)  # zs=cos theta in (-1,1)
th = np.arccos(zs)
ph = np.linspace(0, 2*np.pi, Np, endpoint=False)
dph = 2*np.pi/Np
TH, PH = np.meshgrid(th, ph, indexing='ij')  # (Nt,Np)
W = wz[:, None] * np.ones_like(PH) * dph     # dOmega = d(cos t) dphi with weights

x = np.sin(TH)*np.cos(PH)
y = np.sin(TH)*np.sin(PH)
z = np.cos(TH)

# (1) reflection phi -> -phi  == y -> -y ; check x,z even, y odd
x_refl = np.sin(TH)*np.cos(-PH)
y_refl = np.sin(TH)*np.sin(-PH)
z_refl = np.cos(TH)
assert np.max(np.abs(x_refl - x)) == 0.0
assert np.max(np.abs(z_refl - z)) == 0.0
assert np.max(np.abs(y_refl + y)) == 0.0
print("symmetry pointwise: x even OK, z even OK, y odd OK")

def ip(f, g):
    return np.sum(np.conj(f)*g*W)

# (2) norms
c0 = (4*np.pi)**(-0.5) * np.ones_like(x)
eta = np.sqrt(3/(4*np.pi))*y
n_c0 = np.sqrt(ip(c0,c0).real)
n_eta = np.sqrt(ip(eta,eta).real)
n_x = np.sqrt(ip(x,x).real); n_z = np.sqrt(ip(z,z).real)
cross = ip(c0, eta)
print(f"||c0||={n_c0:.10f} (expect 1)")
print(f"||eta||={n_eta:.10f} (expect 1)")
print(f"||x||^2={n_x**2:.10f} (expect {4*np.pi/3:.10f}), ||z||^2={n_z**2:.10f}")
print(f"<c0,eta>={cross:.3e} (expect 0)")
assert abs(n_c0-1) < 1e-9 and abs(n_eta-1) < 1e-9 and abs(cross) < 1e-9

# (3)+(4): normalized odd-containing targets
lam0, lam1 = 1.0, (1+2)**1.5  # (1+l(l+1))^{3/2} for l=0,1 : 1 and 3*sqrt(3)
for eps in [0.5, 0.1, 0.01]:
    N = np.sqrt(1+eps**2)
    psi_f = (c0 + eps*eta)/N
    assert abs(np.sqrt(ip(psi_f,psi_f).real)-1) < 1e-9
    # H3 distance squared = |1/N-1|^2*lam0^2*||c0||^2 + (eps/N)^2*lam1^2*||eta||^2
    h3 = np.sqrt((1/N-1)**2 * lam0**2 + (eps/N)**2 * lam1**2)
    odd_norm = eps/N  # exact L2 norm of odd part
    # numeric odd part check
    odd = eps*eta/N
    assert abs(np.sqrt(ip(odd,odd).real)-odd_norm) < 1e-9
    print(f"eps={eps}: N={N:.8f}, H3 dist={h3:.8f}, L2-odd lower bound={odd_norm:.8f}")
    # crude analytic bound (1/2+3sqrt3)*eps for eps<=1
    assert h3 <= (0.5+3*np.sqrt(3))*eps + 1e-12

print(" quantitative bound: ||psi_f-c0||_H3 <= 6*eps for eps<=1  =>  H3-dense as eps->0")
print("ALL CHECKS PASSED")
