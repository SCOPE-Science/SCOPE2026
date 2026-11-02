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

# Exact finite verification

The package contains all five labeled graph edge lists, the exhaustive subset enumerator (`enumerate.cpp`), an independent direct-forcing simulator (`direct_check.cpp`), expected count vectors (`baseline_counts.json`), and a reproducibility driver (`verify.py`). Running `python3 verify.py` compiles both C++17 programs, checks graph input validity and count vectors for \(\ell=0,1,2\), and requires successful direct-process comparisons.

For each graph, the exhaustive enumerator visits each of its \(2^{|V|}\) possible white masks. It computes unique-neighbor exposure and recursively records whether any nonempty fort is contained in the mask. Every initial blue mask is then classified, and minimal forts are counted by examining every single-vertex deletion. These loops prove exactness conditional on the source's elementary bit-mask correctness; their execution does not depend on sampling.

The independent direct checker uses iterative force propagation under every at-most-two-vertex leak set. It classifies every blue set on the tetrahedron, cube, octahedron, and icosahedron, checking every leak choice for predicted successful sets and stopping at the first explicit counterexample for unsuccessful sets. It additionally checks all \(2360\) certified optimal blue sets and deterministic further examples on the dodecahedron. The dodecahedral independent comparison is deliberately not represented as a complete direct-forcing census.

Limitations: verification is finite, specific to the five embedded graphs, and uses a C++17 implementation rather than a formally verified theorem prover. Independently validating the asserted graph isomorphisms and manually auditing the short fort recursion remain worthwhile external audit steps. No independent audit has been performed.
