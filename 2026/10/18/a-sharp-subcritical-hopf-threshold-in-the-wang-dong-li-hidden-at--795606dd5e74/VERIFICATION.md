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

# Verification

Run `python3 check.py` with SymPy installed. It reconstructs the published differential field, equilibrium Jacobian, characteristic polynomial and Hopf crossing; it checks exact right/left eigenvectors and the complete first-Lyapunov-coefficient algebra, including the positive closed form. The program computes no finite-orbit approximation: the Hopf and saddle-cycle conclusions follow from the analytic nondegeneracy hypotheses and the established Hopf theorem.

The claim is local in phase space and applies to each fixed `b>0`. It neither certifies any global attractor nor establishes a global basin boundary. All algebraic constants are under the eigenvector normalization displayed in RESULT.md. No independent external verification is claimed.
