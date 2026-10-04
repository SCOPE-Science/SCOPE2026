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
The verifier in `artifacts/verify.py` recomputes the affine local germ, checks all branch contacts, isolates the origin in the Tjurina scheme by saturation with \((x+1)(y+1)\), performs exact rational Gröbner elimination, and confirms local Tjurina length \(10\). It also checks \(\\delta=7\), \(\\mu=11\), the two resolution multiplicities \(4,6\), and the numerical consistency of \(\Delta_p(t)=(t-1)(t^4-1)(t^6-1)\).

The monodromy step uses the classical A'Campo plane-curve resolution formula. The script checks the resolution data supplied to that formula; it does not reprove A'Campo's theorem.
