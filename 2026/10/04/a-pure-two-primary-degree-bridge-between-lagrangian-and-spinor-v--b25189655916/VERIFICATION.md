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
The symbolic proof compares two exact product formulas.

For the Pluecker-embedded Lagrangian Grassmannian,
\[
\deg L_n
=
\frac{M!}{\prod_{i=1}^{n}(2i-1)!}
\prod_{1\le i<j\le n}(2j-2i).
\]
The Vandermonde factor becomes
\[
2^{\binom n2}\prod_{j=1}^{n-1}j!.
\]

For the minimally embedded spinor variety,
\[
\deg S_n
=
\frac{M!\prod_{a=2}^{n-1}a!}
{\prod_{a=2}^{n}(2a-1)!}.
\]
After inserting \(1!=1\), the non-dyadic factors coincide term by term, proving
\[
\deg L_n=2^{\binom n2}\deg S_n.
\]

The bundled checker evaluates both integer products through \(n=100\), verifies the exact quotient and odd-part equality, and separately computes the spinor value from the general shifted hook product through \(n=20\). These finite checks are regression evidence only.

The conclusion is specific to the Pluecker embedding of \(L_n\) and the minimal half-spin embedding of \(S_n\).
