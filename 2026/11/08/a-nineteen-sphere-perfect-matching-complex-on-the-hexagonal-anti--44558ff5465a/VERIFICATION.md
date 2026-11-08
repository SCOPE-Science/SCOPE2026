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

# Exact finite verification

Run `python3 verify.py` from this directory. It reconstructs the 12-vertex, 24-edge graph; enumerates all perfect matchings by least-uncovered-vertex recursion; enumerates the resulting complex a second way by testing every matching for extendibility; and checks all complex faces. It builds two complete acyclic discrete-Morse matchings with opposite element orders and tests all 5,004 incidences by full topological sorting. The first gives 696 pairs and the critical cells \((1,0,19,0,0,0)\) in dimensions zero to five; by the discrete-Morse theorem this proves the integral wedge of nineteen two-spheres.

A separate full mod-two boundary calculation gives ranks \((23,157,300,180,36)\); this is an independent finite homology cross-check, not a substitute for the integral homotopy proof. Signed fixed-face Lefschetz sums calculate the natural dihedral character on every group element; the calculation uses the already-proved concentration of rational homology in degree two. The output of the exact replay is in `verify_output.txt`.

Limits: finite proof for this specific graph only. No integral equivariant splitting or family classification is proved. External independent audit was not performed.
