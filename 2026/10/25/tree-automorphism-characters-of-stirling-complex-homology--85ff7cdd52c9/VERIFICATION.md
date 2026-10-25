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

The mathematical argument checks that each full-support cubical cell has trivial stabilizer for the specified graph-automorphism action, then uses the exact equivariant Euler–Poincaré identity and Kozlov's published sphere-wedge theorem. This is the all-parameter proof; the finite tests below independently corroborate selected cases without replacing it.

Run `python3 verify_stirling_leaf_action.py` using Python's standard library. The expected final marker is `STIRLING_TREE_AUTOMORPHISM_CERTIFICATE_OK`.

Complete mod-two cubical boundary ranks were checked for the three-vertex path with three, four and five resources, the three-leaf star with four and five resources, and the four-vertex path with five resources. The complete ranks and Betti vectors are printed during replay. All tree automorphisms in the displayed small groups, including all six elements of the star's \(S_3\), were checked for cell-fixity and Lefschetz trace. Exact rational integrality of \(q\) was checked independently for stars with \(2\le r\le6\) over six consecutive resource counts beginning at the minimum.

Finite checks cannot certify the universal quantifiers or exclude unindexed equivalent literature. The rational representation classification is proved using freely acting chain modules, the known sphere-wedge theorem, and characteristic-zero representation theory. No independent audit has been performed.
