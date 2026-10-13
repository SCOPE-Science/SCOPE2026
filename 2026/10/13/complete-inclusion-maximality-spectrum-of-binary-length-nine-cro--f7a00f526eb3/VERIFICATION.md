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
# Reproduction and limits

The exact search ranges over all 512 binary nine-character words, retaining the 148 unbordered ones. Both `artifacts/verify_bitset.py` and `artifacts/verify_strings.cpp` build all 3,080 compatible unordered pairs and exhaust all maximal cliques with independently represented vertices and adjacency. Both check every emitted set's self/nonself overlap and verify that every other admissible word fails to extend it. Sorted canonical output from both programs is identical, with 62,280 lines, 7,338,080 ASCII bytes, and SHA-256 `ebacd3ecd51b08c10b05e462a3496200ca3261b0840a0a3351910af91436ecd3`.

Python 3: `python3 artifacts/verify_bitset.py --catalog` writes `catalog_python.txt`. C++17: `c++ -std=c++17 -O2 artifacts/verify_strings.cpp -o verify_strings`, then `./verify_strings --catalog` writes `catalog_cpp.txt`. Compare both outputs byte-for-byte. The compressed catalogue `artifacts/maximal_catalog.txt.gz` decompresses to the same output and can be decoded using the Python standard `gzip` library. The Python program also verifies four-element complement/reversal orbit closure and counts.

This establishes a finite exact classification at blocklength nine. No claim of a proof for other lengths or of external expert validation is made. The scientific origin and remaining bibliographic risks are described in the result and review.
