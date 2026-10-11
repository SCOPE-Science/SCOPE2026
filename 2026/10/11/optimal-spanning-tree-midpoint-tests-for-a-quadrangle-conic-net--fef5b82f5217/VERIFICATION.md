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

The universal argument is symbolic and does not rely on finite sampling.

1. For a side from \\(v_i\\) to \\(v_j\\), restrict a polynomial \\(H\\) of degree at most \\(2\\) to \\(\\phi(t)=H(v_i+t(v_j-v_i))\\). Since \\(\\phi\\) is quadratic,
\[
\phi'(1/2)=\phi(1)-\phi(0),
\]
so the midpoint derivative vanishes exactly when \\(H(v_i)=H(v_j)\\).
2. In a nondegenerate quadrangle, the kernel of evaluation at the four vertices is precisely the two-dimensional conic pencil. Thus evaluation has rank \\(4\\), and the net polynomial space is the preimage of the diagonal line \\(\\{(a,a,a,a)\\}\\).
3. A chosen side set forces evaluations to be constant on the connected components of its side graph. This equals the diagonal exactly for a connected graph. If the graph is disconnected, the constraint space strictly contains the net; a degree-two counterexample is obtained by adding a nonzero pencil polynomial to any lower-degree witness if necessary.
4. A connected graph on four vertices needs at least three edges; its three-edge connected graphs are spanning trees. Cayley's formula gives \\(16\\) such minimal test sets.
5. For entanglement, two distinct opposite-side polynomials of the second quadrangle span its pencil. If both pass the three tests of a spanning tree of the first quadrangle, both lie in the first net polynomial space, forcing equality of the two three-dimensional spaces.

The bundled `verify.py` performs a supplementary exact-rational check on a representative nondegenerate quadrangle. It enumerates all \\(64\\) subsets of the six sides, verifies the predicted rank \\(4-c(G)\\) of the side constraints, and confirms exactly \\(16\\) minimal sufficient three-edge subsets. This finite check is not used to prove the theorem for arbitrary quadrangles or fields.

Scientific limit: the connected-graph theorem does not extend verbatim to degenerate quadrangles because repeated vertices require tangency conditions in addition to equality of vertex values.
