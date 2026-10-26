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

The analytical no-reversal theorem for all ternary communities follows from a formal generating-function identity whose coefficients have a constant sign. The exact four-species witness is checked at every integer sample size by finite integer numerators at sizes 3–13 and a strict power inequality for all sizes at least 14. The extension to larger supports follows by adjoining common species and asymptotic dominance of the unmatched rarest species.

Reproduction: run `python verify.py > certificate.json` in the directory containing `verify.py`, then compare the output byte-for-byte with the packaged `certificate.json`. Only Python standard-library modules are needed. The verifier performs two algebraically independent finite calculations: a direct closed-form power sum and an exact multinomial enumeration. It checks some ternary probability vectors as a finite diagnostic, not as proof of the universal theorem. All analytical details are in RESULT.md. No stochastic simulation or asymptotic numerical fit is used, and independent scientific audit has not been performed.
