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

## Reproduction

Run `python verify.py` with Python 3.9 or later (standard library only). The program enumerates all block-preserving transformations of selected small partitions; checks the stated regularity condition and exact integer-counting formula independently; searches inner inverses exhaustively for monoids of at most 500 elements and spot-checks forty examples for selected larger ones; independently evaluates the uniform exponential-generating-function recurrence; and compares the local counting factors with direct function enumeration. The supplied run finished with `ALL CHECKS PASSED`.

## Mathematical verification and limits

The general exact formulas follow from selecting each occupied target's union of images and subtracting the independent tuples in which no source map is onto that union. The saddle-point asymptotic follows by exponential tilting, positivity of the variance, and the aperiodic lattice local central limit theorem. These analytic arguments were examined symbolically; no finite computation purports to prove their validity for all block sizes or all numbers of blocks. The numeric approximation to \(\rho_2\) was obtained by solving the positive saddle-point equation. Independent audit and independent validation have not been performed.
