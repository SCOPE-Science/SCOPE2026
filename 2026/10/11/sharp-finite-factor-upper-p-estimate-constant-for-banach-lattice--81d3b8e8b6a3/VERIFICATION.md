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

The proof was checked symbolically against the following source statements from Martínez-Fernández--Tradacete, arXiv:2605.28988v1: the canonical factor span is an isometric \(\ell_1\)-sum (Proposition 3.10); the scalar free product has the explicit positive-sphere majorant norm (Proposition 3.13); the full free-product unit ball is the closed solid convex hull of the factor unit balls (Proposition 3.14); and Proposition 8.5 gives only qualitative upper-\(p\) preservation for two factors.

For the upper bound, the only limiting step is approximation from the closed solid convex hull. Finite lattice suprema are norm-continuous because
\[
\left|\bigvee_j u_j-\bigvee_j v_j\right|\le\sum_j|u_j-v_j|,
\]
so no unproved compactness or enumeration claim enters. The factor aggregation and Hölder inequalities hold for arbitrary finite numbers of vectors and factors.

For sharpness, the exact scalar model is used: on the positive \(\ell_\infty^r\)-unit sphere the supremum of the coordinate generators is the constant function \(1\). The norm formula forces every coefficient in a positive coordinate majorant of \(1\) to be at least \(1\), hence the norm is exactly \(r\), while each generator has norm \(1\). This gives the exact ratio \(r^{1-1/p}\).

The verification does not cover countably infinite free products, the endpoint \(p=\infty\), or an optimal formula for unequal factor constants. Same-model review passed; independent audit was not performed.
