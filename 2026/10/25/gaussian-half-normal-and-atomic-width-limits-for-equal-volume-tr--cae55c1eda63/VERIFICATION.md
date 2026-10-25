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

# Verification scope

The exact tree Gram determinant and vertex-support representation were tested on path, star, and broom instances of small sizes; the Gaussian correlation calculation and the critical-parameter inverse-tail construction were checked numerically. An optional direct Gaussian simulation illustrates finite-sample distributions but is not treated as an infinite limit proof. Execute `python verification.py` using NumPy and SciPy; output includes `VERIFY_OK exact_gram=34 independent_support_checks=90 phase_boundary_cases=12 simulation_only=3`.

The proof in `RESULT.md` supplies the general determinant, local-dependence bound, central-limit normalization, and the critical crossover. In particular, the analytic Poisson error bounds, not the finite experiment, imply the Gumbel theorem. The cited Arratia–Goldstein–Gordon Poisson bound is external established mathematics, not an independently re-proved theorem. A full independent mathematical review and exhaustive bibliographic classification are not claimed.
