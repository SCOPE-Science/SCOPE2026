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

# Reproduction and scope of checks

Compile the two C++17 programs and run them as instructed in `README.md`. The canonical-augmentation verifier exhaustively enumerates every isomorphism type of an unrooted tournament through seven vertices and all outgoing/incoming patterns of the eighth marked root. It compares exact directed stable-colour equivalence classes against exact root-preserving automorphism orbits, including the eight-vertex cases. Its output is in `evidence/rooted_census_output.txt`.

The independent labelled verifier uses no isomorphism-type generation: it tests every labelled orientation through seven vertices with root fixed at zero; the largest complete enumeration has 2,097,152 orientations. Its output is in `evidence/labelled_output.txt`. An independent Python implementation uses *both* incoming and outgoing counts and fully enumerates root-fixing permutations of the two explicit eight-vertex exceptions; its output appears in `evidence/witness_output.txt`.

Both exhaustive C++ programs, the independent Python check and the printed output files were run and compared with exact expected counts. Search-space completeness follows from the deletion/extension induction or direct labelled enumeration, not from extrapolated random tests. The conclusion is strictly for orders through eight, and no external independent audit was performed.
