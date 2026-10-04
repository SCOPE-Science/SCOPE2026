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

For an arbitrary cut of the centered cube \(C=[-1,1]^3\), orient the plane as
\[
\langle a,x\rangle=t,
\qquad t\ge0.
\]
Then
\[
C\cap\{\langle a,x\rangle\le0\}
\subseteq
C\cap\{\langle a,x\rangle\le t\},
\]
so it is enough to lower-bound the diameter of every central half-cube.

Cube symmetries reduce the normal to
\[
a=(\alpha,\beta,\gamma),
\qquad
\alpha\ge\beta\ge\gamma\ge0.
\]
The proof uses two exhaustive cases.

For \(\alpha\ge\beta+\gamma\), the boundary point
\[
p=\left(\frac{\beta-\gamma}{\alpha},-1,1\right)
\]
and the cube vertex \(q=(-1,1,-1)\) are in the same central half, with
\[
\lVert p-q\rVert^2
=8+\left(1+\frac{\beta-\gamma}{\alpha}\right)^2
\ge9.
\]

For \(\alpha<\beta+\gamma\), the boundary point
\[
p=\left(-1,\frac{\alpha-\gamma}{\beta},1\right)
\]
and the cube vertex \(q=(1,-1,-1)\) are in the same central half, with
\[
\lVert p-q\rVert^2
=8+\left(1+\frac{\alpha-\gamma}{\beta}\right)^2
\ge9.
\]
The coordinate central cut gives two boxes of side lengths \(1,2,2\), whose diameter is exactly \(3\). Scaling by \(1/2\) yields the unit-cube value \(3/2\).

The standalone `verify.py` was replayed from its actual package path. It checks the two witness formulas exactly over a finite rational test family, verifies all half-space memberships, verifies squared distance at least \(9\), and checks the attaining coordinate half-box. It printed:

`VERIFY_OK cube two-division diameter`

The finite replay is only a consistency check. The continuum result is established by the symbolic inequalities above.
