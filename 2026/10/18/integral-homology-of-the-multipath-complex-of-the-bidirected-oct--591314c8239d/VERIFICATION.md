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

# Reproducing the finite certificate

Run `python3 verify_octahedron.py` with Python 3 and its standard library. No input data or downloaded dependencies are required. The program constructs the 24 permitted directed arcs from the disjoint vertex pairs \(\{0,1\},\{2,3\},\{4,5\}\), enumerates all subsets with at most five arcs, checks selected in-/out-degrees and directed circuits, verifies closure under deletion, and reconstructs the explicit sequential-pivot acyclic matching.

Expected output values: augmented face counts `[1, 24, 192, 616, 744, 240]`; maximal-face counts `[24,240]` in dimensions three and four; 844 pairs; 6,408 directed Hasse covers; critical-cell vector `[1,0,3,92,32]`. Exact signed augmented boundary ranks over \(\mathbb Q\) are `[1,23,169,444,208]`, giving reduced rational Betti vector `[0,0,3,92,32]`. The program terminates with `VERIFIED_OCTAHEDRAL_MULTIPATH_HOMOLOGY` or raises an assertion on failure.

The integral conclusion invokes Forman's acyclic-matching theorem: the certified CW model has rational Betti numbers equal to its cell counts in all positive degrees, forcing every integral differential to be zero. No computation of attaching maps is claimed; the full homotopy type, including possible nonlinear attaching invariants, is undetermined. The verification is finite, exhaustive and exact, but has not undergone independent mathematical audit.
