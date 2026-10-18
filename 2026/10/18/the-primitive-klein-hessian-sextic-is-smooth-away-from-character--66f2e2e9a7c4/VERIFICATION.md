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

# Reproduction and proof limits

Run `python3 verify.py` using Python 3 with no third-party packages. The output ends with `VERIFY_OK` and reports 3358 small-field affine point evaluations. The checker recomputes the integer polynomial identity, local Taylor initial forms, characteristic-two rational points over the eight-element field, and modular product identities. The proof in RESULT.md, rather than finite arithmetic testing, handles every algebraically closed residue field and all primes. The full Elkies chapter was not accessible for a whole-document comparison. No independent audit has been performed.
