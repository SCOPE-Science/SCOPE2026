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
The verification target is
\[
T_{\perp}(X_8)^2=\frac{12+11\sqrt2}{8}
\]
for the regular octagonal norm
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]

The analytical reduction in `RESULT.md` uses the norming-functional criterion for Birkhoff orthogonality and the dihedral symmetry of the unit octagon. It reduces all admissible pairs to two edge-interior branches and four vertex-arc branches.

`verify.py` checks the exact algebra of those branches. In particular it verifies the edge maxima \(49/16\) and \(2+\sqrt2\), the two sharp vertex critical points, the common value \((12+11\sqrt2)/8\), the admissible parameter intervals, and the strict domination of all subsidiary maxima.

The checker does not replace the continuum reduction: completeness of the case split is the support-functional argument in `RESULT.md`. No numerical sampling is used as proof.

No independent audit or independent validation has been performed.
