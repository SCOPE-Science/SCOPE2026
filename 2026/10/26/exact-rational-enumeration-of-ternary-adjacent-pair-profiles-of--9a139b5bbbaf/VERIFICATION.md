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

# Reproducibility

Run `python verify.py` using Python 3 with the standard library only. The program builds coefficients from the separated Euler-flow generating functions, enumerates all ternary words for lengths one through ten and counts unique ordered-pair multiplicity profiles, and separately enumerates every nonnegative \(3\times3\) arc matrix of sum at most seven, applying the degree-balance and connectivity theorem. The checks compare both finite enumerations to the formal-series coefficients, and print `PASS` upon equality.

The rational generating function and the asymptotic theorem hold at all lengths by the structural proof in `RESULT.md`, independently of the bounded exhaustive checks. The program provides no independent human validation and cannot exclude earlier literature reproducing the same formula.
