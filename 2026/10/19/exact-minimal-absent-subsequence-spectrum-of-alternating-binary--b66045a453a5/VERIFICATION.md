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

The correctness argument is symbolic and covers every positive integer \(m\). The supplied `checker.py` performs direct greedy-free subsequence testing against \((ab)^m\), removes each letter to test minimality, and compares the resulting set with the closed structural conditions for \(1\le m\le7\). It separately performs coefficient recursion from \(F(u,z)\), checks the complete length distribution, and verifies the scalar count recurrence on a longer finite prefix. Running `python3 checker.py` yielded exactly the included `computation.txt` output.

Finite enumeration confirms only the instances checked; it does not certify all lengths and does not establish literature uniqueness. Formal proofs are supplied in RESULT.md. Independent audit has not been performed.
