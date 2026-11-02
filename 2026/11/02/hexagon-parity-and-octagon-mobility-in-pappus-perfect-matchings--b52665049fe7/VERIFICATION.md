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

# Verification

`verify_affine.py` enumerates every bijection from nine points to nine lines obeying affine incidence, constructs exact one-cycle symmetric-difference flips of lengths six and eight, checks parity, the three-hub/three-cycle component structure, and full all-source shortest paths.

`verify_lcf.py` constructs the Pappus graph independently from the length-eighteen Hamiltonian cycle with LCF chords, proves exact adjacency equivalence to the affine graph with an explicit vertex bijection, enumerates perfect matchings through a different recursion, verifies that a symmetric difference is one connected 2-regular graph, and independently recomputes all connectivity and metric counts.

Run from the directory containing both scripts:

```
python3 verify_affine.py
python3 verify_lcf.py
```

Expected markers:

```
AFFINE_PAPPUS_HEXAGON_OCTAGON_EXHAUSTIVE_PASS
LCF_PAPPUS_ALTERNATING_CYCLE_INDEPENDENT_PASS
```

Both were observed from executed scripts. These calculations establish a finite, exhaustive graph theorem, not a statement about arbitrarily large related graphs. No external audit has been conducted.
