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
`artifacts/verify.py` uses only the Python standard library.

For
\[
n=3,4,5,
\]
it constructs
\[
D=
\{x\in\mathbb F_3^n:x_1\in\{0,1\}\}\setminus\{0\}
\]
and the systematic generator-column multiset
\[
\{e_1,\ldots,e_n\}\uplus D.
\]

For every
\[
1\le r\le n,
\]
the script enumerates all annihilator subspaces
\[
W\le\mathbb F_3^n,
\qquad
\dim W=n-r,
\]
once in reduced-row-echelon form. It computes each support directly as the total number of generator columns not lying in \(W\).

Independently, it computes
\[
E_{m,h}(s)
=
\binom{m}{s}
\sum_j
(-1)^j
\binom{m-s}{j}
\left[{m-s-j\atop h-s-j}\right]_3
\]
and builds the two closed support branches in `RESULT.md`.

The direct and formula histograms agree for every tested \(n\) and \(r\). The script also checks that each formula histogram sums to
\[
\left[{n\atop r}\right]_3,
\]
that the derived minima equal
\[
r+2\cdot3^{n-1}-3^{n-r},
\]
and that the number of minimizers equals
\[
\binom{n-1}{r-1}.
\]

At
\[
n=3,
\]
the one-dimensional spectrum reproduces the source's published weight enumerator
\[
1+2z^{10}+4z^{13}+12z^{14}+8z^{15}.
\]

Successful replay prints `VERIFY_OK`.
