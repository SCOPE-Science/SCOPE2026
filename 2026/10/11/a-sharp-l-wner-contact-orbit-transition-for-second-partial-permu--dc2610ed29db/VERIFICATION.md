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

# Verification record

The supplied standalone `verify.py` uses Python 3 standard-library rational arithmetic. Run `python3 verify.py` from the directory containing the extracted files.

The exact scalar checks cover all integers \(2\le m\le100\) (99 cases); complete vertex enumeration, full covariance-matrix reconstruction, positivity, support contact, and pointwise gauge verification cover \(2\le m\le15\) (14 cases). Successful execution prints `PASS: 99 exact dimension formulas and 14 independent full-matrix/contact enumerations.`

These calculations test the formulas in finite ranges. The all-dimensional claims rely on the proof in `RESULT.md`: the three-orbit vertex classification, explicit positive moment certificate, and trace/determinant lower bound for every other enclosing ellipsoid. No independent audit or external formal verification has been carried out.
