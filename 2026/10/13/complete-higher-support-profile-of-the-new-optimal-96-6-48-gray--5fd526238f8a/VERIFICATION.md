---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
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

The length-48 blocks have distinct columns within each block, so each spans the six-dimensional message space. The script checks the block lengths, distinctness and column multiplicities. Its first support row checks the ordinary weight distribution
\[
1+58z^{48}+4z^{56}+z^{64}.
\]

It constructs the two excluded subspaces and checks
\[
\dim S_1=4,\qquad
\dim S_2=4,\qquad
\dim(S_1\cap S_2)=3.
\]

For each \(1\le r\le6\), every annihilator of dimension \(6-r\) is generated once by recursion on its intersection with a coordinate hyperplane and, if applicable, its coset of outside vectors. The counts in increasing message-space dimension are
\[
63,\ 651,\ 1395,\ 651,\ 63,\ 1.
\]
For every annihilator \(W\), the number of generator columns outside \(W\), counted with multiplicities, is compared with
\[
96-2^{7-r}+2^{\dim(W\cap S_1)}+2^{\dim(W\cap S_2)}.
\]
The complete histograms and their minima and minimizer counts are compared with `artifacts/certificate.json`. The certificate also supplies a nested sequence of simultaneous-minimum witnesses, which are read with the first character representing the first Cartesian coordinate. The verifier checks both intersection sizes at every dimension.

Successful replay prints `VERIFY_OK`.
