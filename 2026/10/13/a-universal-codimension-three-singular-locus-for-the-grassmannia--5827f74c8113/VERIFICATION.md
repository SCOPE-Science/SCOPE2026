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

The proof was replayed from the chart
\[
A=[I_k\ B]
\]
and the identity
\[
\sum_{|I|=k}\det(A_I)^2=\det(I_k+BB^{\mathsf T}).
\]
Writing \(M=I_k+BB^{\mathsf T}\), exact differentiation gives
\[
\nabla_B\det(M)=2\operatorname{adj}(M)B.
\]
If \(\operatorname{rank}M\le k-2\), then \(\operatorname{adj}(M)=0\). If \(\operatorname{rank}M=k-1\), then \(\operatorname{adj}(M)=c\,vv^{\mathsf T}\) with \(0\ne v\in\ker M\). Vanishing of the gradient would force \(B^{\mathsf T}v=0\), contradicting
\[
Mv=v+B(B^{\mathsf T}v)=0.
\]
Thus the hypersurface singular locus is exactly the radical-at-least-two locus.

For exact radical dimension \(r\), the base of the parameterization is the orthogonal Grassmannian of totally isotropic \(r\)-planes, of dimension
\[
r(n-r)-\binom{r+1}{2},
\]
and the open nondegenerate fiber has dimension
\[
(k-r)(n-k-r).
\]
Their sum is
\[
k(n-k)-\binom{r+1}{2}.
\]

The bundled checker verifies this dimension identity for \(678\) admissible triples in a finite replay range, symbolically checks Cauchy--Binet for \(k=2,3\), and checks exact corank-one and corank-two witnesses through \(k=10\). These computations are consistency checks only; the universal proof is the symbolic argument above.

Scientific limits are recorded in `RESULT.md` and `REVIEW.md`.
