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
# Finite verification protocol

Run `python verify_one_line.py`, `python verify_bipartite_matchings.py`, and `python verify_distance_certificate.py orbit_distance_certificate.json` using a standard Python 3 interpreter. For reproducibility, `python make_orbit_certificate.py` regenerates the stored `orbit_distance_certificate.json` deterministically from lexicographically enumerated derangements.

The two primary graph enumerators independently reconstruct the full pair-distance distribution for three sizes and confirm the unique inverse antipode property. The third certificate checker verifies every entry in all eight complete distance arrays by local edgewise and descending-neighbor constraints; these checks are sufficient to prove shortest-path optimality, not merely a sampling agreement. Compare the outputs with `one_line_output.txt`, `matching_output.txt`, and `certificate_output.txt`; the success sentinels are `VERIFY_ONE_LINE_OK`, `VERIFY_MATCHINGS_OK`, and `VERIFY_CERTIFICATE_OK`.

At size six, the certified vertex count is 265, edge count 1260, eccentricity multiplicities 225 at five and 40 at six, and exactly 20 distance-six unordered pairs, all of the form `{σ, σ^{-1}}` with cycle type `(3,3)`. The graph’s special first-divergence property is established against the complete size-four and size-five graphs. These are exhaustive finite checks, not infinite proofs or estimates of Markov-chain mixing.

All evidence is derived from the embedded stand-alone artifacts and their decoded contents. No external independent audit has been performed.
