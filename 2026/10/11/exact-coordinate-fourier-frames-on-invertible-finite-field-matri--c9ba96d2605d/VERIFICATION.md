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

Run `python verify.py` with Python 3 and NumPy. The script constructs every invertible matrix in each of eight finite cases, including a polynomial representation of the field of four elements; it constructs all \(1+m^2(q-1)\) columns, checks the entrywise Gram formula, and checks the full eigenvalue multiset. It then evaluates the sharp upper-eigenvalue transition using exact rational arithmetic at 576 parameter pairs.

Observed successful output ends in:

`VERIFY_OK direct_Gram_and_eigenvalue_cases=8 tested_inequality_pairs=576 fields_include_GF4=YES sharp_transition=PASS`

Direct cases: \((q,m)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2),(7,2)\). The two-dimensional cases test the underlying formula outside the stated novelty range \(m\ge3\) as a boundary check. The maximum eigenvalue discrepancy among directly checked cases was less than \(3\cdot10^{-15}\); numerical verification is not an exhaustive proof for all \(q,m\).

The unrestricted mathematical proof is independent of this code. No external independent audit has been performed.
