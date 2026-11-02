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

# Reproducibility and limits

Both standalone Python files were executed successfully after construction with Python 3. No external libraries, network requests, or runtime input are required.

```
python verify_direct.py
python verify_forts.py
```

Expected output from `verify_direct.py`:

```
DIRECT_ALL_794_CANDIDATES_OF_SIZE_AT_MOST_FOUR_PASS
FRUCHT_89_SETS_366_EXCHANGES_FAST_PRISM_PLUS_EDGE_PASS
```

Expected output from `verify_forts.py`:

```
LCF_FORT_HYPERGRAPH_AND_PARALLEL_TIMES_PASS
MINIMAL_FORTS 66 ALL_FORTS 851
INDEPENDENT_FOUR_SPEED_LEVELS_PASS
```

The direct program checks the 794 vertex subsets of size at most four, all 3916 unordered pairs of minimum four-sets, all edge and component counts, the prism structure, all claimed diameters, and the shortest four-round bridge between the fast components. The independent program checks all 4095 possible nonempty forts in an alternate LCF graph, computes the 66 inclusion-minimal forts, proves the minimum size, reproduces the four propagation-time classes, checks the exact 89-set roster by a common SHA-256 digest under the explicit isomorphism, and rebuilds the exchange-filtration graph.

The Frucht graph is finite, so complete enumeration is a proof when coupled to the enumerators' correctness arguments; no inference from a finite sample to an infinite family is made. The results have received self-review only, and their historical originality has not been independently verified.
