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

The all-integer proof uses
\[
n-\varphi(n)\ge \frac np
\quad\text{and}\quad
\frac np\ge2^{H(n)-1},
\]
where \(p\) is the least prime divisor of composite \(n\). These inequalities force every defect at most \(3\) into a complete eight-integer candidate list.

`verify.py` independently checks every \(2\le n\le10^6\), recomputing \(\varphi(n)\), \(H(n)\), the least-prime lower bound, and all low fibers. A successful run is recorded in `VERIFY_OUTPUT.txt`.

The finite replay is regression evidence only. No independent audit has been performed.
