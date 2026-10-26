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
Run `python verify.py` with Python 3.9 or later. The script has no third-party dependencies. It checks 300,228 assertions covering the exact projective formula, rational discriminant and seed-side comparisons, exact equality-case solution, domain invariance, and numerical original-ODE examples. Expected output begins with `PASS: 300228 exact and numerical invariant checks`.

The exact checks sample the algebraic identities with rational parameters and independent rational differentiations; the program also checks an exact invariant ray. The fourth-order Runge–Kutta trajectories run to physical time \(t=10000\) and corroborate the critical \(1/t\) law and strictly overcontrolled outcomes. These finite checks do not by themselves establish infinite-time limits, global classification, or mathematical novelty. Those rely on the phase-plane proof and literature comparison in the result and review. Floating-point output is not a certificate of strict asymptotic inequality; the strict separation of the two example seeds is proved by exact rational comparisons in `RESULT.md`.

The priority comparison includes accessible full-length original preprint content and publication search records. The final journal PDF could not be directly inspected through the attempted public link, so no claim of complete journal full-text inspection is made. No independent scientific validation has been performed.
