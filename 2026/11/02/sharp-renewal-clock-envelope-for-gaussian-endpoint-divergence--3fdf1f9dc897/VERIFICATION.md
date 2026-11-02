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

# Reproducibility and limits

Use `python3 verify.py` with Python 3.9 or later. It requires no external libraries and returns a zero exit status only if all assertions pass. The verification covers direct numerical integration of two Gaussian densities, the analytic Gaussian divergence formula, tangent optimality, global supporting-line bounds, Jensen bounds for random finite renewal laws, sharp two-point approximation, inflection uniqueness, and small- and large-width limits. The program produced `PASS: 7123 finite assertions` in the reviewed package.

The proof of the sharp infinite class of waiting-time distributions appears in `RESULT.md`; no finite grid verifies a universal quantifier. Asymptotic series come from analytic Taylor expansion at a simple root. The endpoint functional is a lower-bound-style information-theoretic benchmark and is not presented as the path-space entropy production of an implemented reset device. No independent audit has been performed.
