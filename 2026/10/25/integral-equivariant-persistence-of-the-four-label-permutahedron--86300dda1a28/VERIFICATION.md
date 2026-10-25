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
# Verification and scientific limits

The standalone `verify.py` reconstructs the graph by adjacent-position swaps, shortest-path distances, all simplices at inclusive radii two and three, and the signed simplicial differentials. Its `morse_scale2.json` and `morse_scale3.json` certificates are replayed from the actual extracted files; all elementary free-face conditions, critical maximality, coverage, and complete directed Hasse acyclicity are checked, not inferred from logs. Both certificates have the stated critical-cell distributions. The verifier independently reconstructs the eight facet sphere chains and the twenty-triangle cycle stored in `primitive_cycle.json`; exact integer boundary checks and Smith normal form produce 39 unit nonzero elementary divisors for the 112-by-39 matrix. Reversing the radius-three collapse yields an integral cocycle, checked on every tetrahedron; its pairing with the twentieth-triangle cycle is minus one. Every one of the 48 simplicial symmetry actions preserves the full complexes and permutes the eight oriented facial chains literally, while signed fixed-simplex Lefschetz sums establish the full character table. The last recorded line in `verification_output.txt` is `VERIFY_OK_PERMUTOHEDRON_EQUIVARIANT_PERSISTENCE`.

The nonzero Smith factors prove integral saturation of this explicitly reconstructed lattice, not higher-dimensional or infinite-parameter assertions. The exact sequence splits as abelian groups, but an integral equivariant splitting is not established. SymPy 1.14.0 is needed for Smith form; standard Python suffices for combinatorial reconstruction. Independent external scientific audit is not performed.
