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

The accompanying pure-Python verifier begins from a complete explicit 30-edge graph definition; it does not import graph data or rely on numerical topology libraries. It exhausts all 4096 masks, uses both induced-degree and forbidden-triple predicates, checks the entire reversed matching Hasse graph with a topological sort, computes signed integer Morse cancellation via unit pivots and exhibits a determinant-one minor. A separate chain-boundary rank implementation checks mod 2, mod 3 and mod 5 ranks. The complete automorphism group is generated from two edge-preserving permutations and every one of its 120 signed Lefschetz traces is checked for conjugacy invariance.

Reproduce by running `python3 verify_icosahedral_dissociation.py` from this directory. Standard output must equal `verification_output.txt`; the final line is `ALL_CHECKS_PASS`.

The determinant-one minor, the Morse acyclicity certificate and the absence of critical one-cells together support the integral *homotopy*, not merely homology, conclusion. Mod-prime ranks alone would not exclude integral torsion and are not used as the sole proof. The group representation is rational; no integral lattice classification or equivariant homotopy classification is asserted. Independent audit has not been performed.
