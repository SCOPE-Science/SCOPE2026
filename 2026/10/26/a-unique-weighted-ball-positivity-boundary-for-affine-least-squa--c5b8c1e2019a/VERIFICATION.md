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
The companion `verify.py` is an independent standard-library reproduction of the rational value for the effective-dimension-13 kernel integral, the elementary rational endpoint certificates, and a selection of quadrature and monotone-likelihood-ratio diagnostics.

The exact identity for \(\Phi(13)\) uses a finite binomial expansion, not floating-point quadrature. The cutoff and its uniqueness for a continuum of real effective dimensions require the analytic mixed-log-derivative and stochastic ordering proof in `RESULT.md`; the numerical samples alone do not establish them. The two-term large-parameter asymptotic uses the stated gamma-ratio expansion, not a finite sweep.

Scientific and bibliographic limitations are described in `RESULT.md`. No independent mathematical audit has been performed.
