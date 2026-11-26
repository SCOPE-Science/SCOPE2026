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

There is an independent pathwise proof of the lower bound. Fix a common deterministic contact history. If a target is infected only with vaccination, take a causal chain x_0=s,...,x_l=target in that run, with x_j first infective in round j. None of these distinct vertices is the vaccine recipient. Let j be the first index where the unvaccinated infection time differs. The preceding vertex was infective in the same round in both runs and the shared contact succeeds, so x_j must have been infected earlier without vaccination; it cannot be the target. First-round infections of vertices other than the recipient coincide. Thus j cannot be 1 or 2: in the latter case an earlier unvaccinated infection would be in round 1. Therefore l>=j+1>=4, giving at least five distinct chain vertices plus the vaccinated vertex. A deterministic common-history argument implies the claim for the stated independent contacts. Separately, direct enumeration of relevant contact subsets with first-infective-time tuples reproduced 372 timed states, 140 paired SIR projections and zero adverse terminal states at n=5. Tracing the frozen witness confirms that its common intermediate meets the outgoing successful contact only in the vaccinated run. Finite duration makes each final risk a polynomial, so the strict difference at a cube vertex persists in a relative neighborhood containing interior points and an open neighborhood of such a point.

## originality

PASS

The general calendar-time harm mechanism is prior and credited. The material distinct claim is the sharp five-versus-six population cutoff in the specified single-seed, single-recipient model. The closest primary source proves a broader monotonicity theorem in infection-age-dependent, calendar-stationary models, then explains qualitative failure under calendar-time variation without a finite sharp cutoff in the examined preprint. The nearest indexed result concerns static peak prevalence, not final infection of a specific person.

## value

PASS

The boundary gives a precise limit on when calendar-time dependence can overturn a familiar individual-risk monotonicity theorem. The pathwise obstruction rules out every smaller graph under all contact schedules; a strict difference robust to probability perturbations is stronger than a degenerate isolated example. This is a meaningful minimal counterexample in the abstract model, not a clinical policy finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
