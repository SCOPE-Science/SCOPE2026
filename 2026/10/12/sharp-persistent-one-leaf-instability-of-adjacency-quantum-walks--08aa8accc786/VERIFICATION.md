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

# Reproducible mathematical checks

Run `python3 verify.py` with NumPy and SymPy available. The script checks the cubic determinant and the marked-entry resolvent cofactor exactly; it separately constructs the unreduced adjacency matrices of the clique-plus-leaf graphs and cliques for selected orders, calculates their matrix exponentials through symmetric eigendecomposition, and checks the reduced-block formulas and uniform off-defect bounds at deterministic observation times. It also checks projector masses against exact rational expressions in the computed eigenvalues and examines convergence at increasing orders.

The computed finite tests are cross-checks only. The sign-bracketed cubic roots, projector normalization, reverse triangle inequality, fixed-time lower witness and core-entry decomposition form the unrestricted analytical proof; no numerical root finder or finite grid is used to infer the universal quantifiers. The asymptotic \(O(m^{-1})\) assertion follows from the analytic simple-root perturbation estimate, not numerical regression.

The full claimed result has not been independently audited. Verification status describes the same-model symbolic derivation and reproducible computation only.
