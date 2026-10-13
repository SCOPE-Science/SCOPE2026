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

# Reproduction

Use Python 3 standard library and any C++17 compiler. From the directory containing the accompanying standalone source files, run `python3 verify.py` and `c++ -O3 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`. Both implementations construct the incidence graph directly, without external inputs.

The Python verifier checks all 900 pairwise graph distances by an independent breadth-first search, builds exactly 210 same-side vertex-pair separation masks, exhausts 142,506 size-five and 593,775 size-six subsets, verifies 32,460 successful size-six subsets and the full nine-entry bipartition/induced-edge profile. It verifies the 720 symmetric-group actions and a side-exchanging duality against the actual 45 graph incidences, generating 1,440 automorphisms, and partitions all 32,460 successful masks into 34 exact orbits of sizes 180 once, 240 once, 360 once, 720 eighteen times and 1,440 thirteen times. See the elementary upper bound on automorphisms given in `RESULT.md`.

The separate C++ implementation uses independently built incidence lists and breadth-first-search distance vectors and directly checks that all 30 vertex distance signatures are distinct, for every candidate subset at cardinalities five and six. Its exact answer agrees with the Python enumerator for the complete candidate set (the exact component cardinalities are 142,506 and 593,775).

The 34 rows of `orbits.csv` provide representative vertex lists, bitmasks, orbit sizes and stabilizer orders in the labeling documented in `RESULT.md`. Checks are exact and finite, not extrapolation from samples. They do not establish a general theorem for larger generalized quadrangles, literature novelty outside inspected sources, or independent mathematical verification.
