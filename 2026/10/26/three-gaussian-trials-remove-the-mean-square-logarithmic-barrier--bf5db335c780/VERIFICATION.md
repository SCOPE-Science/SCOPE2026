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

# Reproduction and mathematical verification

Extract `RESULT.md` and `verify_rjd.py` from the same package, then run `python verify_rjd.py` with Python 3.9 or newer. The program requires only the Python standard library. Its successful output reports 896 exact rational eigenbasis-energy identities, 2,400 direct Gaussian trial comparisons, 11 deterministic angular CDF tests, three direct one-trial expectation checks, and two numerical asymptotic constant checks. Each routine derives its checked quantity from a separate algebraic or integral representation, rather than reusing a precomputed output log.

The infinite theorem is established by a closed-form spectral-projector identity, exact circle measure, independent-trial order statistics, and tail integration. The logarithmic leading constant uses a central logarithmic range and bounded endpoint contributions; the at-least-three-trial limit follows by dominated convergence. The exact best objective is verified by a rotation parametrization. Finite numerical tests are not infinite proofs. The stated guarantees use exact eigenvectors, exact arithmetic, real standard Gaussian coefficients, and the source's Frobenius off-diagonal loss. No independent audit has been performed.
