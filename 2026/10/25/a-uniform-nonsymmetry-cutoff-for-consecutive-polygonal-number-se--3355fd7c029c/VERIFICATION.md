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

# Reproducible mathematical checks

Run `python3 verify.py` using Python 3 standard library. It tests polygonal arithmetic, pair gcd bounds, the strict cutoff inequality, independent shortest-path Apéry computations for the triangular boundary, and small nontriangular instances. Expected last line begins `VERIFY_OK`.

The complete proof for all parameters is the symbolic gcd and gluing argument in `RESULT.md`. Direct finite checks cannot prove its universal quantifiers. The result does not classify indices under the cutoff, and the sharp cutoff is unknown. Independent validation has not been performed.
