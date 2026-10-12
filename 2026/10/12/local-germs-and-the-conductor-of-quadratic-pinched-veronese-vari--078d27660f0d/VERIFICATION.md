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

## Reproducibility

Execute `python checker.py` with Python 3 (no external dependencies) and compare its output to `checker_output.txt`. The code enumerates affine semigroup monomials and checks the local associated-graded dimensions for \(2\le n\le6\) through order \(4\), defining binomial identities, and low-degree homogeneous normalization defects. The tested boundary \(n=2\) is not part of the new-dimensional claim.

## Verification limits

The computer checks are exact but finite. The arbitrary-dimensional affine-ring presentation, scheme-theoretic conductor, fiber-product local form, local-filtration count and depth conclusion follow from the proof in `RESULT.md`. Computer output alone is not an infinite proof. The original text of Schenzel (1978) was not accessible during the primary-literature comparison. Independent audit has not been performed.
