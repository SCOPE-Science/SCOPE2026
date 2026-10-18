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

# Reproducibility and scientific limits

Run `python3 verify_sg33.py` in the extracted directory. The verifier uses only the standard Python library; it generates the thirty stable triples directly, rather than loading data. The exact result from the current package is:

```
VERIFIED SG(3,3): vertices=30 independent_faces=15292 matched_augmented_pairs=7644 critical_3=4 incidences=79812 acyclic_vertices=15292 ordinary_critical_0=1 homotopy=wedge_4_S3
```

The two face-generation algorithms produce the same finite sets. A complete directed Hasse graph is checked by topological sorting, which is a finite exhaustive acyclicity certificate, not merely a summary log. The CW consequence relies on Forman's discrete-Morse theorem. The proof establishes the exact finite integral homotopy type; no extension to every Schrijver graph or symmetry-module classification is claimed. Independent scientific audit has not been performed.
