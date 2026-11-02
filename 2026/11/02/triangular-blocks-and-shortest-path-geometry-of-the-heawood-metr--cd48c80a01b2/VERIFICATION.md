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
# Reproducible finite verification

The supplied scripts are self-contained Python 3.10+ programs requiring only the standard library. Run from this directory:

```sh
python3 scripts/direct_enumeration.py
python3 scripts/fano_symmetry_check.py
```

The cyclic-model program enumerates all 1,001 four-subsets and 2,002 five-subsets of the fourteen vertices, identifies precisely 168 metric bases of size five, and checks the incidence-geometric classification separately. It generates all permitted basis exchanges through every possible deleted/added vertex pair. Breadth-first search from every one of the 168 sources returns common shell profile \((1,5,18,49,71,24)\), five-regularity, 420 edges, diameter five, distance pairs \((420,1512,4116,5964,2016)\), and 4,368 one-extra-exchange pairs. It verifies the 56 triangles cover all configurations without intersection.

The binary-vector program uses an independent Fano coordinatization with line-point incidence given by orthogonality over \(\mathbb F_2\). It uses a closed-form distance function rather than the first script's graph BFS, constructs all basis adjacencies by pairwise set overlap rather than token-toggle operations, and enumerates the 336 incidence automorphisms. The group acts transitively on 168 bases. It independently computes the same graph-metric quantities and triangle structure using all-source search.

Expected success markers:

```text
HEAWOOD_DIRECT_ALL_SOURCES_PASS
GF2_FANO_SYMMETRY_PASS
```

These finite verifications do not constitute an independent scholarly audit and do not certify novelty in all potentially inaccessible literature. They do certify the enumerated mathematical statements for the explicitly defined fourteen-vertex graph, conditional on ordinary execution of the included programs.
