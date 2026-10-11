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

Let
\[
\varepsilon_j=2^{-2j},
\qquad
\alpha_j=2^{-j},
\qquad
\Lambda_j=P_j+\varepsilon_jI.
\]
The spectrum of \(\Lambda_j\) is
\[
\{\varepsilon_j,1+\varepsilon_j\},
\]
with \(1+\varepsilon_j\) occurring on \(e_j\). Hence
\[
m(\Lambda_j)=\varepsilon_j,
\qquad
\|\Lambda_j\|=1+\varepsilon_j.
\]

The geometric sum is
\[
\sum_{j=1}^{\infty}\varepsilon_j^2
=
\sum_{j=1}^{\infty}16^{-j}
=
\frac1{15}.
\]
For each coordinate \(k\), the coefficient in the unscaled frame quadratic form is
\[
(1+\varepsilon_k)^2+\frac1{15}-\varepsilon_k^2
=
1+2\varepsilon_k+\frac1{15}.
\]
Thus the exact lower limiting coefficient is
\[
\frac{16}{15},
\]
and the maximal coefficient, attained at \(k=1\), is
\[
1+\frac12+\frac1{15}
=
\frac{47}{30}.
\]

Since
\[
D_j=\alpha_j\Lambda_j^{-1},
\]
the product is
\[
D_j\Lambda_j=\alpha_jI.
\]
Therefore
\[
\sum_j\|D_j\Lambda_jx\|^2
=
\left(\sum_j4^{-j}\right)\|x\|^2
=
\frac13\|x\|^2.
\]

The two eigenvalues of \(D_j\) are
\[
\frac{\alpha_j}{1+\varepsilon_j}
\quad\text{and}\quad
\frac{\alpha_j}{\varepsilon_j}=2^j.
\]
Therefore
\[
\|D_j\|=2^j
\]
and the full block diagonal operator is unbounded.

The complete target proofs were inspected in the published PDFs. Both use the positive lower-bound constants of the analysis blocks after assuming only a positive lower limit for the operator norms. The counterexample makes these two quantities diverge in opposite directions.

No truncation, floating-point certificate, or experimental extrapolation is used.
