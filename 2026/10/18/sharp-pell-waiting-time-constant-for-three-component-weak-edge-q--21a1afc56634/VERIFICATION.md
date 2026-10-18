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

# Reproducible verification

Run `python verify.py` with Python 3, SymPy and mpmath installed (see `requirements.txt`). The checker establishes exact projector entries and the sharp quadratic identity in rational and quadratic radicals, generates positive norm-one Pell solutions with even first coordinate and odd second coordinate, and evaluates multiple high-precision values of \(s^2(1-F(s))\) approaching \(\pi^4/144\).

These exact-algebra tests and finite high-precision samples test implementation consistency and the proposed extremizing sequence. They do not prove that no other real times have a lower asymptotic cost; that infinite assertion is proved in RESULT.md using the integer norm inequality and the phase-minimizing quadratic form. No independent audit has been performed. The \(\varepsilon\to0\) weak-edge limit is inherited from the cited source, not independently re-established here.
