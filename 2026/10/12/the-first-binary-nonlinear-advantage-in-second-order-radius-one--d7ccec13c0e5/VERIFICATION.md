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

# Verification instructions

The precise domain is binary two-row product-form covering with at most one **shared column** of error. Run from the directory containing all supplied files:

```
python3 verify.py
python3 direct_center.py
c++ -O3 -std=c++17 finite_check.cpp -o finite_check
./finite_check
```

The Python subset search independently verifies every smaller code for lengths one through four. The length-five C++ DFS checks all potential 17-word forbidden sets after translation to include zero, with only monotonic validity pruning, and reports 16,829,638 visited recursion nodes with no witness. The direct target-matrix verifier confirms coverage of all 4096 ordered target pairs at length six by the listed 29-word code. The separate `verify.py` covers those same matrices using projection membership instead of literal center enumeration. No inference about length-six optimality is made. The proof of the affine-linear lower bound uses syndrome rank and does not depend on finite enumeration. No independent audit has been performed.
