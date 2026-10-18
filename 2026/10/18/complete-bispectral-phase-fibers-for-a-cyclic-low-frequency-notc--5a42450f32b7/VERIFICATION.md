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

# Verification

The companion `check.py` constructs the full integer relation matrix for each enumerated cyclic frequency mask and calculates its Smith normal form. The result was `PASS: 76 exact Smith-form phase-group comparisons` and `PASS: all small-band wrap cases and 68 analytic wrap witnesses` under Python 3 and SymPy. These checks include the torsion transitions at cyclic orders 9, 10, 12, 14, and 15, along with both sides of the large-band threshold.

The unrestricted result is derived from exact algebraic generators and relators in `RESULT.md`; finite Smith-form computations corroborate but do not certify the infinite family. The data model requires exact power spectrum and full bispectrum as separate inputs. No statement of noise robustness or recovery from bispectrum alone is made. Independent validation was not performed.
