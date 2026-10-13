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

No finite computation is used to establish the claim.

The initiating source verifies the following for
\[
X=\mathrm{S}_2\mathrm{Gr}(k,2n+1):
\]

- \(X\) is smooth and projective.
- The relevant \(\mathbb G_m\)-action has isolated fixed points.
- The corresponding Białynicki--Birula strata are affine spaces.
- For every \(d\ge0\), the number \(a_d\) of \(d\)-dimensional strata equals the number of \(d\)-dimensional Schubert cells of
  \[
  Y=\mathrm{Gr}(k,2n+2-k).
  \]

Brosnan's Theorem 3.5, with integral coefficients, gives
\[
M(X)\cong\bigoplus_{p\in X^{\mathbb G_m}}\mathbb Z(d_p),
\]
where \(d_p\) is the positive-weight tangent dimension. Since this is exactly the attracting-cell dimension, the multiplicity of \(\mathbb Z(d)\) is \(a_d\).

The Schubert filtration of \(Y\) has the same \(a_d\), hence
\[
M(Y)\cong\bigoplus_d\mathbb Z(d)^{\oplus a_d}.
\]
This proves the noncanonical integral Chow-motive isomorphism.

Additivity in the Grothendieck ring over affine cells independently gives
\[
[X]=\sum_d a_d\mathbb L^d=[Y].
\]

Finally,
\[
\dim X=2k(n+1-k)
\]
and
\[
\dim Y=k(2n+2-2k)=2k(n+1-k),
\]
so the common cell-dimensional grading is compatible with the ambient dimensions.

The verification does not establish, and the claim does not assert, an isomorphism of cohomology rings or Chow rings.
