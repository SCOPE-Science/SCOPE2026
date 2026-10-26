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

The accompanying `verify.py` is standalone Python standard-library code. It represents \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\) by irreducible binary polynomials, builds every ordered orthonormal frame in each finite test dimension, and computes the generator coordinates in each frame using bilinear dot products. The code directly compares each full empirical graph-support histogram against the formula, checks full orbit sizes and orthogonal-group orders, and divides by the factorial of the dimension to obtain basis classes.

In addition to representative-vectors checks, every nonzero generator vector was checked in dimensions and fields \( (q,d)=(4,3),(4,4),(8,3)\), amounting to \(63\), \(255\), and \(511\) separate vectors, respectively. The explicit tested pairs \((q,d)\) are \((2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4),(8,2),(8,3)\), with several vectors in each parameter pair chosen to encounter the different orbit cases. A local execution of the included source returned `VERIFY_OK`; no external certification is claimed. The \(q=2\) cases test an excluded boundary only. All infinite-domain assertions rely on the algebraic and group-theoretic proofs in `RESULT.md`, not finite exhaustive checks.

Scientific limits: the theorem requires nonzero generator, zero annihilator, one-dimensional algebra square, characteristic-two finite extension degree at least two, and dimension at least two. Any identification with results outside those hypotheses needs a separate argument. Independent audit has not been performed.
