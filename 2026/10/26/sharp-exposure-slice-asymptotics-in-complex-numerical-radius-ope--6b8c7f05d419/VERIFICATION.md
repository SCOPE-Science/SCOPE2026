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

# Reproducible checks and limitations

The result has an analytic proof with four independently checkable ingredients.

1. For the off-diagonal row and column ranks, optimize \(u^{p-1}(1-u^p)^{1/p}\) or \(u(1-u^p)^{(p-1)/p}\) over \(0\le u\le1\), yielding \((p-1)^{(p-1)/p}/p\). Average conjugation by \(\operatorname{diag}(e^{i\theta},1,\ldots,1)\) to see why this exact radius bounds arbitrary matrices' off-diagonal rows and columns.
2. The state expansion around \(A\mapsto A_{11}\), together with \(\delta=t^p+(1-t^p)(1-\cos\theta)\), gives the correct exponent and produces explicit unit-radius rank-one lower-test operators.
3. At \(p=2\), the combined off-diagonal functional is a difference of two vector states and has norm \(2t\). Directly check the numerical radius of \(\begin{psmallmatrix}-i&1\\1&i\end{psmallmatrix}\) is one; the witness with \(\theta=t\) then gives \(3t/(\sqrt{3/2}\,t)=\sqrt6\) to leading order.
4. The finite-dimensional bipolar convex hull, Jensen's inequality for a concave fractional power, and a deficit-tail estimate transfer the pure-state leading bound to every point of the dual unit ball.

The mathematical limit is proved analytically; illustrative decimal evaluations are not proof certificates. All limits fix the dimension and exponent first; no claim of uniform error bounds in those parameters is made. The bibliography comparison supports a self-review originality assessment but is not an independent priority audit.
