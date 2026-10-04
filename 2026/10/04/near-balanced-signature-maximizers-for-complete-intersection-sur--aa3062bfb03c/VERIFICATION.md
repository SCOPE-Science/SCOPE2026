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
The proof reconstructs the signature from the complete-intersection tangent bundle rather than treating a tabulated value as input. For a smooth bidegree-\((a,b)\) surface in \(\mathbb P^4\), exact Chern-class expansion gives
\[
p_1(T_X)=(5-a^2-b^2)H^2,
\]
and \(\int_XH^2=ab\). The Hirzebruch signature formula then gives the stated integer signature.

For fixed \(S=a+b\) and \(g=b-a\), the proof reduces the optimization exactly to
\[
-3\sigma=\frac{S^4-10S^2+10g^2-g^4}{8}.
\]
The parity restriction on \(g\) makes the infinite classification finite at the conceptual level: among even gaps, \(g=2\) uniquely maximizes \(10g^2-g^4\); among odd gaps, \(g=1\) and \(g=3\) tie and every \(g\ge5\) is strictly worse.

The bundled checker independently evaluates all nondecreasing bidegrees with \(6\le S\le200\), covering 9,799 cases, and confirms both the maximizer sets and the closed maximum formulas. This finite replay is regression evidence only; the parity-gap proof is the infinite argument.

Limits: codimension two, smooth complex surfaces, and the fixed-sum geography slice. No homeomorphism or diffeomorphism classification is asserted.
