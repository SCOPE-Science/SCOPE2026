---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The exact first image from μZ is μ[ν(1−U)+a μ^(−(1−γ))U^γ]. For sufficiently small μ it remains at least νμ; subsequent excursion branches multiply by ν, giving T=1+max(0,ceil(log(y/μ)/log(1/ν))) and R=ν^(T−1)y/μ. Along μ_j=(aν^(j+θ))^(1/(1−γ)), the logarithm is j+θ−V+o(1), and the integer ceiling stabilizes almost surely except countably many phase boundaries. The uniform-U law yields V=v0+Exponential(rate log(1/ν)/γ), giving the exact J tail, geometric long-excursion deficit and conditional power-law density on (ν,1). An interior implicit-function threshold yields the claimed positive first correction. Independent direct orbit iterations and the exact ceiling agree for 15 instances (j=8,16,28); the return coordinate error at j=28 was below 7.1e−9. The almost-sure and expectation results follow from analytic tail bounds, not these iterates.

## originality

PASS

Lima–Perdigão provide the map, natural interval and pointwise return lengths. The present result integrates the entire uniform-initial-condition ensemble to obtain a lattice-phase joint distribution, exact tail and conditional independence, rather than an invariant-measure recurrence law. Their primary Sections 2–4 with return propositions were inspected and do not provide the complete statistical assertions. General shrinking-target theorems concern different sampling measures; no covering implication was established.

## value

PASS

The jointly resolved duration/reinjection law, exact long-excursion independence and first finite-scale correction turn qualitative excursion dynamics into computable stochastic statistics; distinction between natural-section Lebesgue starts and invariant return statistics makes the contribution concrete.

The dated certificate retains the supplied scientific assessment, sources and limitations.
