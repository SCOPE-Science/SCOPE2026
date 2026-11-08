---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For ordinary nonperiodic 6x6 queen attack graph on row-major 36 squares, independent backtracking reproduces exact augmented face-count vector (1,36,340,1024,982,248,4), and the first-vertex toggle pairs the empty face with a singleton and has 1,273 other pairs in the ordinary complex. The 2,635 augmented faces admit the audited global acyclic orientation; critical ordinary cells are 1 vertex, 34 two-cells and 53 three-cells. Independently recomputed signed integral Morse differential has dimensions 34x53, exactly 241 nonzero entries of absolute value <=2, rank over F2=33 and over F3=34; exact unimodular elimination has 33 unit pivots and one remaining row with gcd 2. Hence the Smith data and simply-connected 2-skeleton prove M(Z/2,2) wedge 19 S3, not just field Betti numbers. The audited finite verifier computes the D4 signed fixed-face Lefschetz character (-19,5,-7,5,-1,-1,5,5) and H3 character its negative; the eight character values sum to eight, leaving a one-dimensional invariant. Counts for all smaller square boards were regenerated; the source separately supplies their integral matching certificate for no torsion.

## originality

PASS

This is the ordinary nonattacking-queen complex (diagonal attacks included), distinct from the classical rook chessboard complex and the q-queens lattice-counting functions. Read the primary square-board q-queens paper and checked Resultary records for a stronger result or exact 6x6 table. Their counts do not imply a degree-two cellular attaching map, first torsion occurrence or D4 character. Best-of-knowledge originality PASS with explicit residual risk for unindexed topological queen-placement calculations.

## value

PASS

The nonattacking queen placements on a standard square board are canonical and naturally indexed by board side. The first integral torsion and exact Moore-space homotopy at side six, together with the natural D4 representation, give a meaningful threshold and topology beyond classical placement counts. The finite enumeration is a complete natural-object classification rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
