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

For each d queried binary points, coordinates produce d-bit columns v_i, edge parity outputs v_i XOR v_j. Zero output forces a duplicate, and distinct columns must cover every nonzero group element by distinct-pair XOR; conversely duplication gives zero and any two-basis yields all outputs. All five explicit two-bases validated. For n=10,d=5 the C(31,8)=7,888,725 translated 9-element candidates were independently exhaustively tested in compiled C++17 with complete XOR bit-mask coverage: none works (NO_NINE_POINT_BASIS_PASS 7888725). Direct replay of actual shattering_trees.json validates all 56 leaf witnesses, n=5 depth3, n=7 depth4, n=9 depth5, and no leaf repeats its hypothesis. Cardinality Ldim<=floor(log2 binom(n,2)), duplicate-signature VC upper bound 2^d<=1+binom(n-1,2), and monotonicity imply the exact VC sequence 0,1,2,2,3,4,4,4,4,5 and Ldim sequence 0,1,2,3,3,4,4,5,5,5 for n=2..11. A complete finite exhaustion proves only this finite obstruction, not all-order dimensions.

## originality

PASS

No identified pre-existing claim implies both exact small-n VC/Littlestone table and adaptive cuts for the restricted exactly-two-coordinate parity class. Difference-cover theory may already cover a component; priority qualified. Guingona et al's full nonzero linear combination family does not transfer exact dimensions to a strict subfamily; Ghazi et al's bounds on Boolean-aggregation complexity do not fix either the finite witnesses or nine-signature obstruction.

## value

PASS

A complete, sharply delimited range n=2..11 includes the first static-versus-adaptive divergence at n=5 and further n=9,10; the all-order reduction to binary additive two-bases is an independently useful complexity bridge. The nine-point obstruction is a natural boundary for d=5, not an arbitrary selected computer count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
