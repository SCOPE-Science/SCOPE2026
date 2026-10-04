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

The proof has two exact probabilistic reductions and two algebraic checks.

For the interior law, normalized barycentric coordinates have the Dirichlet \(\operatorname{Dirichlet}(1,1,1)\) moments stated in `RESULT.md`; substituting them into the iid variance identity gives \((a^2+b^2+c^2)/18\).

For the boundary law, choosing a side with probability proportional to its length and then choosing a uniform point on that segment gives exact first and second vector moments. Substitution in coordinates \(A=(0,0)\), \(B=(c,0)\), \(C=(u,v)\), with \(u=(b^2+c^2-a^2)/(2c)\), gives
\[
\mathbb E\|Y-Y'\|^2=\frac{a^3+b^3+c^3+3abc}{6(a+b+c)}.
\]

`verify.py` symbolically replays this coordinate simplification, the side-length gap, the semitangent positive expansion, and the conversion to the \(s,R,r\) formula. It was executed successfully from the packaged path before embedding.

The strict inequality is not inferred from the symbolic checker: the proof itself writes the gap numerator as a polynomial with strictly positive coefficients in \(x=s-a\), \(y=s-b\), and \(z=s-c\), which are positive exactly for a nondegenerate triangle.

Limits: this verification does not claim anything for degenerate triangles, non-Euclidean metrics, powers other than \(p=2\), or arbitrary planar convex bodies.
