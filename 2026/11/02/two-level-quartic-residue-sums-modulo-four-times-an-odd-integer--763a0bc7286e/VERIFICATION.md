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

# Verification of the quartic residue-sum theorem

Execute `python3 verify.py` in the same directory. The script uses standard Python 3 and exact integers. It independently enumerates every odd \(q\) in the range \(3\le q\le1999\) (999 cases) and constructs all units whose square is \(2q-1\pmod{4q}\). It verifies the distinct subgroup count, exact least-positive residue sums, lack of \(-1\), and the translation involution. Expected output:

```
VERIFY_OK odd_q=3..1999 cases=999 empty_cases=764 subgroups=638 exact_CRT_count=PASS exact_two_level_sums=PASS pairing=PASS no_minus_one=PASS finite_only=YES
```

The checker is a finite corroboration, not a universal decision procedure or independent audit. The proof of the infinite statement is in `RESULT.md`; its noncomputational inputs are the elementary criterion for roots of \(-1\) modulo odd prime powers and the Chinese remainder theorem. A complete priority review of the older distribution-vector literature remains outstanding.
