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

# Reproducing the finite theorem

Run `python verify.py` with Python 3 in the same directory as `enumerate_interleavings.py`, `enumerate_pairings.py`, `degree_table_k5.json`, and `degree_table_k6.json`. No external package or network request is needed.

`enumerate_interleavings.py` enumerates every permutation on \(k\) labels and every choice of \(k\) positions for its ordered first subsequence, converts the merged word to a canonical pair partition, and takes the set cardinality. `enumerate_pairings.py` instead enumerates all perfect matchings recursively and all \(2^k\) selections of one endpoint from each pair; it accumulates the distinct induced permutations. The two complete maps are compared for every \(2\le k\le6\). The verifier checks the complete tabulated maps at \(k=5,6\), the stated sharp maxima and unique extremizers, all cyclic shifts, the Catalan identity case, and degree-entry sums.

The computation completed with the final output `ALL_FINITE_THEOREMS_VERIFIED`. Main reference checksums for the compact sorted degree maps are `1dd5f5b293589b9d4415602ea4f0b92406b4759b0e6da630bca7f760113cf98b` at size five and `2d5d5d556335985345bed6f02da914f853aa5e152ed88d27e29899c260440045` at size six.

Exhaustiveness follows from the pair-partition and interleaving lemmas in `RESULT.md`. No sampling, solver timeout, or incomplete bound is interpreted as a proof. The theorem concerns only the specified finite cases, and independent mathematical auditing has not yet been performed.
