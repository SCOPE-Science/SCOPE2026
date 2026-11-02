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

# Reproducibility

Execute `python verify.py` in the directory containing the attached standalone program, using Python 3 standard library only. The program independently constructs adjacency for each crown graph and checks the defensive inequality for each selected vertex, local deletion minimality, and the absence of **all** nonempty proper defensive subsets for global minimality. It compares exact coefficient dictionaries, overlap classes, local-only differences, and parity formulas for \(3\le n\le10\).

Observed result:

```
VERIFY_OK graph_orders=8 tested_nonempty_subsets=1398072 all_formulas_agree=true
```

The finite tests do not establish the all-parameter theorem. That rests on the explicit algebraic characterization and bijective counting proof in RESULT.md. No external or independent validation has been performed, and the arithmetic asymptotic expansion is derived using Stirling's formula, not a numerical fit.
