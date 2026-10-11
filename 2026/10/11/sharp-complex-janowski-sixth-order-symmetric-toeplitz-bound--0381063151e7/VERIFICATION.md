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
# Verification and reproducibility

The mathematical claim and all notation appear in `RESULT.md`. The included standalone Python file `verify_complex_janowski.py` uses standard Python and SymPy. Run `python verify_complex_janowski.py` in the directory containing that file.

A successful run prints `SYMBOLIC_IDENTITIES_OK`, `RATIONAL_GAP_TESTS_OK 9020`, `SCHUR_BODY_SAMPLING_OK 40000`, `EXACT_EXTREMIZER_FORMULAS_OK 1640`, and `VERIFY_OK`. Exact SymPy simplification verifies the coefficient factorization, \(k+m\), \(km\), the expanded reduced determinant, and the proposed extremal value. Exact rational calculations test 9,020 parameter/radial gap instances. Pseudorandom samples additionally test the complex Schur-parameter body; endpoint checks use rational arithmetic.

The script is supplementary and finite numerical sampling is not a certificate of a universal inequality. The general bound is proved by the full angular monotonicity and radial gap computations in Steps 3 and 4 of `RESULT.md`. The source's real-coefficient theorem and its section on the exponential class do not provide the new complex Janowski maximization. Reproducing a symbolic or finite check does not establish novelty or constitute independent validation.
