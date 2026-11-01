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

# Reproducibility and checks

`python3 verify_johnson_character.py` uses only the Python 3 standard library. The run enumerates the full face posets for four Johnson complexes with parameter pairs \((6,3),(7,3),(8,3),(8,4)\), independently computes the signed simplex Lefschetz trace and the proposed permutation/incidence character at every conjugacy-class representative, and compares them. It checks the mod-two homology with exact bit-vector Gaussian elimination, and checks the trivial and sign averages using the exact sizes of conjugacy classes. The required ending is `JOHNSON_ALL_WEIGHT_SYMMETRY_VERIFY_OK 70`. The file `verification_output.txt` records the actual output.

The all-parameter theorem is proved combinatorially in `RESULT.md`; finite computation cannot establish all \(n,k\). The mathematical comparison does not amount to independent publication-priority certification. No independent mathematical audit has been performed.
