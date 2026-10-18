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

Run `python3 verify_franklin.py` using an ordinary Python 3 installation; the program uses only the standard library and prints `PASS` after all assertions. All mathematical inputs are reconstructed from the included LCF definition, without requiring an external table or precomputed group listing.

The script checks all \(4096\) vertex masks and obtains the nonempty face vector \((12,48,76,45,12,2)\); constructs all \(95\) Morse pairs and the five exact critical masks; builds the complete oriented Hasse diagram and verifies a topological order on all \(195\) nonempty faces; enumerates all adjacency- and nonadjacency-preserving vertex permutations, finding \(48\); identifies the central half-turn; evaluates all signed Lefschetz fixed-face contributions; verifies the eight order/trace count classes and the two character inner products; and independently calculates the simplicial boundary ranks over two finite fields.

The logical integral homotopy proof uses the complete acyclic matching and the cellular absence of one-cells, not just finite-field rank agreement. The character proof uses reduced Lefschetz normalization including the empty simplex. Independent scientific validation has not been performed. The sole residual scientific risk is unindexed or inaccessible literature coverage of the same precise statement.
