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

# Reproducible verification

Execute the two included Python 3 scripts independently from a directory containing both files:

```sh
python3 verify_cyclic.py
python3 verify_fano.py
```

The first program builds a 14-cycle plus the seven listed chords, checks every smaller candidate and every six-subset, checks every possible single-vertex exchange and performs breadth-first search from all 448 states. Its successful termination prints `CYCLIC_HEAWOOD_EXHAUSTIVE_PASS`. It verifies 3192 edges, degree multiplicities 28, 168, 168, 84 for degrees 6, 12, 14, 22, all eccentricities six, the complete unordered pair-distance profile (3192, 15204, 32508, 32298, 14868, 2058), and 2940 pairs requiring one extra exchange (1008, 1428, 504 at baseline exchange lower bounds 2, 3, 4).

The second program derives the Heawood graph from the binary dot-product Fano incidence relation, enumerates the 336 automorphisms from all 168 invertible linear transformations and incidence duality, checks all feasibility predicates, computes four full orbits of sizes 28, 84, 168 and 168, and aggregates four complete BFS distance profiles. Its successful termination prints `FANO_GL3_SYMMETRY_CERTIFICATE_PASS`. It independently verifies the same counts.

The two scripts intentionally have different graph constructions, state representations and distance-aggregation approaches. They prove a finite result only; execution is not proof of the absence of historical overlap, and the status of independent scholarly audit remains unperformed.
