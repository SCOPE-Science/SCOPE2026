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

# Reproducibility and limits

Run `python3 verify.py` using the extracted, embedded files. The verifier uses only the standard Python library. It checks 175 exact-rational characteristic-polynomial identities for explicit one- and two-splitting-coordinate Hermitian matrices, 24 radial quadrature ratios against the three asymptotic moment regimes (six splitting dimensions and four moment orders), three exact-rational sample-variance identities, and additional comparisons of the one-dimensional variance and fourth-moment constants. A successful run prints `PASS`. The general mathematical proof is in `RESULT.md`; the finite tests do not prove limits as the scale tends to zero or rule out earlier equivalent theorems.

The published sources support the motivation and comparison, not authorship or independent validation of this theorem. Source publication dates and scope are documented in `RESULT.md`. Scientific limitations: local additive-gap Hermitian Clifford model; fixed interlevel contraction; bounded density continuous and positive at the degeneracy; common random input across levels. No external independent audit or certification was performed.
