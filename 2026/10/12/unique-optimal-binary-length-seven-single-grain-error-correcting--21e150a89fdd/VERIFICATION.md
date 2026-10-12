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

Run `python3 verify.py` with Python 3 and its standard library only. The checker reconstructs all binary words of length \(7\), all permitted single-grain outputs by two distinct formulas, and the complete first-bit-zero compatibility graph.

The first-bit-zero graph has \(64\) vertices, \(432\) confusability edges and \(1584\) compatibility edges. The exhaustive pivoted Bron--Kerbosch traversal has \(91265\) visited nodes with a valid size-\(13\) cardinality prune. A separate increasing-vertex search with a mathematically valid independent-color-class clique upper bound visits \(1212\) nodes when enumerating size-\(13\) cliques and \(334\) nodes when excluding size \(14\). Both methods yield the exact same unique \(13\)-word code.

Because allowed errors preserve the first bit and bitwise complement conjugates the two fibers, these exhaustive counts prove the full maximum \(26\) and exactly one labeled maximizer. The checker also validates all \(325\) unordered pairs within the displayed \(26\)-word optimum against direct error balls.

The required final line is:

`VERIFY_OK maximum=26 labeled_maxima=1 branch_maximum=13 branch_maxima=1 complementary_halves=true`

The finite computation does not provide a theorem for other lengths or error types.
