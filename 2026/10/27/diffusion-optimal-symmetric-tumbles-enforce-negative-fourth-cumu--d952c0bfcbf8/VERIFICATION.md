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

The scientific result is the fourth-cumulant growth theorem in `RESULT.md`. Its proof is analytical, using the spectral gap and perturbative Fourier recursion of a bounded tilted operator. The executable file `check.py` is a reproducible consistency checker, not an external proof certificate.

Run `python check.py` with Python 3, SymPy and mpmath installed. On the reference run the checker completed 2,822 assertions, comprising six symbolic identities, sixteen numerical tilted-generator cross-checks, 350 deterministic parameter configurations and their optimization/negativity and coefficient inequalities, and four additional example matrix checks. It verifies the closed rational expression against the independent complex-resolvent representation and computes near-zero tilted eigenvalues using 50-digit multiprecision arithmetic.

The symbolic assertions establish rational identities by exact simplification. The multiprecision eigenvalue checks approximate the fourth Taylor coefficient and are not infinite-time or all-parameter proofs; those conclusions follow from the rigorous generator argument. Mathematical limitations and priority caveats are in `RESULT.md` and `REVIEW.md`. Independent audit has not been performed.
