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

The exact source equations are reconstructed from Table 1, SE17, in Molaie et al. (2013). Symbolic differentiation verifies \(\dot P=c-kx-q(x-y)^2\), \(\dot y=x-y\), the Jacobian trace, and the rational published coefficients. The runnable standalone `check_se17.py` is accompanied by its actual output in `check_se17_output.txt`; both belong to this package.

The key non-symbolic steps are mathematical: stationary pushforward measures under \(P\) and \(y\) have zero signed one-dimensional flux, compact support forces this flux to vanish, and invariance plus zero \(x-y\) defect forces the unique equilibrium. Liouville's determinant identity then relates averaged divergence to the sum of Lyapunov exponents under ergodicity on compact support.

No numerical integration, finite sampling, or external certification is used to claim the universal stationary identities. The result does not prove that the numerically reported chaotic attractor is a genuine compact invariant chaotic set; published numerical Lyapunov values are not substituted as exact mathematical premises.
