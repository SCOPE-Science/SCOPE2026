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
# Verification of the subdivided complete-graph spectrum

Run `python3 verify.py` with Python 3, SymPy and NumPy. Recorded replay:

```text
SYMBOLIC_OK sector_identities=4
VERIFY_OK exact_graph_orders=3..8 exact_entries=2882 independent_adjacency_spectra=6
```

The code checks four parameterized rational-function simplifications, constructs the exact spectral projectors from explicit incidence matrices for six consecutive graph sizes, matches all 2,882 entries to an independent orbit-block formula, constructs all spectral projectors afresh from the actual subdivided adjacency matrices, and compares their mixing spectra and ranks. The formula for unbounded graph size is established by the mathematical proof, not by extrapolating these tests. Matrix eigendecomposition involves floating-point tolerance in the independently constructed numerical check; the independent orbit equality is exact rational algebra. No independent external review is claimed.
