---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

A_n and C_n have dimensions 4n-3 and 4n-4. The type-A Weyl numerator for weight omega1+omega2 has 2^(2n-2) over positive-root denominators (2n-1)!(2n-2)!, yielding the displayed ordinary degree. Type-C complement to Levi C_(n-2) has 4n-4 positive roots and numerator 3*2^(2n-3) over (2n-1)!(2n-3)!, giving isotropic degree. Schubert-cell W/W_P gives 2n(2n-1) and 4n(n-1) Euler counts. Exact algebra gives the two ratios, and q_n-q_(n+1)=3/[(4n-3)(4n+1)]>0. Independently checked n=2..9 with exact rational arithmetic; source nested verifier checks n=2..100.

## originality

PASS

Both degrees and Euler counts follow known general Weyl/Schubert mechanisms; their explicit comparison for the natural isotropic inclusion and identical Segre–Plücker polarization, including the sharp monotone normalized suppression, was not found in inspected geometric literature. Best-of-knowledge novelty is restricted to this specialized geometric comparison, not the standard formulas.

## value

PASS

The natural codimension-one inclusion of symplectic isotropic flags into ordinary line–plane flags provides genuine geometric motivation for comparing degree and Euler characteristic under the same polarization. The exact competing suppression factors and their monotone sharp 3/4 normalized limit quantify distinct global invariants of this inclusion, rather than an arbitrarily selected polynomial value. The general computational tools themselves remain classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
