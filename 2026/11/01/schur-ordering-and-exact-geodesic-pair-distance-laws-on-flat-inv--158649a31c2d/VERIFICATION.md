---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The metric of T_a/(±1) gives min(delta(x-y),delta(x+y)). The map (x,y)→(x-y,x+y) is onto on the connected torus because multiplication by two is surjective; it sends product Haar to product Haar, so the two origin-distance variables are independent. This proves F=1-(1-H)^2. Substitution |x_i|=exp(u_i), s_i=log(a_i/2), makes H times fixed volume a marginal of the jointly log-concave e^{Σu_i} indicator of convex constraints u_i≤s_i and Σexp(2u_i)≤r²; Prékopa and permutation symmetry yield Schur concavity in log-side lengths. Strict Karamata for Σa_i² implies different circumradii, ensuring strict stochastic dominance somewhere; ball containment and corner simplex scaling give short- and far-tail formulas. Direct independent circular-segment formulas and grid evaluations of four planar shape ratios corroborated the CDF; proofs are all-dimensional analytic, not simulation.

## originality

PASS

Haar pushforward, Prékopa marginal log-concavity and circular segments are longstanding tools, credited rather than claimed. Eskin–Okounkov studies the pillowcase quotient as an object, not this intrinsic pair-distance law. Feldman studies independent compact-group sums/differences, not the combined quotient metric and geometric stochastic order. Xu 1996 cube-ball intersection might contain related shape inequalities, but no decisive stronger theorem was identified. Best-of-knowledge residual priority uncertainty retained.

## value

PASS

Geodesic pair distance is a canonical metric-measure invariant on rectangular flat inversion quotients; quotienting changes survival to an independent-square law. The theorem simultaneously classifies the entire rectangular aspect-ratio family by log-majorization for every radius and every increasing cost, uniquely optimizes the cubic quotient, and determines unusual doubled 2d terminal exponent. This is more than a planar moment or mechanical renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
