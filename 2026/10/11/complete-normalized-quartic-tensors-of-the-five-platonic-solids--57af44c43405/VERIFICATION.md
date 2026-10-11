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
# Verification of the quantified fourth-degree tensor

Let \(X\) be uniform in a centered, filled Platonic solid, and define
\[
R_2=\mathbb E\|X\|^2,\qquad R_4=\mathbb E\|X\|^4,
\qquad \kappa=R_4/R_2^2.
\]
For a unit vector \(u\), the angular profile
\[
F(u)=5\mathbb E\langle X,u\rangle^4/R_4
\]
has spherical mean one.

The exact checker reconstructs the face-barycentric identities
\[
\mathbb E\|Y\|^2=\rho^2(2+c)/6,
\quad
\mathbb E\|Y\|^4=\rho^4(7+6c+2c^2)/45
\]
and uses the independent cone radial density \(3s^2\) on \(0<s<1\) to verify all five entries of
\[
\kappa=\frac{25}{21}\left(1+\frac{\beta^2(8+4c+3c^2)}{180(1-\beta+\beta(2+c)/6)^2}\right).
\]
It separately verifies the Dirichlet fourth moments of the regular tetrahedron, the elementary cube and octahedron moment formulas, and the exact normalized angular coefficients \(-10/19\) and \(5/8\). For the icosahedral group it verifies the exact degree-two and degree-four character averages equal zero.

The independent *numerical* check builds the five polyhedra from their vertices, triangulates their convex hull facets, chooses a central tetrahedron with probability proportional to its volume, then samples Dirichlet barycentric coordinates inside that tetrahedron. This directly tests the derived expressions against the original uniform spatial measure. Because it is finite and stochastic, it is strictly diagnostic, never a proof of all directions or infinite classes.

Run `python verify.py` with the dependencies in `requirements.txt`; the expected success marker is `VERIFY_OK`. All exact mathematical comparisons are executable assertions. The fundamental proof of the universal statement is in `RESULT.md`; it does not infer the theorem from sampling.
