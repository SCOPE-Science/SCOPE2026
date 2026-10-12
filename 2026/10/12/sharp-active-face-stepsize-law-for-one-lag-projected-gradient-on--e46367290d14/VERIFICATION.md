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
The analytic proof is given in `RESULT.md`; the independent finite replay script `verify.py` uses only Python's standard library and exact rational arithmetic.

For \(a=1\), \(s=1\), and \((y_0,y_1)=(3/2,1)\), the exact recurrence runs through
\[
 \frac32,1,\frac12,\frac12,1,\frac32
\]
and repeats. All values are positive, so this is an exact counterexample at the sharp critical step.

At an active boundary \(a=0\), \(s\ge1\), the proof shows \(y_3=y_4=0\) regardless of the feasible initial pair. The checker replays several exact rational instances, including \(s=5/2\).

When \(a=-1\), even a very large step reaches the zero constraint exactly in finite time. The checker tests rational examples and the analytical decrement bound.

For the interior stable case, the checker verifies exact rational instances of the quadratic energy expansion
\[
 E(u-sv,u)-E(u,v)
 =-\frac{s(1-s)}{1+s}u^2-s(1-s)v^2
\]
and confirms projection cannot increase that energy on rational grids. These checks are not claimed as a proof over all real parameters: the theorem follows from the symbolic identities, positive definiteness, and the clipping inequality in `RESULT.md`.
