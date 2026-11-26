---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility checks

With the retained `verify.py` and `rational_certificate.json` in the same directory, execute `python3 verify.py` with a standard-library Python 3 installation. The certificate gives a common denominator and all 17 numerators. The checker verifies the formal transfer equations after clearing the common denominator by exact integer polynomial arithmetic. The five grouped transfer equations and numerators in `RESULT.md` give the same identities. Uniqueness of the formal solution proves the infinite-family generating-function identity.

The script also compares all coefficients against direct enumeration of 74,898 edge subsets over ladder orders 1–6 and checks the total-count recurrence through order 39. Its potential check and degree and leading-coefficient comparisons through order 200 are consistency checks against the already known extremal results, not an originality claim. See the retained `verification_output.txt` for the recorded output. These finite checks do not replace the formal transfer proof.
