---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Here H=I and g∘A=|x₁+x₂|, so the exact model equals the strongly convex objective up to its base constant. With δ=1/N, h=2−δ and q=hδ², one has q<δ since hδ=1−(1−δ)². At v=(δ,−q) the penalty gradient is (1,1); Pv=(δ,−h) cancels the other linear terms exactly. Positive definiteness of P gives the unique metric proximal-gradient direction. The second vector s=(q,δ) is H-orthogonal and det[v,s]=K=δ²+q²>0. On the v-line the left and right slopes at zero are both negative; on the positive half-line the objective is Kt²/2−Dt with D=δ²+hq, so t₁=D/K. On the s-line the slopes straddle zero strictly, since S−C=δ²+(2+δ)q and S+C=δ(h−q) are positive. Thus t₂=0 and the combined-direction solve gives t₃=1. Completing the square writes the objective as ∥x−(1,−1)∥²/2−1+|x₁+x₂|−δ(x₁+x₂). The last two terms combined are nonnegative and vanish at (1,−1), so the joint decrease is one. The line decrease D²/(2K) is exactly the stated ratio; multiplication by N² and passage to δ→0 gives 25/2. Independent piecewise rational arithmetic agrees at N=3,4,256 (first two ratios 289/477 and 845/1952). The zero second solve is allowed: it does not collapse the basis, only the computed sum.

## originality

PASS

The motivating paper already contains the metric, the common-base line solves and the combined direction search. The supported distinct claim is the explicit local counterexample with exact curvature and the quantified ratio against the exact joint minimum, not the procedure, a new convergence theorem, or an algorithmic trajectory counterexample. The closest inspected prior scheme-specific work concerns loss of conjugacy caused by curvature clipping, which is absent here.

## value

PASS

This quantifies a genuine approximation gap in a proposed way to avoid a joint subproblem solve. In dimension two the example holds the smooth Hessian at identity and keeps the first direction tied to the proposed metric, so the effect cannot be blamed on curvature approximation or on choosing both directions freely. It establishes exactly which type of uniform guarantee strong convexity and exact conjugacy alone cannot supply, and points to conditioning and trajectory assumptions relevant to sharper guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
