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

The theorem is established by the symbolic proof in `RESULT.md`; no finite computation is used for the unrestricted conclusion. The standalone `verify.py` is a supplementary integer-only regression program. It constructs divisor sums by a divisor sieve, computes total prime-factor multiplicity by repeated exact division at every prime, and tests the valuation defect for every integer from 2 through 200000 having at most two prime factors. It independently generates the expected Mersenne-prime family in that interval and compares both sides exactly.

The script was run from its actual package source path before packaging. Its stored output is `verification_output.txt`:

`VERIFY_OK n_max=200000 first_defect=[2, 6, 14, 15, 62, 254, 16382] exact_integer_sieve=PASS`

Limitation: finite validation is not an infinite proof and cannot show that no independently published equivalent theorem exists. No independent external audit or validation was performed.
