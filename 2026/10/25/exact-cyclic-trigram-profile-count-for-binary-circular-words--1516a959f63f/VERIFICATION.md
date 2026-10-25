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

Run `python verify.py` in the same directory. This checks direct cyclic-window histograms for every binary word at lengths 1 through 16 against an independent integer-flow construction and the generating-function coefficient formula, followed by parameter-only tests at lengths 20, 24 and 30. The program prints `VERIFY_OK` on success. The unrestricted theorem follows from the Euler-circuit and support-classification proof in RESULT.md, not from finite enumeration. The checker uses only Python's standard library.
