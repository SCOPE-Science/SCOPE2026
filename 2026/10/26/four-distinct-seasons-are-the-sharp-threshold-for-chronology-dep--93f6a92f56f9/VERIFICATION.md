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

# Reproducibility and verification

`verify.py` is a standalone Python 3 standard-library script. It computes Taylor polynomials and rigorous geometric-tail bounds with exact rational fractions. For every nonnegative two-by-two matrix `C_i`, the maximum row sum is at most `28/5`; truncating the exponential at degree 60 leaves each entry between the nonnegative partial sum and that sum plus `((28/5)**61/61!)/(1-(28/5)/62)`. Positive-matrix multiplication preserves entrywise bounds. Scalar exponentials are enclosed similarly at degree 120. The script compares the resulting exact lower and upper bounds to integers and proves that the two seasonal orders lie on opposite sides of the Perron threshold.

It additionally tests the four-factor trace difference for several rational contrasts and migration rates, the six three-factor permutations, and the exactly three quartic permutation trace classes. These finite checks are not proofs of the universal formulas; those are derived algebraically in `RESULT.md`. The checker makes no independent-certification or general scientific-priority assertion.

Independent audit has not been performed.
