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
# Exact verification and scope

Run the bundled standalone script with a standard Python 3 interpreter:

```shell
python3 verify.py
```

Expected identifying output:

```text
VERIFY_OK pattern-four cycle-polytope: vertices=160 edges=2667 dimension=18 diameter=2 independent_cycle_enumerations=yes two_independent_adjacency_tests=yes all_12720_pairs=yes full_degree_profile=yes
```

The script generates all 24 permutations and 6 overlap states, obtains all directed simple cycles by independently picking their smallest state and their smallest labeled arc, and checks equality after rotation to a canonical arc word. For every one of the 12,720 unordered pairs of the 160 cycles, it evaluates the one-dimensional-face condition both through exact incidence-matrix rank computed by connected components and by counting simple cycles within the union support. It then verifies all ten degree classes, the joint cycle-length/degree counts, the handshake sum, the two monotone loop vertices and all-pairs shortest-path eccentricities via breadth-first search. No numerical tolerance, sampling, optimization oracle, downloads or third-party libraries are used.

The face-rank criterion is supported by the proof in `RESULT.md` and by Borga–Penaguiao, arXiv:1910.02233, Proposition 2.6 and Theorem 2.7. The enumeration is complete for this specific finite graph; it is not a general proof for larger pattern lengths. Both computational approaches share the same input definition, and independent audit has not been performed.
