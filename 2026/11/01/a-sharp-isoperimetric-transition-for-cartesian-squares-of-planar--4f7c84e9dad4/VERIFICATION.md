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

# Reproducibility and proof boundary

`verify.py` uses exact rational arithmetic to enclose \(\pi\) through an alternating-series proof of Machin's identity, checks that the quartic discriminant factorization is correct, and certifies strict negativity of the derivative of its remaining factor in Bernstein form on four intervals covering \([0,1]\). It also checks the root-defining sign bracket and rational inequalities separating regular pentagons from regular hexagons. Symbolic identities use SymPy; every inequality is tested by Python `Fraction` intervals rather than floating-point sampling.

Run the standalone script with `python verify.py` after installing SymPy. Success prints `PASS: rational pi, four-interval strict monotonicity, root brackets, polygon cutoff, discriminant, Steiner coefficients`.

The geometric polynomial is derived analytically by splitting the four-dimensional parallel volume into zero, one, or two exterior planar components. The global real-root classification relies on the exact discriminant sign and the small-isoperimetric-quotient root limit; the script verifies the critical nonstandard algebra and signs but is not a separate independent proof audit. Historical priority remains subject to the source comparisons in the review.
