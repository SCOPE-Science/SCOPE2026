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

# Reproducible finite checks

Run `python3 verify.py` (Python 3.10+) in the directory containing the extracted standalone files. It constructs the 32-vertex Dyck graph as the triangle-dual of the Shrikhande graph, verifies there are 417 perfect matchings, compares all unordered perfect-matching pairs, and identifies legal moves by connected symmetric difference. It checks all single-length flip edge counts, component partitions, cutoff-8 disconnection, cutoff-10 connectivity, and the 417 exact eccentricities. Successful output ends with `ALL_VERIFY_OK`.

Independently compile `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_alt.cpp -o verify_alt` and run `./verify_alt`. This constructs the graph from LCF `[-13,5,-5,13]^8`, enumerates all simple cycles of lengths 6, 8, and 10 and toggles each alternating one in every matching. Its output ends with `INDEPENDENT_VERIFY_OK`. The 32-vertex LCF graph and triangle-dual construction were also verified isomorphic using an exact graph-isomorphism test.

The two algorithms use different graph presentations and different adjacency-generation methods; they verify one complete finite assertion. They do not imply a result on arbitrary cubic graphs or certify absence of unindexed prior literature. No separate external scholarly audit has been performed.
