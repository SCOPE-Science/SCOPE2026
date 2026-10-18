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

The full proof is in RESULT.md. Reproduce the generator, Laplace and residue identities with `python verify.py` using SymPy, NumPy and SciPy. The program checks stationary phase-conditioned first and second moments; independently constructs a backward-affine finite-time semigroup; compares its Laplace transform with the factored expression; verifies the small-lag coefficient identities and the two critical residues; and checks samples by a separate matrix-exponential computation.

The infinite-parameter sign and uniqueness conclusions use analytic inequalities in RESULT.md, not finite tests. The equal-rate and strictly positive-stiffness assumptions are essential. The stationary unperturbed model is not inferred from data here; the rate-reconstruction equation does not establish numerical or statistical robustness. Independent audit has not been performed.
