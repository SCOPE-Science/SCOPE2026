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

The analytic verification proceeds from the exact one-step complex multiplier
\[
m_s(\gamma)=1-s\gamma+i(2s\gamma^2-\gamma).
\]
Expanding gives
\[
|m_+|^2=1-2\gamma+2\gamma^2-4\gamma^3+4\gamma^4,
\qquad
|m_-|^2=1+2\gamma+2\gamma^2+4\gamma^3+4\gamma^4.
\]
The included `verify_seg_threshold.py` checks, using only Python's standard library, that their product is \(1-4\gamma^4+16\gamma^8\) and their mean is \(1+2\gamma^2+4\gamma^4\). It also checks the critical moduli \(\sqrt{2}-1\) and \(\sqrt{2}+1\) and the sign of the exact Lyapunov exponent on representative points on each side of the threshold.

The almost-sure limit is not inferred from finite computation: it follows from the strong law applied to iid two-valued logarithmic increments. The critical \(\liminf\) and \(\limsup\) follow from the standard recurrence and two-sided unboundedness of the one-dimensional simple symmetric random walk.

Limit: this verification addresses only the stated two-point linear family and equal constant steps.
