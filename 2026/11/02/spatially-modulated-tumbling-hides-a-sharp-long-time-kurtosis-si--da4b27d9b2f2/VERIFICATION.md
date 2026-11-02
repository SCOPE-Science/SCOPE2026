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

The exact monodromy formula and the second- and fourth-order coefficient comparison in RESULT.md prove the asserted asymptotic cumulant rates, under the positive two-zone switching rates specified there.

Run `python verify_monodromy.py` using Python 3.11 or later. This pure-standard-library checker numerically solves the monodromy equation with high-precision decimal arithmetic and tests 24 cases and sign relations. Its finite tests are diagnostics, not a proof of the all-parameter statement.

The result has received a self-review. Independent auditing and external validation have not been performed. Historical-priority comparison is incomplete for the full text of Angelani and Garra (2019).
