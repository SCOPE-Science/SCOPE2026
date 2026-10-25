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

The proof uses the exact three-stage RKL2 stability polynomial and exact integer entries of the finite Dirichlet path matrix. Matrix products were checked for path lengths \(N=2,3,4,5\); the banded formulas then give the entries for arbitrary \(N\geq3\). The only sign-changing entries within the bulk interval are the boundary-adjacent coefficients, whose exact lower roots are \((15-\sqrt{30})/13\) for \(N=2\) and \((15-\sqrt{15})/14\) for \(N\geq3\). All remaining diagonal and off-diagonal entries are bounded below or factored explicitly in the proof. No numerical experiment is used as an infinite-dimensional proof. The result does not cover other stage counts or operators.
