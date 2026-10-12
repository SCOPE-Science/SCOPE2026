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

The accepted statement is analytic. No finite computation is used as a certificate for an infinite claim.

For every scaled party \(j\), Eq. (18) has coefficients \(a_j=(1+\lambda_j)/2\) and \(b_j=(1-\lambda_j)/2\). On \([-1,1]\), both are nonnegative and satisfy \(a_j+b_j=1\). Expanding the tensor product therefore gives a convex combination of the operators \(\rho^{\Gamma_S}\) over all scaled-party subsets \(S\).

The triangle inequality and positive homogeneity of the trace norm imply
\[
\left\|\sum_S w_S\rho^{\Gamma_S}\right\|_1
\le\sum_S w_S\|\rho^{\Gamma_S}\|_1
\le\max_S\|\rho^{\Gamma_S}\|_1.
\]
At the vertex selecting \(S\), exactly one weight equals \(1\), so the bound is attained. This proves the optimization identity with no hidden regularity assumption.

If every vertex operator is positive semidefinite, the whole convex hull is positive semidefinite; thus an interior nonpositive point cannot add detection beyond the vertices. Finally, \(\rho^{\Gamma_{S^c}}=(\rho^{\Gamma_S})^T\), so complementary cuts have the same trace norm.

The proof assumes finite-dimensional tensor factors and exactly the Eq. (18) scaling family. It does not cover the broader anisotropic maps mentioned in the source's outlook.
