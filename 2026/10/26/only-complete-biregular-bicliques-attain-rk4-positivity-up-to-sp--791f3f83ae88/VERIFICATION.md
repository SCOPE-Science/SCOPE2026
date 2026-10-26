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

# Reproducibility and verification limits

Run `python verify.py` after installing the requirements listed in `requirements.txt`. The program independently constructs exact rational Laplacians from explicit bipartite incidence sets, computes the fourth-order Taylor matrix directly, and checks every indicated off-diagonal entry against separately specified block-polynomial formulas. Additional checks establish strict negative distance-three entries for timesteps greater than \(2/(a+b)\), a complete-graph rational enclosure for the root \(\rho\), exact top-eigenvector relations and the symbolic quadratic/positive-diagonal certificates.

The finite tests are independent of the infinite graph theorem's quantifiers; complete correctness depends on the algebraic and graph-theoretic proof in `RESULT.md`. No external or independent mathematical audit has been performed.
