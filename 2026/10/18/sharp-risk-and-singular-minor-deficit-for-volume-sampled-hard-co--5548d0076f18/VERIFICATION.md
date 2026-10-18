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

# Exact checks and scope

The supplied standalone `CHECK.py` was run with Python 3 and SymPy. It completed 6,275 exact-arithmetic checks over 59 seeded random admissible full-column-rank designs and explicit sharp or singular-degenerate examples.

The tests independently form the full-data least-squares minimizer, reconstruct each constrained minimizer, test exact feasibility, evaluate the full loss, verify the determinant and projector identities, normalize the sampling weights and compute all admissible \(k\)-subset sums. They include a strict-deficit example with expected excess \(87/7\) versus frontier \(88/7\), and two constructions attaining the upper and lower risk ratios.

The proof, not the finite checks, establishes the theorem for all real full-column-rank matrices with \(m>n\ge2\) and integers \(1\le k<n\). The full-data objective is available and constraints are enforced exactly; no numerical-stability or practical runtime claim is validated. Independent verification was not performed.
