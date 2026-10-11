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

The exact proof uses the upper-half-plane formula
\[
\cosh d((x,y),(x',y'))
=
1+
\frac{(x-x')^2+(y-y')^2}{2yy'}.
\]

For the source's vertices, the three row-type maxima are
\[
C_{\mathrm{low}}
=
1+\frac{(q+1)^2}{2q^4},
\]
\[
C_{\mathrm{up}}
=
1+\frac1{2q^2},
\]
and
\[
C_{\mathrm{cross}}
=
1+\frac{2q^2+2q+1}{2q^3(q+1)}.
\]
The first strictly exceeds the second. Their remaining difference is
\[
C_{\mathrm{cross}}-C_{\mathrm{low}}
=
\frac{q^3-q^2-2q-1}{2q^4(q+1)}.
\]
Its sign gives the exact branch.

The bundled `verify.py` enumerates every vertex pair with exact rational arithmetic for
\[
2\le q\le100,
\]
checks the closed formulas and the complete set of maximizing pairs, and verifies the symbolic numerator identity.

The asymptotic checks in the script are numerical sanity checks only. The proof of
\[
q\,\operatorname{diam}(T_q)\to\sqrt2
\]
uses
\[
q^2(C_{\mathrm{cross}}-1)\to1
\]
and
\[
\operatorname{arcosh}(1+x)\sim\sqrt{2x}.
\]
The area comparison uses the source's exact
\[
\operatorname{Area}(T_q)=2\arctan(1/(2q^2)).
\]

No finite computation is used to infer the all-\(q\) theorem.
