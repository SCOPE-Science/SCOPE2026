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
The verification artifact uses only the Python standard library.

It reconstructs the consistent-mass and stiffness matrices for one, two, and three interior nodes using exact rational arithmetic. For three nodes it verifies
\[
h^2M^{-1}S=
\begin{pmatrix}
51/14&-18/7&9/14\\
-18/7&30/7&-18/7\\
9/14&-18/7&51/14
\end{pmatrix}.
\]

A small exact arithmetic implementation of \(\mathbb Q(\sqrt2)\) checks the three stated eigenpairs. High-precision decimal exponentiation then verifies
\[
g(0.21281177692)<0<g(0.21281177693),
\]
so the analytic uniqueness proof places the threshold in that interval.

The script also checks the two-node positivity formula and the signs of the three-node nearest-neighbor and corner entries on both sides of the threshold bracket. No finite enumeration is used as a substitute for the analytic uniqueness argument.
