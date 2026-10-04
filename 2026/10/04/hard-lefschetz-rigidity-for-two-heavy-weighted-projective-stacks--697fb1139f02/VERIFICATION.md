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
The proof is symbolic and infinite. It uses the exact sector age formula for the quotient stack and the identity relating inverse ages to fixed-sector codimension. The decisive checks are:

1. For equal heavy weights \(a=b>1\), a primitive \(b\)-th root forces \(r/b=r(b-1)/b\), hence \(b=2\).
2. For \(a<b\), a primitive \(b\)-th root forces \(2(r+a)=b(r+1)\). If \(a\ge2\), this gives \(0<b-a<1\), impossible; hence \(a=1\) and \(b=2\).
3. The cases \((1,1)\), \((1,2)\), and \((2,2)\) satisfy age symmetry directly.

`artifacts/verify_hard_lefschetz.py` independently enumerates every inertia element with exact integer arithmetic for \(2\le r\le80\) and \(1\le a\le b\le80\), and performs additional primitive-sector regression checks over larger ranges. It prints `VERIFY_OK`.

The finite enumeration is not used to infer the infinite theorem.
