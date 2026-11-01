---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The maximum source-path length strictly increases on arcs and is automorphism-invariant, so quotient directed multigraph D/H remains acyclic and essential. Any arc-orbit path can be lifted by moving a representative arc with a group element to match the current lifted vertex; this preserves path presence and absence in full orbit selections. Hence constant barycentric coordinates on arc orbits give PL identifications |PF(D)|^H=|PF(D/H)| and similarly PM. The published Grinberg–Katthän–Lewis sphere theorem gives fixed dimensions |U/H|-2 and |E/H|-|U/H|-1. A g-invariant face contributes (-1)^(number of arc orbits -1) to augmented Lefschetz, so the orbit quotient's sphere Euler sign yields rank-one integral characters sgn(g|U) for PF, sgn(g|E)*sgn(g|U) for PM. This applies to each subgroup, including degree -1 boundary. Independent all-orbit-subset path-lifting and exact signed face calculations for S2×S2 on a 1-2-2-1 layered network recovered 8 PF/PM trace tests and all four subgroup orbits.

## originality

PASS

Theorems 1.9 and 1.10 of Grinberg–Katthän–Lewis are the explicitly acknowledged non-equivariant input, and do not themselves identify geometric fixed points or automorphism modules. General group-complex Morse results have no such specialized arc/vertex orbit-count dimensions in inspected scope. The signs require both exact orbit-path lifting and Lefschetz orientation; ordinary sphere homotopy alone cannot force an action.

## value

PASS

Exact geometric fixed-point sphere profiles for every symmetry subgroup and the contrasting integral orientation modules of the two naturally Alexander-dual path complexes are substantial usable equivariant data for arbitrary essential finite networks. The formulas distinguish path obstruction and complement-complex representations beyond known ordinary sphere dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
