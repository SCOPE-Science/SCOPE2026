---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Independently checked seven actual pinned/current Git blobs and reconstructed source tree c0c0c6158266c9049da7e778110103a808cab531. Theorem 3.1 of Bárány et al. gives F/L=E[q(U²)^(d−1)] with U~Beta(d,n−d+1), q(z)=sin(π√z)/(π√z). The second beta moment E U²=d(d+1)/((n+1)(n+2)) and exact size-biasing change U² density to V~Beta(d+2,n−d+1), so R=E h_d(V²), h_d=(1−q^(d−1))/z. Since q(z)=∫_0^1 cos(πt√z)dt and d²/dz² cos(a√z)=a[sin(a√z)−a√z cos(a√z)]/(4z^{3/2})>0 for 0<a≤π, 0<z<1, q is strictly convex and nonnegative. q^(d−1) strictly convex for d≥2; hence h_d is strictly decreasing by strict concavity of 1−q^(d−1). Independent Gamma(d+2), Gamma(n−d+1), Gamma(1) coupling gives V_{n+1}<V_n almost surely, proving strict R growth. E V_n=(d+2)/(n+3)→0, bounded h yields limit (d−1)π²/6. n=d+1 gives a spherical simplex and F=d+1 exactly. Lower equality is unique n=d+1; finite-n upper is strict and its coefficient asymptotically optimal. No dimension-uniform limit is asserted. Independent mpmath checks covered 63 d,n pairs (d=2..8, nine n per d), max transformed-vs-original discrepancy 3.67e−55, 29 strictly positive q second derivatives; finite experiments corroborate rather than establish universal theorem.

## originality

PASS

Best-of-knowledge comparison against the three most relevant primary papers and independent semantic database searches finds prior exact F_{d,n}, its n^{-2} asymptotic, broader raw-facet monotonicity, and all-face finite-size formulas, but no prior strict ordering of R_{d,n} or the pair of globally sharp finite-sample deficit bounds. The new step is an explicit beta-second-moment tilt combined with strict decrease of a sinc-secants kernel, a mathematical all-n comparison not contained in raw monotonicity/asymptotics alone. The status is priority-qualified, not a guarantee of absolute novelty.

## value

PASS

Natural question: the expected number of facets in a canonical uniform halfsphere sample has a finite limit with a known n^-2 convergence deficit. The new all-dimension strict normalized-error law upgrades the asymptotic coefficient to a globally sharp finite-n envelope. Both endpoint constants are best possible: n=d+1 is exactly attained on the lower side; the upper endpoint is the limit of all finite n. The ordering gives meaningful optimal nonasymptotic control and is not a finite table, raw-count monotonicity, or a cosmetic renormalization alone; its kernel convexity and beta-shift mechanism may be useful for other random-polytope convergence comparisons. It is specialized to a fixed dimension and exactly uniform halfsphere distribution, no claims about general densities or high-dimensional uniformity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
