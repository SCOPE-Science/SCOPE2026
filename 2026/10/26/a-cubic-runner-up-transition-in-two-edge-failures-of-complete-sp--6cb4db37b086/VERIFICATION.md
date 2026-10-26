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

# Exact reproducibility and limits

Run `python verify.py` in a standard Python environment with the SymPy version range recorded in `requirements.txt`. The checker recomputes the seven expressions for Kirchhoff-index damage, verifies all strict rational-comparison identities using nonnegative-coefficient polynomials in shifted parameters, and confirms the two exact evaluations of the runner-up quadratic at adjacent integers. Its matrix test separately constructs graph Laplacians, removes the two edges, inverts the shifted Laplacian exactly over rationals, and independently compares the resulting Kirchhoff-index changes.

Observed successful completion:

```
SYMBOLIC_OK seven orbit formulas; six strict comparisons; unique integer transition
DIRECT_INVERSE_OK 80 exact independent Laplacian inverse checks
ORBIT_EXHAUSTION_OK four labelled families
```

The infinite two-parameter classification is proved by the symbolic identities and analytic inequalities given in `RESULT.md` and `COMPARISONS.md`, not by the 80 cases. The four labelled-graph checks are examples of orbit completeness, which is proved combinatorially for all sizes. This work has not received an independent mathematical audit. A relevant article on weighted complete split resistance (DOI 10.1016/j.dam.2024.07.040) could not be compared beyond title and bibliographic information; possible specialized historical overlap remains unresolved.
