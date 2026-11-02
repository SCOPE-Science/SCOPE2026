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

The self-contained `verify_comma_free.py` reconstructs the nine primitive six-bit necklace classes, enumerates all comma-free assignments, optionally permits missing necklace representatives and imposes Hamming distance at least two. It checks all 1972 unrestricted and 272 distance-two optimal codebooks directly, verifies orbit sizes and equality-case inventories stored in `full_codebooks.tsv` and `detecting_codebooks.tsv`, and tests every cross-boundary forbidden window. A separate integer-encoded `verify_alt_comma_free.cpp` enumerates the same extrema with a full-triple compatibility test rather than the incremental forbidden-set invariant; a C++17 compiler is needed only for this optional second check.

To replay from this directory: `python3 verify_comma_free.py`. Expected terminal status: `VERIFY_OK`. Optionally compile with `g++ -O2 -std=c++17 verify_alt_comma_free.cpp -o check_alt` and run `./check_alt`; it reports unrestricted 1972 and detector size profile (1,54,1090,8410,23892,22374,5712,272,0,0). The Python verifier is authoritative and requires no compiler.

No infinite parameter range is verified or claimed. The computational proof is exhaustive over a finite, mathematically justified search space rather than a time-limited solver log. A separate external audit has not been performed.
