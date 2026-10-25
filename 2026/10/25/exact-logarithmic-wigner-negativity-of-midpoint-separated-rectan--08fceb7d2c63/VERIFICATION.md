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

# Verification of the mathematical result

The proof derives the Wigner-channel formula directly from the overlap geometry and integrates its exact absolute value in the spatial coordinate. The decisive non-finite step is the bounded-primitive periodic averaging argument, followed by the Wigner marginal and Plancherel. The amplitude maximum uses Cauchy–Schwarz. Each step is analytic and independent of finite numerical experiments.

The companion `verify.py` evaluates forty random frequency-position samples for each of three pulse configurations by an independently coded interval-intersection formula, tests three frequency slices by numerical integration of the spatial absolute value over all channels, and reports the analytic coefficient for one, two, three and seven equal-amplitude pulses. `verify_output.txt` records the actual executed output. An independent frequency-domain quadrature in `integral_check.py` reports numerical decade-difference slopes approaching the asymptotic constants for one, two, and three pulses. The checker cannot certify the frequency-asymptotic result or literature priority; those require the proof and comparison above.
