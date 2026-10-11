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

The published vanishing-cycle classes give
\[
V=
\begin{pmatrix}
0&0&1&1&1&0\\
1&1&0&0&1&0\\
1&0&1&0&0&1\\
0&1&0&1&0&1\\
0&1&1&0&0&0
\end{pmatrix}.
\]

The exact checker enumerates all square minors through size five. Their determinantal divisors are
\[
(1,1,1,1,4),
\]
which forces Smith invariant factors
\[
(1,1,1,1,4).
\]
It also verifies
\[
V(-1,0,0,-1,1,1)^{\mathsf T}=0
\]
and
\[
V^{\mathsf T}(1,1,1,1,0)^{\mathsf T}=2\mathbf 1_6.
\]

The source independently proves that \(\mathbf 1_6\notin\operatorname{im}V^{\mathsf T}\). Hence the class represented by \(\mathbf 1_6\) is nonzero of order two.

The checker output is:

`VERIFY_OK rank=5 determinantal_divisors=1,1,1,1,4 kernel=(-1,0,0,-1,1,1) VTu=(2,2,2,2,2,2)`

The checker validates only the explicit integer algebra. The identification of \(V\) as the PALF boundary matrix and of \([\mathbf 1_6]\) as \(c_1\) comes from the cited handle-theoretic source.

No independent audit has been performed.
