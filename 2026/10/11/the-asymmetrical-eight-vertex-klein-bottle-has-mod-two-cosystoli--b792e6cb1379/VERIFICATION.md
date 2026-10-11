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

Run `python3 verify.py` in this directory. The script uses only the Python standard library. It rebuilds the listed facets, edges, face incidence, and dual graph; checks the closed connected surface and the trivial simplicial automorphism group; performs exact bit-linear algebra over \(\mathbf F_2\); enumerates all \(512\) one-cocycles and \(128\) coboundaries; and recomputes the complete classwise support spectrum and cup-square values.

The decisive checks are exhaustive over the complete finite cocycle space. The finite enumeration is not used to claim an infinite theorem. The proof scope is only the fixed 1133 triangulation and mod-two coefficients.

Expected leading output:

`VERIFY_OK f=8,24,16 H1_F2_dim=2 aut_order=1 nonzero_cosystolic_spectrum=5x1,6x5,6x3 unique_weight5_support=BC,BG,CE,DE,DG cup_square_zero_class=6x5 all_minimizers_single_dual_cycles=yes`

`verification_output.txt` contains the complete output from the packaged replay, including the full weight enumerator of each nonzero class.
