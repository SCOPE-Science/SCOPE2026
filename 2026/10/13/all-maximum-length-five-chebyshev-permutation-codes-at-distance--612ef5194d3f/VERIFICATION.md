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

Run `python3 verify.py` from this directory. The verifier is standard-library-only and performs two exhaustive constructions of the final code set.

First, it generates all \(120\) permutations in \(S_5\), computes Chebyshev distance directly, builds the compatibility graph, and enumerates every clique of size \(10\). The direct low-position argument proves that a larger clique is impossible.

Second, it enumerates every bijection on the ten two-subsets of the five coordinates that sends each two-subset to a disjoint two-subset. It obtains exactly \(60\) such maps, then exhaustively assigns the internal orientations of \(1,2\) and \(4,5\), pruning only by the exact distance test. The resulting code set is compared for exact equality with the graph enumeration.

The replay output is:

`VERIFY_OK perms=120 compatibility_edges=5340 maximum=10 labeled_maxima=192 petersen_maps=60 cycle_types=2^5:6,5^2:24,2+8:30 orientation_counts=4,2,4 natural_group=240 orbits=24,48,120 stabilizers=10,5,2 profiles=30/15,25/20,28/17 balanced=true`

The verifier also checks `census.json` byte-semantically after JSON parsing against the regenerated census, including all \(192\) labeled maxima. No claim is made about parameters outside length \(5\), minimum distance \(3\), or about the full automorphism group beyond the explicit order-\(240\) isometry action.
