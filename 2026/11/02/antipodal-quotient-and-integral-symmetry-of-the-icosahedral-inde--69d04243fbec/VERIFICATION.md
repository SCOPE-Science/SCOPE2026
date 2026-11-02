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
# Verification of the icosahedral independence-complex classification

Run `python3 verify_icosahedral.py` in the directory containing the embedded checker (only Python standard library is needed). The checker constructs the graph from the six explicit fivefold edge families, checks graph-distance antipodes, enumerates its exact independent-face lattice, and tests all triangle/core incidence counts. It verifies core connectivity, link cycles, Euler characteristic, and the six remaining antipodal edges.

Its complete adjacency-preserving backtracking finds exactly 120 graph automorphisms. For each automorphism it checks the signed permutation on antipodal edges, orientation action on the two-sphere fundamental chain, and the signed fixed-simplex Lefschetz identity. Rotation subgroup character counts by element order must be (1 element of order 1 with trace 6; 15 of order 2 with trace -2; 20 of order 3 with trace 0; 24 of order 5 with trace 1). Both entire-group invariant positive-degree homology dimensions are zero.

Expected terminal marker: `ICOSA_HOMOLOGY_CORE_SPHERE_PLUS_SIX_ANTIPODAL_EDGES_OK`.

**Limits.** Exact finite enumeration checks the critical combinatorial premise and action; the surface-classification theorem, homology long exact sequence, Lefschetz fixed-point argument, and quotient-surface classification are proven in `RESULT.md` rather than outsourced to the script. No independent audit has been performed.
