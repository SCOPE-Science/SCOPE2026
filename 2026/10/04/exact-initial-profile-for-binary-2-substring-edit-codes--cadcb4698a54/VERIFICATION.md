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

Run `python3 verify.py` from the package root. The verifier uses only the Python standard library. It reconstructs every at-most-one \(2\)-substring-edit ball in two ways, checks equality of those implementations, forms the disjoint-ball compatibility graph, and runs exact maximum-clique branch-and-bound for each \(1\le n\le8\). It then separately checks the listed length-\(8\) witness.

The computation proves only the finite profile through length \(8\). It does not extrapolate the observed values, and a timeout or altered verifier would not constitute a proof. The supplied run completed and its captured output is in `artifacts/verification_output.txt`.
