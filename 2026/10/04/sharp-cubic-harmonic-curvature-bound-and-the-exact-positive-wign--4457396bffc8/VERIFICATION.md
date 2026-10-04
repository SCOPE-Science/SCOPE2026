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

The universal estimate is verified analytically. For a great-circle restriction
\[
p(t)=A\cos3t+B\sin3t+C\cos t+D\sin t,
\]
one has \(p''+p=-8(A\cos3t+B\sin3t)\). After a phase shift, the third-frequency amplitude \(R\) obeys the exact six-point identity
\[
R=\frac16\sum_{k=0}^5(-1)^k p(k\pi/3),
\]
so \(R\le\|p\|_\infty\). This proves the continuum operator bound without discretization.

For \(q_+\), the norm calculation reduces to maximizing \((1-b^2)b\) on \([0,1]\), whose unique positive interior maximizer is \(b=1/\sqrt3\). The displayed orthonormal pair in `RESULT.md` gives an exact great-circle restriction \(-2\cos(3t)/(3\sqrt3)\), attaining the operator bound and fixing \(M_+\) exactly.

`verify.py` replays the rational coefficient identities after squaring the radicals and checks the endpoint invariant arithmetic. It does not replace the analytic maximization or the support-function argument.

Limits: no sharp claim is made for spherical harmonics of degrees other than three or for arbitrary combinations of the two source cubics.
