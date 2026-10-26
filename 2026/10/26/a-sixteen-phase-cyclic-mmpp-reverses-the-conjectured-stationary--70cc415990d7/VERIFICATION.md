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

The analytic proof in `RESULT.md` is self-contained and requires no computation or external files to establish the sign crossing. It checks the hypotheses (irreducible sixteen-state chain, strictly positive rates, correct stationary and Palm phase laws), derives an exact Fourier integral, and bounds the entire modulation remainder uniformly by a strict margin. The derivative at zero supplies the opposite sign. This is an infinite-precision analytic certificate for the specified finite-state process, not an inference from a finite numerical scan.

`verify.py` is an optional reproducible independent arithmetic check using `mpmath`. It constructs the generator and arbitrary-precision matrix exponentials at the specified time, asserts the sign, and prints the values. Numerical agreement alone would not certify the theorem, because the sign difference is small relative to the probabilities; the proof supplies the exact strict lower margin instead.

Historical interpretation remains open for the full text of arXiv:1802.08400, whose abstract claimed a general stochastic order but whose later same-author work treats it as a conjecture. The present review does not assess independent validation.
