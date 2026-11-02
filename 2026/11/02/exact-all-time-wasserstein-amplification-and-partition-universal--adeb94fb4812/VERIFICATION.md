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

# Verification notes

The analytical proof in `RESULT.md` has five independently inspectable steps: Laplacian spectral projectors, exact signed heat-kernel-row decomposition, matching Kantorovich witness and transport plan, pairwise operator reduction with largest-class monotonicity, and critical-time differentiation. The comparison program `CHECK.py` uses NumPy and SciPy to independently exponentiate the graph Laplacian, solve transportation linear programs and compare all Dirac-pair coefficients for 50 graph/time cases. It also checks the unique peak formulas for three amplifying graphs. All supplied cases completed successfully when replayed; see the program for complete inputs and tolerances.

These finite tests are not exhaustive over arbitrary graph orders, real times, or probability measures; all universal statements rely on the analytical proof. No independent mathematical audit is claimed. The graph generator must use rate one per edge, without degree normalization. Originality remains subject to further historical comparison with equivalent Dobrushin or heat-flow Lipschitz formulations.
