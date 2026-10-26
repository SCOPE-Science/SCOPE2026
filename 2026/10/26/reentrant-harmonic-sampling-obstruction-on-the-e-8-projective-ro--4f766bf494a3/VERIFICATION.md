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

# Reproducibility and limits

The exact standard-library program `check_e8.py` constructs all 240 classical roots as integer vectors scaled by two. It reduces antipodal pairs to 120 representatives; checks 3,780 orthogonal and 3,360 nonorthogonal unordered line pairs; confirms degrees 63, and common-neighbor counts 30 for orthogonal and 36 for nonorthogonal pairs; and calculates Gegenbauer eigenvalues by rational recurrence for even degrees through 28. The numerical table is a **finite** consistency check. It does not establish the infinite rank statement on its own.

The full mathematical proof of all degrees is in RESULT.md: the addition formula translates evaluation Gram spectra into three eigenspaces; the generating function yields closed form values; and an explicit polynomial with positive coefficients after shifting \(\ell=12+s\) establishes strict diagonal dominance for all real \(s\ge0\). The calculation is fully self-contained once the standard spherical-harmonic addition theorem is accepted. The script requires only Python 3 standard library, and prints the expected exact table when run as `python3 check_e8.py`.

Independent audit and external certification have not been performed. Priority is subject to possible equivalent results not found in the bounded comparison.
