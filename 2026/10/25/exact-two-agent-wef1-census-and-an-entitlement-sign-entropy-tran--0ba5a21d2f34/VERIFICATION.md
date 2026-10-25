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

# Verification notes

Run `python verify.py` with Python 3.10 or later. No external modules or remote resources are required. The script independently evaluates both ordered WEF1 comparisons from the original bundle valuations using exact `Fraction` arithmetic, and tests the separately coded count formula. It checks all assignments with \(1\le m\le11\), all sign counts, and seven positive integer entitlement pairs, totaling \(315{,}392\) direct classification comparisons. It separately checks the exact equal-entitlement counts and the zero-total counts with asymmetric entitlements.

The executed script completed successfully. Finite enumeration is a regression check, not a substitute for the analytical proof for arbitrary \(m\), real positive entitlements, or the asymptotic limits. The probability asymptotics are established by a binomial re-encoding and elementary large-deviation/local-limit estimates in `RESULT.md`; no simulation is used as an infinite proof. The distinction between existence of a fair allocation and its frequency under uninformed random assignment is essential.
