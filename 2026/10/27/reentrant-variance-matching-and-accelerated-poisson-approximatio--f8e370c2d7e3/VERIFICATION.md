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

# Reproducibility

Execute `python3 verify_bandpass.py` with ordinary Python 3. The script uses exact rational polynomial arithmetic and rigorously bounded exponential-series tails to verify the analytic sign certificates at the three specified crowding parameters. It also verifies the two finite-sum polynomials from the Palm overlap decomposition, the closed-form integral, and nonzero second-difference coefficients in the signed Poisson expansion.

The checker does not assert that checking three inputs proves all-parameter results. The latter follow from the explicit Mecke identities, factorial-moment analysis, and Cauchy coefficient bounds detailed in RESULT.md. The two interval roots are existence statements deduced from certified signs and continuity, not numerically certified root isolations beyond the intervals.
