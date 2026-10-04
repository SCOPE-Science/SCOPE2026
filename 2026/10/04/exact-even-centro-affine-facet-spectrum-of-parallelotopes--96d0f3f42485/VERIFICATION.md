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

The proof was checked at the level of definitions and exact formulas. The critical steps are:

1. For an invertible linear map \(A\), a facet normal \(u_i\) transforms through \(A^{-T}u_i\). The codimension-one Jacobian cancels the normalization of the transformed support value, giving \(m_i'=|\det A|m_i\).
2. For a ridge with normals \(u_i,u_j\), the codimension-two Jacobian contains \(\lVert A^{-T}u_i\wedge A^{-T}u_j\rVert/\sin\theta_{ij}\), while the transformed sine angle contains the same wedge norm divided by the two transformed normal lengths. Together with the transformed support values, this gives \(c_{ij}'=|\det A|c_{ij}\).
3. On \(\prod_k[-a_k,a_k]\), every signed facet has mass \(2^{n-1}\prod_k a_k\), and every ridge joining distinct coordinate directions has conductance \(2^{n-2}\prod_k a_k\).
4. Even facet functions reduce to \(n\) coordinates. The exact identity
\[
\sum_{i<j}(x_i-x_j)^2=n\sum_i(x_i-\bar x)^2
\]
then proves the quadratic-form equality and the spectrum.

`verify.py` uses exact rational arithmetic and independently checks the box formula for nonconstant test vectors in dimensions \(2,3,4,5\). The observed output is:

`VERIFY_OK exact box Rayleigh identity in dimensions [2, 3, 4, 5]`

The script does not certify the theorem for arbitrary dimension or arbitrary affine images; those parts are proved analytically above. No numerical approximation or finite enumeration is used to infer an infinite statement.
