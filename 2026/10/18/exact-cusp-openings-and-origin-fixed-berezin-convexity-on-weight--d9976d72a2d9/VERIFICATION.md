---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification details

The proof in `RESULT.md` gives the complete local vertical interval near the attained Berezin value one for nonlinear origin-fixed symbols with nonreal multiplier and bounded composition operator on the fractional kernel space. It uses Schwarz–Pick localization, uniform angular inversion and the two extremes of the leading angular mode. Taylor expansion of the linear-symbol curve gives the canonical centerline's quadratic coefficient.

The unchanged standard-library diagnostic `check_berezin_cusp.py` may be run with `python3 check_berezin_cusp.py` from the package directory. The original recorded run passed 48 endpoint checks from twelve polynomial families at two scales. That output tests finite diagnostics only; it does not prove the exact section structure or asymptotics.
