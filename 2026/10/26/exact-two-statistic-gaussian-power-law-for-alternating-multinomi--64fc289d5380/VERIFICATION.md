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
# Verification and limitations

Run `python verification/verify.py` using Python 3.10 or later. It uses only the standard library, recomputes the closed constants, and checks the folded-normal expansion, the Gaussian null variance/covariance identities, and the analytically optimal combined weight. A seeded Gaussian simulation approximates both null and small comb-shift means and their null cross-covariance. The accompanying `verification/check_output.txt` is an actual output record from the packaged script.

Finite simulation cannot prove an infinite-dimensional, iterated-limit central limit theorem; that result follows from the proof in RESULT.md. In particular, the program does not justify interchanging the limits \(N\to\infty\) and even \(n\to\infty\), does not compute multinomial power under simultaneous growth, and does not provide independent certification.
