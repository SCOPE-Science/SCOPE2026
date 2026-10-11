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

The exact proof uses no finite enumeration as a substitute for a global argument. It checks all boundary types of the unit sphere: cubic arcs, opposite-sign line segments, and the nonsmooth coordinate axes.

For the cubic arc, the unique norming functional forces the normalized orthogonal direction \(y=(t^2/(1+t^2),-1/(1+t^2))\). For \(t\le1/2\), one signed distance already exceeds the target by an elementary estimate. For \(t\ge1/2\), differentiating the exact cube \(F(t)=N(x-y)^3\) gives the displayed factorization in RESULT.md; its auxiliary polynomial lower bound is increasing and positive on the full interval, so \(F(t)\ge F(1)\).

On the opposite-sign segment, the norming functional forces the diagonal direction and a strictly increasing cubic expression has its minimum at the midpoint. At an axis, the full interval of norming functionals is used and a two-case estimate covers every permitted orthogonal direction.

Finally, the midpoint pair \(x=(1/2,-1/2)\), \(y=(2^{-1/3},2^{-1/3})\) is checked directly: both are unit, the segment norming functional annihilates \(y\), and both signed distances have cube \(1+3/2^{4/3}\). This proves attainment.

The source comparison was made against the full open-access 2022 paper and against accessible metadata/abstract for the 2016 same-space James-constant paper. The reported decimal \(1.2987\) is consistent with the exact value, but no numerical agreement is used to establish the theorem. Independent audit has not been performed.
