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

The exact symbolic checker `verify.py` uses SymPy to replay the new local calculation from the source sphericity formula.

It checks the homogeneous coordinate identity
\[
2(a^2+2b^2+c^2)=(a+c)^2+(a-c)^2+4b^2,
\]
so with \(u=a+c\), \(v=b\), \(w=a-c\),
\[
h([u:v:w])=\frac{u^2}{u^2+w^2+4v^2}.
\]

For the aspect \(-1\) line \(u=0\), it differentiates both affine charts needed to cover the line. In the chart \(w=1\), the Hessian at \(u=0\) is
\[
\operatorname{diag}\left(\frac{2}{1+4v^2},0\right),
\]
with zero mixed term. In the remaining chart point, represented in \(v=1\), the same normal nondegeneracy is checked directly.

For the aspect \(1\) point, the chart \(u=1\) gives
\[
h(v,w)=\frac{1}{1+w^2+4v^2},
\]
and the checker obtains zero gradient and Hessian eigenvalues \(-8\) and \(-2\).

The checker does not reprove the source's geometric inputs: that the form map is a Nash submersion, that sphericity is a submersion away from aspect \(\pm1\), or that the similarity quotient is a principal bundle and sphericity descends. Those statements were inspected in arXiv:2610.02087v1.

Limits: the verification is local and differential-geometric. It does not compute global topology or compactness of the critical manifolds.
