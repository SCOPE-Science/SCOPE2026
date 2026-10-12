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
# Verification

Run `python3 verify.py` with Python 3 standard library; there are no external dependencies. The script's executed output is `PASS: 1147 rational path/norm equalities; inverse-zero absorption; 2D rate separation`. It reconstructs four inverse-Hessian examples (dimensions two, three and four), their inverse Hessians, each conditional block minimizer, weighted squared-line Markov transition, and direct finite path expansions for histories up to length five. Tests are exact rational equalities. The separate off-diagonal-zero example checks exact two-update absorption even though the original Hessian is fully coupled.

The calculation deliberately does not test infinite time, all positive-definite matrices, or publication novelty by finite enumeration. The general mean-square asymptotic follows from diagonal similarity and Perron spectral decomposition, finite absorption from disjoint independent omitted-label pairs, and the almost-sure limit from an ergodic law. These assumptions and their limitations are stated in RESULT.md. No independent audit has been conducted.
