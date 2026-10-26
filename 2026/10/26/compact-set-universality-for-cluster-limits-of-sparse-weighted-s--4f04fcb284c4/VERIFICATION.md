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

The analytic proof derives each diagonal entry of \(|T^n|^{1/n}\) from the product of the underlying positive weights. Its superlacunary estimate, the bounded-versus-diverging distance-to-next-spike dichotomy, and explicit subsequence construction jointly establish both inclusions of the claimed cluster set. The uniform bound \(0\le |T^n|^{1/n}\le I\) converts coordinatewise convergence into strong operator convergence. A coordinate-difference functional separates the copies of \(K\) in the cluster set. The scalar range follows from the exact operator cluster set.

To reproduce supplementary tests, execute `python3 check.py` using the enclosed standalone file. The verified outcome was `PASS: 4997 index/formula, spike-limit and topology tests`. The script compares exact finite index formulas, checks finite approximations to specified limits, and tests coordinate-jump separation. No finite test proves infinite convergence, all possible clusters, or literature originality. The result has not undergone independent scientific audit.
