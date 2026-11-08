---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For every external cell (i,j), its number of white neighbors in the rook graph is r_i+c_j. Thus W is a fort iff no external cell has r_i+c_j=1. Classifying whether there are empty rows/columns forces: full row/column transversals for the exceptional 2×2, 2×3 and 3×3 cases; 2×2 rectangles when both sides admit an empty row/column; and 2-whites-in-each-row families when m=2. The n=4 four-cell full-column configurations contribute exactly 8,36,24 exceptional configurations for 2×4, 3×4, 4×4. Choosing 2 rows/columns counts binom(m,2)binom(n,2) rectangles; the thin board has binom(n,2)^2 independent row-pair choices. A maximal-cardinality failed blue set must be stalled, because forcing one more vertex would yield a larger still-failed set; complements of stalled sets are exactly forts. An independent adjacency-defined finite enumerator reproduced the classification on 2≤m≤5,m≤n≤6. No finite test was substituted for the all-m,n proof.

## originality

PASS

The previously known scalar extremal failed zero-forcing size and rectangular obstruction are credited to Fetcie–Jacob–Saavedra, while the new final claim concerns complete labeled extremizer multiplicities and exceptional orbit types. Read the relevant prior primary results; no inspected statement implies the full count, subject to unindexed fort- or product-classification risk.

## value

PASS

Forcing-set enumeration on natural Cartesian products is a structural invariant beyond the known maximum cardinality. The complete classification identifies thin-board multiple orbits, all small exceptional shapes, and the stable single rectangular orbit for m≥3,n≥5; this gives usable exact extremizer counts rather than a routine restatement of the scalar number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
