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
# Reproducibility

Run `python CHECK.py` using Python 3.11+ standard library. The code reconstructs the first-return formal series with exact rational coefficients, directly enumerates all invertible 1–4 square matrices over the binary field and 1–3 square matrices over the ternary field, checks all predicted histograms, and exhaustively verifies conditional rank-transition frequencies over three independent small cases. It additionally tests positivity and records numerical values of four q-series variance constants with 65-decimal-digit arithmetic.

The computation was executed on the packaged source and finished with:

`VERIFY_OK matrix_distributions=7 rank_transitions=3 exact_renewal_identity=PASS positive_variances=4`

These tests do not exhaustively certify all dimensions or establish a central limit. The proof in `RESULT.md` supplies the infinite nullity-chain reduction, geometric drift, coefficient extraction, analytic-pole asymptotics, and variance identification. No external independent audit has been conducted.
