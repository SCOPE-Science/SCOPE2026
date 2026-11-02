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

# Verification and reproducibility

The standalone Python standard-library program `kg2_symmetry_check.py` constructs all simplices directly as subsets of common-label stars and exceptional three-edge triangles. For every \(m\) from five through eight it forms all simplicial boundary columns and computes exact ranks over \(\mathbb F_2\) using binary elimination. The output gives face counts \(75,191,455,1044\), and reduced Betti ranks \(4,10,20,35\), each in degree two only.

It calculates the reduced signed Lefschetz number on the actual simplicial chain complex for every permutation in \(S_5\), \(S_6\), and \(S_7\), respectively \(120\), \(720\), and \(5040\) group elements. Every calculated trace agrees with the degree-three exterior-power coefficient computed from cycle lengths. The eight-label case checks all eight rotations, along with the full mod-two simplicial complex. Averaging rotation traces returns quotient second Betti ranks \(0,2,2,4\) for \(m=5,6,7,8\).

Execution: `python3 kg2_symmetry_check.py`. The observed final marker was `KG2_FULL_CHAIN_AND_CHARACTER_CHECKS_OK`.

The calculation is finite, and the mod-two ranks alone do not establish integral torsion-freeness or prove claims for every label size. Those stronger conclusions follow from the separate integral relative-homology and exterior-contraction proof in `RESULT.md`. No independent audit has been performed.
