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

# Reproducibility and proof boundary

Run `python3 verify.py` with Python 3.8 or later and no third-party packages. The verification script checks all explicit coloring constructions on every Möbius ladder with \(3\le n\le300\), including graph-square properness when \(n\) is even. It also enumerates all nonempty strong odd independent color classes for \(n\in\{4,6,8,12\}\), obtaining counts \(8,40,128,1496\) and respective maximum sizes \(1,3,3,5\); the recorded execution terminates in `VERIFY_OK`.

No finite enumeration proves the theorem for infinitely many ladder sizes. The general statements follow from the proof of adjacent-rung exclusion, the parity obstruction to a color class filling an alternating maximum independent set when \(4\mid n\), and the explicit period-four-plus-seven-tail construction. Verification does not include an external or independent audit.
