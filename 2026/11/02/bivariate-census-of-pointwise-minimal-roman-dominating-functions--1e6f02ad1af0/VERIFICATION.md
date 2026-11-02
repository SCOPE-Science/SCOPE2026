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

The standalone `verify.py` is reproducible with Python 3's standard library:

```
python3 verify.py
```

The verifier computes the formal coefficient recurrence for \(-xD_x/D\) in two grading variables. It independently enumerates every labeling \(f:V(C_n)\to\{0,1,2\}\) for \(3\le n\le12\), applies the original Roman domination test, and tests all available single-coordinate decreases; it then compares every \((k(f),w(f))\) coefficient. A separate selected-vertex subset enumeration verifies the private-neighbor criterion through \(n=17\). The historical \(C_5\) count of \(16\) and the displayed initial count sequence are checked explicitly. Execution returned `VERIFY_OK`.

These calculations verify the indicated finite cases, not all cycle orders. The general claim is supported by the mathematical argument in `RESULT.md`. No independent mathematical audit, external proof assistant, or formal certification has been performed.
