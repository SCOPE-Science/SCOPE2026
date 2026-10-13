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

# Reproducibility and proof boundaries

From this directory execute `python3 checker.py`. Python 3 and its standard library suffice; no external packages, network services or omitted data are used. Its expected complete standard output is `checker_output.txt`. Checks include the truncated-cube lattice points and facets, all rank-\(n\) toric singular faces for \(4\le n\le8\), exact rational matrix ranks, the four-cycle equations, and integer recovery of edge potentials.

The universal assertions for all \(n\ge4\) follow from the symbolic argument in RESULT.md: integral facet normals, the two toric class-group presentations, localization, and the parity-based inverse of the edge-restriction map. None of the finite computations is used to assert an infinite classification by enumeration. The source's toric charts and published singular-component decomposition are external mathematical premises, cited in RESULT.md. Independent audit remains unperformed.
