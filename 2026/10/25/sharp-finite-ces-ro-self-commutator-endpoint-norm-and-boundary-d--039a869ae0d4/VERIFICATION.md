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

# Reproducibility and verification

The exact symbolic calculations are reproduced by `cesaro_finite_commutator_check.py` using Python 3 and only the standard library. Its direct rational multiplication checks \(K_n\) and every row sum for \(2\le n\le24\), confirms the first row and sharp step extremizer, and verifies strict first-row uniqueness for \(3\le n\le24\). The script also performs numerical nonproof sanity checks at selected dimensions through \(n=50000\).

The output observed during preparation was:

```
PASS: exact matrices, first-row maximizers, step witnesses,
and finite numerical checks of two-term boundary asymptotics.
```

**Limits:** A finite checker cannot prove the all-dimensional identity, the uniqueness of the extremizing row at arbitrary dimension, or the asymptotic expansion. Those follow from the explicit sign-monotone kernel calculation, discrete row-sum comparison, and Euler--Maclaurin analysis contained in `RESULT.md`. The bibliographic originality comparison has the residual limitations recorded in `REVIEW.md`. Independent scientific audit was not performed.
