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

Run `python verify.py` using Python 3 with NumPy and SciPy. The program independently enumerates all labelled binary spin states for small bipartite systems, checks two distinct marginal computations against an integrated-spin formula, compares exact finite-size minority and critical Curie–Weiss distributions in total variation, and checks second-moment approach toward three quartic crossover laws. A completed execution produced 921 passing assertions and the numerical critical quartic second moment approximately 1.1708286566075303.

These are finite computations with floating-point tolerances. They do not prove the arbitrary-size total variation bound, tail estimates, joint independence, or limiting variances. Those claims rely on the analytic argument and its critical-window moment lemma in `RESULT.md`. The literature comparison is not a claim of exhaustive priority; independent scientific audit has not occurred.
