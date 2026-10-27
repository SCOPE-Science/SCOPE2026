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

Run `python3 verify_bigram.py` in the directory containing the extracted files. The independently constructed literal adjacent-pair multispectra of every one of 524280 words across lengths 3–18 agree with the exact inverse-fiber formula, the maximum, and all maximizing profiles. This includes 1524 distinct observed profiles. A further 1718065 parameter-profile checks cover lengths 19–190 and confirm the stated bound and equality classification over that finite range. The execution output `verify_bigram.out` ends in `VERIFY_OK`.

These are finite consistency tests, **not** a proof for all lengths. All-length correctness rests on the four analytic proof steps in `RESULT.md`, including handling of endpoints, ties, and imbalanced transition-count signatures. No machine-checked proof or independent validation is claimed.
