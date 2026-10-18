# An equisingular transverse \(A_2\) line in the Han–Kwak multisecant threefold

## Finding
Let \(X\subset\mathbb P^5_{\mathbb C}\) be the degree-eight threefold of Han and Kwak, Example 6.2, parametrized by the six cubics recorded below. In the affine chart \(x_0\ne0\), its **reduced singular locus** is exactly
\[
L^\circ=\{x_1=x_2=x_3=x_4=0,\ x_0\ne0\}\cong\mathbb A^1.
\]
At **every** closed point \(p\in L^\circ\), not merely at a general point, the completed local ring is
\[
\widehat{\mathcal O}_{X,p}\cong
\mathbb C[[U,W,Z,B]]/(UW+Z^3).
\]
Therefore the transversal singularity is a Du Val \(A_2\) singularity, uniformly along this entire affine line. Its transversal Jacobian scheme has length two, and the local threefold is normal, with rational singularities, along \(L^\circ\). These claims are local to the displayed chart; the original authors' threefold is globally nonnormal.

## Assumptions and scope
Work over \(\mathbb C\). Use homogeneous source coordinates \([y_0:y_1:y_2:y_3]\) and target coordinates \([x_0:\cdots:x_5]\). The source map is defined by
\[
(s_0,s_1,s_2,s_3,s_4,s_5)=
(y_0y_1y_3,\ y_0^2y_2,\ y_0y_2^2,\ y_0^2y_1,\ y_0y_1^2+y_2^2y_3,\ y_0^2y_3+y_2y_3^2).
\]
The irreducible variety \(X\) is the closure of this image. Let
\[
u=x_1/x_0,\quad t=x_2/x_0,\quad v=x_3/x_0,\quad a=x_4/x_0,\quad b=x_5/x_0.
\]
Here \(x_0\ne0\) forces \(y_0y_1y_3\ne0\) in the parameter domain.

## Proof
Put \(P=y_1/y_0\), \(Q=y_2/y_0\), \(R=y_3/y_0\). On the parameter chart under consideration, \(P,R\ne0\), and
\[
(u,t,v,a,b)=\left(\frac{Q}{PR},\frac{Q^2}{PR},\frac1R,
\frac{P^2+Q^2R}{PR},\frac{R+QR^2}{PR}\right).
\]
Define \(K=bv^2-u\), \(H=1+b^2v\) and
\[
F=a(u-bv^2)+u^2+v^3,\qquad
G=tH+uv+bv^3-ab^2v^2.
\]
Both vanish identically under the displayed parametrization. So do the relations
\[
tK=u^2v,\qquad aK=u^2+v^3.
\]
On \(v\ne0\), the latter relations force \(K\ne0\): if \(K=0\), the first gives \(u=0\), and the second would give \(v^3=0\). Conversely, inverting the parametrization on this locus gives
\[
R=v^{-1},\qquad P=v^2/K,\qquad Q=uv/K.
\]
Thus \(X\cap\{v\ne0\}\) is exactly the smooth, three-dimensional open subvariety with coordinates \((u,b,v)\) satisfying \(vK\ne0\). In particular every point with \(H=0\) is smooth, since \(H=0\) implies \(v\ne0\).

On the principal open set \(H\ne0\), the relation \(G=0\) solves for \(t\). The hypersurface \(F=0\) in the remaining four variables is irreducible: it is linear in \(a\), and its coefficient \(u-bv^2\) is coprime to its constant term \(u^2+v^3\) after \(H\) is inverted. Indeed, setting \(u=bv^2\) in the constant term gives \(v^3H\), while \(v\) is coprime to \(u-bv^2\). The irreducible threefold defined by \(F=G=0\) contains the dense parametrized image, hence equals \(X\cap\{H\ne0\}\) scheme-theoretically (both are integral of dimension three).

The partial derivative of \(F\) with respect to \(a\) is \(u-bv^2\). At a singular point on \(H\ne0\), it vanishes; the equation \(F=0\) then yields \(v^3H=0\), so \(v=0\). It follows that \(u=0\). The derivative with respect to \(u\) is \(a+2u\), so \(a=0\). Finally \(G=0\) gives \(t=0\). Conversely, every point with \(u=t=v=a=0\) satisfies all equations and the derivatives vanish. This proves the claimed *reduced* singular locus on \(x_0\ne0\), since the complementary set \(H=0\) is smooth.

Fix any closed point of that line, with coordinate \(b=b_0\). In the formal completion, eliminate \(t\) with \(G\), then make the invertible changes
\[
W=u-bv^2,\qquad U=a+u+bv^2,\qquad
Z=v(1+b^2v)^{1/3},\qquad B=b-b_0.
\]
The cube root exists uniquely as a formal power series with constant term one because \(H=1\) at \(v=0\). The exact identity
\[
F=UW+v^3(1+b^2v)=UW+Z^3
\]
proves the completed-local-ring assertion. This is the product of a transverse \(A_2\) surface singularity with a formal smooth parameter. Its Jacobian ideal in the displayed coordinates is \((U,W,Z^2)\), so the singular scheme is not claimed to be reduced. Standard properties of \(A_2\) rational double points give the stated local normality and rationality.

## Verification
The accompanying `verify.py` reconstructs the six coordinate formulas, verifies the polynomial identities exactly, performs a Gröbner-elimination check of the scheme-theoretic equations, verifies the extra equations are redundant on \(H\ne0\), and checks the formal-normal-form identity. It also checks smoothness at the potentially exceptional \(H=0\) locus by an exact Jacobian minor. Execute `python verify.py` with SymPy installed; successful completion prints `VERIFY_OK`.

The argument for all points on the affine line is algebraic/formal and does not rely on sampled points or finite-field experiments.

## Relationship to prior work
Han and Kwak, Example 6.2 (arXiv:2610.12078v1, first public date 2026-10-08), construct the threefold and identify its global singular locus set-theoretically as a union of three lines. They do not give the completed local analytic type along the line studied here. Their auxiliary Macaulay2 computations concern the defining equations and singular-set decomposition. The present calculation adds the explicit uniform transversal \(A_2\) type, formal coordinates and scheme-theoretic infinitesimal consequence; the construction and the three-line observation are not new claims.

## Limitations
Only the chart \(x_0\ne0\) and the one affine piece of a singular line are classified. No singularity type at the remaining two lines or at the point \(L\cap\{x_0=0\}\) is asserted. The displayed local normality does not contradict the global nonnormality established by Han and Kwak. Independent expert assessment and exhaustive literature coverage have not been performed.

## References
Han, J. I., and Kwak, S., *Linear syzygies and linear subspaces whose lines are multisecant*, arXiv:2610.12078v1 (2026-10-08), Section 6, Example 6.2; https://arxiv.org/html/2610.12078v1 . The auxiliary Macaulay2 code linked from the preprint provides source defining equations and the global singular-locus computation.
