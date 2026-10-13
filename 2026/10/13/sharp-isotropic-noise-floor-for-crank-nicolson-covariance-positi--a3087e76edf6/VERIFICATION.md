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
The standalone `verify.py` replays the exact rational witness from the stated two-mode Lyapunov equation. It checks the component-level Crank–Nicolson formula, the rational threshold, the critical rank-one orientation, and the determinant behavior on both sides of the threshold.

For \(h=1\), \(a=1/4\), \(b=4/5\), the identities are
\[
r=3/4,
\quad\ell=1/5,
\quad z=19/61,
\quad k=3249/14884,
\quad E=2541/37210.
\]
The exact threshold and rank-one squared weight are
\[
s_*=42/1159,
\qquad t_*=74/209,
\]
and the checker verifies \(F_{s_*}(t_*)=0\). It also verifies that subcritical \(s=1/100\) gives a negative determinant at the same direction.

At zero diffusion, the equal-weight rank-one covariance gives the exact matrix
\[
P^+=\begin{pmatrix}3/10&19/122\\19/122&1/18\end{pmatrix}
\]
with determinant \(-847/111630\), so positivity fails even though each diagonal mode is scalar-positive.

Finite replay is corroborative only. The universal cone condition, equality characterization, and asymptotic coefficient are proved analytically in `RESULT.md`; the script does not certify all real parameters by enumeration.
