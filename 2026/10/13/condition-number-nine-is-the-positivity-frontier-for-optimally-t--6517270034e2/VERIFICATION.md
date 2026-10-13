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
The universal statement is proved analytically. Each diagonal coordinate is a scalar heavy-ball recurrence. With
\[
q=\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu}
\]
and \(t\in[-1,1]\), the normalized error is
\[
e_k=-q^k\left(U_k(t)-qU_{k-1}(t)\right).
\]
The proof uses \(|U_k(t)|\le k+1\) and the elementary inequality
\[
\frac{3k+2}{2^{k+1}}\le1\qquad(k\ge2).
\]
The endpoint \(t=-1\) gives the exact second-iterate ratio \((1+q)^2(1-2q)\), proving sharpness.

The embedded `verify.py` uses exact rational arithmetic to verify the Chebyshev recurrence identity on rational test points, the boundary case \(\kappa=9\), and the strict failure witness \(\kappa=16\). These finite checks corroborate the algebra but are not used as a substitute for the all-iteration proof.

Unproved limits include nondiagonal Hessians, nonzero initial velocity, other momentum parameters, adaptive methods, projections, and finite-precision feasibility.
