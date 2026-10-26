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

# Verification of mathematical checks

The package includes `verify.py` (Python 3 plus SymPy) and `CHECKS.txt`, the latter recorded by executing the former directly before packaging. The checker establishes 56 exact rational slope identities over both critical boundaries and generic interior parameters; four exact identities for the specific published homoclinic trajectory; and 58 exact endpoint-sign conditions for small positive integer rate triples. All checks completed successfully.

For replay, place `verify.py` in the current directory and invoke `python verify.py`. Equality is checked symbolically or as exact rational arithmetic, not by floating-point tolerance. The finite test grid does **not** prove uncountable parameter statements, global existence, asymptotic limits, or exhaustion of all possible orbits; those are proved analytically in the result. No independent audit has been performed.
