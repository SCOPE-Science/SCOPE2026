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
# Reproducibility and verification boundaries

The standalone `verify.py` program uses Python 3, SymPy and NumPy. Running `python verify.py` should reproduce symbolic checks for the local reaction expansions, modal trace and determinant, exact spatial averages, and the exact small path example; it also numerically checks graph eigenvalues and separated instability bands for path orders from \(2\) to \(40\). The general all-graph result is derived analytically in RESULT.md; finite tests are neither infinite proofs nor certificates of independent validation. The nonuniform local equilibria follow from the finite-dimensional simple-eigenvalue bifurcation theorem and an explicit transversality calculation. The equilibrium mean signs follow from the exact identity and a positive quadratic coefficient. The comparison with source literature is limited to the specifically cited inspected primary full text and other stated access constraints. Independent scientific assessment has not been performed.
