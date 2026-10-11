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

The proof's critical independent steps are the Fourier-zero characterization, the two affine-rank cases for the time support, the forced annihilator direction, and the orbit/counting argument. The finite checker verifies these theorem outputs by exhaustive *direct* enumeration and does not assume the formula when testing its predictions.

Use `g++ -std=c++17 -O3 -Wall -Wextra checker.cpp -o checker` followed by `./checker`. The tested source produced `CHECK_PASS families=5013`, and the seven nonempty subfamilies of the three-plane obstruction had common-spectrum counts `16,16,4,16,4,4,0` in bit-mask order. All computations use exact integers, bitwise binary dot products, and explicit Walsh-character sums; there is no floating-point tolerance.

These finite experiments cover all one-set families through dimension four, all distinct unordered pairs in dimension three, and 700 fixed-seed dimension-four families, not all possible higher-dimensional configurations. The proof establishes all dimensions, all positive finite family sizes, and the stated classification; it does not settle analogous problems for larger time supports, odd characteristics, or nonorthogonal Riesz bases. Independent audit status is not performed.
