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
For an integer-valued PMF \(p\) and CDF \(F\), a strict lower record after current value \(\ell\) must satisfy
\[
X<\ell.
\]
Thus
\[
\Pr(L_{\mathrm{next}}=j\mid L_{\mathrm{current}}=\ell)
=
\frac{p(j)}{F(\ell-1)},
\qquad
j<\ell.
\]
The transition probabilities sum to one.

The source instead uses \(F(\ell)\), whose normalized mass below \(\ell\) sums only to
\[
F(\ell-1)/F(\ell)<1
\]
whenever \(p(\ell)>0\).

The bundled checker implements the DAPW CDF and PMF from the source. At
\[
(\alpha,\theta,\beta)=(2,1/2,1)
\]
and strict lower records
\[
(2,1,0),
\]
it obtains
\[
L_{\mathrm{pub}}
=
0.0296696393189962\ldots,
\]
\[
L_{\mathrm{strict}}
=
0.0597390364794552\ldots,
\]
and ratio
\[
0.496654132163646\ldots.
\]
