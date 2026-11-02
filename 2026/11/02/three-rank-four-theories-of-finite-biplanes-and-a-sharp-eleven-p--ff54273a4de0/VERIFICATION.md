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

# Reproducibility and limits

The separately packaged `verify_rank3.cpp` and `verify_rank4.cpp` are standalone C++17 sources using only the standard library. Compile and run them individually, for example:

```sh
g++ -std=c++17 -O2 verify_rank3.cpp -o verify_rank3
./verify_rank3
g++ -std=c++17 -O2 verify_rank4.cpp -o verify_rank4
./verify_rank4
```

The source programs reconstruct four explicit biplanes from cyclic difference sets for \(2\)-\((4,3,2)\), \(2\)-\((7,4,2)\), and \(2\)-\((11,5,2)\), and from the row/column Kummer incidence construction for \(2\)-\((16,6,2)\). For each they independently assert all block/point degrees and exactly two common blocks or points for each corresponding pair.

Each program computes *every* equality, sort, and directed incidence atomic type of an ordered tuple of length equal to the desired quantifier rank, then recursively forms the set of extension types for every shorter tuple. Type identifiers are interned globally across the four designs. Rank-three and rank-four root identities reproduce two and three classes respectively. Recorded stdout and stderr are in `output_rank3.txt` and `output_rank4.txt`.

This finite replay checks the implementations and four representative objects. The proof for every possible biplane uses the exact formulas and positivity bounds in `RESULT.md`. The programs do not exhaust all biplanes or all possible block sizes; no such exhaustive claim is made. Neither priority nor independent mathematical certification is established.
