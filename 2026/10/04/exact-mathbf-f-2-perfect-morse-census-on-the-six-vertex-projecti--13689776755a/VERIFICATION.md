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
The verification script is `verify.py` and is self-contained in the package.

It checks the exact ten-facet standard triangulation, all fifteen edge incidences, all \(1{,}296\) Prüfer spanning trees of the complete one-skeleton, connectivity of every ten-edge complementary dual graph, and its unique-cycle length. The resulting histogram is exactly \(726\) cycles of length \(5\), \(540\) cycles of length \(6\), and \(30\) cycles of length \(9\). Deleting one edge from each complementary dual graph is tested directly, giving \(7{,}140\) compatible dual spanning trees in total.

The script separately enumerates all vertex permutations preserving the facet set, obtaining an automorphism group of order \(60\) with a transitive orbit on the \(15\) edges. It also tallies the leftover edge directly and obtains \(476\) tree-cotree decompositions for every edge. The derived counts are \(428{,}400\) \(\mathbf F_2\)-perfect discrete gradient vector fields and \(28{,}560\) per critical edge.

The script does not attempt to count distinct real-valued discrete Morse functions inducing the same gradient field, and it makes no claim about larger triangulations or other coefficient fields.
