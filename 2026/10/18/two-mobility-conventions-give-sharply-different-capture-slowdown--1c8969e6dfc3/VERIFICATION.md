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

With rates in units of a and hub departure multiplier h=m (edge) or 1 (vertex), use transient states C=distinct leaves, A=searcher leaf/trap hub, B=opposite. The killed Poisson matrix in order C,A,B has rows (1+x,−x,−1), (−hx(m−1)/m,1+hx,0), (−h(m−1)/m,0,x+h). The right side is all ones. Absorbing jumps enter the diagonal departure rates but not the off-diagonal transition terms. Searcher-only paths while the trap waits give a positive capture probability within fixed time uniformly in the finitely many states for each fixed parameter, establishing finiteness and uniqueness. Cramer's rule independently yields both normalized means with positive denominator D=(1+x)(1+2mx+x²); at x=0 both give 1, also the direct leaf-to-hub first-jump mean in original units 1/a. Subtracting 1 gives x times strictly decreasing quadratic brackets divided by D, with positive intercepts for m≥2 and roots equal to the two stated thresholds. Subtracting the two means gives (m−1)x(m−2−x)/D, so the positive crossover exists only for m>2, and for m=2 the edge mean is strictly lower at x>0. Independent symbolic expansion shows that each derivative numerator has positive constant term and strictly negative coefficients of all positive powers for m≥2. Hence each has a unique positive zero and gives the unique global maximum. Positive-polynomial gap identities give the uniform bounds (m+1)/2 and 2; evaluating both at x=m^(−1/2) proves the sharp limits by squeezing. The two positive-root scalings also check exactly. Replay: python3 /workspace/branches/independent_star.py (SymPy), output independent_star.out alongside. The proof covers real a>0 and b≥0, not just the finite rational samples in the frozen package. It is only for independent exponential walkers on a finite star and the specified initial leaf–hub pair, and only for the mean.

## originality

PASS

The general moving-trap slowdown and the product-chain method are credited background. Of the inspected exact sources, none gives or mechanically implies both evaluated fixed-start continuous-time formulas, their exact thresholds and switch, and the incompatible optimal degree scalings under the two clocks. Closely matching Resultary entries differ in clock, parameter comparison, graph, or starting law. This is a bounded assessment, not a priority guarantee.

## value

PASS

A star isolates degree dependence while holding the leaf rate fixed. The two standard normalizations give the same static benchmark and both have a slowdown interval, yet changing how the hub departs changes the largest delay from order m with sharp coefficient 1/2 to a uniform ceiling 2, attained in the large-degree limit. The crossover thresholds and maxima quantify a useful normalization-sensitive distinction for two-particle encounter models, beyond a few numerical comparisons or a textbook first-step calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
