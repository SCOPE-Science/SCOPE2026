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

The exact identities \(\mathbb E(S_n)_j=(n)_j(\lambda/n)^j\) were derived by counting ordered distinct successful coordinates. Uniform integrability for orders below \(k\) follows from the bounded \((j+1)\)-st factorial moment. The order-\(k\) inequality follows from lower semicontinuity.

For attainability, the correction matrices \(((i)_j)_{0\le j,i\le r}\) are triangular with nonzero diagonal \(j!\), hence invertible for each \(r\). The tail estimate \(\mathbb E[(Y)_j\mathbf1_{Y>n}]\le t_n/(n-k+1)^{k-j}\) follows by comparing the falling factorials pointwise on \(Y>n\). These facts justify the stated correction sizes. The positive Poisson component dominates the signed corrections for all sufficiently large \(n\), ensuring nonnegative masses.

The construction yields exact finite-n factorial moments, support in \(\{0,\ldots,n\}\), and weak convergence to the target law. No numerical experiment is used as proof. The claim does not provide rates of convergence or a classification of higher moments.
