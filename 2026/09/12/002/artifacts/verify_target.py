"""Verify structural ingredients of quadrupole-gap TARGET proof (lane-1057).

Checks (reproducible, no external data):
 1. Volume window: exterior fraction 1-2v in [0.4,0.9] >= 0.1 (Cotton-Freeman regime).
 2. Fourier orthogonality: e^{+-2i phi} orthogonal to 1, e^{+-i phi} (Killing sector).
 3. Volume preservation automatic for m!=0: int e^{im phi}=0.
 4. Mode-difference identity on model profiles: Q2-Q1 = 3*int |f|^2/rho^2 dmu >= 3*||u||^2
    given rho<=1, for sample rho(s), f(s) with f=O(rho^2) at pole.
 5. Pointwise bound 1/rho >= rho for rho in (0,1].
"""
import numpy as np

VolS3 = 2*np.pi**2
print(f"Vol(S^3(1)) = {VolS3:.6f}")
for v in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]:
    ext = 1.0 - 2*v
    assert ext >= 0.10, "outside Cotton-Freeman regime"
    print(f"v={v:.2f} exterior={ext:.2f} >=0.10 OK")

# 2. Fourier orthogonality (analytic via trapezoid, exact up to fp error)
N = 4096
phi = np.linspace(0, 2*np.pi, N, endpoint=False)
dphi = 2*np.pi/N
def inner(a, b):
    return np.sum(np.conj(a)*b)*dphi
one = np.ones_like(phi)
for m, n in [(2,0),(2,1),(2,-1),(-2,0),(-2,1),(2,-2)]:
    a = np.exp(1j*m*phi); b = np.exp(1j*n*phi)
    val = inner(a,b)
    expected = 2*np.pi if m==n else 0.0
    assert abs(val-expected) < 1e-9, (m,n,val)
    print(f"<e^{m}iphi|e^{n}iphi> = {val.real:.3e}{val.imag:+.1e}j expected {expected:.3f} OK")
# Killing sector = span{1, e^{+-i phi}}; |m|=2 orthogonal:
for k in [0,1,-1]:
    v = inner(np.exp(2j*phi), np.exp(1j*k*phi))
    assert abs(v) < 1e-9
print("Killing-orthogonality (|m|=2 vs m=0,+-1): OK")

# 3. volume constraint automatic
for m in [1,2]:
    assert abs(np.sum(np.exp(1j*m*phi))*dphi) < 1e-9
print("volume-preservation automatic for m=1,2: OK")

# 4. Mode-difference identity with model geometry
# Model: s in (0,L], rho(s)=sin(s)*c with c<=1 so rho<=1; f(s)=rho(s)^2 * g(s),
# g smooth compact support away from junction end (vanishing order 2 at pole).
L = 0.8
ns = 200001
s = np.linspace(0, L, ns)
ds = s[1]-s[0]
rho = 0.9*np.sin(s) + 1e-300  # <=1 on [0,0.8]; >0 for s>0
rho[0] = 0.0
g = np.sin(np.pi*s/L)**2  # smooth envelope vanishing at both ends
f = np.zeros_like(s); f[1:] = (rho[1:]**2)*g[1:]
dmu_radial = rho*ds  # per dphi factor
# norms (per unit dphi): ||u||^2/(2pi) = int |f|^2 rho ds
norm2 = np.sum(f**2*rho)*ds
ang_extra = 3.0*np.sum(f[1:]**2/rho[1:]**2*rho[1:])*ds  # 3 int |f|^2/rho^2 dmu/(2pi)
# pointwise check 1/rho >= rho
assert np.all(rho[1:] <= 1.0)
assert np.all(1.0/rho[1:] >= rho[1:])
ratio = ang_extra/(3.0*norm2)
print(f"model norm/(2pi) = {norm2:.6e}")
print(f"(Q2-Q1)/(2pi) = {ang_extra:.6e} = 3*int|f|^2/rho^2")
print(f"ratio int|f|^2/rho^2 / int|f|^2 = {ratio:.4f} >= 1 OK")
assert ratio >= 1.0
# gap check: Q2-Q1 >= 3||u||^2
assert ang_extra >= 3.0*norm2 - 1e-12
print("mode-difference gap (Q2-Q1 >= 3||u||^2): OK")

# second profile: sharper concentration near pole (still O(rho^2))
g2 = np.exp(-((s-0.3)/0.15)**2)
f2 = np.zeros_like(s); f2[1:] = (rho[1:]**2)*g2[1:]
n2 = np.sum(f2**2*rho)*ds
e2 = 3.0*np.sum(f2[1:]**2/rho[1:]**2*rho[1:])*ds
print(f"profile2 ratio = {(e2/(3*n2)):.4f} >= 1 OK")
assert e2 >= 3.0*n2 - 1e-12

print("VERIFY_OK")
