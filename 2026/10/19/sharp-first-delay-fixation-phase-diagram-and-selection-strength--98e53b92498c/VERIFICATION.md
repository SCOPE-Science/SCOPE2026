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

I independently built and solved the instantaneous and delayed chains in symbolic arithmetic by listing all ordered distinct reproducer/victim pairs, weighting the reproducer by the historical ratio and the current type. A hold changes the delayed state to (current,current), as required. Eventual absorption follows because a path of bounded length to an endpoint has probability bounded uniformly away from zero over the finite transient state space. Starting at (1,1), elimination gives both frozen probabilities and the factorization -x(x-y)(xy-2y-2) over the stated positive denominator. On the witness game the two sign factors have numerators w(5+13w) and 31w^2-4w-3, with positive denominators. The first is positive for w>0 and the second has its only positive root at (2+sqrt(97))/31 in (0,1); this proves the strict reversal and neutral cases without reversing the relative fitness ordering. For N=2, all pre-absorption history counts are one under the deterministic all-one initialization, for any finite delay. The two exact example differences are 1/70 and -15/2132. Finally the average-payoff identities imply x/y<4 for positive games, and the construction with alpha between x/(4y) and 1 attains every point of that region.

## originality

PASS

The lagged Moran model, no-self-replacement rule, deterministic all-one history, history-valued Markov-chain method, and qualitative dependence on the game and selection strength are prior work. The inspected matches do not resolve the complete first-delay sign boundary in three individuals or the exact sign reversal of the delay effect along the specified fixed positive-game strength path. The smallest-population statement is supported as part of this exact classification, not as a separate novelty claim for the observation that N=2 has only one transient count.

## value

PASS

For the established delayed Moran model, the earliest size at which composition history can matter already has two distinct exact neutrality loci, and the second is reachable within strictly positive games. The fixed-game path separates reversal of the delay effect from reversal of relative fitness ordering. This provides an interpretable phase boundary for when a delay helps, not just isolated numerical fixation values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
