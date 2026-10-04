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

The finite verifier checks the arithmetic entering the link and Euler-characteristic calculations.

For \(\mathbb F_1\), in the basis \((S,F)\) with
\[
S^2=-1,\qquad S\cdot F=1,\qquad F^2=0,
\]
it uses
\[
K_{\mathbb F_1}=-2S-3F.
\]
It verifies
\[
K_{\mathbb F_1}\cdot S=-1,\qquad K_{\mathbb F_1}\cdot F=-2.
\]
These values generate \(\mathbf Z\), while the class \((-2,-3)\) is primitive. This is exactly the arithmetic needed for the homotopy and Gysin arguments: the circle bundle is simply connected, \(H^2\cong\mathbf Z\), \(H^3\cong\mathbf Z\), and there is no torsion in these groups.

The verifier also checks that
\[
c_1(\mathbb F_1)\equiv K_{\mathbb F_1}\pmod2,
\]
so the pullback of \(w_2(\mathbb F_1)\) vanishes on the circle bundle, and it checks
\[
2(4-108)=-208,\qquad -208-4+1=-211.
\]

The classification step turning the simply connected spin \(5\)-manifold with \(H_2\cong\mathbf Z\) into \(S^2\times S^3\) is the Smale--Barden theorem and is not replaced by finite computation. Wuebben's geometric construction and Hodge-number calculation are likewise external mathematical inputs.

The saved replay output must end in `VERIFY_OK`.
