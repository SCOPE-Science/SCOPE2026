---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The target assumes 0<p<=2 and positive integers k,m, with R exactly the sharp root from Sarkar–Das Theorem 3.1. Set s=-k log R>0, lambda=m/k. Then R^m=e^{-lambda s} and R^{2k}=e^{-2s}, so p(1-R^m)/(1+R^m)=2R^{2k}/(1-R^{2k}) is exactly p tanh(lambda s/2)=2/(e^{2s}-1). For fixed p,lambda the first side increases strictly 0 to p as s increases 0 to infinity; the right decreases infinity to 0. Thus s is unique and differentiable/continuous. F_lambda=(p s/2)sech^2(lambda s/2)>0 and F_s=(p lambda/2)sech^2(lambda s/2)+4 e^{2s}/(e^{2s}-1)^2>0 for F=p tanh-2/(exp(2s)-1), yielding ds/dlambda<0. Since RHS<=p at equality, s>=0.5 log(1+2/p)>0; as lambda->infinity, a monotone bounded s yields tanh->1 and the lower-limit equality s->0.5 log(1+2/p). As lambda->0, bounded s contradicts the equation; s->infinity, and any subsequence with lambda*s>=epsilon would keep LHS bounded away from zero against RHS->0. Thus lambda*s->0, and Taylor expansions imply (2s)exp(2s)~8/(p lambda). Positivity and monotone inversion give 2s~W(8/(p lambda)). For k_j->infinity and m_j/k_j->lambda in (0,infinity), exact R_j=exp(-s(m_j/k_j)/k_j) yields k_j(1-R_j)->s(lambda). When m=2k, set y=R^{2k}: p(1-y)^2=2y(1+y), whose sole root 0<y<1 is p/(p+1+sqrt(4p+1)); for p=2 it is y=1/3. No unproved extrapolation to p>2 or uniform boundary k,m limit. Independent SymPy checks verified the balanced-ray quadratic identity; independent 70-digit bisection checked 75 (p,k,m) roots plus 27 profile points, with residuals below 1e-48. Finite tests are corroborative, not an all-parameter proof.

## originality

PASS

Best-of-knowledge PASS for the *combined joint-order logarithmic scaling and endpoint regimes*, not for the already published sharp-radius equation itself. Sarkar–Das Theorem 3.1 determines the exact sharp root for every fixed integer pair and therefore algebraically determines the ratio profile once s=-k log R is introduced. This makes the normalization a direct re-expression, not a newly proven sharp inequality. Nevertheless the inspected source states neither the continuous profile and simultaneous k,m->infinity ratio theorem nor its two endpoint laws and balanced-ray family. Source full-text searches show no Lambert or asymptotic section. A separately published Lambert-W high-tail theorem and its companion stabilization theorem analyze p(1-r^m)/(1+r^m)=2r^N/(1-r), a genuinely different root equation; they do not specialize to the target denominator 1-r^{2k}. The independently inspected January 2026 theorem uses 2(nr)^N(1+r^m)=(1-nr)(1-r^m), also different. An older equivalent root treatment or the assessment that elementary corollaries are already covered remains a genuine novelty risk; the result is not presented as an independent discovery of sharpness.

## value

PASS

The object is the natural *sharp* radius of Sarkar–Das Theorem 3.1, reused in their JB-star-triple Theorem 4.1, and both k and m are geometric Schwarz-mapping orders. The original exact implicit equation and a short numerical table do not express how the two orders interact when both grow. The profile gives a complete continuous law for their fixed ratio, strict direction of variation, an exact ray m=2k and two different endpoint scales (finite saturation versus unbounded Lambert-W logarithmic growth). For later asymptotic analyses of this sharp radius, k(1-R) and its lambda dependence are useful precise normalizations, not an arbitrary finite parameter slice. This is a modest, elementary, self-contained quantitative result about a natural invariant, not a new Bohr inequality or a general theory; no downstream theorem is claimed or required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
