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
The all-parameter theorem follows from the explicit analytic steps in `RESULT.md`, not from a finite simulation. In particular, the drift test must establish the moment integrability necessary for Taylor coefficients before the stationary transform is differentiated. The separate stationary truncation lemma supplies that step.

## Reproducible calculations
Run `python3 check_moments.py` with a Python 3.10+ standard library. Its recorded output is in `check_output.txt`; **773 exact-rational assertions passed**. Inputs include six rational values of the emigration parameter, 21 starting states, three PGF arguments, and tests for both known and new stationary-moment formulas. The computation checks identities at finitely many points; no numerical experiment is offered as proof of the invariant distribution or infinite parameter classification.

## Scope of mathematical checks
The conditional-moment formulas were compared against direct finite geometric summation, and the generating-function identity was tested against its closed geometric-series counterpart. The proof's stationary-moment coefficient extraction and algebra were checked separately. The leading singular coefficient \(24/25\) follows by direct evaluation of rational limits. The exact prior result identified in Carper concerns the stationary mean; the separate second moment is the present theorem's substantive claim.

## Unperformed validation
There has been no independent mathematical audit or historical-priority certification. The possibility of a broader migration-process theorem subsuming the moment threshold remains an acknowledged scientific limitation.
