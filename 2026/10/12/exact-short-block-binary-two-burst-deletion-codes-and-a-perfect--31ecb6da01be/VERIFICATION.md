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

# Verification procedure

Run `python3 verify.py` from the directory containing this file. This checker uses only Python's standard library and prints `VERIFY_OK` after all assertions pass. A separately implemented optional C++ check can be built with `g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp`; it independently enumerates the received words and checks the five transversals, codeword disjointness, and complete length-nine partition.

It recomputes every legal pair of disjoint adjacent-pair deletions at blocklengths \(5\) through \(9\); verifies that the proposed output transversals meet the deletion ball of *every* binary input word; checks the correcting-code condition for the exact exhibited codes; checks all \(24\) distinct-block length-eight cases through the six stated symmetry representatives; and tests that the eight-word linear code of length nine partitions all \(32\) received five-bit words, with ball-size distribution \(1,1,1,1,7,7,7,7\).

For the length-nine code, the bit masks in RESULT.md provide a compact independent finite certificate: all eight are mutually disjoint, and their bitwise union is `0xffffffff`. The upper bounds use explicit transversals and do not require trusting a heuristic optimizer. The checker does not certify any theorem for larger lengths, uniqueness of an optimum, or scientific originality.
