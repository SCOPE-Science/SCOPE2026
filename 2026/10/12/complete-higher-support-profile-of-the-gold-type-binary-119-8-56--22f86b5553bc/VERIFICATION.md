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
\mathbb F_{256}=\mathbb F_2[\alpha]/(\alpha^8+\alpha^4+\alpha^3+\alpha^2+1)
\]
and verifies that \(\alpha\) has multiplicative order \(255\). It checks that
\[
a_1=\alpha^{17}\in\mathbb F_{16}\setminus\mathbb F_2
\]
and
\[
a_2=\alpha\notin\mathbb F_{16}.
\]

The defining set
\[
D=\{x\ne0:\operatorname{Tr}(a_1x^{17})=\operatorname{Tr}(a_2x^{17})=0\}
\]
is reconstructed directly and checked to have \(119\) elements.

The eight polynomial-basis evaluation rows have rank \(8\) and are pairwise orthogonal. Exhausting all \(256\) messages gives
\[
1+136z^{56}+119z^{64}.
\]

For each \(1\le r\le8\), every \(r\)-dimensional binary message subspace is generated exactly once in reduced-row-echelon form. The checked counts are
\[
255,\ 10795,\ 97155,\ 200787,\ 97155,\ 10795,\ 255,\ 1.
\]
For every basis, the bitwise union of its codeword supports is compared with the complete histogram in `artifacts/certificate.json`.

The total number of positive-dimensional subspaces checked is
\[
417198.
\]
Successful replay prints `VERIFY_OK`.
