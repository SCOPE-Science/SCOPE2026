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

The 2026 primary source was checked at the exact formulas
\[
s(2m,2n)=\sum_i\binom{2m-4-2i}{m+n-2-i}
\]
and
\[
s(2m+1,2n)=\sum_i\binom{2m-3-2i}{m+n-3-i},
\]
with its stated exceptional additive \(1\) in the odd \(n=1\) case, and at its exact formulas for \(|K(c)|\), \(|T(c)|\), and the palindromic correction.

For even rows, each summand is \(2^{N_i}\) times a fair-binomial point probability at displacement \(n\), with \(N_i=2m-4-2i\). For odd rows the displacement is \(n-3/2\) and \(N_i=2m-3-2i\). In both cases the normalized powers of two converge to the geometric weights
\[
\frac34,\ \frac3{16},\ \frac3{64},\ldots,
\]
whose sum is one.

Stirling's formula gives the local De Moivre--Laplace estimate uniformly on bounded standardized windows. The maximal fair-binomial point mass is \(O(N^{-1/2})\), so the geometric mixture tail is uniformly summable. The moving finite upper limits remove only exponentially weighted terms in a bounded central window.

The exact cardinality formulas give
\[
|T_p(c)|=2|K(c)|-|T(c)|=O(2^{c/2}),
\qquad |T(c)|\asymp2^c,
\]
so the proxy-to-knot-set error remains negligible after multiplying by \(\sqrt c\).

The bundled finite regression prints:

`VERIFY_OK even_errors=0.00860810,0.00422818,0.00209576,0.00104337 odd_errors=0.07352973,0.05164790,0.03645998,0.02573190 palindromic_ratio_checked_c20_to120=true`

It checks transcription and constants only; finite data are not used as the infinite proof.

The independent-audit channel has not been performed.
