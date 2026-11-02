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

# Reproducible checks

The file `verify_scarpi.py` requires only the Python 3 standard library and prints `VERIFICATION_OK` on success. Its fixed-seed sweeps compare the analytic first-lag formula against finite-difference derivatives of the published Laplace symbol, factorized stationary-point identity, unique-root brackets, sign changes, critical tangencies, Laplace-domain positive-SOE bound and its nearly attaining family.

The exact domain-wide classification is proved in `RESULT.md` by an algebraic derivative identity and a globally monotone derivative factorization, not by extrapolating the checker. The sharp minimax lower bound is proved using monotonicity and an explicit matching infimizing family. The singular square-root law follows from the positive quadratic Taylor coefficient at the only critical point.

Reproduction command: `python3 verify_scarpi.py`.

The example uses `a=0.2`, `b=0.8`, `c=10` with a nonempty negative first-lag step interval, and satisfies the motivating source's sufficient sector condition. Tests use floating-point tolerances; they cannot certify non-asymptotic exact digits, historical novelty, other convolution weights, arbitrary time-domain SOE compression, or independent validation.
