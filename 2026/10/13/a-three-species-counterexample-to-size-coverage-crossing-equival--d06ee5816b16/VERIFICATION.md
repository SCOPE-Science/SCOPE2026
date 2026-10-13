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

# Verification

The standalone Python script `verify.py` depends only on Python's standard library. Run it with `python3 verify.py`; success is indicated by `VERIFY_OK`.

The script evaluates the original richness and expected-coverage formulas using exact `fractions.Fraction` arithmetic for the two rational abundance vectors and checks all six strict rational margins displayed in the proof, as well as one-sample coverage, normalization, and strict majorization. It independently computes the expectations for sample sizes one through three by enumerating all possible ordered samples and weighting their occurrence probabilities. These checks establish the enumerated rational identities without floating-point approximation.

The script does **not** infer all-effort inequalities from a finite sweep. Strict noncrossing for every real effort follows from strict convexity and majorization in the written proof. Existence of the equal-coverage crossing follows from continuity and the two exactly bracketed opposite comparisons. The proof does not determine an exact crossing coordinate or all possible crossing counts, and no independent external audit has occurred.
