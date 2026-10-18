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

# Reproducible finite checks and proved limits

Run `python3 verify_axes.py` using Python 3 standard library only. It evaluates the convolution energy independently of its analytic fiber decomposition, then reconstructs the eight-term deficit and checks the exact identity. The tested finite abelian groups are cyclic orders 3, 4, 5, 6, 7; the Klein four group; a noncyclic group of order 8; and the elementary abelian group of order 9. There are 65 reproducibly seeded complex-integer tests per group, with additional explicit nonzero character inputs and direct dual-Fourier norm checks. The reported successful output is:

`VERIFY_OK groups=8 complex_inputs=562 exact_deficit_identity=PASS axes_extremizers=PASS fourier_normalization=PASS exceptional_order_three=PASS`

The unrestricted mathematical statement follows from the exact fiber decomposition, pointwise Cauchy--Schwarz, pairing estimates, and Fourier equality proof written in `RESULT.md`. The checker is not an exhaustive search over arbitrary functions; neither the finite random sample nor any finite enumeration proves the infinite uniform theorem. The order-three counterexample is checked but **not** within the theorem's quantified domain. No independent audit or external proof certification has been performed.
