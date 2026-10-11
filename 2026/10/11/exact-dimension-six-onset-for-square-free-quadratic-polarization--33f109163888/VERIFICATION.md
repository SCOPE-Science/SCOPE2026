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

Execute `python CHECK.py` using Python 3 standard library. The checker constructs exact rational coefficient identities for all 5,456 pairs of sign vectors across dimensions 2, 3, 4, 5, and 6. For any symmetric zero-diagonal real matrix, each identity gives a signed linear combination of evaluations of its quadratic polynomial, with absolute coefficient sum at most 1 (dimensions 2–5) or 3/2 (dimension 6). Thus the finite vertex coefficient checks are symbolic and cover arbitrary real coefficients in these finite dimensions, not merely a sample of matrices. The checker also verifies the explicit triangle-block example has quadratic norm 8 and bilinear norm 12. A self-contained analytic derivation appears in RESULT.md.

The verified result does not include exact polarization constants in dimensions greater than six or complex scalar spaces. Literature equivalence remains a residual risk. Independent audit has not been performed.
