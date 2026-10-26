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

# Reproducibility

Run `python3 checker.py` in the extracted package directory. It has no nonstandard Python dependencies and prints a series of `PASS` checks after successful completion. Its algorithm constructs exact reduced fractions for every nonempty proper prefix and suffix, checks for any frequency collision, and deduplicates all circular rotations as complete strings. It compares those results to the mean-gap-crossing formula without using that formula in its border test. All directed necklaces with zero counts from 0 through 28 are covered, as are 500 reproducible larger cases and all closed-form distribution values through 149 zeros. The five-one strict-chord counterexample from Charlier and collaborators is checked separately to prevent an unintended broader claim.

## Proof-based reproducibility

The proof is contained in `RESULT.md`. In particular, the exact converse witness cases are: when the first zero gap is no shorter than the last, equal one-one factors of the same length; when the first gap is shorter but violates the first mean condition, one-one versus two-one factors at lengths in a 1:2 ratio; and when it violates the final mean condition, the reversed 2:1 ratio. The proof covers all nonnegative gap lengths, with the final gap positive for the one-start linear lemma. The cyclic case splits all possible admissible boundaries by first/last symbols. Burnside's formula is given with periodic cases treated separately.

## Limits

The computational sampling is finite and does not certify claims for untested lengths. The theorem makes no claims about more than three ones or larger alphabets. Self-review has passed; an independent audit has not been performed.
