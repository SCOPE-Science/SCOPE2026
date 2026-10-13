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

The initiating full text was checked at the construction and proof of its main theorem. The verified source facts are:

- \(Y\) is a normal Gorenstein affine cone over an elliptic curve;
- \(\widetilde Y\) is smooth and \(\widetilde Y\to Y\) is an isomorphism outside the cone vertex;
- \(\operatorname{mld}_{0_Y}(Y)=0\);
- the cyclic action on \(\widetilde Y\) is free;
- the diagonal action on \(Y\times\mathbf A^1\) is virtually free;
- virtually free quotients preserve closed-point minimal log discrepancies;
- the distinguished origin of \(X_m\) has closed-point mld \(1\) and canonical index exactly \(m\);
- that origin is log canonical but not klt.

For a nonidentity group element, no point of \(Y\setminus\{0_Y\}\) can be fixed because its unique lift would be a fixed point of the free action on \(\widetilde Y\). Over \(0_Y\), a point with \(t\ne0\) cannot be fixed because the second coordinate is multiplied by a nontrivial root of unity. Thus the quotient is étale away from \((0_Y,0)\).

Because \(\operatorname{Sing}(Y)=\{0_Y\}\), the product has singular locus \(\{0_Y\}\times\mathbf A^1\). Étale locality of regularity gives its image as the singular locus of \(X_m\). The quotient of the invariant line has coordinate ring
\[
k[t]^{\mathbf Z/m\mathbf Z}=k[t^m],
\]
so the image is an affine line.

At any point of this line, virtual-freeness preservation gives
\[
\operatorname{mld}=\operatorname{mld}_{0_Y}(Y)+\operatorname{mld}_{t}(\mathbf A^1)=0+1=1.
\]
Outside it, \(X_m\) is a smooth threefold, hence the closed-point mld is \(3\).

The product \(Y\times\mathbf A^1\) is Gorenstein. Since the quotient is étale outside the distinguished origin, \(X_m\) is Gorenstein there; the initiating theorem gives index exactly \(m\) at the origin. Along the punctured singular line the étale-local model is the non-klt cone vertex times a smooth curve, while the initiating paper proves the origin itself is non-klt. Hence the non-klt locus equals the singular line.

The verification uses no finite sampling or computational extrapolation. The limits are explicit: the result is not a theorem about arbitrary quotient singularities, and the mld values are closed-point values.
