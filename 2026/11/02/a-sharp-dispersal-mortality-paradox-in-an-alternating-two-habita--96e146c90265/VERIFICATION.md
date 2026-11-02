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

The accompanying `verify.py` is standalone apart from Python 3 and SymPy. Running `python verify.py` reconstructs the period-two matrix, verifies the square factorization and characteristic equation, checks symbolic second derivatives and boundary identities (with the stated strict ordering of habitat multipliers), and rechecks the exact growth-rescue example. It independently compares the per-year Perron-root formula against 38 exact rational matrix characteristic polynomials. This checker passed when run on the final source code. The proof in `RESULT.md`, not the finite test grid, establishes the conclusions for all parameters in the stated domain.

Historical priority, nonlinear/demographic extensions and field validity are outside the verified claim. The independent-audit status in the front matter is unchanged by these checks.
