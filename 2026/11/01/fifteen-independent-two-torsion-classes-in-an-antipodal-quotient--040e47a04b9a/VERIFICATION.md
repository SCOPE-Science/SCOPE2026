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

# Exact integer verification

Execute `python3 verify.py` with Python 3.8 or later, using only the Python standard library. The program constructs every signed edge and signed matching, pairs cells under the free antipodal involution, builds quotient cellular boundary maps with integer coefficients, checks the integer chain identity, and determines the first boundary rank by a complete connectedness search.

For the second boundary, an exact integer unit-pivot algorithm (unimodular row and column operations) removes 270 diagonal ones. All 240 entries left are exactly two in absolute value. After dividing the residual matrix by two, a further exact unit-pivot algorithm removes 15 ones and leaves only zero entries. Thus the original nonzero Smith factors are precisely 270 ones and 15 twos, with no unsupported use of modular-rank extrapolation. Homology and Euler characteristics follow from these factors and full chain ranks.

The program must print `ALL_VERIFY_OK`. It does not classify the quotient's homotopy type or replace independent mathematical verification of its algorithms or definitions.
