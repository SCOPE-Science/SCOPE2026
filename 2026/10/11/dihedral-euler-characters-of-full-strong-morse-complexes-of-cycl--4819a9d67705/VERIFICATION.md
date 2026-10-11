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

# Finite verification and bounds

Execute `python3 verify_full_strong_dihedral.py` using a Python 3 standard-library interpreter. Expected terminal output:

```
VERIFY_OK independent_filtration_faces=1734 signed_action_checks=66 arithmetic_sizes=298
```

The verifier enumerates all vertex orders on \(C_n\) for \(3\le n\le8\), generates their complete downward-closed matching faces, and compares the resulting sets to the cyclic three-symbol criterion. It computes every dihedral fixed-face signed trace by explicit permutations of the \(2n\) matching vertices, including induced orientations, and verifies both quotient Euler averages. A separate integer check verifies the closed arithmetic formulas for \(3\le n\le300\).

This is not an exhaustive experiment over all \(n\); the infinite result relies on the orientation-extension, transfer-matrix, reflection-path and finite-group averaging arguments in `RESULT.md`. No independent external audit or certification was performed.
