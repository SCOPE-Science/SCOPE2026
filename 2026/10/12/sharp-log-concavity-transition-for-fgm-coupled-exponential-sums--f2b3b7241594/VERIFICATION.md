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

# Verification and scope

The finite checks described here were actually executed using the packaged `verify.py` source. Its only dependency is the Python standard library. Run `python verify.py` alongside `RESULT.md` to reproduce the diagnostics.

The program checks 3,520 exact-rational polynomial identities (using an independent formal placeholder for the exponential), 40 direct numerical quadrature comparisons between the FGM joint-density integral and the closed-form sum density, the strict rational bounds on \(\log4\) needed by the explicit counterexample, and finite-grid signs and a numerical minimization of the elementary threshold formula.

The program is not a continuous-domain certificate. The analytic derivations in RESULT.md establish the sign of the curvature for all eligible rates, dependence parameters and positive times. The displayed approximate minimizing parameter and time are diagnostics, not validated rounding statements. There has been no independent audit, authorship verification, or external certification.
