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
\mathbb F_{256}
=
\mathbb F_2[X]/(X^8+X^4+X^3+X^2+1)
\]
and verifies that the residue class \(\alpha=X\) has multiplicative order \(255\).

The defining set is reconstructed as
\[
D=
\{x\ne0:
\operatorname{Tr}(\alpha x^{17})=
\operatorname{Tr}(\alpha^2 x^{17})=0\}.
\]
The script checks
\[
|D|=51
\]
and constructs the trace-evaluation generator from the basis
\[
1,\alpha,\ldots,\alpha^7.
\]
It verifies generator rank \(8\) and the published ordinary weight distribution
\[
1+34z^{20}+102z^{24}+102z^{28}+17z^{32}.
\]

For every
\[
1\le r\le8,
\]
the verifier generates every \(r\)-dimensional subspace of \(\mathbb F_2^8\) exactly once in reduced-row-echelon form. The dimension counts are
\[
255,\ 10795,\ 97155,\ 200787,\ 97155,\ 10795,\ 255,\ 1,
\]
for a total of
\[
417198.
\]

For each basis, the bitwise union of the corresponding codeword supports is computed and counted. The resulting complete histograms are compared byte-for-value with the certificate, as are the generalized Hamming hierarchy
\[
(20,30,38,42,46,48,50,51)
\]
and the number of minimizers at every level.

Successful replay prints `VERIFY_OK`.
