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
The packaged checker `artifacts/verify.py` starts from the multiplication
\[
uv=vu=z
\]
and a completely general \(3\times3\) linear map.

It reconstructs all nine ordered basis-pair Nijenhuis equations. Two square equations force the lower two entries of \(N(z)\) to vanish. After this reduction, the remaining system is verified to be exactly
\[
K^T
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
K=0.
\]

The checker independently verifies the connected automorphisms
\[
\begin{pmatrix}
pq&\rho&\sigma\\
0&p&0\\
0&0&q
\end{pmatrix}
\]
and the component interchanging \(u\) and \(v\), including multiplicativity.

It then checks the block conjugation formula
\[
K\mapsto F K F^{-1},
\qquad
\ell\mapsto(\lambda\ell+rK)F^{-1},
\]
and the diagonal normalization
\[
\begin{pmatrix}
t&s\\
0&0
\end{pmatrix}
\mapsto
\begin{pmatrix}
t&(p/q)s\\
0&0
\end{pmatrix}.
\]

Finally, every one of the seven displayed normal-form families is substituted into all defining equations and verified identically.

The checker returns `VERIFY_OK`.

No finite enumeration is used to establish the complex-field theorem.
