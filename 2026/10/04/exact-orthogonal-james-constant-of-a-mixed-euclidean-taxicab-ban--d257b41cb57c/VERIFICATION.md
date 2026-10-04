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

The final claim was reconstructed from the norm and Birkhoff--James orthogonality, not inferred from the source's decimal.

The unit circle has three analytically distinct locations. On a smooth Euclidean arc, the unique support functional forces an orthogonal direction \(y=(-s,c)/(c+s)\), and at least one of \(x+y\), \(x-y\) remains in a Euclidean quadrant, giving a minimum at most \(\sqrt2\). On a taxicab edge, the support functional forces the diagonal Euclidean unit vector; either one combination has taxicab norm exactly \(1\), or both combinations are Euclidean and their smaller squared norm is at most \(2\). At an axis, the full support-functional interval is used, so nonsmoothness is not silently discarded.

For \(x=(1,0)\), every admissible orthogonal unit vector may be reduced to \(y=(a,\sqrt{1-a^2})\) with \(0\le a\le1/\sqrt2\). The two relevant norms are exactly
\[
F(a)=\sqrt{2(1+a)},\qquad G(a)=1-a+\sqrt{1-a^2}.
\]
Since \(F\) is strictly increasing and \(G\) strictly decreasing, their minimum has one global maximum at their crossing. The substitution \(t=\sqrt{(1-a)/(1+a)}\) converts the crossing exactly to \(t^4+2t^3-1=0\). The polynomial is strictly increasing for positive \(t\), so the admissible root is unique.

`verify.py` performs a separate numerical replay: bisection of the root, evaluation of the exact extremizer in the original piecewise norm, residual checks for both algebraic equations, and dense sampling of the three already-proved analytic branches. The samples are diagnostic only; finite sampling is not used as an infinite proof.

Unproved limits are bibliographic rather than mathematical: indexed searches cannot exclude obscure independent prior work. The theorem does not compute weighted or approximate-Birkhoff variants.
