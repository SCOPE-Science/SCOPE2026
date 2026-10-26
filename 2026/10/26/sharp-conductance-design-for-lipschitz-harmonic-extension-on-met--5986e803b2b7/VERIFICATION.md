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

# Reproducibility and mathematical verification

Run `python checker.py` from the directory containing the files. The script requires only Python 3 standard libraries and uses exact `fractions.Fraction` values for its principal tests.

The routine `independent_vertex_lp` constructs the **original** finite linear program: minimize the norm bound subject to the positive center weights summing to one and each arm's sharp Lipschitz bound. It enumerates independent active-constraint systems, performs exact rational elimination, and compares their feasible minima with the separate water-filling formula. This yields 42 rational minimax comparisons for three to five arms, followed by eight equal-arm checks and 35 one-short-arm phase-law checks.

Expected output:

```
PASS: 42 exact-rational minimax vs independent LP vertex enumerations
PASS: eight equilateral arm-count cases and 35 sharp phase-law cases
```

The code checks finitely many parameter choices and cannot prove universal correctness or novelty. The complete finite-candidate reduction and attainability classification rest on the arguments in `RESULT.md`. No independent audit has been performed.
