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

# Reproducibility and limitations

From the extracted document directory, run `python3 verify.py` with a Python 3 standard-library installation. It uses exact `fractions.Fraction` arithmetic and checks 11,900 deterministic rational configurations across dimensions two, three, and four, including several scales on both sides of the predicted transition, exterior query points, and near-maximizing missing translates. The actual run printed `PASS: 11900 exact-rational translate and threshold checks`.

The continuum theorem, all dimensions, optimal suprema, and halfspace gap are established analytically in RESULT.md. These tests cannot certify their infinitary universal quantifiers or mathematical priority. No independent audit was performed.
