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
# Verification and limits

The analytic proof is contained in `RESULT.md` and is independent of numerical root-finding. Running `python check_two_cluster.py` with SymPy and SciPy checks, by exact symbolic identities, the mass constraint, the critical parameter, the linear unbalanced coefficient, and two distinct quadratic coefficients. It also reconstitutes the original differential equations on complete graphs with three and four vertices for sampled partitions and parameters, verifies local sample roots, and checks residuals below \(2\times10^{-10}\). These computations passed when the scientific package was prepared.

The sampling grid for the direct solver is restricted to a small gap neighborhood. It does not claim a global exhaustive equilibrium count; additional distant roots may exist. Local all-parameter equilibrium counts follow instead from exact analytic reduction plus the implicit-function theorem and, at mobility two, strict concavity. Symbolic algebra is not independent validation. Independent audit: not performed.
