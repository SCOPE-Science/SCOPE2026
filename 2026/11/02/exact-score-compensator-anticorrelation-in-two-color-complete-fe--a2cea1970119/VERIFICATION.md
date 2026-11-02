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

# Verification record

The theorem is supported analytically by the reverse-path compensator identity, the hypergeometric martingale-variance formula, moment-uniform bridge invariance, and an exact double-integral evaluation. The total-score moment limits are taken from the cited 2023 theorem.

`verify_moments.py` checks every balanced sequence for eight finite multiplicities in exact rational arithmetic; it averages ties analytically and compares the squared martingale residual with the derived harmonic-number formula. Independent numerical quadrature checks the two evaluated bridge integrals and their sum. The corresponding deterministic output is `verification_output.txt`.

Finite numerical checks do not establish an infinite asymptotic claim. The prior-art comparison is limited to cited relevant sections and searches; historical priority remains open to independent assessment.
