# Exact isosceles-orthogonal constant of \(\ell_3^2\)
## Finding
For the real Banach plane \(X=\ell_3^2\), define
\[
\Omega(X)=\sup\left\{\frac{\|x+2y\|^2+\|2x+y\|^2}{5\|x+y\|^2}}:x,y\in S_X,\ \|x+y\|=\|x-y\|\right\}.
\]
Then
\[
\Omega(\ell_3^2)=\frac{\sqrt[3]{162}}{5}.
\]
The maximum is attained at the coordinate pair \(x=(1,0)\), \(y=(0,1)\).

## Assumptions and scope
The scalar field is real and the norm is \(\|(a,b)\|_3=(|a|^3+|b|^3)^{1/3}\). The assertion concerns exactly the constant \(\Omega\) introduced for unit isosceles-orthogonal pairs; it does not concern the later generalized constant \(\Omega'\) or direct Takahashi-type constants.

The plane \(\ell_3^2\) is a symmetric Minkowski plane with the standard coordinate axes, because for every real \(t\),
\[
\|(1,t)\|_3=\|(1,-t)\|_3=\|(t,1)\|_3=\|(t,-1)\|_3.
\]
Therefore Proposition 4.2 of Liu--Yang--Li applies.

## Proof
Write, for \(t\ge 0\),
\[
U(t)=|1+2t|^3+|2-t|^3,\qquad
V(t)=|1-2t|^3+|2+t|^3,
\]
and
\[
W(t)=|1+t|^3+|1-t|^3.
\]
The symmetric-plane representation of \(\Omega\) gives
\[
\Omega(\ell_3^2)=\max_{t\ge0}F(t),\qquad
F(t)=\frac{U(t)^{2/3}+V(t)^{2/3}}{5W(t)^{2/3}}.
\]
For \(t>0\), direct substitution gives
\[
U(1/t)=t^{-3}V(t),\qquad V(1/t)=t^{-3}U(t),\qquad W(1/t)=t^{-3}W(t),
\]
so \(F(1/t)=F(t)\). It is therefore enough to consider \(0\le t\le1\).

Because \(s\mapsto s^{2/3}\) is concave on \([0,\infty)\),
\[
U(t)^{2/3}+V(t)^{2/3}
\le 2\left(\frac{U(t)+V(t)}2\right)^{2/3}.
\]
We now prove the exact polynomial bound \(U(t)+V(t)\le9W(t)\) on \([0,1]\). If \(0\le t\le1/2\), then
\[
U(t)+V(t)=18+36t^2,\qquad W(t)=2+6t^2,
\]
hence
\[
9W(t)-U(t)-V(t)=18t^2\ge0.
\]
If \(1/2\le t\le1\), then
\[
U(t)+V(t)=16+12t+12t^2+16t^3,
\]
and therefore
\[
9W(t)-U(t)-V(t)=2\bigl(1-6t+21t^2-8t^3\bigr).
\]
On this interval,
\[
1-6t+21t^2-8t^3=1+t(-8t^2+21t-6).
\]
The quadratic \(-8t^2+21t-6\) is increasing on \([1/2,1]\), because its derivative is \(21-16t\ge5\), and its value at \(t=1/2\) is \(5/2\). Thus the displayed cubic is positive and the bound follows.

Consequently,
\[
F(t)\le \frac25\left(\frac92\right)^{2/3}
=\frac{\sqrt[3]{162}}5.
\]
At \(t=0\), one has \(U(0)=V(0)=9\) and \(W(0)=2\), so equality holds. Equivalently, the coordinate unit vectors satisfy the isosceles condition and give
\[
\frac{\|(1,2)\|_3^2+\|(2,1)\|_3^2}{5\|(1,1)\|_3^2}
=\frac{\sqrt[3]{162}}5.
\]
This proves the claim.

## Verification
The proof is an exact one-variable reduction followed by concavity and two polynomial identities. The accompanying script `verify_omega_l3.py` reconstructs the cubic expansions with integer polynomial arithmetic, checks the reciprocal symmetry on exact rational test points, verifies the two difference polynomials, and confirms the equality value numerically as a consistency check. Its successful output is `VERIFY_OK`.

No finite sampling is used to prove the supremum. The global reduction comes from the cited symmetric-Minkowski-plane proposition, and the inequality is proved for the full interval \([0,1]\).

## Relationship to prior work
Liu, Yang, and Li introduced \(\Omega(X)\) and proved a one-parameter maximum formula for every symmetric Minkowski plane. Their paper gives exact examples for \(\ell_\infty^2\) and for a mixed \(\ell_\infty\)-\(\ell_1\) norm, but the inspected full text does not give the value for \(\ell_3^2\). The present calculation uses their reduction and closes the resulting optimization exactly at the first non-Hilbert odd integer exponent.

A 2026 paper on isosceles-orthogonal Takahashi--von Neumann--Jordan-type constants defines a different invariant \(C_t^I\), with an additional deformation parameter and power mean. Its exact classical-space formulas therefore do not imply the value of \(\Omega\) above. A 2025 paper computes generalized \(\Omega\)-type constants for Morrey and small Morrey spaces, not this classical two-dimensional \(\ell_3\) value.

## Limitations
The argument proves only the exact value for the real plane \(\ell_3^2\). It does not establish a formula for \(\ell_p^2\) at arbitrary \(p\), for higher-dimensional \(\ell_3\), or over the complex scalars. Search-based originality checks cannot exclude an unindexed calculation under different notation; no such covering result was found in the inspected sources.

## References
1. Q. Liu, Z. Yang, Y. Li, *New geometric constants of isosceles orthogonal type*, arXiv:2111.08392, first submitted 2021-11-16; MSC 46B20, 46C15.
2. Y. Li, W. Zhang, J. Qi, Q. Liu, *Isosceles-Orthogonal Takahashi--von Neumann--Jordan-Type Constants in Banach Spaces*, Axioms 15 (2026), 684.
3. Y. Ramadana, *Isosceles Orthogonal Geometric Constants for Morrey Spaces*, Turkish Journal of Mathematics and Computer Science 17 (2025), no. 1.
