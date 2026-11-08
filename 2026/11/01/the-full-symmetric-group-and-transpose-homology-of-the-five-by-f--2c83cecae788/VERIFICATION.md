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

The specified finite board has 20 allowed square vertices; independent enumeration gives cardinality face counts (1,20,130,320,265,44). I inspected complete RESULT.md and the actual verify_derangement5.py blob. Its augmented, oriented integral boundary construction tests d^2=0 and uses exact ±1 unit cancellations with explicit Schur-complement operations and adjacent-differential restrictions, which preserve the integral chain homotopy type. It specifies 383 contractions leaving precisely one degree-two and 13 degree-three generators with all residual differentials zero, thereby proving integral freeness rather than just ranks over a field. H2 is rank one over Z, so an automorphism acts ±1; checking all 120 row-label permutations and their transposed partners modulo 101 validly distinguishes the two signs. For H3, the reduced simplicial signed Lefschetz sum for every group element combines with the known H2 action; the closed trace matches the standard four-, four-, and five-dimensional Specht characters. Rational semisimplicity proves the claimed decomposition. I inspected the algorithm and independently reconstructed the face counts; I did not independently reproduce all 383 integral cancellations or all 240 traces, so the bundled exhaustive checker is essential evidence, not a substitute for inspecting its logic.

## originality

PASS

The familiar degree-two Z value for D5 is explicitly in Shareshian–Wachs Table 8.1 and cannot be claimed novel. The final result is the complete degree-three integral group and the S5 by transpose rational characters, including a nontrivial 13-dimensional action. The full rectangular chessboard representation theorems use a different complex and independent row/column symmetries; they do not yield this induced deleted-diagonal module without additional exact sequence analysis. Inspected primary Section 8 and its table do not state H3 or the 240-element character. No stronger exact-object representation theorem was found in the bounded searches; this is best-of-knowledge, with residual unindexed-literature risk.

## value

PASS

The diagonal-deleted board D5 is the first small canonical derangement-type chessboard with higher adjacent homology; a complete integral and full graph-symmetry description refines the previously tabulated degree-two group and can serve as an exact equivariant benchmark. The nontrivial 13-dimensional H3 character is not a textbook substitution or a known-table recomputation; the board and symmetry action are independently natural.

The dated certificate retains the supplied scientific assessment, sources and limitations.
