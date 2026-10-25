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

# Verification and scope

The exact finite diagnostics in the standalone `verify.py` completed with `VERIFY_OK`: 220 rational arithmetic tests for the unperturbed binomial identities, six deterministic nonlinear lift cases, and 1020 rescaled orbit-membership checks away from the limiting quadratic body's boundary; it also checked the coefficient-volume rational value `544/9`. The verifier uses standard Python 3 only.

The analytical proof in `RESULT.md` supplies the all-length and all-center argument. Its non-finite steps are a uniform ergodic average over a compact family of mean-zero continuous cocycles, an interpolation estimate forcing the first displacement to be quadratic-order small, and convex-body volume convergence. The tests alone cannot establish these infinite claims.

For every irrational base and every periodic real `C1` perturbation, the conclusion concerns a fixed sufficiently small radius and the product maximum circular metric. No uniform convergence rate in the base rotation, general nonsmooth cocycle conclusion, or independent certification is asserted.
