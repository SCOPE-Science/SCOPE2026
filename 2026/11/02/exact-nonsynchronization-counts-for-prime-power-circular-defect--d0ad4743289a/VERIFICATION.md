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

# Exact verification and reproducibility

The theorem relies on the explicitly cited defect-one primitivity theorem and the proved elementary counting steps, not on a finite-experiment extrapolation.

From a directory containing the two supplied source files, use Python 3 and a C++17 compiler:

```sh
python3 formula_check.py
g++ -std=c++17 -O2 census_check.cpp -o census_check
./census_check 4
./census_check 8
```

The Python verifier computes the stated inclusion-exclusion formula in exact integer arithmetic for prime powers at state counts \(4,8,9,16,27,32\); checks the exact expected outputs; and independently enumerates small compatible quotient permutation groups. Its success marker is `FORMULA_VERIFY_OK`.

The C++ program enumerates every map for state counts four and eight, selecting those of rank \(n-1\) by its exact image multiplicities. It checks synchronizability using reverse breadth-first reachability on unordered state pairs for the two letters, and independently checks all applicable residue congruences. At order four its counts are 144 total rank-defect-one maps, 128 synchronizing maps and 16 nonsynchronizing maps; at order eight, 1,128,960 total, 1,114,112 synchronizing, and 14,848 nonsynchronizing. Both give zero discrepancies. A mismatch aborts when the verifier is run with either of these two state counts.

These computations check small examples and relevant arithmetic, not the infinite quantifier or originality. Independent scientific audit has not been performed. The source bibliography and the scientific assessment explain the remaining priority risks.
