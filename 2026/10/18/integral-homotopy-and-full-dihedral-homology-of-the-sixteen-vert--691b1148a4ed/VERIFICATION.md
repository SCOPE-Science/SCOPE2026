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

The stated 24 graph edges generate exactly 11,393 nonempty ordinary matchings. Independent Python replay (replays/4_ladder.py; output replays/4_ladder.txt) checks all directed face covers and 5,690 pairs, leaving critical cells (one 0-cell, five 4-cells, seven 5-cells). The signed 5-by-7 degree matrix agrees entrywise; the specified 3-minor is -1 and all 4-minors vanish. The CW model is the mapping cone of a map from a wedge of seven S^4 to a wedge of five S^4. Hurewicz determines those attaching maps by degrees, and integral basis changes are realized by homotopy self-equivalences of the source and target wedges. The three unit pairs cancel, leaving two S^4 and four S^5. Rim and rung edges have respectively one and two incident 4-cycles, so preserving the rim forces the full graph automorphism group to be the indicated order-32 dihedral group. The independent equivariant replay over F97 gives degree-four rotation weights 0 and 8, degree-five weights 0, 4, 8 and 12 (each once), and s and rs traces respectively (0,0) and (2,-2) across degrees (4,5). Torsion-free integral homology identifies the reduced lattice with finite-field homology by base change. Rotation eigenspace ranks lift via the order-16 idempotents at a prime above 97 of the cyclotomic integer ring (16 is invertible there), and reflection eigenspace ranks lift via the ± projectors. The two nonreal rotation weights combine into E; subtracting its zero reflection traces, the two axis traces give exactly the stated signs on the one-dimensional lines. This also verifies the half-turn and full-group invariant assertions. No claim about integral dihedral-lattice splitting or equivariant homotopy is needed.

## originality

PASS

The supported distinction of the full finding is the degree-by-degree rational dihedral action. Two distinct indexed records demonstrably cover its entire nonequivariant assertion, not its character calculation. Their displayed dates are later than the frozen record's displayed date; neither equivalent coverage nor those dates establish priority. The wedge and Betti numbers alone are not credited as a distinct contribution in this review.

## value

PASS

The natural high-symmetry cubic ladder is a meaningful test object for ordinary versus extendable matchings. In the two nonzero ordinary homology degrees, the action distinguishes an invariant degree-four line from no degree-five full-group invariants even though the central half-turn is trivial in both. The full modules provide these subgroup-sensitive invariants, which cannot be recovered from the already covered sphere counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
