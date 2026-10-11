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
The theorem in `RESULT.md` is a complete finite proof for the graph associahedron of \(K_{4,4}\). The exact source-code checker is `verify.py` and its reference data are in `orbit_certificate.json` in the same directory.

Run `python verify.py` with Python 3. It requires no external packages and recomputes all enumerations rather than trusting the certificate as an output log. Actual checks include:

1. Generic recursive root/component enumeration of all maximal tubings from connected induced subgraphs of \(K_{4,4}\).
2. Independent generation from all \(70\) colored-broom patterns and all their allowed labelings; equality of both full tubing sets.
3. Exhaustive one-tube-exchange adjacency from common \(7\)-tube keys, with exactly two completions for every proper-tube deletion.
4. Degree, undirectedness, vertex count \(29{,}616\), and edge count \(103{,}656\).
5. The exact \(S_4\times S_4\) orbit-size sum, and all \(70\) complete breadth-first searches over the graph.
6. Every representative's exact eccentricity \(15+s\), farthest-vertex tube tuple, and orbit size, checked against the packaged certificate.
7. The four class sizes and overall diameter \(22\).

One diametral pair is certified by the tube tuples
\[
(128,136,200,232,248,252,254,255)
\]
and
\[
(1,17,19,23,31,63,127,255).
\]
A tube bitmask uses bit \(2^i\) for graph vertex \(i\) in the order \(0,\ldots,7\).

The program uses integer and exact-set operations only. Finite exhaustive verification does not establish an infinite-family formula, and the separate scientific literature comparison is not certified by running the checker.
