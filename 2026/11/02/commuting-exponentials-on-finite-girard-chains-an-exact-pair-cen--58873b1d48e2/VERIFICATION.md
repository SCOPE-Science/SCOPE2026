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

Execute `python3 checker.py` in the directory holding this file. The script is self-contained and uses no package outside Python's standard library. Its source is included as an independent artifact.

The checker enumerates all \(50,068\) unary maps across nilpotent-minimum chain orders \(2\) through \(6\), directly tests the original four bang equations and checks that every and only the predicted floors satisfy them. It verifies monoid associativity/unit, the explicitly computed residuum, and involutive negation for those chains. For abstract idempotent chains of orders \(2\) through \(9\), it enumerates all ordered pairs of endpoint-containing fixed-point subsets, compares actual functional commutation with the gap condition, and confirms the exact pair counts \(1,4,14,48,164,560,1912,6528\). Actual execution returned `ALL_CHECKS_OK functions_examined=50068 commuting_counts=[1, 4, 14, 48, 164, 560, 1912, 6528]`.

These computations exhaust precisely their declared finite ranges, not all finite lengths. The analytic proof in `RESULT.md` establishes the unbounded finite-chain claim. Independent audit is not performed.
