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

# Verification instructions

Compile the standalone `verify.cpp` with `c++ -O2 -std=c++17 verify.cpp -o verify` and execute `./verify`. It enumerates all candidate vertex subsets of sizes one through six in the two graphs, checks all closed-neighborhood identifying signatures, constructs complete token-jump exchange graphs, counts vertices and edges and degrees, and identifies connected components. For nine ground points it also generates the 280 ground-set partitions into three triples, all 27 center choices for each partition, and tests equality of these 7560 labeled spanning-three-path configurations with the directly enumerated optimum codes. A separate mathematical exchange argument identifies each component as a ternary Hamming graph. No random sampling, heuristic cutoff or floating-point approximation is used.

Expected final output line: `ALL_VERIFY_OK`. The test is finite and makes no claim about other graph orders. This is computational and self-review only; no independent audit has been performed.
