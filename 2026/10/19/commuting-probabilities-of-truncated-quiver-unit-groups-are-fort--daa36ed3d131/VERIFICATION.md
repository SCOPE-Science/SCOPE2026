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

Execute \(\texttt{python3 checker.py}\) using only the Python 3 standard library. The checker independently enumerates ordered pairs of units and compares their actual commutativity equations with a separate union-find subgraph sum in ten finite examples. Included cases cover a loop, parallel arrows, directed and transitive triangles, two finite-field characteristics other than two, and characteristic two. It separately verifies the exact cycle closed formula in nine numerical cases. The command prints \(\texttt{VERIFY_OK}\) on success.

The proof of the all-field theorem is symbolic: each arrow contributes a one-equation finite-field solution count, and the FK identity is obtained by expansion and counting constant colorings on connected components. The group nonisomorphism is proved by comparing full character-relation kernels for prime fields with \(p\ge5\); finite checks do not establish this infinite assertion. No automated isomorphism classifier or independent audit was used. No assertion of formal verification or exhaustive bibliographic novelty is made.
