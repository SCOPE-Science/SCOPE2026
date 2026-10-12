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
The standalone checker uses \(n=3\), \(K=1\), \(G=(1,1,1)^\top/\sqrt3\), and the orthonormal complement with columns \((1,-1,0)^\top/\sqrt2\) and \((1,1,-2)^\top/\sqrt6\). For \(\sigma_b^2=\sigma_c^2=1\), it verifies
\[
\operatorname{Cov}(Z\mid\eta)=2I+BB^\top,
\]
whose eigenvalues are \(2,3,3\), in contrast to any spherical covariance in the two nontrivial subspaces. It verifies
\[
\operatorname{Cov}(B^\top Z,\xi\mid\eta)=I_2
\]
and
\[
I(\xi;B^\top Z\mid\eta)=\log(3/2)=0.405465108108\ldots.
\]

It checks equality of the normalized Gaussian likelihood for pairs of error variances \((1,1)\) and \((0.5,1.5)\), holding the latent state and all other parameters fixed, and verifies the zero eigenvalue of the error-scale Fisher information. The algebraic proof establishes this observational equality for every positive allocation with the same sum and any number of survival observations governed by the latent state alone.

Limit: simulation and finite linear algebra are diagnostic checks; the universal assertion is proved by Gaussian convolution and likelihood factorization, not by a finite test.
