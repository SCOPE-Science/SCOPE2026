# A unique extremal conic–five-line septic with two line-only triple points and no tacnodes

## Finding

Let \(C\subset\mathbb P^2_{\mathbb C}\) be a reduced union of one smooth conic and five distinct lines with only ADE singularities. Suppose that two ordinary triple points are intersections of three lines off the conic, and that there are no \(A_3\) points. In this class \(\tau(C)\le 27\), with equality in exactly one projective equivalence class of unmarked arrangements. A representative is

\[
f=xyz(x+y)(x+z)(y^2+yz+z^2+xy+xz)=0.
\]

It has basket \(2D_6+3D_4+3A_1\) and is free with projective exponents \((3,3)\).

## Assumptions and scope

All components are complex; the conic is smooth, and each line occurs once. The global Tjurina number is the sum of local Tjurina numbers. The two prescribed triple points are the maximum possible number involving only lines: distinct triples of line labels share at most one label, so three such triples would use at least six distinct labels. Absence of \(A_3\) means that each tangent line meets the conic at a point shared by another line. Neither an unrestricted classification at \(\tau=27\) nor novelty of the upper bound in the unrestricted class is asserted.

## Proof

The ADE condition allows at most three smooth local branches. Pairwise intersection multiplicities are one except for conic–line contact of order two. The possible local types are therefore \(A_1,A_3,D_4,D_6\), where \(D_6\) is the transverse crossing of a third branch with a tangent pair. Write \(t\) for the number of tangent lines, \(e\) for the number of distinct two-line intersections on the conic, and \(r\) for the number of three-line intersections off the conic. Bézout gives a pairwise multiplicity total of \(\binom52+5\cdot2=20\). Compared with this total, a tangency contributes one unit of Tjurina excess, and a three-branch point contributes one more. Thus \(\tau=20+t+e+r\).

The two line-only triples share exactly one line, which joins their centers. Make it the line at infinity. The remaining four lines fall into two distinct parallel pairs, so an invertible affine change of coordinates makes them \(u=0,u=1,v=0,v=1\). The four finite pair crossings are the grid corners. Hence \(e\le4\). The line at infinity cannot be tangent: its only crossings with the grid lines are the two triple centers, which are off the conic, and a tangency elsewhere would be \(A_3\). Any tangent grid line contains a corner on the conic, and it cannot contain two such corners by Bézout. A corner cannot be the tangency point of two different lines of a smooth conic. Thus \(t\le e\); for \(e\le2\) this gives \(t+e\le4\). For \(e=4\) every grid line is secant so \(t+e=4\). For \(e=3\), two grid lines are secant, so \(t+e\le5\). This proves the bound, and equality requires exactly three corners and the two grid lines with a single corner to be tangent.

Reversing either grid coordinate moves the missing corner to \((1,1)\). A conic through the other three has equation
\[
A u(u-1)+B uv+D v(v-1)=0,
\qquad AD\ne0,
\]
since the two line-only triple centers are off the conic. On \(u=1\) the restriction is \(v(Dv+B-D)\), and on \(v=1\) it is \(u(Au+B-A)\). Tangency at the respective single corners forces \(B=D\) and \(B=A\). Up to scalar there is only one equation. Homogenizing with \(u=-y/x,\ v=-z/x\) gives the displayed representative and line factors.

For existence, the Hessian determinant of \(q=y^2+yz+z^2+xy+xz\) is \(-2\). Its two tangent grid contacts are \([1:0:-1]\) and \([1:-1:0]\), each with a third transverse branch, giving \(D_6\). The other occupied finite corner \([1:0:0]\) has three distinct tangents and is \(D_4\), as are the triple centers \([0:0:1]\), \([0:1:0]\). The missing corner \([1:-1:-1]\) is a node. On \(x=0\), \(q\) meets at the two simple roots of \(y^2+yz+z^2=0\), away from the centers, producing two further nodes. The multiplicities \(2\cdot4+3\cdot3+3\) exhaust the Bézout total, so no other singularities occur.

For freeness, the following degree-three columns are Jacobian syzygies (their contractions with \(\nabla f\) vanish):
\[
\begin{aligned}
U={}&\bigl(x(y-z)(3x+8y+8z),\,-y(11xy+10xz+6y^2+7yz+8z^2),\,z(10xy+11xz+8y^2+7yz+6z^2)\bigr)^{\mathsf T},\\
V={}&\bigl(-x(3x^2+7xy+4xz+4y^2+9yz-4z^2),\,y(4x^2+7xy+10xz+3y^2+5yz+4z^2),\,z(4x^2-4xz-4y^2-2yz-3z^2)\bigr)^{\mathsf T}.
\end{aligned}
\]
Expansion gives \(\det[(x,y,z)^{\mathsf T},U,V]=-147f\). Euler's column sends \(f\) to \(7f\), so Saito's determinant criterion gives freeness and the two asserted projective exponents.

## Verification

The unchanged companion `verify.py` checks the representative's integer Jacobian identities, determinant and selected incidences. Its incidence computations do not establish projective uniqueness; that conclusion is the grid argument above.

## Relationship to prior work and limitations

Merta–Zieliński, [*On the non-existence of certain maximizing curves of degree 7*](https://arxiv.org/abs/2610.16658v1), Proposition 3.2, exclude \(\tau=28\) in the one-conic/five-line ADE class. Czarnota, [*On maximizing curves of degree 7*](https://arxiv.org/abs/2401.14721v2), Examples 4.5–4.8, gives free one-conic/five-line arrangements attaining \(27\) with projective exponents \((3,3)\). Together with the elementary incidence bound \(\tau\le28\), these give the unrestricted optimum and its free attainment with these exponents. The four printed baskets are different from the one above. Only Example 4.6 among them has no \(A_3\); it has three \(D_6\) points and cannot belong to the two-line-only-triple class without \(A_3\) (here \(t\le2\) whenever \(\tau=27\)). The classification here concerns the two-line-only-triple stratum without isolated tangency. It is not a census of all extremizers, and comparisons with known explicit examples cannot establish global priority.

The freeness criterion is from K. Saito, *Theory of logarithmic differential forms and logarithmic vector fields*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. 27 (1980), 265–291.
