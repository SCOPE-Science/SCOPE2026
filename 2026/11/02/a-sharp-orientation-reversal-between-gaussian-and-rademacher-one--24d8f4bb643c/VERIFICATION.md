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

The standalone script `verify_rank_one.py` was executed in Python 3 without third-party dependencies. Output: `VERIFY_OK exact=7904 numerical=1123`.

Exact rational tests use independently expanded projection-residual numerators and compare them to the determinant identity over many positive-definite rational Gram matrices and four integer direction vectors, including explicit diagonal and maximally rotated examples. Deterministic numerical tests independently check the trigonometric Gaussian integral, the two-sign average, both sharp extremes, crossing orientations, and the full rotation average across multiple singular-value ratios.

The infinite-dimensional quantifiers are limited to the arbitrary number \(m\ge2\) of rows; the right input dimension is fixed at two. Finite tests are not treated as proof of the universal claim, which follows from the samplewise Cayley–Hamilton identity, the exact Gaussian integral, and exhaustive consideration of Rademacher signs. The proof does not address finite-precision effects, oversampling, other probe laws, or independently established publication priority.
