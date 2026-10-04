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
`artifacts/verify.py` uses only the Python standard library. It reconstructs the published ternary generator matrix, checks rank \(5\) and full Euclidean Gram rank, enumerates all \(3^5\) codewords, and enumerates every subspace of \(\mathbb F_3^5\) in reduced row-echelon form.

The replay checks all \(2663\) nonzero-dimensional subcodes and reproduces every support histogram and
\[
(d_1,d_2,d_3,d_4,d_5)=(12,17,19,21,23).
\]
It projectively canonicalizes the generator columns, finds exactly one repeated point at coordinates \(7\) and \(22\), and verifies by MacWilliams transformation
\[
A_0^\perp=1,\quad A_1^\perp=0,\quad A_2^\perp=2,\quad A_3^\perp=22.
\]
Successful replay prints `VERIFY_OK`.
