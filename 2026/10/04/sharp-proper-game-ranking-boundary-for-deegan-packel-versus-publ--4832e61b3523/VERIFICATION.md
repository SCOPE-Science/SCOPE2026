---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

A monotone simple game is uniquely represented by its nonempty antichain of minimal winning coalitions. The inspected verifier independently generates those antichains recursively and by brute force, checks properness on all coalitions, computes the Public Good counts and exact-rational Deegan--Packel sums, and compares every pairwise weak relation. It obtains simple/proper counts \((1,1),(4,3),(18,11),(166,80)\), no proper disagreements through three players, and exactly 30 at four. Canonicalization under all 24 relabelings yields exactly the three stated orbit representatives with multiplicities 12,12,6; direct weighted-coalition enumeration checks the three quota/weight representations. The raw vectors printed for the representatives also directly exhibit the ranking disagreements.

## originality

PASS

Freixas--Kurz directly compare the Public Good and Deegan--Packel indices, give the three-player weighted family \(\{\{1\},\{2,3\}\}\) where their normalized values differ, and study subclasses where ranking behavior improves. That three-player example is improper, exactly matching the audited unrestricted boundary. The checked literature does not state that properness postpones the first ordinal disagreement to four players, nor the 80-game/30-disagreement/three-orbit census. Resultary's targeted query returned no prior exact small-game classification.

## value

PASS

The result gives the exact first size at which two classic minimal-winning-coalition power measures can disagree in the important proper/weighted setting, and completely resolves all smaller cases plus the boundary orbits. This is a motivated finite cutoff in voting-power theory rather than an arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
