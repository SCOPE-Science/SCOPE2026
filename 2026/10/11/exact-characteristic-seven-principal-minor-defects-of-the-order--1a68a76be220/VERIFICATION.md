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
# Verification scope

The theorem has a **finite, exhaustive** domain: all \(2^{15}-1=32767\) nonempty index sets for both Frobenius orbits of primitive fifteenth roots in characteristic seven. The `verify_f15_char7.cpp` program implements exact field arithmetic in the quotients by the two monic quartics of \(\Phi_{15}\). For each nonzero residue it verifies a multiplicative inverse; it checks order fifteen of both chosen roots; it determines every principal-matrix rank by exact elimination, and checks that singular masks agree exactly with the translated seed orbit and its complements. Each orbit returns 15 singular size-six sets, 15 singular size-nine sets, and 32737 invertible principal sets, all singular ranks deficient by one.

The separate `verify_seed_polynomial.py` program computes the exact determinant by 720 signed permutation terms and reduces it in \(\mathbb Z[X]/(\Phi_{15})\); it confirms the coefficient identity written in `RESULT.md`. This confirms that the singularity in characteristic seven is genuinely a reduction phenomenon rather than a complex singularity.

Reproduce using Python 3 and a C++17 compiler:

```sh
python3 verify_seed_polynomial.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_f15_char7.cpp -o verify_f15_char7
./verify_f15_char7
```

Expected final lines include `SEED_IDENTITY_OK`, two `PASS` lines for the distinct root orbits, and `VERIFY_OK`. This does not independently certify originality, value, or the scientific status of the wider complex conjecture. No independent audit has been performed.
