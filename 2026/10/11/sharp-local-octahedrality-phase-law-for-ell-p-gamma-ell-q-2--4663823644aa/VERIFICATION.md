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
For finite \(q\ge2\), if
\[
(r,s)\in S_{\ell_q^2},
\]
then
\[
(s,-r)\in S_{\ell_q^2}
\]
and both symmetric chords have \(q\)-th power
\[
|r+s|^q+|r-s|^q.
\]
Scalar Clarkson gives
\[
|r+s|^q+|r-s|^q
\ge
2(|r|^q+|s|^q)
=
2.
\]
This is the exact fiber lower mechanism.

For the one-coordinate upper witness, if
\[
a=\|y_{\gamma_0}\|_q,
\]
one sign gives a fiber chord of \(q\)-th power at most
\[
1+a^q.
\]
The full outer \(p\)-th power is therefore at most
\[
H(a)
=
(1+a^q)^{p/q}+1-a^p.
\]
Writing
\[
b=a^q,\qquad r=p/q,
\]
one has \(H\le2\) for \(r\le1\) by subadditivity and \(H\le2^r\) for \(r\ge1\) by monotonicity. This yields
\[
s=2^{1/\min\{p,q\}}.
\]

The bundled `verify.py` checks these scalar inequalities and representative fiber witnesses numerically over a broad parameter grid. The checks are supplementary; the proof above is analytic over the full parameter range.

No independent audit or independent validation has been performed.
