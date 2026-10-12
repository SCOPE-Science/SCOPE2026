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

Run `python3 verify.py` with a standard Python 3 interpreter.

The verifier constructs \(S_5\) and computes Ulam distance independently in two ways: by longest-common-subsequence dynamic programming and by breadth-first shortest paths in the graph of single-symbol translocations. It checks equality of the two distances for all \(7140\) unordered pairs.

It then constructs the distance-\(\ge 3\) compatibility graph and exhaustively enumerates every four-clique. Exactly \(4020\) occur. For every four-clique the intersection of its four neighbor sets is empty, which excludes every five-clique and proves the optimum \(4\).

The verifier counts exactly \(134\) maxima containing \(12345\), checks the incidence identity, verifies that every maximum has six pairwise distances equal to \(3\), explicitly constructs the \(240\) natural transformations from symbol relabeling and optional position reversal, and recomputes all \(24\) code orbits.

Expected terminal line:

`VERIFY_OK vertices=120 pair_checks=7140 maximum=4 normalized_maxima=134 labeled_maxima=4020 distance_profile=3x6 natural_group=240 orbits=24 orbit_sizes=60x5,120x7,240x12 normalized_sha256=97ab783da1ad9cec5ac603f0822c9446ed206af79f0a9eef75733de73dc7e53e labeled_sha256=3a32e8546a7d31c8bd78dd0d1d764d59e704ddd37c9cda6f9dc995b5dd26c583`

The verifier does not attempt to identify the full Ulam-isometry group or the full automorphism group of the compatibility graph.
