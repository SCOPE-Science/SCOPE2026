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

The finite verifier is `check_collision.py` and needs only Python 3.10 or later. Run `python3 check_collision.py` from the directory containing the file. The program constructs the Laurent-polynomial constant terms for every bias-profile coefficient and separately enumerates the independent Bernoulli convolution law with exact rational arithmetic. It tests every nondecreasing weight vector of lengths 1 through 6 with entries in 1 through 5, using six exact rational parameters, and checks strict positivity, coefficient normalization, both global bounds, the finite collision identity, and the unbiased endpoint. The completed run returned `PASS: 9681 exact assertions across all positive weight multisets of length 1 through 6 with weights at most 5`.

The universal proof does not rely on the finite test range. It uses Fourier Plancherel for finite integer-supported measures and strict positivity of trigonometric-square products almost everywhere. Explicit limits: no independent validation has been performed; no Shannon-entropy concavity or uniform fixed-length optimal envelope is established.
