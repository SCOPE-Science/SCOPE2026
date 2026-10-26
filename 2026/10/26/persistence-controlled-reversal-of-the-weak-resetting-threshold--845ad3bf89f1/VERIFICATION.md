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

# Verification and reproducibility

Run `python3 verify.py` from the extracted package directory. Only Python's standard library is needed. The included verification checks the passive threshold polynomial and derivative, the exact zero-relaxation polynomial limit, Green-function integration against an independently discretized pair of Dirichlet–Neumann boundary-value problems, local differential equation residuals, the transition between opposite signs, and the fast-relaxation asymptotic. A successful execution prints `PASSED 905 deterministic checks` and coefficient summaries. These are reproducibility checks, not an independent audit.

The proof uses the renewal identity, stopped backward moment equations, Girsanov integrability for small active perturbations, exact Green inversion, a simple-root implicit-function argument, and controlled resolvent asymptotics. The finite numerical sign-change location is not a uniqueness proof. Independent validation and a wider originality assessment have not been performed.
