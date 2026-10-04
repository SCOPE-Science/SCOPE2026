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

`verify.py` uses only the Python standard library. It constructs all \(64\) binary length-six words and, for each word, the exact no-error/single-transition-smear error ball from the stated channel definition. It joins two words exactly when their balls are disjoint, then performs deterministic Bron--Kerbosch enumeration of maximal cliques with a cardinality prune that can discard only branches incapable of reaching the current maximum.

The program compares the recomputed maximum-clique list byte-for-byte at the word-list level against the four codebooks in the package, directly rechecks pairwise ball disjointness, checks closure under binary addition, and checks the global-complement action. Expected output is:

`VERIFY_OK maximum=16 labeled_maxima=4 linear_maxima=1 complement_closed=2 complement_map=3,1,2,0`

The verified domain is finite and complete. No claim is made for other lengths or for more than one grain error.
