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

# Reproducibility and exact scope

Run `python3 verify_periods.py` from the directory containing the file. Standard-library `fractions.Fraction` represents every coefficient, intermediate row operation, polyhedral inequality and orbit coordinate exactly.

For proposed lengths \(1\) through \(11\), enumerate every binary sign word; solve the affine periodicity equations over rationals. Empty systems are discarded. For singular systems, apply exact Fourier–Motzkin elimination to the non-strict sign inequalities in the free rational variables, proving existence or absence of **real** solutions. Zero coordinates are allowed for either sign. For nonsingular systems, the unique rational point is checked directly and deduplicated under cyclic orbit rotation. Minimal periods are computed by divisibility and direct state equality, not inferred from word lengths. At length \(6\), feasible singular sign words are detected, but an exhaustive classification of their solution components is **not** asserted.

Checker summaries (length, feasible words, feasible singular words, isolated primitive cycles):

```
1: 1,0,1
2: 1,0,0
3: 1,0,0
4: 1,0,0
5: 11,0,2
6: 13,7,1
7: 1,0,0
8: 1,0,0
9: 1,0,0
10: 11,0,0
11: 23,0,2
```

Actual output is archived in `certificate_output.txt`. The four isolated length-five/eleven representatives were independently iterated as rational states, and the Jacobian product uses the ordinary smooth derivative only on their nonzero branches. The checker verifies the least-period-six explicit witness.

**Proof limits:** The exhaustive result ends at proposed period \(11\). It neither certifies longer-period absence nor resolves properties of infinite orbits. The original 1984 source was not available in complete form for literature comparison; this is an originality-access caveat, not a mathematical gap in the finite exhaustive deduction.
