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
# Verification and limits

The proof in `RESULT.md` establishes the exact polynomial reversal identity, a single unit-circle crossing under a strict coefficient inequality, a Gaussian orthogonal decomposition, an exponential integral for the threshold distribution, and the exact moment convergence range. The same coefficient realization is used at all amplitudes; the random crossing is excluded from the 0/1/2 count formula. The stated Gaussian variance convention and all other hypotheses are essential.

The stand-alone finite checker `verify_gaussian_quadratic.py` was executed with its fixed seed. It compares the quadratic-root formula against the Schur classification for 100,000 generated triples at eight amplitudes, examines empirical frequencies against the exact distribution, and tests both sides of 5,000 random crossing thresholds. These computations do not prove probabilistic equalities or uniqueness over uncountably many parameters: the analytical proof does.

The literature comparison distinguishes deterministic complex-trinomial Schur stability, bounds for real-Gaussian coefficient polynomials, asymptotic Littlewood polynomials, and infinite Gaussian Taylor series. Historical priority under other terminology remains a residual risk. Independent audit was not performed.
