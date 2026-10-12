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

The source archive is entirely standalone. From the directory with these files, run `sh run_checks.sh` with a C++17 compiler and Python 3. The scripts enumerate all normalized proper four-edge-colorings of the unique order-three projective plane and calculate their equivalence orbits. Intermediate files (`colorings.bin`, `gmap.txt`, `conjugacy_reps.txt`) are regenerated, not imported as prior evidence.

The exhaustive normalized line-coloring traversal tests every permutation of the four symbols on each line, rejecting a partial state only when it duplicates a color at a point. It yields `normalized_coloring_count=80640`. A separate cyclic difference-set implementation verifies the same normalized number, and a different method enumerates all perfect matchings and residual even-cycle completions, yielding `perfect_matchings 3852` and `total_labeled_edge_colorings 1935360`.

The group generators produce exactly 5616 collineations. Exhaustive orbit closure yields classes of sizes 5616 (12), 1872 (7), and 144 (1). Independent conjugacy enumeration finds twelve group conjugacy classes and a Burnside fixed-point sum of 112320, giving twenty orbits. The twenty representative codebooks pass direct Hamming-distance and constant-composition checks in `verify_codes.py`.

The finite computations establish the stated exactly finite domain only. They invoke known uniqueness of the order-three projective plane and standard projective-group results. The established optimal size of thirteen is literature, not re-proved by the enumerator. This verification is not an independent external audit.
