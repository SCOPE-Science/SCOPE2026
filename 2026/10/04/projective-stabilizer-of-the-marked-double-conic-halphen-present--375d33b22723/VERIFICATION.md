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

The proof reduces the problem to exact polynomial identities. Run `python artifacts/verify.py` from the package root. The script uses only the Python standard library and prints `VERIFY_OK` if all identities and the two surviving involutive cases are confirmed.

The script verifies the conic parametrization-induced transformation formulas, the condition that preservation of the second conic forces the ratio \(d/a\) to square to \(1\), and the exact cubic difference \(r(2\varepsilon x-r y)Q\). It does not attempt to certify automorphisms of the blown-up surface that do not descend to the marked plane model.
