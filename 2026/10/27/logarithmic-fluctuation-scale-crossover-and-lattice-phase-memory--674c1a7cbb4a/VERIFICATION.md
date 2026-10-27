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

The proof reconstructs the magnetization as a circular average of length-\(t\) products of iid signs. Exact overlap counting proves its covariance for every \(u+v<N\), and the covariance-tail bound plus independent block decomposition establishes joint Gaussian convergence at diverging logarithmic observation times.

Run `python verify_kac.py` using Python 3 and NumPy. The standalone script enumerates all scatterer configurations at small ring sizes to check the exact mean and covariance, verifies positivity of finite limiting covariance matrices, and compares finite-time covariance to its limit. These arithmetic checks do not prove convergence; see the uniform Lindeberg block proof in RESULT.md. The sourced annealed fixed-horizon covariance is prior work and is not presented as novel. The 2004 thesis has an incomplete full-text comparison, so priority is provisional pending independent examination.
