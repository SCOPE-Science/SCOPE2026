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
# Verification
The proof in `RESULT.md` establishes the universal statement. The independent direct finite checker in `verification/verify_wheel.py` uses explicit Gram matrices and cut enumeration, with output recorded at `verification/verification_output.txt`.

The checker enumerates every cut for rim sizes 3–11 at 16 nonnegative test weights; tests objective optimality for 144 explicitly constructed positive semidefinite Gram matrices, samples 45 other random feasible Gram matrices per configuration (6,480 total), and performs five rational symbolic Gram PSD and objective comparisons. Additional parameter trials check the extremal ratio location for rim sizes 3–80. These tests have no logical bearing on untested continuum parameters or unbounded sizes; the spectral and arithmetic proof supplies those quantifiers.

To reproduce from the embedded package, run `python verification/verify_wheel.py` with Python 3, NumPy and SymPy. The code does not download inputs or depend on any external research data. A successful output starts with `PASS` and lists the comparison counts. The literature comparison is not a formal exhaustive novelty certificate; Delorme--Poljak (1993) remains inaccessible in full.
