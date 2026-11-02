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

The code file `checker.py` computes multiplication matrices directly in the monomial basis, and obtains ranks of their powers by row reduction over prime and quadratic-extension fields. The predictor is a separate valuation formula. It enumerates all nilpotent parts and compares the exact full Jordan histograms, allowing all scalar constants. Run `python checker.py` in the same directory as this document; expected output is `checker_output.txt`. The last line must be `JORDAN_MULTIPLICATION_VALUATIONS_OK 11_EXHAUSTIVE_CONFIGURATIONS`.

Eleven configurations are exhaustively checked: `GF(2),n=2,3,4,5`; `GF(3),n=2,3,4`; `GF(5),n=2,3`; `GF(4),n=3`; `GF(9),n=2`. A true irreducible quadratic represents each extension field. All checked histograms match the formula and have total cardinality equal to that of the algebra. Computations do not establish correctness for untested fields/dimensions, nor do they establish publication priority or independent validation. The general proof is given in `RESULT.md`.
