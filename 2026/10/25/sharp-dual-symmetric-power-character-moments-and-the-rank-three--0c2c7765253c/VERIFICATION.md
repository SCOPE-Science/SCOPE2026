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

# Reproducing the mathematical checks

Run `python checker.py` with a Python 3 environment providing SymPy and NumPy. The reference output in `verification-output.txt` is

```
PASS: 984 exact overlap, formula, calculus, algebra and independent finite-grid Weyl quadrature assertions
```

The checker enumerates Dynkin-label constituents and confirms all rank-dependent intersections for ranks 3–8 and highest weights 1–12. Five exact coefficient choices are checked against the independent representation-ring orthogonality expansion in each rank/weight. A symbolic derivative calculation verifies the rank-three cubic. Positive roots and improvements are sampled for 20 weights, and six finite Weyl quadratures check the proposed integration formulas in the group model independently of the formal character-ring calculation.

The exact claims for all ranks and all highest weights are justified in `RESULT.md` through Pieri decomposition, character orthogonality, sharp triangle inequalities, a balancing comparison, and a one-dimensional derivative sign argument. Enumerations and numerical quadratures alone would not verify those infinite-quantifier statements, and no claim of machine certification or independent audit is made.
