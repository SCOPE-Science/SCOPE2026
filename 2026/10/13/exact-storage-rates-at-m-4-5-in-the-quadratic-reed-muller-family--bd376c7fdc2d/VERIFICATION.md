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

For each \(1\le m\le5\), it enumerates all vectors \(x\in\mathbb F_2^m\), vectorizes \(xx^{\mathsf T}\) in upper-triangular coordinates, and builds every translated indicator row of
\[
M_m(S,T)=\mathbf 1\{\operatorname{rank}(S+T)\le1\}.
\]
It then performs exact Gaussian elimination over \(\mathbb F_2\) using integer xor rows.

The expected exact rank table is
\[
(1,4,28,448,13658).
\]
For \(m=4\) and \(m=5\), this yields kernel dimensions \(576\) and \(19110\), hence rates \(9/16\) and \(9555/16384\).

The verifier also hashes the resulting pivot bases. The \(m=4\) digest is `561bbbb3a2857b38e78d21486b7e850bac8a2076712ee01d83fe07d4d342294f`; the \(m=5\) digest is `ade82677807e3b6ffc3bb00922de9d7c2d6a64a66d039b9343a7be18b1479906`.

Successful replay prints `VERIFY_OK`.
