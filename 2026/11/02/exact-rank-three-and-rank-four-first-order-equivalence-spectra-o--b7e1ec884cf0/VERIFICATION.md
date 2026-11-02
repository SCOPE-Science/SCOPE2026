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

The claim concerns squared paths with exactly the simple-graph adjacency predicate and equality; endpoints and path order are not named. The complete recursive types include all ordered tuples, repeated choices, and all one-point extensions. The C++17 checker enumerates sizes one through forty-seven and compares complete rank-three/rank-four sentence types by interning their exact extension signatures. It checks the asserted class identifiers rather than trusting precomputed output. The independent Python checker uses a different atomic-type representation and verifies the early segment and the twenty-five/twenty-six/twenty-seven rank-four boundary.

From the extracted package directory:

```sh
g++ -O3 -std=c++17 verify_types.cpp -o verify_types
./verify_types 47 > replay_finite.txt
python3 independent_types.py > replay_independent.txt
```

The exact final success strings are `COMPLETE_RANK_THREE_AND_FOUR_FINITE_TYPE_CHECK_PASS through_n=47` and `INDEPENDENT_PYTHON_TYPE_CLASSIFICATION_PASS`. Original result logs are included as `finite_types.txt` and `independent_check.txt`. All finite status comparisons are exact integer/set operations.

The all-size continuation is a mathematical Duplicator strategy with gap thresholds \(3\cdot2^r\); it proves rank-four equivalence for every two sizes at least forty-seven and rank-three equivalence for every two sizes at least twenty-three. Computation bridges the gap down to the sharp thresholds twenty-six and eleven, respectively. The program does not itself establish the all-size step, nor do these checks establish historical priority or independent scientific validation.
