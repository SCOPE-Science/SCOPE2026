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

# Reproducibility and limits

Run `python3 verify_cyclic.py` and `python3 verify_vectors.py` with standard Python 3. Neither script uses third-party packages, external files, network calls, or randomized sampling. Both independently construct the graph, enumerate all dominating sets of cardinality three and four, and compare all pairwise guard movements with shared-endpoint incidence. Their checks include that every attack on an unoccupied vertex has a reachable minimum dominating response.

The first verifier constructs the incidence lines from differences \(\{0,1,3\}\) modulo seven and enumerates complete matchings using permutations. It outputs 21 minimum configurations, 168 shift edges, degree 16, diameter two, and 21 winning initial positions. Its distance histogram counts ordered pairs, including 21 distance-zero pairs, 336 ordered adjacent pairs and 84 distance-two pairs.

The second verifier builds the binary projective plane from the seven nonzero vectors of \(\mathbb F_2^3\), uses bitwise closed-neighborhood coverage, and checks guard transitions with a separate recursive matching algorithm. It independently finds 21 minimum configurations, 168 legal moves and 42 blocked pairs, exactly those pairs of incident edges sharing endpoints.

The files `cyclic_output.json` and `vectors_output.json` record the observed outputs. These finite checks supplement the explicit proof and its sixteen-route transition table; they do not assert a family-wide result for all projective planes, and neither the scripts nor this note represents external certification.
