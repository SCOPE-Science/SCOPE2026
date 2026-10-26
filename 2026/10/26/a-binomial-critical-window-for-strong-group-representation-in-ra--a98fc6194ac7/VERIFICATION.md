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
# Verification details

The analytic proof establishes the uniform event on which **all** size-\(k\) committees simultaneously have both group-representation scores equal to their share of selected cohesive candidates. The event is estimated by \(m\binom{m-1}{k}(1-p(1-p)^k)^n\). The binomial cohesive-candidate law uses only independence across candidate approval columns. The critical-window law follows from the binomial CLT and requires fixed \(m,k\); it is not certified by experiments.

`verify_sjr.py` exhaustively enumerates all approval matrices for five specified small instances at \(p=1/2\). It computes both exact committee optima and the separation event, checks lower and upper feasibility bounds, and asserts agreement with the common-optimum formula whenever the separation event holds. The accompanying `verification_output.txt` is the actual recorded program output. The independent-audit channel is not performed. The score for an empty cohesive-candidate set is assigned the vacuous-satisfaction value one by convention.
