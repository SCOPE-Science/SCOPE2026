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

# Reproducibility and checks

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy; the expected output on successful replay is:

```
PASS: 3342 checks; exact spectral identity, KKT, asymmetric feasible comparisons, price bounds and four asymptotic regimes.
```

The program checks the centered-cut inverse-square trace by exact rational matrix identities on stars with three to seven leaves; verifies modal eigenvalue sums against explicit weighted Laplacian eigenspectra; checks the one-premium-edge cubic and its KKT conditions across several dimensions and price ratios; compares the candidate allocation against thousands of nonuniform feasible alternatives; checks arbitrary positive price vectors with numerical constrained optimizers; and tests fixed-price, high-price, budget-share and conductance-ratio limits at finite sizes.

The exact rational tests cover finitely many parameter combinations. Floating-point optimizer success is diagnostic, not certification of a global mathematical optimum, and limiting numerical tests cannot prove an asymptotic statement. The unrestricted uniqueness, strict price sandwich, and all-limit claims rely on the analytic proof in `RESULT.md`. This is not an independently performed audit.
