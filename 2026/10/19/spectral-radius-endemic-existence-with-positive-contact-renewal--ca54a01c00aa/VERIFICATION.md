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

Run `python3 verify.py` with a standard Python 3 installation. The program uses the standard-library `fractions.Fraction` for exact rational calculations and verifies stationary prevalence/contact equations, positive edge levels, and supercritical reproduction values over two nontrivial creation-response families. The observed output is `PASS: 7959 exact rational assertions`.

These tests confirm the displayed rational witness \((7/10,1/10,5/9)\) and additional constructed finite examples. They do **not** certify the infinite-dimensional family of parameter instances; arbitrary directed finite networks are covered by the analytical compactness/Perron/Brouwer argument in the proof. They do not establish stability, uniqueness, or the unrestricted interior-zero contact-creation case.
