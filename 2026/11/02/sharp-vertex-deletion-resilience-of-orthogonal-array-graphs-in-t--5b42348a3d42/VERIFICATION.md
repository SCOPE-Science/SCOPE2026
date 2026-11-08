---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The array pair-uniqueness yields graph degree t(n-1), common-neighbor counts lambda=n-2+(t-1)(t-2) for adjacent and mu=t(t-1) for nonadjacent anchors; subtracting yields exactly the adjacent pattern (A,B,B,C) and nonadjacent (D,E,E,F). Deleting at most min-1 vertices retains every 2-point extension pattern. An arbitrary-round three-pebble strategy matches equality/adjacency to at most two anchors, proving FO^3 equivalence at every finite quantifier rank. Deleting all witnesses of a minimum-pattern anchor pair provides a rank-three separating sentence. For q=2h or 2h+1 the D and C inequalities give exact optimal row counts; finite-field projective directions realize every allowed t. Independent direct field construction checked all 9 q,t profiles for q=3,5,7 with exact pattern counts and parity optima; finite checks corroborate the all-array counting proof.

## originality

PASS

The SRG parameters and 2-existential extension concepts are classical. Cioabă–Koolen–Li 2014 studies connectivity of Latin-square/OA strongly regular graphs, not this all-deletion FO^3 guarantee. Byrne–Byrne–Cioabă 2026 studies VC dimension and existential closure of SRGs including Latin-square graphs, making it a plausible related predecessor, but the full 2026 text could not be read; only abstract/version metadata were accessible, and authorized institutional full text returned VPN disconnected. In the sources actually inspected there is no decisive prior theorem giving all six exact deletion counts and parity-optimized resilience. The survival of this specific natural classification is a qualified best-of-knowledge assessment, not established historical priority.

## value

PASS

The deletion-tolerance radius is a sharp, array-independent invariant of a natural strongly regular graph family, and directly quantifies finite-variable logical robustness. The six witness counts and parity-sensitive optimized row split classify which balanced designs resist worst-case vertex erasures. Though the fixed-graph step follows elementary SRG counting, the complete all-array sharp classification and row optimization form a useful natural exact problem, not an unsupported toy check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
