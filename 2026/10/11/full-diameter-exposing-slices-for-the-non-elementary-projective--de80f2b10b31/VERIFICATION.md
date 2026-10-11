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

The proof was checked directly against the focal construction. For every \(j\) and \(n\), \(f_j(w_{j,n})=r_n\), so \(r_n\le\|w_{j,n}\|_Y\le1\). Hence the normalized tensors used in the proof approach the exposing level \(1\).

For the auxiliary functionals, their values on the three bidual generators are exactly
\[
(1,0,-1),\qquad(0,-1,1),\qquad(-1,1,0),
\]
and their norms on \(\frac14B_{c_0}\) are respectively at most \(1/2\), \(1/2\), and \(1/3\). Because every finite generator \(w_{j,n}\) is \(r_nP_nz_j\) and these functionals use only the first two coordinates, all generator values have absolute value at most \(1\). Thus the induced operator \(C:X\to Y^*\) has norm \(1\).

The separating bilinear form then gives the exact lower estimate
\[
\|v_{1,n}-v_{2,n}\|_\pi\ge r_n\left(\frac1{t_{1,n}}+\frac1{t_{2,n}}\right)\ge2r_n.
\]
Since \(r_n\to1\) and both tensors are unit vectors, the slice diameter is exactly \(2\). The symmetric statement uses only the published identities that \(J\) is isometric and \(\Psi(Jv)=\varphi(v)\).

For the main broader-coverage check, choose \(n\ge3\) with \(r_n>1/2\) and \(3(1-r_n)<B<3r_n\). On the exact generating set of \(B_Y\), the functional \(h=2e_1^*+e_n^*-Be_{n+1}^*\) has the unique uniform maximum \(3r_n\) at \(w_{1,n}\); hence it strongly exposes that generator. This independently verifies that the factorwise local-diameter-two tensor theorem cannot be used through \(Y\). Also, \(B_{X^*}=\{(a,b):|a|\le1,|b|\le1,|a+b|\le1\}\) is a hexagon, so \(X^*
ot\cong\ell_1^2\); since \(X^*\) is an \(L\)-summand of \(Z^*=X^*\oplus_1Y^*\), the focal \(Z^*\) is not an \(L_1\)-space. These checks separate the final claim from the strongest directly relevant global diameter-two sufficient hypotheses inspected.

No finite enumeration is used to establish the quantified statement over all \(\alpha>0\). No claim is made about all exposing functionals or the higher-degree constructions.
