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

# Reproducibility and limits
Execute `python verify_pendant_clique.py` with Python 3, NumPy, and SymPy in this directory. The checker constructs each weighted Laplacian directly, tests the dual projector certificates and full eigenspaces with exact rational parameters, verifies budget identities and sharp prices for graph orders \(4\) through \(13\), and samples independently weighted competitors. It reports `PASS 1960 independent assertions across exact duals, spectra, budgets and random asymmetric edge allocations`.

The proof in `RESULT.md` independently establishes the infinite parameter family by an analytic semidefinite certificate and equality-rigidity argument. Random finite competitors cannot demonstrate universal optimality and are only supplementary stress tests. The symmetry-reduction literature is contrasted with, not used as a substitute for, the unrestricted global uniqueness proof. No independent review has been performed.
