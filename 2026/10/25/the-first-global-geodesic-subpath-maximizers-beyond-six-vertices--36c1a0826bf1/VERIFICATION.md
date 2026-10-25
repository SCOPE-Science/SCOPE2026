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

# Verification evidence and reproduction

All files below are embedded complete alongside this document. Work in a directory containing these source files and data.

1. `g++ -O3 -std=c++17 -Wall -Wextra verify.cpp -o verify7` then `./verify7`; compare its output to `verification_output.txt`. Expected 2,097,152 labelled cases, 1,866,256 connected, 49 maximum, 455 labelled maximizers in two exactly checked permutation orbits.
2. `g++ -O3 -std=c++17 -Wall -Wextra verify8.cpp -o verify8` then `./verify8 atlas7_masks.txt`; compare with `verification8_output.txt`. Expected 1,044 base classes, 133,632 extensions, 119,980 connected, maximum 74 and nine maximizing extension records, each isomorphic to one of two explicit witnesses.
3. Install the pinned requirements in `requirements.txt` and run `python verify_atlas.py` to independently count all shortest paths in 853 connected seven-vertex Atlas classes. Compare with `atlas_output.txt`; exactly two attain 49.
4. With the same NetworkX version, run `python generate_atlas7.py`, then compare its generated `atlas7_masks.txt` byte-for-byte with the bundled input. The file has 1,044 distinct integers encoding all seven-vertex graphs from the standard Atlas.

The published completeness of the seven-vertex Graph Atlas is mathematical input to the eight-vertex census. Its 1,044 source masks and generation procedure are supplied. All count arithmetic is integer-exact. Finite exhaustive enumeration is an adequate proof only of the stated seven/eight-vertex finite results; it does not establish any upper bound beyond eight vertices. The second library-based test independently corroborates seven, but not every eight-vertex execution path. No independent mathematical audit has been performed.
