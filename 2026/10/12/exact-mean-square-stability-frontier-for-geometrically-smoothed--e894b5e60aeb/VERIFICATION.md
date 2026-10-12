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

The embedded `verify.py` is Python 3 standard-library-only. Run `python3 verify.py` from the extracted package directory. It calculates 64 exact rational characteristic-determinant identities and independently enumerates all selection histories up to five steps for each parameter triple, yielding 320 exact moment comparisons. It checks the sharp half-probability root at representative parameters and the rational determinant witness. The finite grid is not an infinite proof; the positivity and determinant argument in RESULT.md supplies the proof for the stated uncountable parameter domain. No external verification or independent audit has been performed.
