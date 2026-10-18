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

# Reproducibility and limits
The standalone `certificates.json` gives one explicit three-color partition for each of thirteen weighted exponent rectangles. Run `python3 verify.py` alongside that JSON. The script uses only integer arithmetic and Python's standard library; it checks every tile color, the 13 exact equal-sum identities, and disjoint exhaustive translated tilings across 256 exponent pairs. The universal theorem additionally uses the elementary, fully proved fact that any side length at least three is a sum of 3,4,5 and any side length at least four is a sum of 4,5,6,7. Finite experiments by themselves are not an infinite proof; the argument in `RESULT.md` supplies the unrestricted reduction. No independent external mathematical audit has been performed.
