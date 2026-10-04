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
The proof is symbolic and does not depend on finite enumeration.

The rank calculation has three independently checkable ingredients:

1. A nonzero weighted path with \(r\) edges has rank
\[
2\left\lceil\frac r2\right\rceil.
\]

2. Proper cycle supports are encoded by the transfer matrix
\[
M=
\begin{pmatrix}
1&(q-1)u&0\\
1&0&q-1\\
1&(q-1)u&0
\end{pmatrix},
\]
whose nonzero eigenvalues satisfy
\[
\lambda^2-\lambda-q(q-1)u=0.
\]

3. On an all-nonzero even cycle, the Pfaffian is the difference of the two alternating edge products. Exactly
\[
(q-1)^{n-1}
\]
all-nonzero assignments make it vanish; those matrices have rank \(n-2\), while the remaining full-support matrices have rank \(n\).

The packaged checker `artifacts/verify.py` constructs the weighted antisymmetric cycle matrix and performs exact finite-field row reduction for
\[
(n,q)=(5,2),(5,3),(6,3),(7,3),(8,2),(6,4),(5,5).
\]
For each case it verifies the complete rank-count vector against the formula and confirms that the counts sum to \(q^n\). For odd \(q\), it also checks the character-degree sum-of-squares identity after applying the factor \(q^{n-2i}\).

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the formulas.
