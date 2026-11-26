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

Use the fixed strict-order signature and n≥2 (n=2 is the four-point crown). The crown is a quantifier-free reduct of the alternatingly colored directed 2n-cycle. After the first move in cycles of length at least 24, preserve clockwise order, colors, and gaps either equal and <L_r or both ≥L_r of equal parity, with L_0=2 and L_r=2L_{r−1}+1. A repeated choice uses the same partner; at a newly split short gap the equal offset works. At a long gap either copy a subgap shorter than T=L_{r−1} (both remaining subgaps then exceed T), or choose T or T+1 of the required parity, leaving at least T on both sides. Thus the invariant is symmetric, preserves color and at r=0 preserves exactly the distance-one arcs among selected vertices, including a one-pebble whole-cycle gap. This proves a tail from n=12. The frozen type recursion is sound by induction, storing sets of possible extensions rather than counts; its supplied programs and output were inspected, not executed. Independent replay /workspace/crown_rank4_replay.py (stdout /workspace/crown_rank4_replay.txt) tests the two-board EF game on all 55 pairs with 2≤m<n≤12. Each proposed move is matched in its atomic-relation bucket; moves on both boards are checked, and the first-move rotations preserve all choices within each level. The only equivalent pairs in this finite range have both parameters at least seven. This bridges to the analytic tail, giving six classes and the sharp fourteen-point tail representative within this family. The same game calculation on uncolored C12 and C14 independently confirms their rank-four equivalence. It does not rely on verification of the numbering of Brown–Hoshino's cited theorem.

## originality

PASS

The supported distinct claim is the sharp unmarked strict-order crown classification, especially the threshold n=7 and separation of the 12- and 14-vertex crowns despite rank-four equivalence as pure cycles. Inspected indexed results cover different signatures, ranks or graph families. Pure-cycle equivalence, known as prior work in the frozen record and independently confirmed for this pair, goes in the wrong direction to imply equivalence of the orders. No exact or mechanically implying antecedent was identified in the bounded comparisons; the primary pure-cycle attribution remains an access risk, not evidence of absence.

## value

PASS

Finite crowns are a canonical family of two-level orders with cycle Hasse graphs. Comparing exactly the four-round cutoff with the pure-cycle benchmark is a motivated test of what information is lost on forgetting the comparison direction. The twelve- versus fourteen-point contrast is a concrete sharp witness, and the fourteen-point optimal representative answers the exact bounded-rank question throughout the family. Neither a finite census alone nor a coarse gap bound establishes that cutoff. No broader claim about all finite posets is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
