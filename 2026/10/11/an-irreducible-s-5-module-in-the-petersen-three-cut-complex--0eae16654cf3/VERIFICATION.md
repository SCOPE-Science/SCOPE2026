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
# Verification record

Execute `python3 verify_petersen.py`. The code reconstructs the ten Kneser-graph vertices, all fifteen adjacency pairs, ninety disconnected-triple-complement facets, and every nonempty face. It tests the seven-dimensional face vector `(10,45,120,210,252,210,90)`, 937 faces, and all 4440 Hasse covers.

Its staged element-toggle matching contains 465 distinct pairs. It orients every unmatched Hasse cover downward, every matched cover upward, and topologically sorts all 937 faces. The remaining critical profile is one zero-cell and six six-cells. Since there are no intermediate cells, this proves the claimed homology support and wedge type.

For each of all 120 permutations of five labels, the checker verifies that adjacency is preserved, computes the signed fixed-simplex Lefschetz sum, subtracts the degree-zero trace, and verifies equality to the exterior-square character computed independently from fixed letters and squared permutations. Class sizes and the irreducibility inner product are checked with exact integers.

The program prints `VERIFY_OK` on successful completion and fails on assertion violations. No floating point arithmetic, outside packages, external logs, or probabilistic sampling are needed. Only this finite graph and its natural rational symmetry representation are established. No independent audit is asserted.
