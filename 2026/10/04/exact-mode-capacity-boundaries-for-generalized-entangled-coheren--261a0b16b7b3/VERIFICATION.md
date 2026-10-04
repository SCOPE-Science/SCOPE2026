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

The normalization bound and both source optima were independently reduced to two cubic inequalities in
\[
s=\sqrt d.
\]
For
\[
x\ge1,
\]
the coefficients multiplying \(s^3\) and \(s\) are positive in both cases, so the positive root is unique and gives an exact iff boundary.

`verify_ecs_capacity.py` checks the original inequality against the cubic classification on a deterministic grid, verifies strict positivity of the cubic coefficients, and brackets the \(|\alpha|=4\) capacities between consecutive integers. It also checks convergence of the continuous capacity ratio to \(16\) at large amplitude.

The finite replay is supplementary. The all-parameter statement is supplied by the analytic proof in `RESULT.md`.

No independent audit has been performed.
