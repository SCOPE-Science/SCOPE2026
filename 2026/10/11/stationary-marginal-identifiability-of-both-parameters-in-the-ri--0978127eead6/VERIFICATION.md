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

The proof was reconstructed from the defining map and invariance, with hypotheses checked at the logarithmic boundary. For \(U=X/K\) and \(Y=\log U\), the exact pointwise increment is \(Y\circ F-Y=r(1-U)\). Invariance of \(Y\) gives \(\mathbb E[U]=1\); invariance of \(Y^2\) gives \(2\mathbb E[Y(U-1)]=r\mathbb E[(U-1)^2]\). Rescaling yields \(2K\operatorname{Cov}(\log X,X)=r\operatorname{Var}(X)\).

The bundled standard-library checker was executed from its packaged path. It verifies, using exact rational arithmetic, the square expansion and the covariance/variance rescaling used in the proof. Its output is recorded in `verification_output.txt`.

Limits: the checker verifies algebra only. The infinite-measure statement is justified analytically by invariance of bounded observables. The logarithmic argument requires compact support bounded away from \(0\), and the explicit formula for \(r\) requires nonzero variance. No claim is made for stochastic, transient, noncompact, or noisy-observation settings.
