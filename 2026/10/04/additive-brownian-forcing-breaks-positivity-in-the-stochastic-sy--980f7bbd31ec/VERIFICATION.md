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

The primary publisher full text was checked at the displayed stochastic system, the global-positivity theorem, the later multiplicative-noise extinction theorem, and the Appendix Itô calculations. The twelve additive diffusion terms in Eq. (24) were distinguished from the state-dependent diffusion terms used later.

The proof was reconstructed from the printed equations. Term-by-term summation leaves only recruitment, natural loss, the unmatched susceptible-female prevention loss, and the additive Brownian sum. The integrating-factor comparison with a scalar Ornstein--Uhlenbeck process is exact. The Gaussian lower bound uses the closed mean and variance of that scalar process; no simulation or finite enumeration is used to infer the universal result.

The packaged `verifier.py` checks the symbolic transfer cancellation and evaluates a representative positive Gaussian lower bound. It does not certify the universal theorem; the universal theorem is established by the analytic proof in `RESULT.md`.

Limits: the result applies to Eq. (24) as printed with nonzero aggregate additive noise. It does not analyze a multiplicative, reflected, or truncated replacement, and it does not determine the identity of the first compartment to reach the boundary.
