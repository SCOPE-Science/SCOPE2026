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

The theorem was checked from the definitions and from the finite-dimensional extreme-point criterion.

1. **Primal extreme points.** In a finite graph metric, an elementary molecule is extreme exactly when its two endpoints have no third vertex in their metric segment. This is equivalent to adjacency: an edge has distance \(1\), while a nonedge has an interior vertex on a shortest path. Hence the primal extreme points are precisely the oriented edge molecules.

2. **Dual polytope.** The dual unit ball consists of basepoint-zero potentials satisfying \(|f(u)-f(v)|\le1\) on graph edges. All other shortest-path inequalities follow by summing along paths.

3. **Dual vertices.** If the tight-edge graph \(H_f\) is connected, every midpoint decomposition of \(f\) must preserve the endpoint value \(\pm1\) on every tight edge, so the two summands differ by a constant and coincide at the basepoint. If \(H_f\) is disconnected, a non-base component can be shifted by \(\pm\varepsilon\); finiteness makes the minimum slack over crossing nontight edges positive. Thus \(f\) is extreme iff \(H_f\) is connected.

4. **Bipartite direction.** For an original edge \(uv\), any path from \(u\) to \(v\) in the connected spanning subgraph \(H_f\) has odd length. Summing \(\pm1\) along that path gives an odd integer equal to \(f(u)-f(v)\), and the edge inequality bounds its modulus by \(1\). Therefore every primal-dual extreme pairing has modulus one.

5. **Nonbipartite direction.** A spanning-tree parity potential takes values in \(\{0,1\}\), is 1-Lipschitz, and has every tree edge tight, so it is dual-extreme. A nonbipartite graph has an edge joining equal tree parity classes, producing a primal extreme edge molecule paired to zero.

6. **Numerical-index conversion.** McGregor's finite-dimensional theorem states that \(n(X)=1\) iff \(|x^*(x)|=1\) for every \(x\in\operatorname{ext}B_X\) and every \(x^*\in\operatorname{ext}B_{X^*}\). The two graph directions above meet the hypotheses and obstruction exactly.

The standalone script `verify_small_graphs.py` uses only the Python standard library. It enumerates every connected labeled simple graph on \(2\) through \(5\) vertices, enumerates integer-valued 1-Lipschitz potentials in a diameter-controlled range, recognizes dual extreme points by tight-edge connectedness, and checks the theorem's extreme-pairing condition. Its replay output is:

`VERIFY_OK connected_labeled_graphs=771 extreme_dual_vertices=16716 n=2..5`

This computation is a finite stress test, not an exhaustive proof for arbitrary finite order. The symbolic proof establishes the theorem. No complex-scalar or weighted-graph claim is made.
