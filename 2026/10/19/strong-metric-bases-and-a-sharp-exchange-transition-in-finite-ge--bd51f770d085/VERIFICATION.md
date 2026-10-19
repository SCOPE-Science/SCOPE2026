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

Use Python 3 standard library. Run `python3 verify_symplectic.py` and compare its normalized JSON output byte-for-byte with `symplectic_output.json`. Run `python3 verify_asymmetric.py` and compare its normalized JSON output byte-for-byte with `asymmetric_output.json`. Both programs generate their incidence structures rather than relying on an input graph or an external certificate.

The symplectic script verifies generalized-quadrangle axioms, incidence BFS distances, the exact MMD graph, enumeration of all geometric strong metric bases, all unordered exchange costs, connectivity of the sharp-threshold graph and eccentricity distributions at orders \((2,2)\) and \((3,3)\). The asymmetric script derives a double-six 27-point, 45-line GQ of order \((2,4)\), checks its axioms and graph distances, independently enumerates every largest point and line MMD-independent set with maximal-clique search, enumerates 1215 bases and verifies all pairwise costs, threshold graph and diameter three.

These are complete checks of each stated *finite* geometry but are not a computational proof for all values of \(s,t\). The all-parameter result depends on the elementary combinatorial proof in RESULT.md. No independent scientific audit has been performed.
