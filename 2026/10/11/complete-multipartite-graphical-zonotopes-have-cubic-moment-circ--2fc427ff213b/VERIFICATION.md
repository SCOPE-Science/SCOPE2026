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
The arbitrary-part-size theorem is proved symbolically in `RESULT.md`; finite enumeration is corroborative only.

Critical checks:
- the standard graphical zonotope is centrally symmetric about one half of the degree vector;
- a vertex indexed by an acyclic orientation has coordinate vector equal to the indegree vector;
- centered coordinates are one half of indegree minus outdegree;
- the squared norm equals one quarter of the degree-square sum minus the number of directed two-edge paths;
- in a complete multipartite graph, every triple from three distinct parts contributes exactly one directed two-edge path regardless of order;
- a triple with two vertices in one part contributes exactly when the third vertex interleaves them;
- zero interleaving is equivalent to a topological order with each part contiguous, hence to a total order of the parts;
- the resulting exact radius simplifies to \((N^3-\sum_i n_i^3)/12\);
- antipodal farthest vertices give diameter \(2R\).

`verify.py` exhaustively enumerates all distinct multipartite topological words for every integer partition of total order at most \(8\), reconstructs the centered indegree norm, verifies the cubic-moment formula, and checks that the maximizers are exactly the block words. It does not assess originality.
