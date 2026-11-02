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
# Executable verification

Use `python3 verify.py` from the same extracted package. The sole dependency is the Python standard library. The checker reconstructs the \(27\) graph vertices and six-neighbor adjacency of each vertex, without loading a precomputed graph. It checks every \(\binom{27}{j}\) subset for \(1\le j\le7\), confirms the exact degree-test solution counts \((0,0,0,0,0,54,0)\), and proves every six-element class is one of the \(54\) coordinate boxes. It examines all triples of these boxes, finding \(288\) valid complementary nine-classes, all using a common full coordinate. A structurally separate \(3\times3\) rook-graph matching enumeration confirms \(96\) quotients per axis, split \(24\) straight-line and \(72\) L-shaped residual triples. It verifies the explicit four-colour witness, checks all \(1296\) full graph automorphisms preserve adjacency, and computes partition orbit sizes \((18,54,216)\).

The verifier's completed local execution printed `ALL_SMALL_CLASS_SUBSETS_OK 1285623`, `ALL_OPTIMAL_UNLABELLED_PARTITIONS_OK 288`, `INDEPENDENT_ROOK_PARTITION_COUNT_OK 96`, `FULL_AUTOMORPHISM_ORBIT_CENSUS_OK [18, 54, 216]`, `NAMED_FOUR_COLOURINGS_OK 6912`, and `VERIFY_OK`. No floating-point computations, timeouts, partial enumerations, external data, or probabilistic assumptions occur. The finite loops exhaust the fixed case; they neither prove a result for larger graphs nor confer independent certification.
