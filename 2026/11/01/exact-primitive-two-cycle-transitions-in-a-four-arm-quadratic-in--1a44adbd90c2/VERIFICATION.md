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
# Reproducibility and validation boundary

Execute `python CHECK.py` with a Python 3 interpreter and SymPy. The program uses symbolic algebra and rational Sturm intervals. It independently evaluates the factorizations of the two corner equations and the four composition-polynomial discriminants, and isolates every root of each admissible second-iterate branch for six rational parameters, with exact inequalities to distinguish branch domains. It also checks the two quartic parameter root brackets.

These exact computational checks supply finite parameter representatives; the parameter-uniform conclusion depends on the analytical nonvanishing-discriminant and seam-exhaustion argument stated in RESULT.md, plus the one-sided boundary-root analysis. The numerical decimal values printed in the statement are explanatory only. No claim of external or independent mathematical certification is made.
