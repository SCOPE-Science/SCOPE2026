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

Unitary reflection splits H into an irreducible tridiagonal even block B_(m+1) and a real-symmetric odd path A_(m−1). Determinant recursion yields (z²+γ²−4)U_(m−1)(z/2)². The even tridiagonal eigenvector is determined by its first coordinate, so it has exactly one Jordan block at each eigenvalue. The simple U roots μ_j=2cos(πj/m) coincide with moving roots ±sqrt(4−γ²) precisely at specified subthreshold γ. At γ=2 both moving roots collide at zero with the odd path root iff m even. Jordan exponential establishes matching upper/lower norm powers. Independent exact symbolic characteristic-polynomial and γ=2 nullity calculations for m=2,…,7 corroborate, but the tridiagonal argument proves all m.

## originality

PASS

Qualified PASS for full Jordan and operator-growth classification, not for the known spectral polynomial or four-site EP3. Jin–Song exact moving/fixed eigenvalue description and Ortega et al.s singular-state work are especially close, but the relevant inspected primary formulas do not explicitly state the complete defect sizes and all-parity time-growth law. Generalized-eigenvector calculations in an earlier source could imply portions.

## value

PASS

Provides the crucial physically observable distinction between a real spectrum and a bounded propagator: subthreshold embedded Jordan defects cause linear amplification. The even/odd m jump at γ=2 supplies an exact design boundary for non-Hermitian lattice dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
