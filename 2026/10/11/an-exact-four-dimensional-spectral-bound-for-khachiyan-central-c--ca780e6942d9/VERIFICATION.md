---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Normalized John ellipsoid B_2^4 and candidate a+AB_2^4 imply alpha=lambda_min(A) in (0,1] (det A<=1). The primary source (Theorem 1.1, Eq.5.1) gives det A<=U1(alpha),U2(alpha) for every feasible center-excluding candidate; its rank-one matrix premise was checked structurally: bb^T<=A^2, negative fractional powers reverse Loewner order, trace differentiation and integration yield the scalar lower increment. For alpha in (0,1], all logarithmic bases are positive. Independently eliminated the unsquared U1=U2 relation to exactly P/268435456 and the D2 stationary relation to alpha^3*Q/16; rational Sturm root counts give exactly one P root in (0,1), bracketed by 0.523194 and 0.523195, and one Q root in (0,1), bracketed by 0.5165 and 0.5166. Exact rational signs and D2(1/2)=3/175>0, D2(1)<0, plus D1-positive cubic prove D1(alpha*)>0 and D2(alpha*)<0. Since f_j(e^x) are convex, log Uj(e^x) are concave; thus U1 increases throughout (0,alpha*] and U2 decreases throughout [alpha*,1]. The pointwise minimum therefore has unique global maximum at the crossing, C4=0.81623940332041060897589..., below sqrt(e)/2. The n=4 explicit cone witness gives 4*sqrt(3)/9. Finite high-precision bisection serves display only; exact resultants/root counts and analytic concavity establish the global theorem.

## originality

PASS

Best-of-knowledge new evaluated scalar spectral certificate, rather than a new geometric inequality: the full-text 2026 source already gives the stronger pointwise pair for arbitrary n and alpha, so the four-dimensional inequality is mathematically a consequence once the nontrivial maximization is supplied. It neither states nor evaluates the exact 4D crossing root/envelope maximum, and explicitly does not claim a fixed-dimension optimum in Section 5.1. The submitted new part is the exact global 4D minimax of the two published functions (degree-eight crossing elimination, degree-nine derivative elimination, exact root counts, concavity), not those functions themselves. The published circular half-cone result gives the opposite, lower-witness direction only. A matching published indexed hit is a mirror of the assessed record, not earlier independent priority. This is a qualified originality PASS, not a claim that the universal 4D bound is logically independent of the published pointwise inequalities.

## value

PASS

The maximum John-ellipsoid volume after a central cut is a natural invariant in fixed-dimensional convex geometry and ellipsoid cutting-plane algorithms. The general n-dependent bounds of Zhou–Zou–Liu leave concrete fixed-dimensional quality-of-cut benchmarks unevaluated; n=4 gives a genuinely active two-constraint crossing at a nontrivial algebraic alpha* (rather than a bare parameter substitution), with an exact determinant guarantee and comparison to the canonical cone. An explicit universal improvement 0.8243606... to 0.8162394... is modest but mathematically motivated, and the root-isolation/crossing geometry can guide more refined four-dimensional estimates. A full solution of the fixed-dimensional extremal problem is NOT claimed or required for an independently useful exact benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
