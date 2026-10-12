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

The proof is analytic. For unit Bloch vectors \(\mathbf a,\mathbf b\) with \(c=\mathbf a\cdot\mathbf b>-1\), the collective mean has norm \(\sqrt{(1+c)/2}\). Product-state covariance reduces the transverse variance to a two-vector Euclidean minimization, and the optimizing axis is parallel to \(\mathbf a-\mathbf b\), giving
\[
(\Delta J_\perp)^2_{\min}=\frac{1+c}{4}.
\]
Substitution into the original \(N=2\) definitions gives
\[
\xi_1=\sqrt{\frac{1+c}{2}}=\cos(\gamma/2),\qquad \xi_2=1.
\]

`verify.py` independently checks the same identities on representative canonical Bloch-vector pairs, reproduces the source example \(c=-1/2\) with \(\xi_1=1/2\), and checks approach to the antipodal endpoint. The recorded checker output is in `verification_output.txt`.

The computation is supplementary; finite numerical checks are not used as proof of the quantified statement. The theorem is limited to pure two-qubit product states, the original collective squeezing parameters, and the nonzero-mean domain \(\gamma<\pi\). No statement is made about mixed states, \(N>2\), or the source's locally invariant replacement criterion.
