---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Two-stage order-three Radau IIA has rational stability map R(z)=(6+2z)/(6-4z+z²). For Q_n=S_n-I, denominator invertible on CTMC spectrum and R(hQ_n) has row sums 1. Taylor R(z)=1+z+z²/2+z³/6+z⁴/36-z⁵/108+O(z^6); for n<=5 any generator reachable off-diagonal minimal path length <=4 yields local positivity, whereas n>=6 directed cycles have length-5 target with negative leading coefficient. Exact modular inversion modulo S^n=1 of the rational matrix coefficients, supported by explicit all-polynomial certificates for n2..6, shows all entries strictly positive n2..5 for all h>0. n6 only exceptional coefficient is h^5 q(h) where q=h^5+15h^4+60h^3+90h²+36h−12, with strictly positive q derivative, unique root rho~0.208608859735; other coefficient numerators and denominator positive, including diagonal via two interval arguments. At h0 the identity is nonnegative. Fourier diagonalization yields positive rank-one limit at large h for any n. Fresh independent rational matrix evaluations for n2..6 and Taylor/root checks agreed; source SymPy modular inversion code checks full identities, not simply sampled logs.

## originality

PASS

Earlier diagonal Padé positivity theory (Zappavigna et al), scalar absolute-monotonicity radius (Lóczi–Ketcheson), and a published 8-state [2/2] Gauss-Padé Markov failure are distinct. This precise [1/2] Radau directed-cycle n6 recovery quintic and n<=5 all-step classification were not identified in primary material read. Specialized older RK positivity examples could still be present, so best-of-knowledge qualifier.

## value

PASS

Exact dimension and timestep boundaries for endpoint Markov positivity in an L-stable high-order integrator are natural numerical analysis invariants; the small-step loss followed by large-step recovery illustrates a practically significant nonmonotonic positivity phenomenon with a reproducible algebraic certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
