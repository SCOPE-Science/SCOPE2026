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

# Reproduction and limits

Run `python verify.py` using Python 3 and the standard library. The program independently enumerates all labeled perfect matchings with two through six chords, computes crossings by alternating endpoints and cyclically adjacent chords by consecutive labels including wrap-around, and verifies the exact mixed factorial identities and moment formulas with rational arithmetic. It also checks the formula for the number of disjoint collections of boundary-cycle edges. All enumerated sizes completed successfully during preparation.

The infinite-size result uses an analytical dominated-convergence argument and the established crossing central limit theorem in Paguyo, arXiv:2104.01134. Finite enumeration and computation do not certify unbounded-size statements. Independent audit has not been performed.
