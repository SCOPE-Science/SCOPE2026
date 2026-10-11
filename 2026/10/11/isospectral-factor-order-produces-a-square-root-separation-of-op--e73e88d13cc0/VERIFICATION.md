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

# Analytical and computational verification

The proof in `RESULT.md` directly verifies the operator expansions, both triangular period maps, positivity and sharpness of the Green inverses, the Gaussian rescaling near the two nondegenerate extrema, the pulse-area limit, and matching bounds for the downstream filter maximum. These are analytic arguments with all time variables on the real line, not extrapolations from finite samples.

For a reproducible numerical consistency check, run `python verify_order_response.py` with Python 3 and its standard library. The script uses a composite trapezoidal grid with 90,000 intervals on a full trigonometric period to compute the periodic responses, then asserts the zero-modulation normalization and increasing convergence trends at modulation parameters 25, 80, and 240. On execution it printed:

```text
delta0 1.0000000004061589 1.00000000081232
delta=25: KA/leading=1.04658105 KB/leading=0.71694199 KA/KB=2.90641176
delta=80: KA/leading=1.01421221 KB/leading=0.79758340 KA/KB=4.52893417
delta=240: KA/leading=1.00470393 KB/leading=0.86182092 KA/KB=7.19159095
CHECK_OK
```

The slower approach of the second normalized constant is consistent with the narrow-pulse delay of the downstream filter; it is not itself a rate-of-convergence proof. No independent audit, formal proof assistant, or external numerical certification was performed. The validity of the main claim rests on the elementary factorization and Laplace estimates reconstructed in `RESULT.md`.
