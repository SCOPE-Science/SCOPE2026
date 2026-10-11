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

# Exact verification and boundaries

Run `python3 verify_discrete_bmo.py` using the Python 3 standard library. The program uses `fractions.Fraction` throughout and performs three logically finite checks. First, it verifies the exact maximum mean deviations for every consecutive block starting at 1, 2 or 3 and ending by 127 of \(Ce^{(2)}\). Second, it verifies the harmonic lower witness for every jump length 3 through 199. Third, it certifies the rational bounds on \(\log4\) and \(\log(997/600)\), using explicit positive series and remainder bounds; it also checks \(e^5>128\) by a finite lower series bound.

The corresponding infinite ranges are **analytically** controlled in `RESULT.md`: blocks starting at index at least 4 have oscillation at most \(1/4\); longer blocks with earlier start have a uniform harmonic tail bound; jump lengths at least 200 have a uniform strict lower witness. Exact finite arithmetic therefore constitutes a complete certificate only in conjunction with the supplied analytic inequalities. The computation does not address general decreasing sequences or independent validation.
