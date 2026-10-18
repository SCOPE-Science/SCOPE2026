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

The exact standard-library checker `verify.py` enumerates every valley-shaped nonnegative integer sequence of length \(3\le n\le10\) whose entries lie in \(\{0,1,2,3\}\), and tests the precise path-ball definition, valley preservation, endpoint formulas, sharp bound, quantitative deficit, and equality implications. It also verifies endpoint-spike sharpness and four noninteger rational input profiles.

The executed checker reported `VERIFY_OK valley_profiles=13652 nonconstant=13620 rational_profiles=4`. Each tested comparison of averages and inequalities uses exact rational arithmetic.

These finite checks do not exhaust arbitrary lengths or real amplitudes. The universal proof is in `RESULT.md`; its key noncomputational steps are the one-sided sign-change property for fixed-width sliding averages, reproduction of clipped intervals from earlier or later centers, and the exact endpoint-prefix-average argument. No independent external audit has been performed.
