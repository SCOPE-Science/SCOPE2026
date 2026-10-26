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
# Reproduction and verification

Execute `python3 verify.py` with Python 3 and its standard library. The output is captured in `verification_output.txt`.

The code enumerates all simple labeled graphs on four, five, and six vertices and checks the triangle mean, degree-one mean, and their covariance independently at every fixed edge count. It also checks the independent-edge covariance at probability \(1/2\) by exact graph enumeration; performs 6948 exact-rational sign evaluations at characteristic edge counts for \(4\le n\le500\); and compares finite sparse covariances at four densities against the analytically established limit. All tests completed successfully.

The proof establishes the unlimited-parameter statements by elementary conditional hypergeometric counting and algebraic sign analysis. The verifier is a finite diagnostic only. The older functional-limit source could not be reviewed in full; priority uncertainty is scientific, not a failed computation.
