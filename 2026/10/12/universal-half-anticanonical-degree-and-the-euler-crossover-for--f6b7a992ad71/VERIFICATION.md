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
Let
\[
N=|\Phi^+|.
\]
Borel--Weil and Weyl's dimension formula give
\[
h^0(G/B,L_{m\rho})
=
\prod_{\alpha>0}
\frac{\langle(m+1)\rho,\alpha^\vee\rangle}
{\langle\rho,\alpha^\vee\rangle}
=
(m+1)^N.
\]
Therefore the leading Hilbert coefficient is \(1\) and
\[
\deg_{L_\rho}(G/B)=N!.
\]

The Schubert cells are affine and indexed by \(W\), so
\[
\chi_{\mathrm{top}}(G/B)=|W|.
\]

With Weyl exponents \(e_i\),
\[
|W|=\prod_i(e_i+1),\qquad N=\sum_i e_i.
\]
Since
\[
e+1\le2^e
\]
for every positive integer \(e\),
\[
|W|\le2^N.
\]
For \(N\ge4\),
\[
N!>2^N.
\]
The cases \(N\le3\) are checked directly.

The bundled checker verifies the standard exponent data for every irreducible finite Weyl type and replays the low-dimensional comparison. Finite checks are regression evidence only.
