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

It constructs \(\mathbb F_{p^3}\) for \(p=3\) and \(p=7\) using an automatically selected irreducible monic cubic.

For each prime it reconstructs
\[
S=\{(x,y):\operatorname{Tr}(x^2+y^2)=0\},
\]
checks
\[
|S|=p^5-p^3+p^2,
\]
and forms seven punctured generator rows: one constant row, three rows from the \(b\)-coordinate trace basis, and three from the \(c\)-coordinate trace basis.

The script checks rank \(7\) and verifies that the punctured Euclidean Gram matrix is zero.

For \(p=3\), all \(3^7=2187\) codewords are enumerated, reproducing
\[
1+952z^{144}+1008z^{153}+224z^{162}+2z^{225}.
\]

For the unpunctured code, the source first coordinate is appended. The resulting Gram matrix is checked to be exactly the outer product of the trace functional on the \(b\)-basis with itself, hence has rank \(1\) and a six-dimensional radical.

Successful replay prints `VERIFY_OK`.
