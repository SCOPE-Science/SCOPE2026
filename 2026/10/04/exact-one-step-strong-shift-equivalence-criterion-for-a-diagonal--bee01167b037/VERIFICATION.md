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

The proof is self-contained exact arithmetic over nonnegative integers. The critical chain is:

1. For \(n^2\ne bc\), an elementary factorization \(A=RS\), \(B=SR\) has nonsingular \(R\), hence \(AR=RB\).
2. Solving \(AR=RB\) entrywise forces \(R=\begin{pmatrix}p&br\\r&cp\end{pmatrix}\).
3. Writing \(S=R^{-1}A\) and using that its bottom row is nonnegative integral gives nonnegative integers \(U,V\) with \(S=\begin{pmatrix}cV&bU\\U&V\end{pmatrix}\).
4. The \((1,2)\)-entry of \(RS=A\) gives \(pU+rV=1\). Nonnegative integrality leaves only four cases, each forcing \(b\mid n\) or \(c\mid n\).
5. Conversely, each divisibility condition has an explicit two-by-two factorization written in RESULT.md.

A separate bounded sanity check over \(1\le n,b,c\le8\), excluding \(n^2=bc\), and candidate parameters \(0\le p,r\le30\) found no disagreement with the theorem. That computation is not used to certify the universal statement.

Limit: the singular locus \(n^2=bc\) is outside the theorem. No claim about arbitrary-length strong shift equivalence is made for the non-elementary cases.
