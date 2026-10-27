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

# Reproducible verification

Run `python3 verify.py` from this folder. No external dependencies are required. It solves an exact finite-state absorbing coupon chain with states (unseen types, types seen exactly once). A new unseen type increments the singleton count; a repeat of a singleton removes it; repetitions of a multiply-seen type leave these states unchanged. The program checks exact rational means and mixed moments against the harmonic identities for every \(2\le n\le14\), and exact second moments for \(3\le n\le14\). It also prints large-sample numerical diagnostic ratios. Output ends with `VERIFY_OK` on success.

The proof of the infinite two-scale convergence is analytic. Finite rational-state checks are *not* an exhaustive infinite-size certificate, and the numerical asymptotics are diagnostics only. The independently audited status remains not performed.
