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

It encodes
\[
g(x)=x^9+x^7+x^6+x^3+x^2+1
\]
as a binary bit vector and forms the six shifted rows
\[
g(x),xg(x),\ldots,x^5g(x).
\]
The verifier checks that these rows have rank \(6\).

It enumerates all \(64\) messages and verifies the exact ordinary weight distribution
\[
1+25z^6+30z^8+3z^{10}+5z^{12}.
\]

For each
\[
1\le r\le6,
\]
the script generates every \(r\)-dimensional subspace of \(\mathbb F_2^6\) exactly once in reduced-row-echelon form. It checks the dimension counts
\[
63,\ 651,\ 1395,\ 651,\ 63,\ 1,
\]
for a total of
\[
2824.
\]

For every basis it computes the bitwise union of the corresponding codeword supports, compares the complete histogram with `artifacts/certificate.json`, and checks one explicit minimizing basis in each dimension.

Successful replay prints `VERIFY_OK`.
