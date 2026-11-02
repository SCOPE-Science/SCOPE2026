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

The symbolic proof is the primary mathematical evidence. `verify.py` independently evaluates both defining products on every permutation of the rectangular band with two rows and \(r=1,2,3,4\) columns, then checks a separate parameter enumeration and cycle-enumerator identity. It requires only Python's standard library.

Command: `python verify.py`

Observed direct one-sided/two-sided counts: \((2,2)\), \((16,12)\), \((288,144)\), \((9216,2880)\). Parameter counts for \(r=1,2,3,4\): \(2,12,144,2880\). Cycle sums for \(r=1,\ldots,7\): \(2,6,24,120,720,5040,40320\). Final output: `VERIFY_OK`.

Finite enumeration is not a substitute for the proof valid for every integer \(r\ge1\). No other external validation is claimed.
