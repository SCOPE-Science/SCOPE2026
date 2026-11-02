---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The explicit strict 3-by-3 complete market has exactly the three perfect stable matchings A, middle 0 and B; independent stability enumeration confirmed that each of the six five-agent submarkets has a unique stable matching, and the final missing entrant leads only to A (man) or B (woman). Considering the first full-market occurrence proves nonreachability of the middle target for every finite history of original agents, even with repeated exits and entries. Independently traced the eight-step rejection/acceptance chain after one woman a enters µ_B: a→m1 accept, w3→m1 reject, w3→m2 accept, w1→m2 reject, w1→m3 accept, w2→m3 reject, w2→m1 accept, a→m1 reject; the target µ0 is stable and a exits unmatched. Preferences preserve the original strict order and acceptability. Therefore the minimum temporary population for this exact market-target pair is 1, not a general bound.

## originality

PASS

The exact source cyclic market, its three stable matchings and nonreachability with zero temporary agents are already Yang Example 1/Theorem 1. Yang Theorem 2 gives target-dependent augmentation with larger temporary scaffolds, and §6.3 explicitly says minimization is not done. The specific one-auxiliary-woman constructive upper bound, hence sharp minimum 1, is a genuine additional statement; do not count the nonreachability example itself as original.

## value

PASS

PASS: The exact minimum historical augmentation for the canonical smallest known obstruction is a natural quantitative strengthening of a new reachability theorem that expressly leaves agent minimization open. A one-agent constructive witness is nontrivial because each event must end in a stable matching while preserving all original preference orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
