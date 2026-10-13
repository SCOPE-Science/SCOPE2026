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

The supplied `verify.py` enumerates every \(n\)-step path for \(2\le n\le14\) and uses Python `fractions.Fraction` for all probabilities, comparing all four cells and total variation to the exact binomial-coefficient formulas. It also verifies the parity equalities and strict central-binomial decrease for indices \(1\le k\le30\). Execute `python3 verify.py` in the directory holding this file and the program. Success prints `VERIFY_OK` and the path count; these finite experiments are not a proof for arbitrary \(n\). The complete analytic proof, including the Catalan excursion factorization, the endpoint-only adjacent-level event, and the parity sign comparison, is in `RESULT.md`.

Scientific scope is limited to symmetric nearest-neighbor walks and the first two shifted order statistics; ties between observed heights count as repeated observations. Originality relies on substantive statement comparisons with the inspected primary literature, with unresolved older rank-statistics bibliographic risk. No independent audit or external certification was performed.
