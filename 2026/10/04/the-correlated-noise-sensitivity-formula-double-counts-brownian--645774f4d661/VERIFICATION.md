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

The proof uses the covariance identity for the linear SDE \(dz=Fz\,dt+G\,dB\) with \(d\langle B\rangle_t=R\,dt\). Itô's product rule gives \(M'=FM+MF^\top+GRG^\top\). For the source's diagonal diffusion matrix, its printed \(Q\) is exactly \(GRG^\top\).

`verifier.py` checks the key identities with exact `fractions.Fraction` arithmetic for a three-dimensional Hurwitz example and a nontrivial rational correlation matrix. It also checks the independent limit \(R=I\), where the source-style equation produces exactly twice the correct stationary covariance. The verifier has no external dependencies and prints `VERIFY_OK` on success.

The exact factor-of-two conclusion for the source itself does not depend on the illustrative example: it follows by linearity and uniqueness of the continuous Lyapunov equation when \(F\) is Hurwitz. No assertion is made about large-noise accuracy, global dynamics, or other results of the source article.
