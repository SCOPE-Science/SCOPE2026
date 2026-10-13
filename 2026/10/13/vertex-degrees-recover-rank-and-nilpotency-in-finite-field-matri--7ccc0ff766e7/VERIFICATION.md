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

The proof has two independent layers.

First, the symbolic argument shows that for \(U=\operatorname{im}(A)\), nilpotency of \(AB\) is exactly nilpotency of \((AB)|_U\). The map \(B\mapsto(AB)|_U\) is surjective onto \(\operatorname{End}(U)\), with constant fibers. The exact Fine--Herstein nilpotent count then gives \(q^{n^2-r}\) matrices \(B\) before the simple-graph exclusions. Deleting zero and deleting the self-vertex precisely in the nilpotent case yields the theorem.

Second, `verify.py` exhaustively constructs the graphs for \((n,q)=(2,2),(2,3),(3,2)\). It computes every vertex degree from adjacency rather than from the claimed formula, and separately computes rank and nilpotency. It checks every vertex, all realized degree profiles, and both extrema. A successful run ends with `VERIFY_OK`.

The exhaustive tests use prime fields because they are small enough for transparent full graph construction. The theorem for arbitrary prime powers does not depend on this enumeration; it follows from finite-dimensional linear algebra and the finite-field nilpotent count.
