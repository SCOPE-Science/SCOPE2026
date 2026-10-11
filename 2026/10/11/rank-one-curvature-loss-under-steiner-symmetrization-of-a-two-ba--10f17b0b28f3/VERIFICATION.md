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

# Verification details

The analytic proof derives the spherical graph identity \(-D^2f_i=(W_i/R)(I+p_ip_i^{\mathsf T})\), the two hypersurface fundamental forms, and the exact transverse normal-curvature ratio \((W_1+W_2)/(2RW)\). The Euclidean norm's strict midpoint convexity proves that ratio is at least \(1/R\), with strictness when the gradients differ. Sylvester inertia converts positivity on a hyperplane into the assertion about all principal eigenvalues. Continuity gives the smooth branch-boundary cases. The 2026 primary paper supplies an explicit example with curvature below the threshold, so the dimension-free bound is sharp.

Execute `python verify.py` with standard Python 3. The script tests 16,000 transverse quadratic-form instances over four dimensions and independently evaluates the smallest generalized principal curvature of the published three-dimensional lens example. The expected successful output begins `VERIFY_OK` and reports a smallest value near 0.968946368. This is finite numerical support only; it is not a substitute for the universal proof. The source decimals are used for numerical cross-checking. No independent audit or third-party verification has been performed.
