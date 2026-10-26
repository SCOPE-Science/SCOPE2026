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

The proof is a general linear-algebra argument in the exterior-degree-one, -two, and -three free algebra. The finite computations provide independent checks of its defining product and subspace classifications, not a substitute for the infinite family argument.

`checker.cpp` is self-contained C++17. Its finite-field rank-three multiplication table has seven coordinates. It enumerates all 925771 RREF four-subspaces over the field of three elements, counts precisely 40 square-zero subspaces, and tests the ideal condition against all basis vectors for each. It additionally enumerates 93556 RREF four-subspaces in selected pivot strata over the field of five elements, finding 156 square-zero ideals in that non-exhaustive sample. The latter coincidence with the predicted total does not certify an exhaustive field-five census.

`check_rank4.py` constructs the exterior-graded multiplication independently in Python 3. It enumerates the complete *predicted family* of 1081 rank-four maximal abelian ideals over the field of three elements. For every candidate, it confirms vanishing internal multiplication and two-sided ideal closure. It does not enumerate every subspace of the rank-four algebra. Both programs were executed during preparation and printed the expected success messages.

Commands:

```
g++ -O3 -std=c++17 checker.cpp -o checker
./checker
python check_rank4.py
```

The scripts assume prime fields for arithmetic; the mathematical proof and its finite-field formula apply to all odd prime powers. No exhaustive computation or independent external verification for arbitrary rank or arbitrary finite field is claimed.
