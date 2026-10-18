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

# Reproducible verification

Run `python3 prism_fixed_point_verifier.py` from this directory using Python 3 (standard library only). Compare standard output byte-for-byte with `prism_fixed_point_verification_output.txt`.

The standalone checker generates all 76 labeled graphs on zero through four vertices to test the generic recursive matching. Its primary theorem is stated for at least one vertex, but the checker also tests the empty graph as an internal recursion base case. Each enumerated graph is tested via (i) a direct two-layer prism edge-orbit matching criterion, (ii) an independent fully whiskered matching enumeration, (iii) partner involution and Hasse cover checks, (iv) a directed global topological sort checking acyclicity, and (v) exact equality of critical simplex sets and perfect matchings of the original graph. Six larger complete examples are checked without the orbit enumeration step. The output prints 3,822 total Hasse-cover comparisons for the exhaustive small-graph sweep, and ends with `VERIFY_OK`.

Finite tests do not certify all finite graphs. Universality follows from the partition-by-pivot argument and induction in RESULT.md. The verifier does not determine homotopy types of the *entire* ordinary prism matching complexes, and it does not perform an independent scientific audit.
