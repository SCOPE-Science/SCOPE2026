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

# Exact reconstruction and checks

Execute `python3 verify.py` in any Python 3 installation; no downloaded tables, third-party packages, or external files are needed. The program constructs the 27 triples, their Hamming distances, and the 0-, 1- and 2-threshold clique complexes from first principles.

The scale-zero check counts 27 vertices. The scale-one check finds 27 vertices, 81 edges, and 27 coordinate triangles, with each edge contained in exactly one triangle; elementary free-face deletions leave a connected 54-edge graph. The scale-two check enumerates 5,949 nonempty faces with dimension counts \((27,243,945,1728,1620,945,351,81,9)\). The canonical 27-stage vertex-toggle face matching produces 2,951 matched pairs and 47 critical cells, one in dimension zero and 46 in dimension three. A topological sort of the oriented Hasse diagram checks 27,189 incidences and visits all 5,949 faces; this is the decisive complete acyclicity certificate. Exact mod-two boundary ranks provide an independent numerical cross-check, not a surrogate for the integral proof.

These checks are complete only for the specified 27-point metric. Inference to all triple categorical graph products is expressly unproved. No independent validation has been claimed.
