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

# Reproducibility checks and limits

The complete proof is in `RESULT.md`. Run `python3 verify.py` from the same directory; the script requires only the Python standard library. It checks the exact startup coefficient, both boundary orders of the BDF2 negative-binomial convolution, direct low-index coefficient recurrences, seven positive finite-index differences for the uniform density, and logarithmic scaling at three large indices. It also evaluates two nonuniform order-density endpoints. Its tests are numerical and finite; they do not establish the asymptotics, eventual sign, or absolute summability. Those conclusions depend on the analytic ratio expansion, endpoint Laplace integration, and Abel argument in the proof.

The source model has a uniform order density in Ren–Su, while the theorem assumes a general nonnegative integrable density with a power endpoint. A separate independent mathematical audit has not been performed.
