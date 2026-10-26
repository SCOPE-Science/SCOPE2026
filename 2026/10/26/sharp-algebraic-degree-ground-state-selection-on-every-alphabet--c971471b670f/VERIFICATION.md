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

Run `python3 verify.py` with only the Python standard library. The observed output was `VERIFY_OK determinant_samples=54 numerical_dimensions=58`.

The program constructs the directed graph and checks its determinant at six integer arguments for each size from 3 through 11 by exact Bareiss elimination. For every size from 3 through 60 it checks the explicit Perron eigenvectors, invariant masses, finite-temperature transition matrices, and temperature-independent jump probabilities; it also numerically checks the exact last-state probability. These are exact finite determinant tests and floating-point Markov tests, not exhaustive symbolic proofs for every size.

The universal determinant formula follows instead from the two mutually overlapping simple cycles. The algebraic degree relies on Selmer's established irreducibility theorem for the polynomial \(t^N-t-1\), whose complete proof is independently available in the cited Keith Conrad exposition. Uniform fixed-word convergence and the continuous-time finite-dimensional scaling limit are mathematical arguments in `RESULT.md` and are not inferred from checker success.
