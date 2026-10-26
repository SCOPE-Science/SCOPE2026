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

# Reproducible exact finite verification

All evidence is embedded in the accompanying files. Run `python3 verify_kneser.py` with `deletion_orbit_witnesses.txt` in the same directory. It uses only Python's standard library. Optionally compile `chromatic_obstruction.cpp` using any C++17 compiler (for example `g++ -std=c++17 -O3 chromatic_obstruction.cpp -o verify_cpp`) and run `./verify_cpp`.

Both programs reconstruct each independent three-subset of a nine-cycle plus an isolated vertex from the defining edge condition, construct every disjointness edge, and confirm that there are exactly 57 vertices and 498 edges. The first program checks the explicit six-color assignment, all 18 dihedral permutations, six orbit representatives of sizes 9,18,9,3,9,9, and all transformed five-color deletion witnesses; every one of the 57 deletion targets is covered.

Both programs also use a full canonical-color-name search: select an uncolored vertex maximizing number of used neighbor colors, break ties by remaining uncolored degree then smallest index, try all allowed used colors plus one fresh color. There are exactly 122153 recursion calls and no legal five-coloring. Canonicalizing unused color names preserves completeness because a permutation of color names does not affect properness. No optimization cutoff, timeout, random sampling, or unexplored branch is present.

Observed replay:

`VERIFY_OK vertices=57 edges=498 canonical_search_nodes=122153`

`VERIFY_OK vertices=57 edges=498 χ=6 6-critical orbit_representatives=6 search_nodes=122153`

This is a finite computer-assisted proof. It does not establish the corresponding statement for larger cycle lengths or set size, and it has not undergone independent audit.
