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

Run `python3 checker.py` with an ordinary Python 3 interpreter; no third-party packages are needed. The program executed successfully with the opening line:

```text
D4_CENTRAL_SECTIONS_OK root_vertices=24 edges=96 facets=24 chamber_strata=15 orbit_types=7 sample_normals=15
```

It computes 24 integer root vertices, 96 incident edges, 24 octahedral facets and all fifteen nonempty masks of the fundamental chamber. Every intersection coordinate and rank calculation uses exact rational arithmetic. It checks the seven claimed polygon inventories, their chamber-mask invariance, 15 alternative positive-normal samples, multiple signed coordinate permutations and Euler's relation.

The proof of exhaustiveness over uncountably many nonzero normals uses the classical root-system chamber reduction and root-sign constancy, not numerical sampling. The computation has not been independently validated and does not establish historical priority.
