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

Execute `python verify.py` in a directory containing the supplied script; it requires NumPy and uses the Python standard-library `fractions.Fraction` for exact rational identities. The program checks seventy parameter pairs for the one-step and two-step covariance identities, three exact critical boundaries, the first-moment versus mean-square separation, the sharp four/five-row transition, and two row-distributions with the same adjacent-selection collision probability but different stability. It also compares the eigenvalues of a three-dimensional numerical second-moment recurrence matrix to the analytically predicted strict phase. The expected success prefix is `VERIFY_OK`; a failure stops execution with an assertion.

These reproducible finite checks verify algebraic examples and test internal consistency only. Geometric mean-square decay, all-parameter necessity, and the probability-simplex characterization are analytic conclusions proved in `RESULT.md`. Neither computational sampling nor independent external certification has been performed here.
