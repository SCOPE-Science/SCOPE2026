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

For every binary matrix \(B\) of size
\[
k\times r,
\qquad
1\le k,r\le3,
\]
the script computes \(t=\operatorname{rank}B\) and exhausts every binary matrix \(U\) of the same size. It directly tests
\[
BU^T+UB^T=0
\]
and compares the exact number of solutions with
\[
2^{k(r-t)+t(t+1)/2}.
\]

The matrix of the linear map \(f_B\) is also constructed independently and its binary rank is checked against
\[
\frac{t(2k-t-1)}2.
\]

Canonical rank-\(t\) matrices are checked for all
\[
1\le k,r\le6,
\qquad
0\le t\le\min(k,r),
\]
by direct linear-map rank computation. The adjacent-rank exponent identity
\[
e(t+1)-e(t)=t+1-k
\]
is verified over the same range.

The exhaustive finite checks are stress tests. The formula for arbitrary sizes follows from the symbolic rank-normal-form proof in `RESULT.md`.

Successful replay prints `VERIFY_OK`.
