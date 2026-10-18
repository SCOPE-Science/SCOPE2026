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

# Reproducibility and mathematical limits
Run `python3 verify.py` to check the generalized Lucas row-membership identities using exact integer-square-root evaluation of powers of metallic means. This implementation avoids floating-point endpoint ambiguity. In the submitted regression set, the three metallic parameters c=2,3,4 and odd Lucas indices m=3,7,11 give the explicitly predicted lists of rows; the script also tests 750 additional integer inputs for admissible row bounds. Successful output is `VERIFY_OK 759`.

The script does not compute the infinite densities or verify the infinite upper bound. Those claims depend on the irrational rotation, integer-point counting, norm inequality, and periodic-arc tail arguments proved in the article. No independent audit has yet been performed.
