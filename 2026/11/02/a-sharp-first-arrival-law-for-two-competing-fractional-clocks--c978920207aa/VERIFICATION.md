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

The analytic proof consists of a symmetric exponential-mixture clock-race identity, a killed nearest-neighbour walk recurrence, a conditioned marked subexponential convolution limit, an exponential-tail bound for the number of events, and Tonelli's formula for the mean.

Reproduce the supplementary calculations with `python verify.py` (requires Python, NumPy, SciPy). The script was executed against the package source and returned 943 passing assertions. These checks include inverse-Laplace spectral integration, independent race-probability quadrature, finite embedded-chain mass conservation, discrete first-arrival transforms, and critical waiting-tail diagnostics. Exact infinite identities, asymptotic limits and historical novelty cannot be certified by finite numerical checks.

Independent audit has not been performed.
