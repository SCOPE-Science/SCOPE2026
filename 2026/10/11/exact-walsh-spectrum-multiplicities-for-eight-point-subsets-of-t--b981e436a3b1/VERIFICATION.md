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

# Verification and limits

Run `python checker.py` using Python 3.10 or newer. All operations are exact integers, without numerical tolerances or random sampling. The checker reconstructs all \(12870\) eight-element masks, computes the fifteen nontrivial Walsh coefficients and all nonzero pairwise frequency differences, counts spectra by the direct orthogonality criterion, independently determines complementing translations, and validates the complete multiplicity profile and the ordered-pair count.

Observed result:

```text
CHECK_PASS: 12870 eight-point sets, spectral multiplicities 0:10080, 2:1920, 4:840, 256:30
CHECK_PASS: direct Walsh orthogonality, antiperiod formula, pair-incidence 14880
```

The proof in `RESULT.md` supplies the finite-dimensional classification and exact counts without reliance on a program. The checker is a reproduction of the same finite mathematical object, not independent expert certification. No claim is made for other ambient dimensions or non-Walsh orthogonal bases. Independent audit remains unperformed.
