---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The attached standard-library verifier `verify_hs_identity.py` independently computes coefficient-square sums for normalized monomial bases and the closed-form multiplicity formula with exact rational arithmetic. Cases include \(n=2,3,4\), integral sample \(\alpha\) and \(\beta\), and degrees up to \(7\). It also checks the critical two-dimensional harmonic-number identity through degree \(21\). Success output is `BALL_CESARO_HS_IDENTITY_EXACT_OK`.

Analytical steps not verified by finite computation are the infinite sum rearrangement (Tonelli for nonnegative terms), the gamma-ratio three-regime asymptotics (dominated convergence, harmonic comparison, and an endpoint-controlled beta-integral Riemann sum), and the power-logarithmic moment asymptotic. They are proved in `RESULT.md`.

The criterion is exact for positive finite measures on the specified complex Bergman balls; it does not validate general complex measures, other Schatten ideals, or any unpublished equivalence. Same-model review passed; independent audit has not been performed.
