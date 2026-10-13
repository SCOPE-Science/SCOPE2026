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

# Computational verification

Use `python verify.py --csv orbit_representatives.csv three_color_obstructions.csv` (Python 3.10 or later, standard library only). The script derives 168 linear collineations from the 168 invertible linear transformations on the three-dimensional binary vector space, creates another 168 by polarity, checks the graph edges under all 336 maps, generates every proper restricted-growth class partition with two to four classes, applies every automorphism to test color preservation, and independently constructs the 51 canonical four-class orbits. It regenerates both CSVs deterministically. The exact expected output includes 1, 350, and 29610 proper unlabelled partitions with respectively two, three, and four classes; 13692 distinguishing four-class partitions; and 51 orbits with size multiset 56,84,112,168 repeated 16 times,336 repeated 32 times.

Compile the independently structured palette enumerator with `g++ -std=c++17 -O2 enumerate_cpp.cpp -o enumerate_cpp`. Running `./enumerate_cpp 3` yields zero distinguishing colorings, and `./enumerate_cpp 4` yields 719052 proper colorings, of which 328608 are distinguishing. Its automorphism tables are literal data in `heawood_aut.h` and have no external dependency. The two methods enumerate different spaces, respectively color-class partitions and palette-labelled colorings, and agree after multiplication by 24 for the successful four-class solutions.

This is an exhaustive finite computation, not probabilistic testing. The graph automorphism completeness relies on the linear-collineation and polarity proof in `RESULT.md`. No independent third-party audit or machine-checked proof has been conducted, and possible historical unindexed priority is not excluded.
