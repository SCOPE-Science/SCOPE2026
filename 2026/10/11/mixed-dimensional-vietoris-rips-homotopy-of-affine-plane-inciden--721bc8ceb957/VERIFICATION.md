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

# Reproducibility

Run `python3 verify.py` using only the Python 3 standard library. It independently builds finite affine planes over the prime fields of orders \(2\) and \(3\), checks incidence axioms, computes graph distances by breadth-first search, enumerates all maximal cliques of the distance-two graph with Bron–Kerbosch search, checks equality with an independently derived predicted facet family, enumerates the resulting simplices, and computes reduced mod-two boundary ranks. The actual execution returned `VERIFY_OK` with reduced homology supported in degree \(2\) of rank \(4\) for order \(2\), and in degrees \(2,3\) of rank \(16\) each for order \(3\).

These exhaustive finite checks are not a proof for all affine planes. The universal theorem is certified mathematically by the explicit simplicial union, two collapses, simply connected join, homotopy pushout, and graph cycle-rank argument in `RESULT.md`. The precise conditions for passing from homological checks to homotopy type are supplied by that argument, not inferred from finite data. No non-Desarguesian finite plane was enumerated here.
