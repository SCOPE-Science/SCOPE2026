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
# Verification

For a relation \(R\) on the chain \(C_n\), the proof shows:
\[
R\text{ is forward-confluent}
\]
if and only if nonempty rows form a suffix and their maxima are weakly nondecreasing.

For fixed nonempty-row count \(k\), a row of maximum \(m\) has exactly
\[
2^{m-1}
\]
possible contents. Summing over weakly increasing maxima gives
\[
h_k(1,2,\ldots,2^{n-1})
=
\begin{bmatrix}
n+k-1\\k
\end{bmatrix}_{2}.
\]

The bundled `verify.py` enumerates every binary relation for \(n\le4\), tests the source forward-confluence quantifiers directly, and separately tests the row-normal form. It confirms exact counts
\[
2,\ 11,\ 198,\ 13377.
\]

The script also evaluates the Gaussian-binomial formula through \(n=12\), verifies fixed-\(k\) counts independently for small \(n\), and checks the displayed initial values. It prints `VERIFY_OK`.

## Limits

The exhaustive relation enumeration stops at four worlds because the ambient relation space has size \(2^{n^2}\). The arbitrary-\(n\) theorem and asymptotic are proved symbolically and do not depend on extrapolation from these finite checks.
