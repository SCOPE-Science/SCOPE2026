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

The bundled `verify_identity.py` checks the algebraic core of the proof. For
\[
h(x)=\frac{x}{d+x},
\]
it verifies the pointwise decomposition
\[
\frac{m}{d+m}-\frac{x}{d+x}
=-\frac{d(x-m)}{(d+m)^2}
+\frac{d(x-m)^2}{(d+m)^2(d+x)}.
\]
After averaging with \(m=\mathbb E[x]\), the first term vanishes. The checker then verifies that combining
\[
\mathbb E[h(x)]=h(u_*),
\qquad
u_* = \frac{cd}{w-c},
\]
with the averaged decomposition yields
\[
m-u_*=
\frac{d+u_*}{d+m}
\mathbb E\!\left[\frac{(x-m)^2}{d+x}\right].
\]
It also verifies exactly that the source parameters \(c=7/10\), \(w=2\), \(d=20\) give \(u_*=140/13\). The stored checker output is `VERIFY_OK`.

The invariant-measure step is analytic. On compact support contained in \((0,\infty)^3\), \(\log u_3\) is smooth and
\[
\frac{d}{dt}\log u_3=-c_3+w_3\frac{u_2}{d_3+u_2}.
\]
The integral of this flow derivative against an invariant probability measure is zero. No numerical trajectory is used to infer the infinite-time identity.

Strictness uses only the printed vector field. If \(u_2\) is constant on an ergodic positive invariant state, the balance fixes \(u_2=u_{2*}\), the top-predator equation fixes \(u_3\) along trajectories, and the strictly increasing function \(u_1\mapsto w_1u_1/[(d_1+u_1)(1+f_2u_3)]\) fixes \(u_1\). The state is then an equilibrium point mass. Thus every non-equilibrium ergodic state has positive defect.

The verification does not establish existence, uniqueness, stability, Hopf direction, basin size, persistence, or any boundary-support extension.
