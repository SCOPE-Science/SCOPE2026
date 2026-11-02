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

# Verification evidence and limits

The included standalone `check.py` is runnable with Python 3 and no third-party packages. It checks exact detailed-balance ratios, exact sign patterns of successive stationary likelihood-ratio comparisons, and exact cross-multiplied radial mass/tail inequalities. The integer examples use \(S=20\), \(Z_1=2\), \(Z_2=5\), \(q_1=5\), and \(q_2\in\{6,7,8\}\).

An execution of `python3 check.py` from this package passed 38,556 detailed-balance identities and 87,808 exact adjacent likelihood-ratio phase comparisons; it also passed the three-regime integer certificate. Its 1,568 floating-point comparisons of the threshold ratio are corroborative only. The strict increase of that ratio for infinitely many possible parameters follows from the fully written weighted-integral proof in RESULT.md, not from these finite tests.

The source stationary law is Eq. (10) of Mobilia (arXiv:1506.04911). Its derivation is recapitulated independently for normalization and boundary checks; it is not asserted to be novel. No external independent scientific validation or historical-priority certification has been performed.
