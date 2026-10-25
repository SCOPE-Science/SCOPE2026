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

Run `python verify.py` with Python 3 and SymPy. The checker executes exact symbolic 3-cycle elimination, exceptional weighted-product checks, a six-permutation rational three-dimensional example, and the exact determinant/inverse of the full-support three-view variance map. These checks passed at manuscript preparation time.

The analytic assertion that one profile recovers its weighted-width multiset uses the classical sine Weierstrass product, nonzero zeta coefficients and Newton identities; it holds for any finite dimension and is proved in RESULT.md. The universal two-view counterexample and the exact three-dimensional fiber theorem follow from displayed algebra, not empirical tests. The script is an independent computational check of that algebra, not a proof that every possible historical source has been read.

Unproved here: stability under noisy sections; reconstruction of arbitrary oriented parallelotopes; smallest number of full-support views in higher dimension; an exhaustive global literature priority claim. Independent audit has not been performed.
