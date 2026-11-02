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

# Reproducibility and verification

Run `python verify.py` with standard Python 3 in the extracted directory. The script depends only on the standard library, uses `fractions.Fraction` throughout and prints a PASS message after completing its assertions.

**Executed:** 35,388 exact-rational assertions for all complete-graph sizes from 4 through 18 and each permitted matching size. Tested claims include every stated eigenvector and its eigenvalue for the matching-deleted allocation, dual edge squared lengths, dual trace, nonnegative dual quadratic forms on the explicit basis, and optimal unit-gap costs. A unit-gap check for uniformly weighted graphs is also included. The proof in RESULT.md, not this finite test suite, establishes the result for unbounded sizes and continuously varying positive prices.

**Limitations:** Finite assertions are not an exhaustive validation of arbitrary real prices or every possible asymmetric allocation. The general proof uses a universal PSD lower bound, explicit attaining weights and exact complementary-slackness implications. An independent audit has not been performed.
