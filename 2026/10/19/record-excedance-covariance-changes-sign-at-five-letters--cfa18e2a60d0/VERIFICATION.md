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

`verify.py` is self-contained Python 3 code (standard library only). Run `python verify.py` to enumerate all permutations at orders two through eight and check the threshold covariance array by exact integer counts and `fractions.Fraction` arithmetic. The script verifies the local record–excedance covariance profile, aggregate reciprocal-binomial formula, recurrence through order 399, strict sign transition, and strict monotonicity for the displayed finite range. The expected result is `PASS: 2524 exact checks`.

The finite program does not certify the infinite family. The proof in RESULT.md establishes the unrestricted identities from conditional symmetry and binomial algebra. Historical literature inspections support a provisional originality comparison; they do not constitute independent scientific validation.
