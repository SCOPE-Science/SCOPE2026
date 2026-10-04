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

The claim is proved symbolically; no numerical experiment is used as evidence.

For a two-point support \(\{x,y\}\), invariance forces each transformation to act as either the identity or the transposition. If \(T_\beta\) transposes, then \((\beta+1)(x-y)\) is a nonzero integer. If \(T_\gamma\) transposes, then \((\gamma+1)(x-y)\) is a nonzero integer. If either map fixes both points, its corresponding factor \((b-1)(x-y)\) is a nonzero integer. Therefore every case containing a transposition forces one of
\[
\frac{\gamma+1}{\beta+1},\qquad
\frac{\gamma-1}{\beta+1},\qquad
\frac{\gamma+1}{\beta-1}
\]
to be rational.

Substituting \(\gamma-1=(m/n)(\beta-1)\) and using irrationality of \(\beta\) gives, respectively: \(m=n\), a contradiction \(m/n=-m/n\), or the contradiction \(0=2\). The first would make the bases equal, which is excluded. Thus both maps act identically on the two-point support, so every support point is a common fixed point.

The final fixed-point set is independently matched to Proposition 5.1 of arXiv:2609.31156v1. The proof does not enumerate or infer anything about supports of size at least three.
