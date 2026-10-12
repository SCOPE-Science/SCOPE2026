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

Run `python3 verify.py`.

The verifier uses only the Python standard library. It performs these finite checks:

1. Generates all \(27\) words of \(\{0,1,2\}^3\).
2. Reconstructs every one-error non-wraparound output ball in two independent ways and requires equality.
3. Verifies that the nine stated triples partition the ambient space and that every pair inside each triple is confusable.
4. Verifies that \(\{0,2\}^3\cup\{111\}\) has nine words with pairwise disjoint output balls.
5. Enumerates every maximal compatibility clique with an exact Bron--Kerbosch traversal and requires maximum size \(9\) with exactly one maximum.
6. Independently counts all compatible nine-subsets by fixed-size recursive search and requires count \(1\).
7. Reconstructs the modulo-\(2\) lift of the binary repetition code and requires it to equal the unique maximum.

The expected terminal line is:

`VERIFY_OK maximum=9 labeled_maxima=1 unique_code=corners_plus_center`

The computation is exhaustive only for the stated finite channel.
