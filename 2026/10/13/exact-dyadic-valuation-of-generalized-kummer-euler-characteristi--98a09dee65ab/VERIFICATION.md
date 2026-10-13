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
The geometric input is the published identity
\[
\chi_{\mathrm{top}}(K_m(A))=m^3\sigma(m).
\]

For
\[
m=2^a\prod_i p_i^{e_i},
\]
multiplicativity of the divisor-sum function gives
\[
\nu_2(\chi_{\mathrm{top}}(K_m(A)))
=
3a+\sum_i\nu_2(\sigma(p_i^{e_i})),
\]
because
\[
\sigma(2^a)=2^{a+1}-1
\]
is odd.

For each odd prime \(p\),
\[
\nu_2(\sigma(p^e))=
\begin{cases}
0,&e\ \text{even},\\
\nu_2(p+1)+\nu_2(e+1)-1,&e\ \text{odd}.
\end{cases}
\]
The second line follows from the exact two-adic lifting-the-exponent formula for \(p^{e+1}-1\).

The bundled checker computes the divisor sum, direct Euler value, prime factorization, and both sides of the valuation identity for every
\[
2\le m\le100000.
\]
It also checks the odd-square classification and local odd-prime-power formula.

The finite computation is regression evidence only; the proof is symbolic.
