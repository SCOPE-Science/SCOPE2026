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

`verify.py` uses only Python's standard library and the exact rational `fractions.Fraction` class. Run `python3 verify.py` from the folder containing the six documents and checker. The output is captured byte-for-byte in `verify_output.txt`.

The implementation builds the original \((2k+1)\)-vertex unweighted combinatorial Laplacian, constructs its principal follower submatrix after removing three vertices, and calculates its inverse trace by exact Gauss–Jordan elimination. It independently compares this trace against the Schur-derived arm-profile formulas across all 90 leader-placement orbit representatives for \(3\le k\le11\). For \(k=3,4,5\), it enumerates all 284 labeled leader triples and compares their exact objective against the claimed minimum. It additionally checks the exact optimal-set counts for nine arm counts.

The successful output is:

```
VERIFY_OK orbit_full_inverse=90 exhaustive_full_inverse=284 analytical_profile_comparisons=90 optimal_counts=9
```

The finite enumeration does **not** certify the infinite family; global optimality for every integer \(k\ge3\) follows from the six symbolic orbit formulas and strict rational inequalities in `RESULT.md`. No independent audit is claimed.
