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
# Reproducibility and proof scope

Run `python verify.py` in the package directory, using standard Python 3.10 or later. The program reports a total assertion count on success and exits nonzero on a failed check. It has no network dependencies and does not read any other file.

The verification checks exact rational Walsh kernel values, full matrix inversions, positivity of the resolvent, probability preservation, off-diagonal signs, 2-coordinate cubic signs, exact binomial central moments, and strictly improved returns after rational pair balancing. It also checks numerical root ordering and the two-correction asymptotic for an explicitly finite dimension range. Finite instances, numerical root finding and finitely many rational tests **do not** prove any real-parameter or infinite-dimensional assertion.

The all-dimensional correctness evidence is the self-contained proof in `RESULT.md`: graph-semigroup resolvent positivity, complete Walsh eigenbasis, pair-balancing convexity, the deletion coupling for sample means, and a controlled binomial moment expansion. Published general Markov resolvent formulas and earlier scalar Crank–Nicolson positivity theory are acknowledged, not counted as new.

Independent scientific audit has not been performed.
