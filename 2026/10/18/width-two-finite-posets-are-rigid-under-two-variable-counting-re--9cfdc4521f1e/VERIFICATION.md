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

# Reproducibility record

The proof in RESULT.md is an all-size, noncomputational proof. Three standalone Python 3 programs provide finite consistency checks; they use only the standard library and were executed from the packaged source directory.

`python3 verify_small_posets.py` enumerates transitively closed subsets of the natural order for one through six vertices, tests antichain width and directed counting-refinement fingerprints, and checks isomorphism of all finite-poset competitors sharing a fingerprint with a width-two example. Its final output marker is `SMALL_POSETS_OK`; see `small_posets_output.txt` for detailed counts.

`python3 verify_matching_skeletons.py` exhausts ordered doubleton comparison templates with all four cross-comparisons or either orientation of a perfect matching for one through five classes, retaining transitive templates only. It checks that two valid orientations of the same complete-vs-matching profile differ by classwise swaps, with final marker `MATCHING_SKELETONS_OK`; see `matching_skeletons_output.txt`.

`python3 verify_stabilizers.py` uses a fixed random seed to generate chain-decomposable orders of three to twelve vertices, and compares their automorphism-group orders with the predicted powers of two for 800 accepted instances; see `stabilizers_output.txt`. These randomized tests do not constitute exhaustive validation of that size range.

All executable sources and logs are embedded alongside this verification report. The programs do not inspect a publication database and do not prove infinite statements or establish priority. Independent audit remains unperformed.
