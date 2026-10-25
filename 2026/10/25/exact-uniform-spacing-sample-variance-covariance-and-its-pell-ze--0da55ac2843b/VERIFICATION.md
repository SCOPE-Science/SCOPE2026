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

The `verify.py` program uses only the Python standard library and exact rational arithmetic. To run from this directory, execute `python verify.py`.

It checks every rank in samples of sizes \(2\) through \(18\) using a direct factorial-multiplicity expansion of Dirichlet monomials in the pairwise squared-distance representation of unbiased sample variance. This is computationally independent of the conditional overlap simplification in the proof. It also checks the covariance sum across every full spacing vector, the numerator's sign for every tested rank, the closed Pell recurrence through twelve nonnegative powers, and the complete set of zero numerator ranks for \(2\le n\le 2000\).

Actual execution of the packaged source prints:

```
PASS: 2402 exact-arithmetic checks including full-gap direct moments, symmetry, and Pell zero ranks
```

The analytic argument in `RESULT.md` proves the claims for every allowed sample size. Exhaustive finite checks do not certify an infinite claim or establish historical originality. No independent audit has been performed.
