---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS. Independently reconstructed all 96 categorical edges and exhaustively enumerated exactly 196226 nonempty independent faces with the reported 16-entry f-vector. Replayed all 98087 greedy face pairs leaving precisely one critical 0-cell, 24 critical 4-cells and 27 critical 5-cells. Independently generated the full 1457216 Hasse incidences, checked acyclicity on all 196226 faces by Kahn topological sorting, recomputed the signed 27x24 integral Morse boundary and eliminated it by 21 *unit* integer pivots with zero residual block; thus kernel Z^6 and cokernel Z^3. The high connectivity of the resulting single-0-cell, 4/5-dimensional Morse CW model identifies five-cell attaching maps with integer degrees in pi4(vee24 S4)=Z^24; unimodular elementary cell slides/cancellations give the asserted actual wedge homotopy type, not just Betti ranks. Calculations exhaust one fixed graph, not an infinite family.

## originality

PASS

PASS, best of knowledge, subject to an explicit close neighbor. Antolin Camarena--Carnero Bravo 2024 Theorem3.17/3.18/Question3.19 bounds possible homology dimensions for C_(3r+2) x Kn and asks whether torsion is absent, but does NOT give integral C8 x K4 ranks or homotopy decomposition. A 2026-10-11 indexed C7 x K4 theorem gives 3 S3 plus 6 S4; the equal multiplicities shifted by one are notable but the record has a different graph and no demonstrated general suspension/reduction from C7 to C8. The published paper explicitly lists C8 x K3 rather than this C8 x K4. New computation is a separate complete finite case, though a not-yet-recognized recurrence could imply it.

## value

PASS

PASS. The finite case is the first natural four-color 8-cycle instance immediately adjacent to a published torsion question; it resolves its exact integral torsion-free homotopy and both sphere multiplicities. The construction supplies a verifiable signed discrete-Morse certificate and homotopy upgrade, not a routine Euler characteristic alone. A complete natural example is useful even without a universal torsion-freeness theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
