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

# Reproducibility and check limits

The package contains `certificate.json`, holding the 82-bit witness, a 32-root ordering, and 20 explicitly listed proper-subset cuts for a 33-vertex directed Hamiltonian-cycle model. `verify.py` independently regenerates all required squares and every pairwise overlap and checks that all 32 factors appear in the witness.

The optimization has one binary variable for each ordered pair of distinct vertices, hence 1056 binary variables. The 66 exact degree equations and 20 valid subset inequalities are built from the supplied data. SciPy `milp` with zero requested relative gap must return a globally optimal integral tour, with lower bound and objective both agreeing with 82 within numerical tolerance \(10^{-7}\); a separate integer calculation then verifies that the returned edges make one 33-vertex circuit of cost precisely 82. Any Hamiltonian circuit obeys every supplied cut, so this is a lower-bound certificate for the full model when the mixed-integer solver's optimality assertion is reproduced.

The expected complete command is `OPENBLAS_NUM_THREADS=1 python verify.py`, run with NumPy 2.3.5 and SciPy 1.17.0 (bundled HiGHS). The recorded output from the packaged source is:

`VERIFY_OK square_superstring_n5=82 all_32_factors=present integer_program_optimal=yes small_orders=4,12,24,48`

Small-order verification uses a separate exact subset dynamic program for half-lengths 1 through 4. The computation is finite, and the optimization solver is not independently formally verified. No claim of independence or formal proof certification is made.
