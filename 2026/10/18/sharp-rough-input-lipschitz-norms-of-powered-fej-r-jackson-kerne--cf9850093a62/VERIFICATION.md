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
# Verification record

The included `verify_jackson.py` computes two independently implemented finite norms (lobe total variation and direct absolute-derivative quadrature) and the rational coefficient normalization. It completes 706 assertions for degree/power combinations, stationary-maxima envelopes, exact low-degree identities and checks of Gaussian scaling. Successful execution requires Python, NumPy and SciPy. The fixed-power sinc series is numerically truncated with an explicit upper tail bound, and its first-power decimal is improved using a separately identified asymptotic tail approximation.

The general finite formula is proved by the sign-attainment and lobe decomposition in `RESULT.md`. The fixed-power limit is proved by dominated convergence, and the degree-uniform high-power limit by a uniform Laplace estimate and bounded total sidelobe variation. Finite tests cannot certify these quantified limits or historical priority. Independent external validation has not been performed.
