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

The Jacobian ideal on the chart \(x=1\) is \((f,f_t,f_s)\) by Euler's identity. To check the removal of \(f\), multiply out \((t+t^q)f_t+(s+s^q)f_s\) using \(f_t=1+t^2s^q\) and \(f_s=t^{q+2}+s^2+k\). The two copies of \(t^{q+2}s^q\) cancel, and the remaining terms are exactly \(f\). The resulting ideal is \((A^2,B^2)\), with \(A,B\) as in the proof. There are no support points on \(x=0\), by the homogeneous derivatives \(F_z\) on that line and \(F_x\) at \([0:0:1]\).

To replay the geometric count and algebra, set \(r=q(q+2)/4\), \(\kappa^2=k\), and \(H(s)=s^{r+1}+\kappa s^r+1\). The reduced equations give \(s\ne0\), \(t=s^{-q/2}\), and \(H(s)=0\); \(H(0)=1\) and \(H'=s^r\) give \(r+1\) distinct points. The determinant for the coordinate change to \((A,B)\) is \(s^{q/2}\), yielding the local basis \(1,A,B,AB\) after completion. Alternatively the full affine quotient is obtained from \(K[s,s^{-1}]/(H^2)\) by adjoining \(t\) with monic relation \(t^2-s^{-q}\), giving dimension \(4(r+1)\). These are exact symbolic checks; no finite enumeration is needed.
