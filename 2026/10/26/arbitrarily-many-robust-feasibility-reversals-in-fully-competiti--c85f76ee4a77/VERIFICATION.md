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

# Verification and limitations

The analytical evidence is the exact two-species inverse, the separation of finitely many strict feasible and infeasible test points, the finite-dimensional resolvent estimate, the hyperbolic saddle determinant, and the relative-entropy Lyapunov identity. These are independently reconstructible from `RESULT.md` and require no datasets.

Run `python reentrant_verify.py` to check the rational construction in dimensions \(2\) through \(11\). The program checks all interlacing witnesses against exact linear-system solutions for both the block and fully competitive matrices, and verifies a rational quantitative sign margin and global-attraction diagonal-dominance criterion. Its finite results are not asserted to establish the theorem for arbitrary dimension. A separate historical-priority risk is the uninspected supplementary material of the motivating 2026 paper; a failed search is not proof of novelty. No independent audit was performed.
