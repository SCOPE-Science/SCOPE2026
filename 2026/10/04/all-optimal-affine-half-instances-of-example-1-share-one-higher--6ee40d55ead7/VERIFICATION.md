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
\mathbb F_8=\mathbb F_2[z]/(z^3+z+1)
\]
and constructs the \(9\) Desarguesian spread components
\[
E_\lambda=\{(x,\lambda x):x\in\mathbb F_8\},
\qquad
E_\infty=\{(0,x):x\in\mathbb F_8\}.
\]

For each of the \(36\) unordered component pairs it forms the union of their orthogonal complements and verifies that exactly \(49\) nonzero affine normals lie outside. For every one of the resulting \(1764\) source instances it builds the exact \(7\times95\) generator matrix.

Every subspace of \(\mathbb F_2^7\) is generated once in reduced row-echelon form. The counts in dimensions \(1\) through \(7\) are
\[
127,\ 2667,\ 11811,\ 11811,\ 2667,\ 127,\ 1.
\]
The verifier computes the support union for every subcode. In total it checks
\[
51528204
\]
subcode instances and confirms that all \(1764\) codes have one identical complete support spectrum.

The one-dimensional spectrum is checked against the published Example 1 weight enumerator, and the generalized Hamming hierarchy is
\[
(22,56,74,84,90,93,95).
\]
Successful replay prints `VERIFY_OK`.
