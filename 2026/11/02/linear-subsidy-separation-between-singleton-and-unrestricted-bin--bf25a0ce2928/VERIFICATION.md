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

The complete proof is in `RESULT.md`. `verify.py` uses the Python standard library to enumerate all complete allocations modulo indistinguishability of goods of the same valuation type for \(r=2,3,4\). A weak composition records how many non-distinguished goods each labeled agent holds, and a second composition locates the unique distinguished good. Therefore the state space is exhaustive for the specified profiles (rather than a partial random sample).

For each allocation, the code constructs the exact integer difference constraints \(p_i\ge p_j+v_i(X_j)-v_i(X_i)\). The componentwise least nonnegative solution, if one exists, is obtained by iterating their max-plus update; an improving extra iteration after \(2r\) rounds detects a positive cycle. Because all weights are integers, this least solution is integer-valued even though the mathematical problem permits real subsidies. This does not replace the direct infinite-family proof.

Observed output:

```
r=2 n=4 allocations_reduced=80 house_reduced=4 unrestricted=1 house=3 unrestricted_witnesses=2
r=3 n=6 allocations_reduced=1512 house_reduced=6 unrestricted=3 house=5 unrestricted_witnesses=9
r=4 n=8 allocations_reduced=27456 house_reduced=8 unrestricted=4 house=7 unrestricted_witnesses=16
VERIFY_OK
```

The source can be rerun using `python3 verify.py`. No external packages or data are required. The theorem for all integers \(r\ge3\) is justified by the analytical proof, not these finite enumerations. Independent validation has not been performed.
