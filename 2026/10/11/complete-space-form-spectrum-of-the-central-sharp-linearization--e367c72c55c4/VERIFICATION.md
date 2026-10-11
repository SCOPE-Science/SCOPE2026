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

The primary identities used are
\[
\Gamma_{1,1}(R)(S)=\frac14R\#S,
\qquad
d\mathcal Q_R(S)=-2\Gamma_{1,1}(R)S,
\]
and, at
\[
R_\kappa=\frac{\kappa}{2}g^2,
\]
\[
\Gamma_{1,1}(R_\kappa)
=
\kappa\sum_{a<b}D_L(E_{ab})D_R(E_{ab}).
\]

For a diagonal curvature operator with weights \(w_{ij}\), the derivation action yields
\[
(\Gamma S)_{ij}
=
\kappa\sum_{k\ne i,j}(w_{ik}+w_{jk}).
\]

The three representative calculations are:

\[
w_{ij}=1
\quad\Longrightarrow\quad
(\Gamma S)_{ij}=2(n-2)\kappa\,w_{ij},
\]

\[
w_{ij}=s_i+s_j,\qquad \sum_i s_i=0
\quad\Longrightarrow\quad
(\Gamma S)_{ij}=(n-4)\kappa\,w_{ij},
\]

and, for a diagonal Weyl tensor with
\[
\sum_{j\ne i}w_{ij}=0,
\]
\[
(\Gamma S)_{ij}=-2\kappa\,w_{ij}.
\]

The source's irreducible Ricci decomposition and equivariance extend these representative scalars to their whole summands. Multiplication by \(-2\) gives the displayed spectrum of \(d\mathcal Q_{R_\kappa}\).

The bundled checker builds the exterior-square derivation matrices from first principles and verifies these eigenvalues in every dimension from four through nine. This finite replay is a consistency check; the arbitrary-dimensional proof is the coefficient computation above.
