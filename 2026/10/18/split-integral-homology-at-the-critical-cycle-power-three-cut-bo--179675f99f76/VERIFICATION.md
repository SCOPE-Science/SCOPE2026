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
# Reproducibility and verification

Execute `python3 verify.py` with standard Python 3. The observed output is:

```
octagonal complex: 78 faces; 20 certified collapses; sphere triangulation (8,18,12)
block-map sanity: all p from 2 through 64; symbolic proof required beyond
degree-matrix sanity: p=2..16, identity-minus-cyclic-shift integral pairing
```

The checker enumerates the complete octagonal Alexander dual, validates individual elementary collapses and the terminal two-sphere, and directly tests the block-section and quotient maps and exact integer degrees in the indicated finite ranges. The unbounded statement additionally requires the explicit all-parameter combinatorial argument and Alexander duality in RESULT.md. The checker does not prove a complete homotopy classification or torsion absence, and no independent audit is claimed.
