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
# Reproducibility and verification

`verify.py` is a standalone standard-library Python 3 checker. Running `python3 verify.py` generates the result recorded in `verify_output.txt`. It constructs Sierpiński adjacency directly from the first-differing-coordinate definition, independently constructs regular symmetric relations, validates all row-degree and diagonal conditions, checks all constructed sets for domination and limitedness, and inspects all cross-row adjacency pairs from selected vertices. For every profile with at most sixteen graph vertices, it independently exhausts all subsets to verify the minimum cardinality.

Recorded run output:

```
ALL CHECKS PASSED
construction_parameter_profiles=69; exhaustive_minimum_profiles=36; tested_candidate_subsets=160164
```

The checks include only the parameter profiles specified in `verify.py`, notably \(m\in\{2,\ldots,8\}\), \(1\le k<m\), and heights whose order does not exceed 125. Full enumeration is restricted to graphs with at most 16 vertices. Finite computation is not an infinite proof. The general correctness rests on the row-block inequality and uniform symmetric-relation construction in `RESULT.md`.

Independent external mathematical audit has not been performed.
