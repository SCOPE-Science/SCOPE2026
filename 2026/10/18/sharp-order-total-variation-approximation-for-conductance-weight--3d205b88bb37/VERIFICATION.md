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

The proof in `RESULT.md` is analytical and self-contained except for standard weighted matrix-tree and classical i.i.d. central limit facts. The key nonstandard identity is independently reconstructed by exhaustive enumeration in the attached executable file `verification/check_weighted_oneout.py`, using only `fractions.Fraction`, `itertools` and `collections`.

Run: `python verification/check_weighted_oneout.py`. Six finite networks of order 2, 3, 4 and 6 are enumerated without random sampling. The code verifies each tree probability, normalization, the exact TV expression, the size-bias change of mean, and the claimed bound. It reports exact fractions for all examples and ends in `All exact finite checks passed.`

The asymptotic sharpness is a mathematical deduction from the independent triangle-block construction and a standard CLT plus uniform integrability. Numerical checks do not certify a universal asymptotic statement. No independent audit has yet been performed.
