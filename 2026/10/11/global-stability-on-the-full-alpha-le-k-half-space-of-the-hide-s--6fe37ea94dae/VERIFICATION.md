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

The vector field and the candidate Lyapunov function were independently re-expanded. The exact derivative is
\[
\dot V=-\frac{2\alpha(k-\alpha)}{k}x^2
-2k\left(y-\frac{\alpha}{k}\right)^2
-2\alpha\beta b z^2.
\]
No numerical approximation enters this identity.

For \(0<\alpha<k\), all three coefficients are strictly dissipative. For \(\alpha=k\), the derivative vanishes precisely when \(y=1\) and \(z=0\); invariance then forces \(x=0\) through \(\dot z=x-bz\). This is the complete equality-case check required by LaSalle's principle.

A strict-extension witness was also checked: at \((\alpha,k,b,\beta)=(1,2,1,3)\), the extra expression in the 2022 theorem is \(4>0\), so that theorem does not apply, while the new Lyapunov derivative remains negative definite.

Limits: the proof establishes a sufficient global-stability region only. It does not show that \(\alpha\le k\) is necessary. Whole-document comparison with the 1996 original model paper was unavailable; this is retained as a literature risk rather than treated as evidence of noncoverage.
