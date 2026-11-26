---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the repaired statement, the pair blocks give a negative eigenvalue iff q/d^2 < (1-q)m, where m is the geometric mean of the top two populations. For low s, a centered Cauchy–Schwarz bound on their sum and AM–GM give the first branch, attained only by equal leaders and a constant tail (with the uniform endpoint). For high s, with leader sum t>0, s+2m^2 <= t^2+(1-t)^2 <= 1; equality requires t=1. The two roots (1±sqrt(2s−1))/2 attain the bound, including the single occupied level and empty NPT set at s=1. The two branches meet at s=1/2 and q=q_* is always PPT. Inspect RESULT.md proof and frozen verify.py lines 3–24 for formulas and finite witness construction. The original recorded 8,016 finite checks were not rerun and are not used for the continuum theorem.

## originality

PASS

The pass is confined to the all-d, all-s fixed-collision-purity envelope and its equality spectra. The fixed-output white-noise threshold, uniform example, and unconstrained optimum are known or direct consequences of earlier work and are not credited as original. The endpoint repair does not enlarge the scientific claim.

## value

PASS

A collision probability constrains how strongly a pure input can populate the two levels that control white-noise entanglement survival. The full attained continuum boundary and equality spectra show exactly when the population tail is necessary and when it must disappear; this is a natural optimization at a measurable constraint. The known unrestricted peak is not the basis for the pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
