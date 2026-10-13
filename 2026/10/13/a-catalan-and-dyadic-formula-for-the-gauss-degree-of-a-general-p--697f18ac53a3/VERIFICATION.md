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
The source formula reconstructed in the checker is
\[
D(g)
=
\prod_{j=0}^{g-4}
\frac{\binom{g+j}{g-3-j}}
{\binom{2g-7-2j}{g-3-j}}.
\]

The symbolic proof shows
\[
D(g)=2^{g-3}C_{g-2}
\]
by matching the initial value and the exact recurrence
\[
D(g+1)/D(g)=4(2g-3)/g.
\]

The Prym Gauss degree is then
\[
2^{g-3}(C_{g-2}+1).
\]

For Catalan numbers,
\[
\nu_2(C_m)=s_2(m+1)-1.
\]
When \(m+1\) is a power of two, an odd-factorial induction gives
\[
C_m\equiv1\pmod4;
\]
otherwise \(C_m\) is even. This proves the exact valuation formula.

The bundled checker reads the source-product implementation from the actual package path and verifies the product identity, Gauss-degree identity, and two-adic law for every
\[
3\le g\le300.
\]
Finite checks are regression evidence only.
