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

# Reproducible exact checks

Both executables use Python 3's standard library and run directly with the accompanying complete `certificate.json`:

```text
python verify_flips.py certificate.json
python verify_direct.py certificate.json
```

The first program enumerates cycle edge masks and symmetric differences with all host-graph four-cycles; it independently derives component diameters and the full graph-automorphism action. The second constructs the graph from its triangular faces and produces legal two-opt moves by explicit segment reversal of vertex sequences. They check the entire ordered list of cycle masks and the entire unordered switch-pair list against the certificate.

Recorded successful checks:

```text
VERIFY_FLIPS_OK edges=30 undirected_Hamilton_cycles=1280 4cycles=30 switch_edges=1800
VERIFY_FLIPS_OK components=30x36+60x2+80x1 nontrivial_large_components_each_58edges_diameter8
VERIFY_SYMMETRY_OK automorphism_order=120 component_orbits=[(1, 20), (1, 60), (2, 60), (36, 30)]
VERIFY_DIRECT_OK source_faces=20 edges=30 tours=1280 independent_2opt_edges=1800
VERIFY_DIRECT_OK exact_cycle_and_transition_tables_equal=true components=30x36,60x2,80x1
```

The certificate uses the edge ordering stored in its `icosahedron_edges` field. Each Hamiltonian cycle is one nonnegative integer bitmask; switch pairs use zero-based indices into the sorted bitmask list. The programs compute these quantities afresh and abort on any mismatch. The exhaustive domain has precisely 12 labeled vertices, 30 edges, and all Hamiltonian cycles of that graph; no claim for arbitrary graph size is checked or implied. These are internal computational checks, not independent external validation.
