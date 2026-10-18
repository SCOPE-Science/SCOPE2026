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

# Reproduction checks

The included `verify_galois.py` enumerates all \(52\) rational order-three elation subgroups, the \(486\) geometrically smooth invariant quartics per fixed subgroup, every resulting projective-normalized equation, and the full projective orbit classification. Its catalog is `galois_output.json`, with \(19\) orbit representatives in descending \(X\)- then \(Y\)-degree order. Its output must agree with `census_result.txt`.

The included `check_geometric_smoothness.py` checks the Jacobian ideal of each orbit representative on all three projective affine charts using exact Gröbner arithmetic in characteristic three; the expected outcome is `groebner_result.txt`. The included `check_stabilizer.py` independently enumerates \(\operatorname{GL}_3(\mathbf F_3)\) matrices and checks the exceptional stabilizer; its expected output is `stabilizer_result.txt`. The algebraic normal-form and exact smoothness criterion establish why these finite checks cover **every** qualifying quartic; singularities outside the base field are covered by the unit-ideal tests.

Commands (from the directory containing these files):

```
python verify_galois.py
python check_geometric_smoothness.py
python check_stabilizer.py
```

NumPy and SymPy are the only non-standard Python dependencies. The results classify rational arithmetic inner Galois centers over \(\mathbf F_3\), not geometric centers over an algebraic closure; global publication priority and independent audit remain unestablished.
