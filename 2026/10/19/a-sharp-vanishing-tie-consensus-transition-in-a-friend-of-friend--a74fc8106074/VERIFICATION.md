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

Symmetry, unit diagonal and [0,1] invariance are compatible with the weight field. Uniqueness preserves zero cross-block weights. Lower exponential comparison preserves any initially positive edge; the nonnegative source in the edge equation and an integrating factor then propagate positivity through paths at every positive time. In particular, an initially missing within-component pair is eligible for the critical and supercritical scalar lower comparisons. The two diagonal terms in (W²)_ij give 2w_ij; linearization of the exact edge field at zero has coefficient r=c(2+2/N)−1 with full-population N, not component size. The maximum tie sees at most (N−2)m² from off-diagonal intermediates, leaving strictly negative quadratic coefficient −4c/N at criticality. These scalar bounds give exponential decay below threshold, two-sided reciprocal bounds at the threshold, and a positive asymptotic lower bound above. Below threshold Q is integrable, giving a limit of the bounded stochastic fundamental matrix U; its determinant converges by Liouville to exp(∫tr Q)>0. Component blocks fix their constants, so an invertible block cannot map any nonconstant profile to a constant. At and above threshold one can check contraction directly: at max and min vertices of a nonsingleton component, the contribution of their mutual tie of weight at least ℓ(t), with k_i≤N, yields D⁺diam≤−2cℓ(t) diam/N. Using respectively ℓ(t)≳(1+t)⁻¹ and ℓ(t)≳1 gives polynomial and exponential decay, and the monotonic extrema give actual limits. Independently simplifying the critical maximum-edge field gives −z²[4+(N−2)z]/[2(N+1)]. Substitution of the stated two-agent w(t),d(t) gives d'=−(2/3)wd/(1+w) exactly; inverse-linear decay for the gap is nontrivial when the initial opinions differ (zero gap remains zero).

## originality

PASS

Passes for the exact homogeneous FOAF trichotomy, in particular the critically vanishing inverse-time ties that still enforce consensus and the strict subcritical obstruction for all initially nonconstant component profiles. The original model, triadic closure, zero cross-component ties and generic persistent-connectivity consensus are credited inputs or overlaps. The close Warwick doctoral thesis was obtained and its model and FOAF case-study passages compared; no equivalent constant-response theorem was found in those inspected passages.

## value

PASS

The exact cutoff resolves whether mere positive homogeneous interaction ensures consensus in this model. Its critical regime quantifies how ties can all disappear without destroying cumulative communication, while below it the total influence never collapses a nonconstant profile. The two regimes at vanishing weights are mathematically and interpretively distinct; the result covers sparse initial graphs componentwise, not only a symmetric complete-graph trajectory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
