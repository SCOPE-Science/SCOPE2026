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

The exact proof of the two finite-field claims is the exhaustive field and incidence calculation in `verify.cpp`, independently cross-checked by `check_parameter.py`. Both scripts are included in full. `verify.cpp` compiles with a standard C++17 compiler, tests all inverses in the selected polynomial quotient fields, enumerates every affine curve point, adds the unique point at infinity, enumerates each projective line, and counts every four-secant through every projective center. `check_parameter.py` needs only the Python standard library and instead builds the points from the rational BKS parametrization and generates secant lines using all pairs of points.

Run `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`; expected terminator: `VERIFY_OK`. Run `python3 check_parameter.py`; expected terminators: `PARAM_OK 3` and `PARAM_OK 4`. Both succeeded for the enclosed versions. No arbitrary-field or infinite-extension conclusion follows from these finite computations. Public verification is repeatable but neither independently audited nor independently validated.
