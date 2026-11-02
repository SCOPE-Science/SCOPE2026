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

Execute `python verify.py` with Python 3, NumPy and the standard library. The code checks the exact inverse of \(I_{m-1}-m^{-1}\boldsymbol1\boldsymbol1^{\mathsf T}\), the two-observation uniform cumulative distribution, the analytic continuous-density coefficient for \(w_\rho\), and the local quadratic asymptotic. Independent seeded Monte Carlo illustrates two finite-\(\varepsilon\) tail probabilities. The verified printed completion marker is `VERIFY_OK exact_matrix_ids=13 cdf_checks=5 moment_checks=8 local_taylor_checks=21 mc_n=2000000`. Exact arithmetic verifies the linear algebra identities; the infinite-family probability and moment statements rely on the written analytic proof, not this finite computation. No external audit or independent mathematical validation was performed.
