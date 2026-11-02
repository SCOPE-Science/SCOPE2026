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

# Reproducibility record

Run `python3 verify.py` from a folder containing the standalone Python script. It requires no third-party packages. The observed execution produced:

```
VERIFY_OK field q2: (5, 5) dual q4 n1: (67, 15) sampled n2: 399 group64: (67, 15, 15) odd q3: (212, 23)
```

The checker separately implements finite truncated polynomial arithmetic, additive-subgroup construction, symplectic orthogonality, full double-annihilator tests, direct multiplication and centralizer enumeration of the 64-element group, and 399 deterministic rank-two sample modules. For the ternary length-two ring, all 212 additive subgroups are enumerated and the 23 submodules determined. The field case is included as a boundary comparison. The code does not exhaust larger-rank groups or prove a statement for arbitrary parameters; the unconditional proof is in RESULT.md. An independent mathematical audit has not been performed.
