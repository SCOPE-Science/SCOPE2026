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

In the same directory as `verify.py` and `CERTIFICATE.json`, run `python3 verify.py CERTIFICATE.json` with Python 3 standard library. The checked execution returned:

`CERTIFICATE_OK vertices=256 edges=408 matching_edges=112 independent_vertices=144 components=13`

The checker constructs the unique \(256\) integer box values, tests all \(32640\) unordered pairs with exact `math.isqrt`, checks every member of the 144-element independent set, and verifies that all 112 upper-bound edges belong to the graph and have pairwise distinct endpoints. The disjoint-edge bound gives \(256-112=144\). The supplementary component census is exact but not needed for optimality. Finite exhaustive calculations can prove this finite claim; they make no statement about an infinite family. No independent audit has been performed.
