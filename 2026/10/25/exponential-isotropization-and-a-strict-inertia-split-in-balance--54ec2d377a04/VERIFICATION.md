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
# Verification details

The seven-file record contains a standalone Python 3 program, `verify.py`, using no third-party packages. Running `python3 verify.py` produces:

```
VERIFY_OK exact_spectra=54 independent_polytope_integrals=6 seeded_mc=4 asymptotic_ratios=4
```

The exact beta-tail evaluation uses integer binomial sums. It checks the formula for both covariance eigenvalues and the exact positive gap for all 54 pairs with \(3\le r\le8\) and \(1\le m\le9\); the \(m=1\) check tests algebraic moments only because no within-block eigenspace then exists. Independently, direct rational polynomial integration over the truncated three-block simplex verifies the conditional second moment for each \(1\le m\le6\). Four seeded Dirichlet simulations provide numerical checks, and four large-parameter exact-rational comparisons test the announced Stirling coefficient.

All-dimensional correctness is supplied by the proof in `RESULT.md`, not by the finite checks or simulations. Publication overlap checks did not establish any external independent validation. The historical literature comparison is incomplete to the extent that equivalent formulas could appear under different probabilistic names.
