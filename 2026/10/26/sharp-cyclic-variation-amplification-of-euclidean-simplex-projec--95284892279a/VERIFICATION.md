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

# Reproducibility and proof boundary

Run `python3 checker.py` with standard Python 3; no third-party package is required. The exact-rational checker enumerates all nonempty active sets and proper cyclic intervals for dimensions \(2\) through \(10\), tests the attained pair from each dimension, and verifies additional rational inputs and one-input contractions.

Observed output:

```text
PASS: exhaustive selector/interval cases 115226
PASS: attaining data pairs n=2..10 (9 dimensions)
PASS: random exact-rational input pairs 2280
PASS: one-input variation inequality 2280
```

These checks are finite. The infinite-dimensional-parameter claim (all finite integers \(n\ge2\)) follows from the analytic cyclic-interval decomposition, separator inequality, integer maximization and explicit witnesses detailed in `RESULT.md`. This verification is not an independent audit.
