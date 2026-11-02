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

The accompanying `verify.py` is an ordinary Python 3 standard-library checker. Running `python3 verify.py` reconstitutes the state-transition generator and solves a normalized stationary balance system using exact `fractions.Fraction` arithmetic, independently of the rational stationary formula in RESULT.md.

A successful run emits `VERIFY_OK assertions=2103`. It verifies 288 sets of exact-rational parameters, including 1,152 stationary balance-equation checks, exact stationarity, normalization and positivity, and the sign of the analytic quadratic. Additional checks include the strictly negative–positive–negative rational witness, the critical colonization threshold on a broad numeric grid, and the finite tangency formulas.

The all-real-rate phase classification is proved analytically; finite checks are not treated as a substitute for the proof. The proof does not address larger metapopulation networks or field measurement. The literature comparison is limited by access to several full historical papers. There has been no independent audit or independent external validation.
