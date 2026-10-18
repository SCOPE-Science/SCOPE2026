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

# Reproducible verification

Run `python3 verify.py`. The executable uses only the Python standard library and reproduces the base certificate \(M_{10}\equiv2^{22}\pmod{2^{23}}\), the even-index normalized coefficient \(8128\equiv64\pmod{128}\), several nonresonant exact modular valuations, and the cancellation inequality on an explicit resonant pair. The executable prints `VERIFY_OK` after these finite checks. The infinite theorem rests on the inductive and valuation proof in `RESULT.md`, not on finite enumeration.

All exponents in the test are positive integers; no heuristic floating-point or external reference data is used. Source-priority novelty and independent audit are not established by this program.
