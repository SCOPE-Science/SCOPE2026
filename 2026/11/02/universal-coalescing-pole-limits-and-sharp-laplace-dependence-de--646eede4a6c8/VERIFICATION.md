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

The proof in `RESULT.md` supplies the infinite-limit argument. The standalone deterministic program `verify_two_pole.py` was executed with Python 3 and SciPy and returned:

`PASS 183 numeric assertions; analytic infinite-n statements require proof`

The program checks the exact coincidence identity, numerical strict ordering at sampled distances, the scaling law, both asymptotic constants, and finite-circle convergence for uniform and continuous nonuniform sampling densities. These tests do not establish every-distance strictness, infinite-time convergence, or historical originality; those aspects require the displayed analytic arguments and additional independent assessment. Numerical quadrature tolerances are described by the program. No external certification or independent audit has been performed.
