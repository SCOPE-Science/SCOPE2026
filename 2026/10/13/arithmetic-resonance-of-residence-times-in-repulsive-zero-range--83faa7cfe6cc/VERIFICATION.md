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

# Mathematical verification

Running `python3 verify.py` with standard Python 3 checks exact two-site detailed-balance ratios for finite occupation configurations, the independently evaluated grand-canonical fugacity identity, conditional Gaussian mean bounds, one rational resonance, a denominator-three periodic correction, and an irrational equidistribution example. Actual output: `VERIFY_OK 41 rational_psi -0.133225119838 q3_residual_per_site 0.000958094765`.

The all-depth proof does not depend on those finite samples. Its essential steps are the stationary product law and entrance Little identity, a rapidly summable negative Gaussian tail, irrational rotation averages, and analytic Fourier estimates. The displayed check values are illustrations and are not certified infinite precision or evidence of publication priority. No independent audit has been performed.
