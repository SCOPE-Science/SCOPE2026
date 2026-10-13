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
The universal rate/mass/time phase diagram is proved analytically in `RESULT.md`. The included `verify.py` uses only Python standard-library exact fractions and checks its finite algebraic certificate and one strict sign example.

With \(R=4\), \(\varepsilon=1/8\), put \(Z=[z,G_Rz]\), \(M=Z^{\mathsf T}Z\), and \(H=Z^{\mathsf T}G_RZ\). The checker exactly reconstructs
\[
M=\begin{pmatrix}65/64&-17/16\\-17/16&5/2\end{pmatrix},
\qquad
H=\begin{pmatrix}-17/16&5/2\\5/2&-8\end{pmatrix},
\]
\[
\det(H-sM)=\frac{361s^2+1400s+576}{256},
\quad
\det(H+4M)=\frac{47}{16}.
\]
The characteristic roots are
\[
\lambda_\pm=\frac{-700\pm68\sqrt{61}}{361}.
\]
Using only the rational enclosure \(39/5<\sqrt{61}<8\), the checker proves \(\lambda_->-7/2\), \(\lambda_+<0\), and \(\lambda_+-\lambda_->29/10\), hence
\[
\frac{4+\lambda_+}{4+\lambda_-}<8
\quad\text{while}\quad
e^{\lambda_+-\lambda_-}
>1+29/10+(29/10)^2/2>8.
\]
This is a rigorous sign certificate at \(t=1\): the third component of the two-step Lanczos approximation is negative, while the exact component is \(\varepsilon(1+e^{-8})/(2(1+\varepsilon))>0\).

The checker also verifies the determinant identity for several rational positive rate/mass pairs. Those finite replays do not replace the symbolic proof for arbitrary \(R>1\), \(\varepsilon>0\), and \(t\ge0\). No claim is made about minimum dimension or irreducible chains.
