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

For \(n\ge2\), the source change of variables satisfies
\[
q_1z_1^2
=
w_1^2+(q_1-1)w_2^2.
\]
After multiplication by the source prefactor \(\sqrt{q_1}\), the Jacobian factor is
\[
\frac{w_1}{
\sqrt{w_1^2+(q_1-1)w_2^2}
}.
\]
It is at most \(1\), and is strictly below \(1\) whenever \(q_1>1\), because \(w_2>0\) on the integration chamber. The transformed coefficient sequence
\[
1,\ q_1+q_2-1,\ q_3,\ldots,q_n
\]
has prefix sums \(1,r_2,\ldots,r_n\), so the same prefix-defect identity shows that its quadratic form is at least \(\sum_jw_j^2\). Therefore the strict Jacobian loss cannot be cancelled by the exponent.

When \(q_1=1\), put
\[
\delta_k=r_k-k\ge0,
\qquad
z_{n+1}=0.
\]
The coefficient identity
\[
q_j-1=\delta_j-\delta_{j-1},
\qquad
\delta_0=0,
\]
gives
\[
\sum_{j=1}^n(q_j-1)z_j^2
=
\sum_{k=1}^n
\delta_k(z_k^2-z_{k+1}^2).
\]
Every square difference is strictly positive on
\[
z_1>\cdots>z_n>0.
\]
Thus any nonzero prefix defect makes the Gaussian comparison strict.

The bundled checker verifies the algebraic identities symbolically and tests exact rational admissible examples. The analytic positivity argument, not finite testing, proves the theorem for all dimensions and all admissible parameters.

Unproved limits: no quantitative stability modulus and no global equality classification for the full polytope theorem. In dimension one, direct rescaling makes the normalized comparison an identity and therefore prevents rigidity.
