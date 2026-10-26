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

The finite claim was checked by two Python 3 standard-library programs, `verify_switch.py` and `verify_direct.py`, executed from the same directory as this file. See their exact recorded outputs in `verify_switch.out` and `verify_direct.out`.

The first program enumerates all fifty-six spreads by smallest-uncovered-point exact-cover backtracking, verifies all \(560\) deletion triples have exactly one opposite triple, tests all \(280\) switches, and uses exhaustive bitmask Bron–Kerbosch enumeration on the complement to identify exactly eight largest independent sets (size \(21\)). The thirty-five original lines each occur in eight spreads and have distinct incidence fingerprints, proving that the collineation action on spreads is faithful. Every spread has exactly three intrinsic labels, all fifty-six triple signatures are different, and all unordered spread pairs satisfy the Kneser-disjointness equivalence. It additionally prints SHA-256 digests of the exact ordered spread list and switch-edge list for comparison.

The independently structured second program tests all \(\binom{35}{5}=324632\) line choices directly, recomputes the switch/intersection and common-neighbor counts, and checks all \(560\) local replacement triples. Each executable prints `PASS` only after all assertions succeed.

Finite enumeration proves only the stated order-two theorem; it does not establish an analogous isomorphism for arbitrary finite fields. The originality check included inspected open full papers and source-specific search comparisons, while the 1974 switching paper and Jeurissen's 1995 paper on this finite space remained inaccessible in full. No independent audit has been performed.
