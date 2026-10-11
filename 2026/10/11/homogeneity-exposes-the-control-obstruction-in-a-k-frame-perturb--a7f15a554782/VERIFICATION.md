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

The target perturbation inequality was checked in its finite-support form. For each fixed coefficient vector \(c\), substituting \(tc\), dividing by \(t>0\), and taking \(t\downarrow0\) removes exactly the term \(\alpha t\|c\|\,\|T_Fc\|\). No interchange of an infinite sum with a limit is used.

From the reduced inequality,
\[
(1-\beta)\|T_Gc\|\le(\sqrt{B_F}+\gamma)\|c\|,
\]
so the synthesis map is uniformly bounded on finitely supported sequences and extends to \(\ell^2\). This proves the stated ordinary Bessel bound.

For sharpness, the one-atom choice \(F=(\sqrt{B_F})\) and \(G=((\sqrt{B_F}+\gamma)/(1-\beta))\) makes the reduced perturbation inequality an equality.

For the controlled counterexample, with \(0<\varepsilon<1\),
\[
S_G=\begin{pmatrix}1&\varepsilon\\\varepsilon&1+\varepsilon^2\end{pmatrix},\qquad
CS_G=\begin{pmatrix}1&\varepsilon\\2\varepsilon&2+2\varepsilon^2\end{pmatrix}.
\]
Thus \(CS_G\ne(CS_G)^*\). At \(f=(1,i)\), its quadratic value has imaginary part of magnitude \(\varepsilon\), so it cannot satisfy a real controlled Bessel inequality. The source smallness condition reduces to \(\varepsilon<1\), exactly the range chosen.

No computation beyond these exact symbolic identities is required. The result does not assert a controlled conclusion without \(CS_G=S_GC\), and it does not identify the source's controlled upper bound with the ordinary Bessel bound \(B_F\).
