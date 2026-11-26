---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

`python3 verify_finite_boolean_w.py` runs from this package with Python 3 standard library. The tested code computes \(\mathcal W\)-membership by the published Lemma 4.4 algorithm, generates the canonical Boolean carrier for each formula, and directly evaluates the specified \(\mu\)-extension; distinct syntax trees are retained separately.

Observed successful output:

```
EXACT PASS
all_distinct_binary_formulas_by_leaf_count [(1, 2), (2, 8), (3, 64), (4, 640), (5, 7168)]
canonical_checks 12882
max_nontheorem_atoms_in_exhaustive 6
two_element_semantic_cases 576
formula_nontheorems_in_exhaustive 6620
two_element_separation_failure_3_chain_counterexample PASS
```

The 12,882 cases include 7,882 exhaustive two-variable formula trees through five leaves and 5,000 deterministic random formulas drawn from a three-variable language. The 576 two-element cases are assignments across three-leaf formulas. The checker separately enumerates all \(2^5=32\) two-element choices for the separating formula and directly recomputes the three-chain witness. These finite tests cannot certify the unlimited formula theorem or noncoverage in the literature. The exact general proof is the structural induction in `RESULT.md`, relying on Lemma 4.4 with Corollary 4.8 and on the soundness theorem in the cited work.
