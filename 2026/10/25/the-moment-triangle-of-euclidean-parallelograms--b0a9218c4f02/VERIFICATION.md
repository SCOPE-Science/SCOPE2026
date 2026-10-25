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

The structural proof uses the independent triangular-coordinate-difference law, exact second/fourth/sixth moment integration, an invertible affine map, and the complete positive-definite Gram region. The verifier tests identities but does not certify infinite assertions on its own.

With Python 3 and no external dependencies, run `python3 verify.py`. The checked package output was:

`VERIFY_OK 7449 exact checks; MC 200000 samples, relative errors [0.0013589578587013737, 0.0033457318635059345, 0.005719838727530971]`

The exact checks enumerate a reproducible seeded set of rational Gram matrices, independently evaluate moments using multinomial expansion of the triangular law, reconstruct normalized Gram invariants, verify the image triangle vertices and test 101 pairwise distinct shapes sharing the first two moments. The final Monte Carlo step independently samples two-point coordinate differences for a nonorthogonal parallelogram, checking all three moments within a prespecified relative-error threshold of 4.5%.

Limits: numerical sampling is not a universal proof; finite tests are not exhaustive. The analytic proof in RESULT.md supplies all quantified conclusions. No independent scientific audit has been performed.
