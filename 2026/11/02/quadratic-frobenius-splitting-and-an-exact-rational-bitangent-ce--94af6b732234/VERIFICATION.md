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
# Reproducible finite-field checks

Run `python3 verify_ciani_bitangents.py` from this directory with Python 3. The script has no third-party dependencies. It enumerates all rational projective lines in each tested field and tests geometrically squared restrictions using exact arithmetic. It checks every smooth parameter in fields of sizes 3, 5, 7, 9, 11, 13, 17, 19, 23, 25, 29, 31, 49, including three quadratic extension fields; total 204 smooth parameters.

The script must terminate with `CIANI_BITANGENT_CLASSIFICATION_PASS` and prints independently computed bitangent-frequency counts for each field. The proof in `RESULT.md` is universal in odd characteristic. These finite checks do not prove completeness over untested finite fields, and no independent audit or validation was performed.
