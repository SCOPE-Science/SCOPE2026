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

# Reproduction checks

The accompanying `check_escape_wavelet.py` computes finite eigenvalue samples from normalized incomplete beta functions; for the integer-weight check \(p=1\) it also uses elementary differences of powers. It tests finite truncation agreement with trace \(pL\), strict top-mode placement, thin and finite-relative-width operator norms, integer and fractional Schatten moments, and explicit gamma constants. Execution in Python with the versions listed in `requirements.txt` reported **PASS 152 total assertions including Schatten tests**.

For completeness, the exact trace comes from summing the beta-prime densities analytically; truncated numerical sums only check it to the stated finite tolerances. The asymptotic results are proved by the uniform exponential majorant and dominated Riemann sums, not by fitted convergence plots. No general-purpose machine proof or independent mathematical audit was performed.

Conventions: \(p>0\), \(q>0\) fixed; area density \(p(1-|z|^2)^{p-1}/\pi\); radial coordinate \(t=|z|^2/(1-|z|^2)\). The scalar gamma function in the asymptotic constants is the ordinary Euler gamma function, and every operator trace is on analytic Bergman space.
