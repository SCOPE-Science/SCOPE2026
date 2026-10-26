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

Execute `python sorting_star_checker.py` from a directory containing the supplied file with Python 3.10+ and NumPy. The checker constructs star Laplacian quadratic forms independently of the proof, verifies inverse/trace formulae using exact `fractions.Fraction`, enumerates permutation chambers in low dimensions, and exhibits actual within-chamber input pairs attaining the sharp modulus to numerical precision. Expected successful message: `PASS: 2704 independent exact-rational, chamber and attaining-pair checks`.

The proof in `RESULT.md` establishes the universal result independently of these finite computations. Numerical tests are **not** a proof for all dimensions or all couplings. General weighted stars, infinite graphs, and Sobolev exponents other than the quadratic case remain unproved. The review recorded in `REVIEW.md` is not an independent validation.
