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

The result is analytically proved in `RESULT.md`. The script `verify.py` can be executed with standard Python 3 and no external dependencies. It uses exact integer edge-state weights \(a^{|F|}(b-a)^{|E|-|F|}\) for rational transmissibility \(p=a/b\), enumerates all vaccine subsets and every two-vaccine interaction for all cycles \(C_n\), \(3\le n\le8\), at \(p\in\{1/4,1/2,3/4,9/10\}\), and checks the symbolic formula and all nonempty-background inequalities. It independently uses the unique path in each Prüfer-coded rooted tree through size six to check all \(1,441\) labeled trees and every vaccine set at \(p=2/5\). Execution from the packaged source reports `All exact-integer checks PASSED`.

Finite enumerations are not proofs of the all-orders and real-parameter conclusions. Those rest on the closed expectation formula, path-coverage lemma, analytic inequalities, and monotonic reciprocal-power root classification. No independent scientific audit has occurred.
