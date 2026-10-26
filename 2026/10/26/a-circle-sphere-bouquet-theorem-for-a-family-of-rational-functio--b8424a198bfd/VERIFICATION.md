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

# Verification notes

The general proof is elementary topology, not a finite computer experiment. All critical steps can be checked symbolically and topologically:

1. Differentiate \(q(y)-x(c-p(x))\) to verify smoothness and the simple zero condition \(h_c'(r)=-rp'(r)\ne0\).
2. For \(q(y)=1\), write \(y=a+ib\), obtain \(a\cdot b=0\), \(|a|^2=1+|b|^2\), and verify the explicit deformation retraction in RESULT.md at both endpoints.
3. Near each simple root use \(u=h_c(x)\) to identify the total space over a disk with \(q^{-1}(D)\), which is star-shaped under real scaling. The radial segment preimage is also star-shaped.
4. Trivialize \(q(y)=h_c(x)\) away from its zeros by a locally chosen square root. Glue by homotopy pushouts along regular fibers over a loop and \(m\) attached stems.
5. Collapse the first mapping-torus fiber and check that \(M_\varphi(A)/A\simeq S^1\vee\Sigma A\); the remaining cone attachments are null on \(A\), adding \(m-1\) suspensions.
6. Independently compute \(\chi(F_{p,c})=(-m)(1+(-1)^{n-2})+m=m(-1)^{n-1}\), which matches the wedge. This numerical check alone is not a homotopy proof.

No claim is made about exceptional levels, arbitrary rational functions or independent verification. Historical mathematical priority is not externally certified.
