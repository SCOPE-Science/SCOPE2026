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

Under the stated strict complete preferences and feasibility consisting of all and only perfect pairings, blocking-neutral domination forces containment of blocking pair sets: each new blocker endpoint weakly improves and the pair therefore also blocks the old matching. Any Pareto improvement is a blocking-neutral improvement: each changed partnership consists of two strict improvers, hence forms an old blocking pair, and no agent loses. At two agents the pairing is stable (likewise the empty pairing if admitted). An independent exact census generated the fixed-point-free involutions and used per-agent rank differences for the two dominance relations: all 1,296 four-agent profiles were tested; the 48 without a stable matching have three distinct singleton blocking sets and all three matchings in both solution sets. At six, the unchanged directed cycle on 3,4,5 supplies a blocker in every pairing. The nine one-cross pairings and no others are Pareto optimal: keeping four internally matched agents internal forces their original pairs, whereas in an all-cross pairing four agents can move to internal partners. At baseline the nine blocker sets are distinct two-element sets. After agent 0 changes from 1 above 2 to 2 above 1, the three pairings with 02 have only the unchanged V-blocker; those with 12 cannot be dominated by the only candidate with a smaller blocker set because the cross-matched V-blocker would lose. Each pairing with 01 is dominated by the same-V-edge pairing with 02, in which the only loser (1) is no longer a blocker. The independent census tested all 15 pairings before and after, exactly reproducing the 9-to-6 transition and the excluded pairings {01,23,45}, {01,24,35}, {01,25,34}.

## originality

PASS

The distinct claim is the sharp minimum under the joint no-stable and perfect-only restrictions and the explicit adjacent reversal witness. Neither general BN inclusion nor the four-agent stability census is new; the most relevant general results and explicit examples do not give the restricted boundary or the 9-to-6 transition.

## value

PASS

Because the known inclusion behaves differently when a stable pairing exists, conditioning on unsolvability isolates the effect of the new solution concept in its intended regime. The sharp first population and the one-swap construction show that BN can materially contract at fixed PO and fixed unsolvability, not just disagree in a chosen feasible set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
