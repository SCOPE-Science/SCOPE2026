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

# Verification

The proof establishes every universal assertion algebraically. A reproducibility program `eksm_step3_check.py` uses Python 3 with NumPy and SymPy. Execute from a directory containing the included program:

```sh
python eksm_step3_check.py
```

The program was actually run and reported:

```text
PASS: rational full-rank premature breakdown, exact residual, two sign reversals
PASS: symbolic one-parameter singular asymptotic coefficient
PASS: 3600 independent random 3/4/6-dimensional projection comparisons
```

Its exact arithmetic verifies the determinant, inverse-Rayleigh cancellation, second normalized residual, contrasting starting-vector moments, and the perturbation coefficient. The randomized comparison constructs Euclidean projectors afresh, checking the candidate-ratio formula against independent Gram–Schmidt-style calculations for definite, indefinite, and nonsymmetric invertible matrices. Random cases cannot certify an all-matrix theorem. All universal assumptions are stated in the proof: real invertible matrices, unit initial vector, nonzero second inverse residual, and an independent split-channel third candidate.

The classical publisher abstracts were not substituted for inspection of their full texts, and no independent assessment has been performed.
