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

## Reproducibility and scope
Run `python nonagon_chord_checker.py`. The script uses solely standard-library exact rational fractions and computes outward intervals without approximate comparisons. It checks the cubic-root isolating bracket, the signs of eight trigonometric denominators, the count of \(\binom{18}{4}=3060\) possible support-normal quadruples, the precise 1548 bounded sets, and two sharp ninefold optimizer orbit classifications. Strict rational separation bounds certify each losing configuration. The executable artifact has been run against the actual packaged source text. This finite verification is exhaustive for the nonagon and makes no statement for all regular polygons or for an unrestricted quadrilateral.

No independent audit or external validation is claimed.
