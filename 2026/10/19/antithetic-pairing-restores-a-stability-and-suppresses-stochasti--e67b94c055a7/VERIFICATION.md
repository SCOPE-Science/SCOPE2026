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

# Reproduction and limits

Execute `python3 check.py` with Python 3.10 or later (standard library only). On the checked package path the script passed 441 exact rational paired-amplification identities, 288 sampled complex-half-plane inequality checks, and exact symbolic-fraction evaluations of the two uniform moments. It compared high-precision 4000-node quadrature evaluations of the exact finite-step output variances against the asymptotic constants on three step grids for each coupling. Finite checks are non-exhaustive; the full complex-half-plane and Gaussian-limit statements use the proof in RESULT.md, not grid evidence. No independent audit has been performed.
