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

The bundled `verify.py` checks the stationary zero-current identity and all exact parameter arithmetic used in the finding. Running it with ordinary Python must print `VERIFY_OK`.

The proof of non-convergence is analytic rather than simulation-based. Starting from the printed Itô susceptible equation, divide the integrated `log S` identity by time. Under hypothetical convergence to the deterministic disease-free point, the deterministic integrand tends to minus one-half the squared susceptible noise amplitude, while Brownian motion divided by time tends to zero almost surely. This is incompatible with `log S` divided by time tending to zero.

The boundary-law check is finite symbolic algebra: for a density proportional to `s^(-k-1) exp(-q/s)`, the zero-current equation reduces coefficientwise to the two definitions `k=1+2 mu/a^2` and `q=2 Lambda/a^2`. No numerical trajectory is used as a proof.

Limit: this verification does not establish convergence in distribution of every interior trajectory to the boundary inverse-gamma law; that stronger assertion is outside the accepted claim.
