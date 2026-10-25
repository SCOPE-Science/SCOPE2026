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

# Reproducible checks and limits

Run `python verify.py` with Python 3. This uses standard-library exact integer and prime-field arithmetic only. The exact detector expands all 3276 triple-line determinants using the relation \(\zeta_8^4=-1\), computes the 13-level absolute-norm histogram, and independently enumerates all 378 line pairs over \(\mathbb F_{p^2}\) for \(p\in\{5,7,17\}\). The first calculation covers *all* primes at least five by the prime-factor obstruction, while the three exhaustive finite-field calculations supply the incidence counts. The program completed with `VERIFY_OK`.

The argument does not depend on probabilistic sampling, a timeout, or a finite collection of primes extrapolated to infinitely many primes. It requires the standard 28-bitangent theorem for smooth plane quartics in characteristic different from two and the displayed algebraic norm calculation. An independent external audit has not been performed.
