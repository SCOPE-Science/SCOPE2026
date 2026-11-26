---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A subset is a face exactly when it avoids the 60 triples consisting of a vertex and two of its neighbors. Independently generating faces by the largest label in each forbidden triple reproduced all 62,048 nonempty faces and f-vector (20,190,1080,3985,9784,15910,16600,10390,3460,564,60,5). Pairing on the specified parity-first vertex order gave 31,003 pairs and the critical multiplicities (dimension 0: 1, dimension 7: 41); sink deletion certified the orientation of all 400,760 nonempty-face covers by deleting every face. The acyclic matching theorem gives a CW model with one 0-cell and 41 7-cells only. Their attaching maps into the 6-skeleton are constant, proving the wedge homotopy type and the integral homology, not just mod-two Betti numbers.

## originality

PASS

No prior equivalent classification was established. The closest exact catalogue record and two extensions have later indexed provenance. The earlier matching machinery and graph-family theorems do not determine this graph's homotopy type; the closest earlier Desargues entry computes a different complex.

## value

PASS

The Desargues graph is a canonical cubic incidence graph, and Ind_2 is the first higher-independence analogue of its previously studied ordinary independence complex. The exact integral homotopy type is stronger than the face numbers, Euler characteristic, or field homology, and the concentration in dimension seven despite dimension eleven is an informative bounded benchmark. It requires the concrete matching data and is useful for subsequent family and symmetry comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
