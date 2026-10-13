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

It reconstructs the defining set
\[
D=(\Delta_A+u\Delta_B)^c
\]
for
\[
A=\{1,2\},\qquad B=\{1,3\}
\]
and forms both binary Gray generator columns
\[
(d_2,d_1),\qquad(d_1+d_2,d_1)
\]
for every defining-set element.

The script verifies:
\[
|D|=48,\qquad \operatorname{rank}(G)=6,
\]
and the ordinary weight distribution
\[
1+58z^{48}+4z^{56}+z^{64}.
\]

It constructs the two excluded subspaces and checks
\[
\dim S_1=4,\qquad
\dim S_2=4,\qquad
\dim(S_1\cap S_2)=3.
\]

Every positive-dimensional subspace of \(\mathbb F_2^6\) is generated once in reduced row-echelon form. The dimension counts are
\[
63,\ 651,\ 1395,\ 651,\ 63,\ 1.
\]
For every subspace, the direct union of codeword supports is compared with
\[
96-2^{7-r}+2^{\dim(W\cap S_1)}+2^{\dim(W\cap S_2)}.
\]
The complete histograms are compared with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.
