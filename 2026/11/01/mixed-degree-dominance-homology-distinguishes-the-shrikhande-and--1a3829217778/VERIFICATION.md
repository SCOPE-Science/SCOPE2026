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

# Reproducible exact finite verification

Run `python3 verify_dominance_twins.py` from the same directory as the standalone script. It requires only Python 3's standard library. The recorded output is `verification_output.txt`; the verifier ends in `DOMINANCE_SHRIKHANDE_ROOK_EXACT_INTEGRAL_HOMOLOGY_OK` only after all assertions pass. All graph data and all simplices are reconstructed from definitions, not loaded from prior outputs.

The run checks both sixteen-vertex degree-six strongly regular graphs, every one of the \(65,536\) possible vertex subsets, independent exact tests for membership in both neighborhood and dominance complexes, all boundary signs and their incidence dictionaries, and every free-face pair. It reduces the two complexes to simplicial cores of \(652\) and \(1,072\) nonempty faces, then performs respectively \(324\) and \(530\) unit-pivot integral cancellations. Boundary-square-zero and transpose consistency are checked throughout and on termination. The remaining chain groups have vanishing differentials, giving the complete torsion-free integral homology of the neighborhood complexes, which transfers by integral combinatorial Alexander duality to the dominance groups.

The original neighborhood-complex mod-two boundary ranks are independently recomputed and yield the same Betti ranks. Direct Euler-characteristic and face-vector checks further corroborate the calculations. The executable records ordered cancellation-pair hashes so the exact integer computation can be compared across executions.

These finite exhaustive calculations establish only the specific two graph cases and only integral homology of their dominance complexes. Chain cancellations are not asserted to be homotopy-preserving simplicial collapses, and neither the homotopy types of the dominance complexes nor the general strongly regular graph case is determined. No independent external mathematical audit has been performed.
