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

The two experiments are separate, so only the A/B and C/B payoff submatrices matter. Under random replacement the common reproduction/target factor cancels from T_i^-/T_i^+, leaving exp(-w times mutant payoff advantage). Taking first differences in the absorption recurrence and summing up to the fixed boundary at i=6 gives the reciprocal-fixation denominator. Independent exact reconstruction gives prefix sums (-4,-4,0,8,20) and (3,4,3,0,-5), hence D_A=2+2z^4+z^-8+z^-20 and D_C=2+2z^-3+z^-4+z^5. Termwise subtraction verifies z^20(D_A-D_C)=P(z). Exact replay by substitution gave P(1)=0, P'(1)=-15, P(6/5)=3174820597963420709/298023223876953125>0, P(2)=-323583. Three Descartes variations and disjoint brackets at 1, (1,6/5), (6/5,2) exhaust the positive roots counting multiplicity, so the crossings are simple. The fixation difference is -P/(z^20 D_A D_C), giving the stated ordering and neutrality tie. The frozen checker was read, not run. The reported decimal refinements are illustrative; the exact brackets, rather than an independent decimal refinement, were used to certify all positive-selection regimes.

## originality

PASS

The standard Moran recurrence is covered. The supported distinct claim is an exact two-switch ranking of distinct rare mutants versus the same resident as selection strength varies in one well-mixed model. The closest inspected results change the parameter, comparison or observable; they do not realize this reentry.

## value

PASS

The witness tests a natural inference about using weak- and strong-selection rankings to screen rare invaders of the same resident. Both ends favor the same mutant, yet a whole intermediate interval favors its competitor. The exact two-crossing result establishes the failure in a fixed elementary model without conflating mutant identity with an update rule, invasion site, or coexisting mutant dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
