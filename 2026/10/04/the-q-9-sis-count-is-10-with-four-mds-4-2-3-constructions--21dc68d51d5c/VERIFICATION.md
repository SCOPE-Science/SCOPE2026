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

It represents \(\mathbb F_9\) as \(\mathbb F_3[u]/(u^2+1)\), exhausts every symmetric matrix
\[
\begin{pmatrix}a&b\\b&c\end{pmatrix}
\]
with \(a,b,c\in\mathbb F_9\), and checks \(A^2=-I_2\) exactly. It obtains ten matrices and checks them against `artifacts/certificate.json`.

For each SIS matrix, the verifier constructs \(G=[I_2\mid A]\), checks \(GG^T=0\), enumerates all \(81\) messages, and computes the exact minimum distance. The resulting distance distribution is six codes with \(d=2\) and four with \(d=3\). For the explicit matrix \(A=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\), it recomputes the weight distribution \(A_0=1\), \(A_3=32\), \(A_4=48\). The finite computation contains no heuristic or floating-point step.
