---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

All roots have orders r satisfying r/gcd(r,d^n)=m. Primitive order-r roots above alpha form a single Gal(Q(zeta_r)/Q(alpha)) orbit of size phi(r)/phi(m); Gal(KQ(zeta_r)/K) acts freely, so its orbit count is exactly [K intersect Q(zeta_r):Q(alpha)]. Kronecker–Weber gives a finite conductor C for E=K intersect Q^cyc, and cyclotomic intersection Q(zeta_C) intersect Q(zeta_r)=Q(zeta_gcd(C,r)) caps prime exponents. Summing stabilized coordinate intervals yields an exact finite polynomial, with positive highest-degree coefficient [H:F] product b_p; Euler totient sums yield the cyclotomic product. Independent Galois-orbit enumeration matched all 160 small cases (m=1..5, cyclotomic M, d=2,3,4,6 and n=1,2). Infinite claim rests on Galois and conductor arguments, not finite tests.

## originality

PASS

Tucker–Zhu 2026 Theorem 2.1(iii) already gives the root-order parametrization and the exact factor count over F=Q(alpha), with general-K degree bounds. The present field-intersection orbit formula, invariance under cyclotomic intersection and eventual exact polynomial sharpen those bounds. Jones–Levy 2017 establishes eventual-stability framework but not this explicit all-K count in accessed descriptions. Original Tucker–Zhu full arXiv HTML unavailable, and an authorized full-text retrieval attempt returned vpn_disconnected; this is substantive priority risk, but no accessible statement establishes a stronger general-K formula.

## value

PASS

The published sharp question concerns factor counts of monomial preimages across arbitrary number fields; the exact abelian-intersection dependency, eventual polynomial degree, leading constant and non-primewise quadratic examples are substantive structural refinements of stated degree bounds, useful to dynamical Galois theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
