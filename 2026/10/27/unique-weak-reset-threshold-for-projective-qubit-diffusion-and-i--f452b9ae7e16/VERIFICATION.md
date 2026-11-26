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

For the specified projective generator and 0≤x<b<1, write L/c in divergence form ∂_x[x(1−x)∂_x]. The absorbing boundary at b and the bounded branch at the entrance 0 give cm=log[(1−x)/(1−b)]. The bounded stopped mean solution gives a uniform bound on the mean, and iteration of the Markov bound at a fixed time using the strong Markov property gives a geometric survival bound. For V=c² Var(T_b), the product rule gives [x(1−x)V']'=−2x/(1−x), hence x(1−x)V'=2[x+log(1−x)]; integration with V(b)=0 yields the displayed dilogarithm expression. Poisson renewal gives M=(1−ϕ)/(rϕ); its expansion gives M'(0+)=(m²−Var)/2=−Φ_b/c². The continuous function yΦ_b'(y)=−log(y)/(1−y)−1−log(y/δ) decreases strictly from positive to negative, while Φ_b(δ)=0 and Φ_b(1)<0 by the series comparison. Thus there is exactly one interior zero with the claimed signs after reversing coordinates x=1−y. Setting x=zb, the expansion starts with b²(1−z)(3z−1)/4 and its cubic coefficient at z=1/3 is −7/243; the leading factor has z-derivative 1/2 there, giving z=1/3+(14/243)b+O(b²). For δ<e^-1, Φ_b(e^-1)>0 so the unique root satisfies y_c>e^-1. Then L+log y_c≥L−1 for L=log(1/δ). The root equation first implies y_c=e^-1+O(1/L), then expansion at e^-1 yields the stated positive correction in y_c and negative one in x_c. This proves only the infinitesimal-rate transition; it does not classify global rate optima or the next response at equality. Frozen CHECK.py and VERIFICATION.md were inspected: they report finite moment, transform and threshold checks (not executed here, not an all-parameter proof).

## originality

PASS

The specific contribution is the single cap-dependent critical fidelity for the surface/projective diffusion at every b, and its two quantified endpoint laws. General Jacobi moment methods and Poisson renewal are prior; the CV rule by itself gives a criterion, not the number of changes of its sign as the initial fidelity varies. The leading small-cap-coordinate fraction 1/3 agrees with the flat-disk result and is not a distinct universal reset criterion. The available source statements do not give the projective one-crossing result and its sharp corrections.

## value

PASS

This identifies exactly when a small resetting intervention helps rather than harms a geometrically natural first-passage task. A generic CV condition or endpoint checks cannot resolve the partition of initial states. The flat-limit correction and slow logarithmic approach to 1−e^-1 distinguish the two geometries and quantify where the change of sign occurs without overclaiming finite-rate optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
