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

The accompanying `verify.py` performs exact integer-coefficient checks of the algebra used in the proof. It reconstructs the derivative numerator from
\[
p(v)=v+v^2+v^3+v^4,\qquad L(v;t)=t\,p(v)-v^5-1,
\]
verifies
\[
P=(v-1)(v+1)v^5R(v+v^{-1};t),
\]
and independently verifies the stated expansion of \(R(2+z;t)\).

The infinite-domain conclusion is not delegated to finite computation. It follows from the displayed coefficient signs for \(0\le t\le(\sqrt{11}-2)/2<1\), reciprocal symmetry, and positivity of the remaining derivative factors on \(\mathscr V_1^+(\theta)\).

The verification does not test or claim anything for \(k\ge6\), for nonhomogeneous boundary laws, or for models outside the cited source reduction.
