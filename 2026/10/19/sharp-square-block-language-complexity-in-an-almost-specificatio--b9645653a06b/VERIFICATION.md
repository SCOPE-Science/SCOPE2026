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

Run `python3 verify.py` with Python 3. No third-party dependencies, network access, external mathematical packages, or paper downloads are required.

The verifier independently enumerates all words up to length five in both specified symbolic languages and compares their counts with the exact free/good renewal recurrence. It checks twenty tail identities with `fractions.Fraction` and independently confirms the rational constants \(31/36\), \(72/5\), \(1296/25\), \(864/25\), and \(3456/25\).

The asymptotic claim holds for unbounded word lengths. No finite enumeration, including this one, proves the subexponential convolution estimate, the geometric renewal-tail theorem, or existence of all square phases. Those infinite arguments are in the proof. The independently sourced general renewal theorem is cited there. There has been no independent mathematical audit.
