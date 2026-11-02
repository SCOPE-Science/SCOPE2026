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

# Exact verification

Run `python verification.py` (Python 3 with SymPy). The program symbolically constructs the exact published mean-field vector field, computes its Jacobian and its two implicit sensitivities, and asserts both global algebraic identities. It then checks the full rational equilibrium, the two mean-state inequalities, the exact Jacobian trace/determinant, and the strict derivatives \(688/785\) and \(-1220/471\). These are **exact** identities/certificates, not finite sampling of a parameter domain.

The proof in `RESULT.md` supplies the sign analysis, the interior ordering, the nondegenerate implicit-function step and the physical undirected-network realization. Only small openness perturbations near the verified equilibrium are covered. Finite-agent stochastic dynamics, broader global dynamics and independent audit are not verified.
