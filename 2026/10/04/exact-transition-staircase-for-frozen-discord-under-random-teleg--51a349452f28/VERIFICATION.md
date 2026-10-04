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

`verify_telegraph_transition_count.py` evaluates
\[
\Lambda(\nu)
=
e^{-\nu}
\left[
\cos(\mu\nu)+\frac{\sin(\mu\nu)}{\mu}
\right]
\]
directly.

The script checks the derivative identity and the exact absolute maxima
\[
|\Lambda(n\pi/\mu)|=e^{-n\pi/\mu}.
\]
For deterministic \((\mu,\rho)\) grids it independently bisects every sign-changing solution of
\[
|\Lambda(\nu)|-\rho=0
\]
on each lobe and compares that root count with
\[
2\left\lceil
\frac{\mu}{\pi}\log\!\frac1\rho
\right\rceil-1.
\]

Separate exact-boundary cases set
\[
\rho=e^{-m\pi/\mu}
\]
and confirm that the equality at the \(m\)-th maximum is a tangency rather than an additional transition pair.

The two parameter sets plotted in the source are also replayed and give total counts \(3\) and \(7\).

The finite replay is supplementary. The exact count is proved analytically in `RESULT.md`.

No independent audit has been performed.
