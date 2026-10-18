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

Run `python3 verify.py`. The verifier uses only Python's standard library. It checks the polynomial characteristic transport identity underlying the exact moment generating function at an exact-rational grid, tests the non-Gaussian tilted two-point distribution's mean and variance formula, and evaluates the zero-infectivity/no-mutation witness and positive hard-cap bound.

The decisive unrestricted-time conclusions are proven by the positive-susceptible contradiction and the integral \(\int_0^\infty i\le(1-r_0)/\mu\), not by numeric integration, sampling, or finite-time simulation. The code does not certify all positive parameters or infinite time. The biology of unbounded or negative probability traits is explicitly excluded from the interpretation. Self-review only; no independent audit has occurred.
