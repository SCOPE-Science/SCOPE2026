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

The analytic proof in `RESULT.md` covers all integers \(n\geq2\) for the bound and each fixed positive integer \(r\) for joint convergence. Its critical ingredients are the vertex–edge bijection, the even Hermite covariance inequality \(\operatorname{Cov}\leq\rho^2p\), the exact mean squared correlation \(1/(n-1)\), and a Gaussian sixth-moment bias calculation. These imply the displayed \(L^2\) error bound without simulation.

Run `python verify.py` in a directory containing this file and NumPy. It enumerates actual cube-edge endpoint signs independently from their equivalent threshold inequalities for dimensions \(3\) through \(9\). For dimensions \(3,5,8,12\), it performs seeded Gaussian draws and compares observed mean-square errors with the proved analytic bound. A successful local execution printed `DIRECTIONAL_CUBE_SANITY_OK` and four dimension-specific diagnostics. The experiment does not prove an asymptotic law, certify external novelty, or assess independent verification.

The prior exact expected total vertex count is credited to Lonke; new content is the joint directional fluctuation theorem. Full mathematical claims and literature risks are in `RESULT.md` and `REVIEW.md`.
