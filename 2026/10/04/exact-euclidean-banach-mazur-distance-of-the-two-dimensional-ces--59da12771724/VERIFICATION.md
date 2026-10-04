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

The proof was replayed from the defining norm and the published linear normalization.

1. Substituting \(T(u,v)=(2u/\sqrt5,2v)\) into the two-dimensional Cesàro norm gives exactly
   \[
   \|T(u,v)\|^2=u^2+v^2+(2/\sqrt5)|uv|.
   \]
2. For \(N_a^2=u^2+v^2+2a|uv|\), the bounds
   \[
   \|z\|_2^2\le N_a(z)^2\le(1+a)\|z\|_2^2
   \]
   give an explicit admissible Euclidean ellipsoid pair with factor \(\sqrt{1+a}\).
3. The identity
   \[
   N_a(z)^2=\max\{z^TQ_+z,z^TQ_-z\}
   \]
   reduces every possible inner ellipse to two simultaneous matrix inequalities.
4. For \(A=\begin{pmatrix}p&r\\r&q\end{pmatrix}\), the conditions \(A-Q_\pm\succeq0\) imply
   \[
   (p-1)(q-1)\ge(r-a)^2,\qquad (p-1)(q-1)\ge(r+a)^2.
   \]
   Hence \(\max\{p,q\}\ge1+a\).
5. Since \(e_1,e_2\) are points of the unit ball, containment of the unit ball in \(\lambda E_A\) gives \(p,q\le\lambda^2\). Therefore \(\lambda\ge\sqrt{1+a}\).

The exact lower bound ranges over every origin-centered ellipse, which is equivalent to ranging over all invertible linear images of the Euclidean disk. No numerical experiment or finite enumeration is used as proof.
