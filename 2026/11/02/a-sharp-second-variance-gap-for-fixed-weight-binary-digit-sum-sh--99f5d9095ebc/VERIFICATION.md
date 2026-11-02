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
# Verification record

The command `python3 cusick_verify.py` executed successfully with Python's standard library. Its exact rational comparisons against the known, independently derived even/odd variance recursion covered every shift from 1 through 8191. Exhaustive independent enumeration of all one-bit subsets across widths 2 through 11 covered 4017 supports and checked both extremal levels and every equality pattern.

Ten shifts were additionally tested by directly evaluating squared binary digit-sum differences for 262144 consecutive arguments each. The largest difference between an empirical second moment and the exact prediction was 0.00810623; the predeclared finite-sample tolerance is 0.02. The direct samples do not prove the moment formula, and the finite combinatorial checks do not prove the infinite all-weight classification. Infinite quantifiers are discharged by the carry-covariance and strict-compression proofs in RESULT.md. There is no independent audit.
