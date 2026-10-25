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

The following checks were performed on the new claim and its embedded files:

- Reconstructed the weighted kernel from the one-zero decomposition formula and factored the numerator exactly.
- Verified the identity
  \[
  |rz+r^2-2|^2-|((2r^2-1)z-r)|^2
  =(1-r^2)\left((4r^2-1)|z|^2-6r\operatorname{Re}z+4-r^2\right).
  \]
- Proved the bracket is at least \(3(1-r)^2>0\) on \(|z|\le1\), which rules out zeros of \(P_r\) on the closed bidisk.
- Reduced the sharp minimum to the torus and handled both regimes \(r^2\le1/2\) and \(r^2\ge1/2\); the exact minimum is attained at \(z=v=1\).
- Checked the endpoint \(r=0\) directly, obtaining \(P_0(z,v)=2-zv\) and minimum \(1\).
- Verified the rotation from \(a\in\mathbb D\) to \(r=|a|\), so the margin is \((1-|a|)^2\) for any interior zero.

The proof is analytic and covers the full parameter range \(0\le r<1\); no finite experiment is used as proof. The sharp margin is for the canonical polynomial numerator, not for the full kernel modulus. The perturbation threshold follows from the triangle inequality and is sharp at equality by a constant perturbation. The general kernel formula is prior work; the exact minimum and stability radius are the claim under review. Independent audit and independent validation have not been performed.
