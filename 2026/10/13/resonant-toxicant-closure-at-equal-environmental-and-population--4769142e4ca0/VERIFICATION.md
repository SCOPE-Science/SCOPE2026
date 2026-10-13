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
At \(g=v=c>0\), the post-pulse period map has linear part
\[
\begin{pmatrix}E&kTE\\0&E\end{pmatrix},
\qquad E=e^{-cT},
\]
so its spectral radius is \(E<1\).

The fixed point is
\[
T_e^*(0^+)=\frac{\Lambda}{1-E},
\qquad
T_0^*(0)=\frac{k\Lambda TE}{(1-E)^2}.
\]
The between-pulse solution gives the complete periodic orbit stated in RESULT.md.

Period integration yields
\[
\int_0^T T_e^*(t)\,dt=\frac{\Lambda}{c},
\qquad
\int_0^T T_0^*(t)\,dt=\frac{k\Lambda}{c^2},
\]
hence
\[
\left\langle T_0^*\right\rangle=\frac{k\Lambda}{c^2T}.
\]

The accompanying checker numerically replays the source's equal-rate parameter example and the nonresonant-to-resonant limit. These numerical checks corroborate but do not replace the exact proof.
