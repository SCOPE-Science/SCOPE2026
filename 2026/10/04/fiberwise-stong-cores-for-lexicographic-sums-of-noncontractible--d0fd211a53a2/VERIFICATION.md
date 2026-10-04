---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof in `RESULT.md` is the primary evidence. The standalone `verify.py` supplies a finite computational stress test without replacing the proof.

It constructs four index-poset shapes and four noncontractible fiber types. One fiber type contains a genuine beat point and reduces to a four-point core. The script enumerates all fiber assignments for the chosen index shapes, replays each local beat deletion in the corresponding global lexicographic sum, and checks both equality with the lexicographic sum of the separately computed cores and absence of beat points in the terminal space.

The final replay covers \(352\) lexicographic sums and \(320\) fiberwise beat deletions. It also checks the boundary example with a singleton lower fiber and a two-point antichain upper fiber; the global core has one point rather than the naive fiber-core sum \(3\).

The exact replay output is stored in `verification_output.txt`. The finite tests do not establish the infinite family by enumeration; the theorem is established by the symbolic beat-witness argument in `RESULT.md`.
