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


# Reproducibility and scope

Run `python3 verify.py` from this directory in a standard Python environment. The script recomputes the Pell and companion sequences; for indices \(1\le n\le40\), it uses exact rational upper/lower bounds for the infinite reciprocal tail to check the predicted integer part. It separately checks all forty residue classes, an exact Pell congruence, and quadratic-field expressions for three asymptotic coefficients. It reports `VERIFY_OK` on success.

The infinite assertion is established in the five-step proof in `RESULT.md`. Rational bracketing of forty test indices is not substituted for the global proof. The inequalities used in the proof bound the entire omitted binomial tail for every \(n\ge3\); the two remaining indices are handled by exact short rational comparisons. Prior asymptotic results on the same sequence are credited in `RESULT.md`, rather than being relabeled as new.
