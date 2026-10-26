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

# Reproducibility and scientific limits

The exact proof in `RESULT.md` establishes the universal result by Fourier diagonalization, a strict one-dimensional polynomial root, nonnegative-stochastic kernel composition, reaction saturation, and the small-input derivative. It does not rely on a finite parameter enumeration.

Run `python verify.py` using Python 3 and its standard library; no external dependencies or online resources are required. It reports `PASS 3533 checks`, threshold `0.6093778634360062`, and the explicit witness at three-quarters of the threshold with opposite component near `-0.21351581611963422` while heat-only gives `+0.05601190446206642`.

Numerical checks include exact rational algebra at sampled values, randomized cube data, and explicit failure witnesses. They are supplementary, not exhaustive evidence for an infinite domain. Literature comparisons are source-specific and do not constitute independent novelty certification. The claim is limited to exact subflows on the four-site canonical pseudospectral grid.
