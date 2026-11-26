---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For each fixed 1<theta<2 the inverse branches are g_±=1/2±u^2, u=(sqrt(K^2+theta(1-z))-K)/theta, and the signed analytic transfer weight for each is w=u/sqrt(K^2+theta(1-z)). On the real interval the weight is nonnegative and bounded by 1/(1+theta/2)<1. The inverse derivatives stay bounded by some q<1 on a sufficiently small complex tube of radius delta, and the inverse images lie in the q delta tube by integrating on segments from the nearest real point. Montel on the compact closure of the smaller tube gives compactness of the weighted-composition operator on H-infinity. Cauchy estimates give a continuous injective restriction to W^{2,1} intertwining both operators. The cited primary spectral gap, unit spectral radius and convergence of the real iterates on 1 imply the compact operator has radius 1 (larger would produce an inadmissible eigenvalue, smaller would send 1 to zero). Its peripheral eigenvector restricts to the simple real invariant density up to scalar. A positive interior subinterval of this continuous normalized density contains a full cylinder by uniform contraction; its contribution to a sufficiently high iterate gives positivity everywhere on the interior, since inverse images and weights remain interior and positive there. In the exterior interval the analytic identity evaluates only at 1/2±u^2 with u^2<v=K^2/theta^2<1/2. Continuing w itself, not its absolute value, gives sqrt(x_*-x) w(x) -> -K/theta^{3/2} at x_*=1+(2-theta)^2/(8theta). The limiting density sum is positive, giving the exact nonzero negative coefficient. Integer-order Laurent poles cannot reproduce this limit; rational equality a.e. would imply equality by analytic identity, and a Taylor radius larger than x_*-1 would contradict divergence. Replay: RESULT.md lines 26–44 and arXiv:2610.23180v1 Sections 3–4. The frozen script was read, not run; its radical-limit tests use a trial polynomial, not the invariant density. No exact Taylor radius or result at theta=2 is inferred.

## originality

PASS

The primary same-family work supplies the inverse formulas and invariant-density spectral input, and holomorphic transfer techniques are standard. The supported contribution is the forced noncanceling exterior half-order singularity of the spatial density, including its coefficient and consequent nonrationality at every parameter in the given open interval.

## value

PASS

The exact coefficient shows that the branch point suggested by the inverse geometry survives in the actual invariant eigenfunction. It forbids rational densities and locates a quantitative upper bound on the Taylor radius tending to zero quadratically as the cusp disappears, information not supplied by real regularity or a qualitative existence theorem. Its value is fixed-parameter spatial information, not a claim about a uniform complex domain or an exact nearest-singularity radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
