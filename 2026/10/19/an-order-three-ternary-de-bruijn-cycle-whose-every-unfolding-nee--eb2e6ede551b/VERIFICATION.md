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

# Reproducibility and proof checks

Run `python3 debruijn_attractor_check.py` in a standard Python 3 interpreter (no third-party dependencies). It checks all \(27\) length-three cyclic factors against \(\{0,1,2\}^3\), calculates the three critical bigram occurrence lists, verifies each residue obstruction, and exhaustively confirms both the nine-mark failure and a size-ten full string attractor for each of the \(27\) cuts and all factor lengths from \(1\) to \(29\). The expected output begins with `PASS deBruijn=27_distinct_trigrams all_27_cuts=gamma_exactly_10`.

The noncomputational lower-bound certificate uses 27 distinct length-three occurrences and the fact that each marked position meets at most three starts, forcing exactly the nine positions \(3,6,\ldots,27\) if size nine were possible. The residue-class bigram table rules out those positions for every cut. For the upper bound, all triplets are already covered and only one bigram fails at each cut; adding a position in that bigram fixes it. Uniqueness of each triple then implies coverage of every longer factor. No unbounded assertion is based on finite experimental extrapolation.

This is a complete finite-instance proof. The literature comparison is bounded by accessible source material and records. Independent audit has not been performed.
