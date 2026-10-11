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
For \(N=4m+2\) and \(\alpha=\pi/N\), the proof first uses the exact Radon-plane reduction
\[
MS_B(X_N)
=
\max\{\|x-y\|:x,y\in\operatorname{ext}(B_{X_N}),\ x\perp_B y\}.
\]
At a fixed vertex \(v_0\), the two adjacent norming facets show that, modulo sign, the only Birkhoff-orthogonal vertices are \(v_m\) and \(v_{m+1}\).

Their two possible chord norms are
\[
D_-
=
\begin{cases}
2\sec\alpha\,\sin(\pi/4-\alpha/2),&m\text{ even},\\
2\sin(\pi/4-\alpha/2),&m\text{ odd},
\end{cases}
\]
and
\[
D_+
=
\begin{cases}
2\sin(\pi/4+\alpha/2),&m\text{ even},\\
2\sec\alpha\,\sin(\pi/4+\alpha/2),&m\text{ odd}.
\end{cases}
\]
The proof shows \(D_+>D_-\). Hence the displayed branch of \(D_+\) is the exact value of \(MS_B\).

`verify.py` reconstructs the regular polygon from its supporting normals, enumerates every ordered vertex pair for \(1\le m\le100\), detects Birkhoff orthogonality by the adjacent-facet sign criterion, and verifies that the largest distance matches the formula. It also checks the regular hexagon and decagon closed forms.

The finite enumeration is a reproducibility check only; the proof establishes the infinite family analytically.

No independent audit or independent validation has been performed.
