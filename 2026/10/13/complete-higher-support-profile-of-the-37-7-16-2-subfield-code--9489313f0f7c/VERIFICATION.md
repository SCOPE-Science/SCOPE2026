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

It realizes
\[
\mathbb F_8=\mathbb F_2[X]/(X^3+X+1)
\]
and implements
\[
\operatorname{Tr}_{8/2}(u)=u+u^2+u^4.
\]

The verifier constructs
\[
S=\{(x,y)\in\mathbb F_8^2:\operatorname{Tr}(xy)=0\}
\]
and checks
\[
|S|=36.
\]
It reconstructs the source codeword map
\[
c_{a,b,c}
=
\left(
\operatorname{Tr}(b),\
(a+\operatorname{Tr}(bx+cy))_{(x,y)\in S}
\right)
\]
from a seven-element binary message basis.

It checks generator rank \(7\) and the source ordinary weight distribution
\[
1+31z^{16}+32z^{17}+31z^{20}+32z^{21}+z^{36}.
\]

For each
\[
1\le r\le7,
\]
every \(r\)-dimensional binary message subspace is generated once in reduced-row-echelon form. The checked counts are
\[
127,\ 2667,\ 11811,\ 11811,\ 2667,\ 127,\ 1.
\]
For every basis, the bitwise union of its codeword supports is computed and compared against the complete histogram in `artifacts/certificate.json`.

The total number of positive-dimensional subspaces checked is
\[
29211.
\]

Successful replay prints `VERIFY_OK`.
