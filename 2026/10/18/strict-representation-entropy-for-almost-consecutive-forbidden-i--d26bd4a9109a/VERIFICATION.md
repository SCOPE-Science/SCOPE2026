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
# Reproducibility

Run `python3 VERIFY.py` using standard Python 3. The script enumerates legal index subsets and their sums exactly for several small parameter pairs, constructs the greedy sequence by smallest missing positive sum, cross-checks those independent counts against a suffix-state transfer algorithm and the published count recurrence, verifies the greedy recurrence on its established \(c=1,k\ge11\) range, and evaluates both root equations by bisection. In the executed test the script printed `PASS all 18 parameter tests; finite checks not an infinite proof`.

The proof in RESULT.md provides the infinite arguments, including primitive transfer and companion matrices, strict root comparison, truncated mean sandwich and large-parameter asymptotic. No certificate of independent review or external validation is claimed. The output of finite checks cannot certify an infinite result by itself.
