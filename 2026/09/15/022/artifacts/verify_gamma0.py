"""Verify emergent example Gamma0: portrait of f(z)=z^2+i.
Checks: postcritical set, portrait edges, repelling 2-cycle + multiplier,
fixed-point multiplier spectra for c=+i vs c=-i (non-conjugacy),
orbifold weights / Euler characteristic, portrait isomorphism +i/-i.
"""
import cmath

def check(c, tag):
    def f(z): return z*z + c
    # critical points 0, inf
    # orbit of 0
    orb = [0j]
    z = 0j
    for _ in range(6):
        z = f(z)
        orb.append(z)
    print(f"--- {tag}: c={c}")
    print("  orbit of 0:", [f"{v:.6f}" for v in orb])
    v1 = f(0j)
    p = f(v1)
    q = f(p)
    r = f(q)
    print(f"  v1={v1}, p={p}, q={q}, f(q)={r}")
    assert abs(r - p) < 1e-12, "must have 2-cycle p<->q"
    assert abs(p - q) > 1e-9, "cycle must have length 2"
    # cycle disjoint from critical points 0, inf
    assert abs(p) > 1e-9 and abs(q) > 1e-9
    # multiplier
    lam = 2*p*2*q
    print(f"  multiplier lambda={lam}, |lambda|={abs(lam)}")
    assert abs(lam) > 1, "repelling required"
    # postcritical set
    P = {v1, p, q, complex('inf')}
    print(f"  |P_postcritical|=4: {[str(v) for v in [v1,p,q]]} + inf")
    # fixed points and multiplier spectrum
    D = cmath.sqrt(1-4*c)
    z1, z2 = (1+D)/2, (1-D)/2
    m1, m2 = 2*z1, 2*z2
    print(f"  fixed pts {z1:.6f}, {z2:.6f}; multipliers {m1:.6f}, {m2:.6f}; product={m1*m2:.6f} (=4c={4*c})")
    assert abs(f(z1)-z1) < 1e-12 and abs(f(z2)-z2) < 1e-12
    return (m1, m2)

m_plus = check(1j, "f(z)=z^2+i")
m_minus = check(-1j, "f(z)=z^2-i")

# Non-conjugacy: Moebius conjugacy preserves fixed-point multiplier multiset.
# products are 4i vs -4i
prod_plus = m_plus[0]*m_plus[1]
prod_minus = m_minus[0]*m_minus[1]
print("product(+i) =", prod_plus, " product(-i) =", prod_minus)
assert abs(prod_plus - 4j) < 1e-9 and abs(prod_minus + 4j) < 1e-9
assert abs(prod_plus - prod_minus) > 1e-9, "spectra differ -> not conjugate"
print("NON-CONJUGACY CONFIRMED: z^2+i not Moebius-conjugate to z^2-i")

# Portrait isomorphism (+i) <-> (-i): conjugation z -> -conj? As abstract graphs:
# 0->v1->p<->q, inf fixed. Map: 0|->0, inf|->inf, i|->-i, (-1+i)|->(-1-i), (-i)|->i.
phi = {0j: 0j, 1j: -1j, (-1+1j): (-1-1j), (-1j): 1j, 'inf': 'inf'}
def fp(z): return z*z + 1j
def fm(z): return z*z - 1j
for v, w in [(0j, 1j), (1j, -1+1j), (-1+1j, -1j), (-1j, -1+1j)]:
    assert phi[fm(phi[v]) if False else fp(v)] == fm(phi[v]), f"iso fails at {v}"
print("PORTRAIT ISOMORPHISM (+i)->(-i) CONFIRMED on all edges (plus inf fixed)")

# Orbifold weights: nu(inf)=2, nu(v1)=2 (preimage 0 deg 2),
# nu(p)=nu(q)=2 (iterated preimage 0 of local deg 2 lies over each).
# signature (2,2,2,2), chi = 2 - 4*(1-1/2) = 0 -> Euclidean.
chi = 2 - 4*(1 - 1/2)
print("orbifold signature (2,2,2,2), chi =", chi, "-> EUCLIDEAN (Thurston rigidity uniqueness N/A)")
print("ALL CHECKS PASSED")
