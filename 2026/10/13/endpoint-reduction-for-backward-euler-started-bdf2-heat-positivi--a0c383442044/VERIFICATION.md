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

The proof is analytic. The executable check uses exact rational arithmetic to reconstruct the \(n=2\), \(s=5/2\) backward-Euler resolvent and the first BDF2 transfer matrix from both
\[
(3I+2sT_2)^{-1}(4R_2(s)-I)
\]
and
\[
4R_2(s)-3R_2(2s/3).
\]
Both give
\[
\frac1{1904}\begin{pmatrix}-11&45\\45&-11\end{pmatrix}.
\]
The checker also verifies the endpoint numerator polynomial \(-4s^3+5s^2+8s+3\) at \(s=5/2\), confirming that the witness is on the negative side of the exact two-point boundary. No finite computation is used as a substitute for the general endpoint-minimum proof.
