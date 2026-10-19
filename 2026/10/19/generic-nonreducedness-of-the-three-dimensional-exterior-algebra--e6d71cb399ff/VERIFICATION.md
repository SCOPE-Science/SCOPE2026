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

The standalone `verify.py` implements matrix multiplication and modular row reduction directly using Python 3 standard-library arithmetic. Execute `python3 verify.py` after extracting the packaged files into the same directory. It produces:

```
q=2: square-zero matrices=22, points=148, orbits=6, sizes=[1,21,21,21,42,42], tangent profiles=(8,8,10,18), quotient tangent profiles=(6,6,9,18)
q=3: square-zero matrices=105, points=1665, orbits=7, sizes=[1,104,104,104,104,624,624], tangent profiles=(8,8,10,18), quotient tangent profiles=(6,6,9,18)
VERIFY_OK
```

Every \(3\times3\) matrix over the two prime fields is considered. The program tests the complete candidate pair sets and their \(\operatorname{GL}_3\) conjugacy orbits, rather than just representatives, and computes linearized matrix relations independently. These checks are finite corroboration; the proof establishes the geometric classification and the formulas for all fields in the stated scope. Generic primary multiplicities and higher-order obstructions remain unproved.
