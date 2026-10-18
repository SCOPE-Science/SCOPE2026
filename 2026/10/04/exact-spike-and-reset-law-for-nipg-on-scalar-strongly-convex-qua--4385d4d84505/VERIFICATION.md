---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For f(x)=a x²/2, g=0, exact NIPG1/2 prox has x_{k+1}=(1−at_k)x_k, source A1=A2=a|x_{k+1}−x_k|², and positive x_k,t_k makes strict curvature test equivalent to at_k>c0; then next step resets exactly t_{k+1}=c1/a. If at_k<=c0, expansion factor 1+gamma'_k is safe for NEXT iterate uniformly iff gamma'_k<=2/c0−1, sharp at at_k=c0 because objective ratio (1−at)^2>1 iff at>2. At source initialization t_-1=t_0=c0/a, test equality selects expansion, source ratio branch only caps gamma when t_k/t_{k-1}<1, so gamma'_0=gamma0. Any arbitrarily large finite gamma0 can be first entry of positive summable sequence; F(x2)/F(x1)=[1−c0(1+gamma0)]² is unbounded, while t2 resets to c1/a (take gamma avoiding accidental x2=0). Verified source Algorithm3.1 pp.6–7 including strict test and gamma conditional, and exact rational illustrative source replay; proof holds for all admissible scalars, finite checks are corroborative.

## originality

PASS

Best-of-knowledge statement-level comparison against original and broader sources, with explicit covered components and material-access residual risks. A failed search is not proof of novelty.

## value

PASS

An explicit sharp one-step safety cap and arbitrarily large objective spike reveal a quantitatively important missing finite-transient guarantee of a concrete adaptive proximal algorithm whose convergence theorem only controls eventual descent. Even on a strongly convex quadratic, initial monotone descent does not preclude a huge next jump; the post-hoc curvature reset identifies why. This motivated failure mode can guide safe adaptive expansions; it does not purport to invalidate asymptotic convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
