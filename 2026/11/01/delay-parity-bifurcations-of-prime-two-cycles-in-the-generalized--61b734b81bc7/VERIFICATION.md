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
# Reproducibility and verification

Run `python3 verify.py` in this directory (no nonstandard modules). This program enumerates exact sign-chamber linear systems over dimensions \(2\le d\le12\), all \(1\le k<d\), seven rational dissipation parameters and a forty-point positive rational strength grid, excluding critical lines from the nonsingular enumeration. Exactly 18,150 parameter-delay combinations are checked; every isolated pair is substituted into the original recurrence for positive and negative indices.

Three singular resonance examples are separately tested: a positive continuum for odd nonlinear delay, even linear delay; a positive continuum for both delays odd; and a negative continuum for even nonlinear delay, odd linear delay. The example \(\{2,-6\}\) is checked exactly. Positive and negative fixed-point formulas are also checked on the rational grid.

The universal theorem rests on the complete analytic sign classification in RESULT.md. Tests of a finite parameter grid cannot prove the absence of other nonrational or critical periodic orbits. The proof explicitly handles singular denominators and zero-valued phases. The program's optional finite checks do not assess global stability, invariant measures, entropy or higher periods.
