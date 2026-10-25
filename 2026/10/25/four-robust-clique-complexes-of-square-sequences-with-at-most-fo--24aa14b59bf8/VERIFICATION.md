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

# Verification record

The package includes `square4_verify.py` and `square4_homology.py` as self-contained Python scripts (the only third-party requirement is NetworkX). Their companion `.out` text files contain recorded outputs. The graph-isomorphism enumeration was executed for all four levels, every simplicial face was directly generated for every representative, and every Hasse covering was checked to establish acyclicity of the complete matching. This supports the integral homotopy type through discrete Morse theory. Independently, the second script rebuilt the graph and face enumeration and reduced every mod-two boundary matrix. Its homology classifications agree for all 39 graphs. Limit: these finite computations certify only the stated bound of four constituent squares and cannot establish Conjecture 5 for arbitrary length.
