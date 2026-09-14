"""Verify the elementary bounds behind the disproof of the two-box merger claim.

Checks:
 1. C = int x^{-2} dmu = 1/2 (analytic + numeric quadrature).
 2. For sample (t,v): v/(4+v^2) <= A(v) <= v/2 where A(v)=Im-corrected
    Stieltjes moment A(v) = int v/(x^2+v^2) dmu.
 3. Sign thresholds: f(v)=t*v-(t-1)/A(v) is <0 below sqrt(2(t-1)/t)
    and >0 above 2*sqrt(t-1).
 4. Numeric subordination solve at z=i*eta confirms omega on imaginary
    axis with v(eta) in [m,M] and limiting density A(v*)/pi > 0.
"""
import mpmath as mp

mp.mp.dps = 40

DMU_DENSITY = mp.mpf('0.5')

def A_quad(v):
    f = lambda x: v / (x**2 + v**2)
    return DMU_DENSITY * mp.quad(f, [-2, -1]) + DMU_DENSITY * mp.quad(f, [1, 2])

def G_imag_axis(v):
    # G_mu(i v) = -i A(v); return A(v) via direct quadrature of Stieltjes
    w = 1j * v
    f = lambda x: 1 / (w - x)
    G = DMU_DENSITY * mp.quad(f, [-2, -1]) + DMU_DENSITY * mp.quad(f, [1, 2])
    assert abs(mp.re(G)) < 1e-25, f"Re G(iv) should vanish, got {G}"
    return -mp.im(G)

def F_of_iv(v):
    return 1 / G_imag_axis(v)  # = 1/A(v) times i; magnitude only

print("== 1. constant C = int x^-2 dmu ==")
C_num = DMU_DENSITY * mp.quad(lambda x: x**-2, [-2, -1]) + DMU_DENSITY * mp.quad(lambda x: x**-2, [1, 2])
print(" numeric C =", C_num, "(expect 0.5)")
assert abs(C_num - mp.mpf('0.5')) < mp.mpf('1e-25')

print("== 2./3. A-bounds and f-sign thresholds ==")
for t in ['1.01', '1.1', '1.27432', '1.5', '2', '5']:
    t = mp.mpf(t)
    m = mp.sqrt(2 * (t - 1) / t)
    M0 = 2 * mp.sqrt(t - 1)
    # test just below m and just above M0
    for v, expect in [(m * mp.mpf('0.999'), -1), (M0 + mp.mpf('0.001'), +1)]:
        A = A_quad(v)
        lo = v / (4 + v**2)
        hi = v / 2
        assert lo - mp.mpf('1e-30') <= A <= hi + mp.mpf('1e-30'), (t, v, A, lo, hi)
        f = t * v - (t - 1) / A
        print(f" t={float(t)} v={float(v):.6f} A={float(A):.6f} in [{float(lo):.6f},{float(hi):.6f}] f={float(f):.6f} expect {expect:+d}")
        assert (f < 0) if expect < 0 else (f > 0)
    # cross-check quadrature vs Stieltjes imaginary part
    for v in [mp.mpf('0.3'), m, M0 + 1]:
        assert abs(A_quad(v) - G_imag_axis(v)) < mp.mpf('1e-20')

print("== 4. subordination spot-check ==")

def Gc(w):
    f = lambda x: 1 / (w - x)
    return DMU_DENSITY * mp.quad(f, [-2, -1]) + DMU_DENSITY * mp.quad(f, [1, 2])

def omega_of_z(z, t, n=4000):
    w = z
    for _ in range(n):
        w = (z + (t - 1) / Gc(w)) / t
    return w

for t in [mp.mpf('1.05'), mp.mpf('1.2'), mp.mpf('2.0')]:
    eta = mp.mpf('1e-4')
    w = omega_of_z(1j * eta, t)
    assert abs(mp.re(w)) < mp.mpf('1e-3'), (t, w)
    v = mp.im(w)
    m = mp.sqrt(2 * (t - 1) / t)
    M = (1 + mp.sqrt(1 + 16 * (t - 1))) / 2
    print(f" t={float(t)} omega(i eta)={w} v in [{float(m):.4f},{float(M):.4f}]?")
    assert m * mp.mpf('0.99') <= v <= M * mp.mpf('1.01')
    dens = -mp.im(Gc(w)) / mp.pi
    print(f"   approx density at 0: {float(dens):.5f} > 0")
    assert dens > mp.mpf('0.01')

print("ALL CHECKS PASSED")
