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

# Verification record

The standalone `verify.py` in this package was run successfully with Python 3, SymPy and mpmath; it returned `PASS: 129 checks; exact Radau algebra and polynomial root exclusion; high-precision samples`.

Reproduce with `python verify.py` in the package directory. It checks both rational tableau stage equations, the deleted-node indicator, symbolic elimination at the rational witness, and strict inequalities at sampled parameters using 70-digit precision. The infinite parameter classification, logit power-series positivity and sharp limiting supremum are proved in `RESULT.md`, not inferred from those samples.

Only a mathematical self-review is represented. External independent audit has not been performed.
