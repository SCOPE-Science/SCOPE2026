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

The reproducible evidence is in `verify_pappus_perfect.py`, `CERTIFICATE.json` and `VERIFY_OUTPUT.txt`. Invoke `python3 verify_pappus_perfect.py` with Python 3.9 or newer and no third-party dependencies. The script must terminate with `VERIFY_OK PAPPUS_PMC_INTEGRAL_MIXED_WEDGE` and the exact graph, face, gradient, matrix and homology summaries preserved in the output file.

The verifier reconstructs the LCF graph and matching complex; checks its 42 perfect matchings both by uncovered-vertex recursion and by bipartite assignment enumeration; checks extendibility of all 35,368 ordinary graph matchings; enumerates every simplex; validates all 7,901 discrete-Morse pairs and the full directed-Hasse-graph acyclicity; calculates signed Morse differentials with integral path recursions; verifies a \(-1\) determinant maximal-rank minor; matches the independently stored finite certificate; and computes ordinary simplicial boundaries independently modulo two.

The resulting CW complex has no one-cells, five two-cells, ten three-cells and one four-cell. Its integral three-cell differential is primitive and onto, and the four-cell differential is zero. The homotopy conclusion additionally uses ordinary Hurewicz and Whitehead theorems, as explained in `RESULT.md`, rather than assuming torsion-free homology alone implies a wedge of spheres.

Scope: this single finite graph only. The checker is a reproducible computational witness; it is not an independent audit or a proof of bibliographic uniqueness.
