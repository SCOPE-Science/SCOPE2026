---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the finite witness and asymptotic

Given \((a,R,b)\) satisfying the hypotheses, compute \(Q=Q_a(R)\) and the least nonnegative representative \(r\) of the two congruences in `RESULT.md`. Put \(m=aQ\); the witness is \(r+m(\lfloor(Rb-r)/m\rfloor+1)\). Verify that it is strictly between \(Rb\) and \((R+1)b\). To check a particular witness directly, enumerate the integers \(0\le y\le\lfloor n/b\rfloor\). Whenever \(a\mid n-by\), set \(x=(n-by)/a\) and check \(\gcd(x,y)>1\). The sample cases in `RESULT.md` include \(Q=1\) and a nonprimitive representation.

The general obstruction follows from the residue of \(y\) and the prime factor argument in the proof. The liminf is a prime number theorem consequence of the finite obstruction and needs no computation. The known boundary value at \(a=2\) is cited as context, not claimed or certified as a new finding.
