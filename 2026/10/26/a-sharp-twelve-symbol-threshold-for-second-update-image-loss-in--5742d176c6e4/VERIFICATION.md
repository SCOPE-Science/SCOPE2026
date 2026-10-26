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

# Reproduction and boundaries

Running `python3 verify.py` enumerates all 256 rules, generates `classification.csv` in the same directory, and reproduces the exact 72 equal/184 strictly shrinking classification. For 184 shrinking rules, it proves the shortest difference length by breadth-first subset-pair search, including the histogram `(4, 2, 16, 28, 40, 46, 24, 4, 8, 8, 2, 2)` for lengths 1–12.

The four-state and sixteen-state de Bruijn graph construction is exact for an arbitrary-length finite output word: paths biject to compatible finite input windows. The equality decision is exhaustive only when every relevant subset pair has been visited. For shrinking cases, breadth-first search terminates with a shortest witness; this does not need to enumerate every later pair. The maximum visited pair count before termination is 252.

Separate direct enumeration of all input blocks of lengths \(n+2\) and \(n+4\) for \(1\le n\le5\), across all 256 rules, verifies both graph-language membership predicates. Every shortest discrepancy witness is independently confirmed by direct input enumeration. The two extremal length-12 witnesses are also checked by enumerating all \(2^{16}\) five-neighbourhood input blocks. Finite checks alone would not prove unrestricted equality; the complete subset-graph argument supplies that implication.

No independent scientific validation has been performed. No claim is made concerning the eventual stabilization time of the rules whose first and second images differ.
