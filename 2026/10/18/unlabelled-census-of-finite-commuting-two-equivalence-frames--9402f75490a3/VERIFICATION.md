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

# Computation and limits

Run `python verify.py` with standard Python (no external packages).

- The exact Burnside/cycle-index and multiset coefficient implementation computes the first 12 coefficients, including the empty size, as rational/integer polynomial arithmetic and checks the values in the result.
- A separate generator enumerates all set partitions through six elements. For every ordered pair, it checks both relational compositions literally before retaining the frame.
- A separately constructed connected-component matrix signature, minimized over independent row and column permutations, verifies the isomorphism counts through size six. The full labelled counts agree with published OEIS A354458.
- The finite checks confirm the code and stated coefficients but do not prove the all-size generating-function theorem; the full proof is in RESULT.md.
- No independent external audit or publication-wide precedence certification has been performed.
