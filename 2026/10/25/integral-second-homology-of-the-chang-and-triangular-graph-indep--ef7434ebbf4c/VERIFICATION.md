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

The standalone `CHANG_CHECK.py` was executed on the package's actual source path and produced the embedded `CHANG_CHECK_OUTPUT.txt`. It uses complete finite enumeration, never random sampling or floating point arithmetic. Exact checks include the adjacency parameters, all independent sets, a second direct brute-force enumeration of every four- and five-subset, unique triangular facets of tetrahedra, the two chain identities, connectivity, and rank \(183\) of the simplicial second boundary over \(\mathbb F_2\). The upper bound \(183\) on the rational rank and the unit-pivot split-injectivity argument appear in the proof, rather than being inferred from computational logs.

The calculation proves the integral degree-two ranks in the exact four-graph domain. It does not determine any possible integral degree-one torsion, the full homotopy type, or an infinite graph-family result. The original Chang 1959 full text and a related published repository page were not inspected. Independent audit and independent validation have not been performed, and no external verification status is claimed.
