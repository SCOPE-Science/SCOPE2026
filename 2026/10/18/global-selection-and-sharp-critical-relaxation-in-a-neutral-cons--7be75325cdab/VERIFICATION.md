---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the closed physical region 0≤w≤1, 0≤q≤(1−w)^2, direct substitution gives z′=ρz(w−α), q′=2ρq(w−α), w′=G(w)−cq. No boundary equilibrium exists in the simplex, and the upward-opening G changes sign exactly once in (0,1), at a simple root w_s. In the polarized case G(α)=cq_*>0 so w_s>α and the diagonal equilibrium is a saddle (its z and w eigenvalues have opposite signs). Differentiation of the entropy Lyapunov function cancels the q term and leaves (w−α)[G(w)−G(α)], strictly negative off w=α. Its sublevels stay away from q=0 and the only invariant state on w=α there is q=q_*. Sign preservation gives the two basins relative to the interior. The quadratic Lyapunov function gives (w−w_s)G(w)+cq(w_s−α) for w_s≤α; the zero set at equality reduces to the single invariant point by w′=−cq at w=α. At criticality q>0 tends to zero, so u=w−α must eventually be negative (at any zero u′=−cq<0). The exact quotient s=−u/q obeys s′=c−[B−(c−ρ)u]s. The bracket tends to B>0; comparison above and below by constant coefficients gives s→c/B. Integrating (1/q)′=2ρs gives the claimed 13/16 in the example and B/(2ρc) generally. The unchanged companion verification/check_consensus.py corroborates algebra and samples; the review relies on the analytic reconstruction, not finite integrations.

## originality

PASS

Pass the distinct exact critical coefficient and its every-unequal-interior-start law for the full deterministic flow at arbitrary positive beta and rho. The source model, equilibrium geometry and local types are antecedents; no separate priority is assigned to the qualitative basin portrait given the closest supplement's advertised scope. The reviewed comparisons do not establish coverage of the exact amplitude.

## value

PASS

An exact critical observable in the full model is materially more informative than a threshold and local stability picture. It gives a normalization-sensitive benchmark for deterministic relaxation at every positive rate ratio, and the invariant sign and Lyapunov arguments show precisely which initial conditions obey it without a fast–slow hypothesis. It makes no stochastic or experimental extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
