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

Run `python3 verify.py` with Python 3.8+ in this directory; no packages outside the Python standard library are required.

The verifier constructs the two pentagonal rings, ten cap spokes, ten ring edges and ten cross-ring edges of the icosahedral graph, checking 12 degree-five vertices and 30 edges. It executes two separately implemented zero-forcing procedures on all 4096 initial subsets, checks the complete seven-coefficient generating polynomial, and enumerates all 120 graph automorphisms with a backtracking adjacency/nonadjacency test. It partitions all 924 six-subsets into the 18 explicitly listed orbits and verifies the eight-or-nine induced-edge criterion for every six-subset, with the three winning orbit sizes 20, 60 and 120.

The same executable generates all 200 minimum sets, checks the single-exchange adjacency using both move generation and direct Hamming distance on every pair, and runs a complete shortest-path search from each of the 200 configurations. It checks 1320 exchange edges and the full distance vector. Finite exhaustive enumeration is legitimate here because all relevant state spaces are precisely bounded and fully traversed; no larger or infinite-family assertion is made. Assertions in the executable trigger failure rather than a success report if a check disagrees.

Independent external validation has not been performed; completion of the local verifier does not certify originality or substitute for independent expert audit.
