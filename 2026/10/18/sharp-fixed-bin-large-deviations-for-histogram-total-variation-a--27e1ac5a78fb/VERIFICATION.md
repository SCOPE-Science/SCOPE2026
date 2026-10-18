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

The analytic proof identifies the maximizing sign patterns, applies the entropy variational inequality, and derives the lattice constant via exponential tilting and the bounded maximal-span lattice local central limit theorem. The maximum-threshold formula follows from a direct independent-set characterization of supports.

`python3 verification/check.py` ran successfully using Python and SciPy. It performed 8,212 exact rational sign-score comparisons, 75,498 exhaustive finite histogram checks, and 12 numerical comparisons with exact binomial upper tails, all passing.

The finite checker does not verify the limiting local central limit theorem, which is a standard analytic ingredient. No independent audit has been performed. The coefficient asymptotic applies only at fixed positive thresholds strictly below maximal variation, and no uniform estimates near either endpoint were tested.
