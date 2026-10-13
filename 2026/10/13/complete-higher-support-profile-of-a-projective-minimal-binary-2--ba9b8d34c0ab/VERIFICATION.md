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
\mathbb F_8=\mathbb F_2[\alpha]/(\alpha^3+\alpha+1)
\]
and
\[
\operatorname{Tr}_{8/2}(u)=u+u^2+u^4.
\]
It constructs
\[
D_1=
\{(x,y)\in\mathbb F_8^*\times\mathbb F_8:
\operatorname{Tr}_{8/2}(x^2y+xy+x)=0\}
\]
and checks
\[
|D_1|=24.
\]

The six message-basis evaluations form a rank-\(6\) binary generator. All \(64\) codewords are enumerated, giving
\[
1+24z^{10}+12z^{12}+24z^{14}+3z^{16}.
\]

For every
\[
1\le r\le6,
\]
all \(r\)-dimensional subspaces of \(\mathbb F_2^6\) are generated exactly once in reduced-row-echelon form. The checked counts are
\[
63,\ 651,\ 1395,\ 651,\ 63,\ 1.
\]
For every basis, the bitwise union of its codeword supports is computed and compared with the complete histogram in `artifacts/certificate.json`.

The total number of positive-dimensional subspaces checked is
\[
2824.
\]
Successful replay prints `VERIFY_OK`.
