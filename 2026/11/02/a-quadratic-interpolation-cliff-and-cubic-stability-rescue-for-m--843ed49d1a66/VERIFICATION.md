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

# Reproducibility notes

Run `python3 CHECK.py` using Python 3. The checker requires only the standard library and reports `MUB_PROJECTIVE_CUBIC_EXACT_CHECK_OK` on completion. It evaluates the degree-one, degree-two and degree-three normalized projective-harmonic hypergeometric polynomials with `fractions.Fraction`, tests derived eigenvalues for dimensions 3 through 70 and all admissible numbers of bases, checks exact qutrit mutual unbiasedness using the algebra of cube roots of unity, and recomputes several small Gram ranks by rational Gaussian elimination.

The proof in `RESULT.md` uses the complex-projective harmonic addition formula and algebraic factorization of three spectral sectors. Computations are finite corroborations; no computation is claimed to establish infinitely many dimensions by enumeration. No independent mathematical audit or validation has been performed.
