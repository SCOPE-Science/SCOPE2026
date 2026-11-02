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

# Verification of the stated diagonal row-selection theorem

The statement and analytical proof appear in `RESULT.md`. The executable checker is `verify.py` and uses only Python's standard library. Invoke `python verify.py`; the evaluated script reported `PASS: 15133 exact rational assertions`.

The checker exhaustively compares consecutive-window optimization against all possible retained subsets over nondecreasing integer weights up to seven coordinates; checks exact probabilities by independently enumerating short sequences of iid row draws; recomputes all exact rational values for the four-row rate-versus-completion counterexample; and verifies the parametric three-row Frobenius-surrogate separation across a finite set of rational parameters.

The universal claims are not inferred from the finite tests. Their proofs use the coordinate-survival identity, sorted-index inequalities and finite inclusion-exclusion followed by geometric-series summation. All rows are positive; the full-completion interpretation requires every retained initial error coordinate to be nonzero. The sample count includes zero-update draws on an already satisfied row; methods that reject these draws have a different step count and are outside the result. Pseudoinverse setup, roundoff, noise and wall-clock effects are not assessed. Independent audit and independent validation have not been performed.
