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

# Verification

`python3 CHECKER.py` was run against the attached code. It uses bitmask sets and directly evaluates implication and co-implication via the finite Kripke order, rather than using the signature characterization in the semantic evaluator. All tuples of \(k\) upsets were checked for \(m,n\in\{1,2,3\}\), \(k\in\{0,1,2,3\}\), totaling **8,936** semantic comparisons, and the direct complete-generator census was compared with the symbolic formula in **36** parameter cases. Result: `BI_HEIGHT_VERIFY_OK semantic=8936 counts=36`. The proof of the general formulas and of the random asymptotic are mathematical, not inferred from these tests. The checker does not simulate the Gaussian asymptotic, and its finite parameter range cannot establish an infinite claim.

Self-review passed for the explicit definitions, algebraic reconstruction, counting logic, and central-limit argument. Independent audit has not been performed.
