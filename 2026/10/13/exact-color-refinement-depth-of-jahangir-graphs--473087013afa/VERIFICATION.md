---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For m>=4 degrees m,3,2 separate hub, spoke attachments and sector interiors after one round; further 1-WL rounds propagate color information inward by distance from equally colored sector endpoints, one layer each step, with final split at floor(n/2). For m=3 the hub shares degree 3 with spoke vertices at round one, but neighbor-degree multisets separate them at round two; sector distance propagation remains unaffected. Dihedral rotations/reflections across the identical m paths put precisely vertices of the same nearest-spoke distance in one orbit, and the color classes separate all other orbit types. Independently implemented one-WL and orbit formulas and checked n=2..18 and m=3..12 (170 pairs), including small n and m=3 boundaries. This finite check is supporting evidence for the all-parameter inductive distance-wave argument.

## originality

PASS

Named Jahangir graph literature found concerns domination/chromatic/Ramsey/burning invariants; Krebs–Verbitsky characterize general 1-WL refinement and universal covers but do not state the exact 1-WL stabilization for this spoke-even cycle family in inspected material. No Resultary mathematical record or queried primary title establishes the m=3 exception or all-n formula. Originality remains best-of-knowledge; unindexed equitable-partition computation could be equivalent.

## value

PASS

Jahangir graphs form a standard well-studied infinite family. Stabilization round depth and whether 1-WL detects every automorphism orbit are natural computational graph invariants, and this theorem determines both exactly for all permitted parameters. The m=3 hub/spoke degree-collision introduces a genuine sharp structural exception; more than a finite table or a relabeling of generic universal-cover bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
