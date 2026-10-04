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

Normalize the longest side to \(1\), reflect if needed, and write
\[
P(d,h)=\operatorname{conv}\{(0,0),(1,0),(d,h),(1+d,h)\},
\]
with
\[
0\le d\le s=\sqrt{1-h^2}.
\]

The published corrected formula is
\[
S_h(d)
=
\max\left\{
\frac1{1-d+s},
\sqrt{d^2+h^2},
1-d
\right\}.
\]
The first two terms increase with \(d\), while the third decreases. Hence the unique minimizer is the first crossing of the decreasing term with one of the two increasing terms.

The first crossing gives
\[
d_A
=
1-\frac{\sqrt{s^2+4}-s}{2}.
\]
The second gives
\[
d_B=\frac{s^2}{2}.
\]
At \(d=d_B\), the sign deciding which crossing came first is the sign of
\[
\left(1-\frac{s^2}{2}\right)
\left(1-\frac{s^2}{2}+s\right)-1
=
\frac{s}{4}
\left(s^3-2s^2-4s+4\right).
\]
The cubic is strictly decreasing on \((0,1)\), changes sign there, and therefore has one threshold root.

The embedded `verify.py` was replayed from its actual package path. It checks the threshold numerically, all branch equality and dominance relations over \(999\) interior heights, three-way equality at the transition, fine-grid minimization of the original three-term formula at representative heights, strict increase of the closed profile, and the small-height quadratic coefficient.

The replay output was:

`VERIFY_OK parallelogram folding height profile`

The finite checks are consistency tests only. The continuum theorem follows from the exact monotone-crossing argument.
