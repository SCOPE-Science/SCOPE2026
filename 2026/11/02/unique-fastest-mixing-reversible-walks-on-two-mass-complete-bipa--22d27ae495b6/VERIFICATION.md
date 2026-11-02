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

Run `python verify_bipartite.py` with the three dependencies in `requirements.txt`. A fixed random seed provides reproducibility. The checker performs 112 exact-rational stochasticity, detailed-balance and characteristic-polynomial test cases; 1,800 independently generated nonuniform feasible edge-flow comparisons; 45 fixed-marginal nonuniform perturbation cases; eight exact Metropolis threshold cases; and six numerical constrained optimality comparisons (1,971 test cases total). The packaged program passed all cases.

The theorem is certified within the written argument by explicit Rayleigh quotient bounds, complete uniform-flow spectrum, a scalar minimax, and a rigidity argument for equality at the top and bottom spectral bounds. Finite tests do not prove the universal claims. The constrained optimization tests use absolute tolerance `1e-4` because the objective can be nonsmooth; those numerical results alone do not certify optimality or uniqueness. Neither independent audit nor independently performed validation is represented.
