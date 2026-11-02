# A wild formal hypersurface normal form on the characteristic-eleven Klein cubic

## Finding
Let \(k=\overline{\mathbb F}_{11}\). On the characteristic-eleven Klein cubic threefold
\[
K:\quad F=\sum_{i\in\mathbb Z/5\mathbb Z}x_i^2x_{i+1}=0\quad\subset\mathbb P^4_k,
\]
the completed hypersurface germ at \(P=[1:3:9:5:4]\) is **formally contact equivalent** to
\[
\boxed{y_1^2+y_2^2+y_3^2+t^{11}=0}.
\]
Contact equivalence permits a formal coordinate change and multiplication of the equation by a formal unit. The assertion is stronger than merely knowing that the tangent quadratic form has corank one and that the Tjurina scheme has length eleven. In particular, a form with last exponent twelve has those same two numerical properties but a different formal contact type.

## Assumptions and scope
The ground field is algebraically closed of characteristic eleven. Work at the identified singular point of the coefficientwise reduction of the displayed integral cubic equation; the result concerns the formal completion of this local hypersurface only. Write \(x_0=1\) and use affine coordinates \((x_1,x_2,x_3,x_4)\). Contact equivalence here is an isomorphism of complete local hypersurface rings induced by ambient formal coordinates and an invertible multiplicative change of the defining equation; no claim of right equivalence of the functions is made. The characteristic is odd, so square roots of units exist formally after choosing constant square roots in \(k\).

## Proof
In the affine chart the equation is
\[
g=x_1+x_1^2x_2+x_2^2x_3+x_3^2x_4+x_4^2.
\]
The point \((3,9,5,4)\) is on \(g=0\) and all four first derivatives vanish there. The Hessian on these four variables, reduced modulo eleven, is
\[
H=\begin{pmatrix}7&6&0&0\\6&10&7&0\\0&7&8&10\\0&0&10&2\end{pmatrix}.
\]
Its rank is three. The block associated with \((x_2,x_3,x_4)\) has determinant \(8\ne0\) in \(k\). Thus the formal implicit-function theorem uniquely solves the three transverse critical equations \(\partial g/\partial x_j=0\), for \(j=2,3,4\), as formal functions of \(x_1\) near the point.

Introduce a local parameter \(v\) by \(x_1=3v^5\), with \(v=1\) at \(P\). This is an invertible formal change because its derivative there is \(15=4\ne0\) in characteristic eleven. An **explicit** transverse critical section is
\[
(x_1,x_2,x_3,x_4)=(3v^5,\;9v^6,\;5v^4,\;4v^8).
\]
Direct substitution into the three transverse first derivatives shows each vanishes *identically* in \(k[v]\). By uniqueness from the invertible Hessian block, this is the formal critical section. Substitution in the defining cubic gives the exact identity
\[
\begin{aligned}
h(v)&=3v^5+8v^{16}\\
&=3v^5(1-v^{11})\\
&=-3v^5(v-1)^{11}.
\end{aligned}
\]
The last equality uses Frobenius in characteristic eleven. The parameter-dependent formal Morse lemma (applied to the three nondegenerate transverse directions, not to the degenerate fourth direction) now splits the function as \(h(v)+Q_v(Y_1,Y_2,Y_3)\), where \(Q_v\) is a nondegenerate quadratic form over \(k[[v-1]]\). Since two is a unit and \(k\) is algebraically closed, a formal linear transformation diagonalizes and normalizes the quadratic form. Setting \(t=v-1\), we obtain a contact representative
\[
Y_1^2+Y_2^2+Y_3^2-3(1+t)^5t^{11}.
\]
Multiply the equation by the unit \((1+t)^{-5}\). A simultaneous rescaling of the three transverse coordinates by a square root of \((1+t)^{-5}\) restores the quadratic form to constant coefficients. Finally rescale \(t\) by an eleventh root of \(-3\), which exists in \(k\). This yields \(y_1^2+y_2^2+y_3^2+t^{11}=0\), proving the formal contact classification.

The exponent eleven is not a consequence of the numerical tangent Hessian rank and Tjurina length alone: both \(\sum_{j=1}^3y_j^2+t^{11}\) and \(\sum_{j=1}^3y_j^2+t^{12}\) have nondegenerate ternary quadratic parts and Tjurina algebra isomorphic to \(k[[t]]/(t^{11})\), because in characteristic eleven the derivative of \(t^{11}\) vanishes whereas the derivative of \(t^{12}\) is \(t^{11}\). The first nonzero order of the one-variable residual germ is respectively eleven and twelve, a formal contact invariant after Morse splitting. The exact critical-section calculation resolves this ambiguity for the Klein cubic.

## Verification
The standalone `verify.py` reconstructs the affine equation, checks the displayed singular point, exact Hessian rank and determinant, checks the transverse critical equations as polynomial identities modulo eleven, and checks the identity \(h(v)=-3v^5(v-1)^{11}\). It reports `VERIFY_OK`. These computations verify the concrete algebraic inputs; the formal splitting and unit equivalence are mathematical arguments above, not claims of automatic computational certification.

## Relationship to prior work
Gross and Popescu identified the Klein cubic as a birational projective model of the moduli space of \((1,11)\)-polarized abelian surfaces with level structure, working over characteristic zero (1999 preprint, 2001 journal publication). Existing arithmetic descriptions of the characteristic-eleven fiber identify its singular point, tangent Hessian rank, and the length-eleven singular scheme. Those data do not by themselves determine the formal contact type; the two explicit model germs compared in the proof show why. The present result gives the missing exact one-variable residual order and formal contact normal form. The neighboring literature on singular cubic threefolds predominantly studies characteristic zero, and no equivalent characteristic-eleven formal normal form was identified in the checked material.

## Limitations
The statement is over an algebraic closure of \(\mathbb F_{11}\) and is local to the indicated point. It does not determine a minimal or small resolution, the singularity's deformation space, canonical discrepancies, or a moduli interpretation in characteristic eleven. Contact equivalence is not asserted to preserve the gradient-only critical ideal of an arbitrary choice of equation, nor is a finite computation substituted for the formal Morse lemma. The assessment of historical priority remains provisional.

## References
1. M. Gross and S. Popescu, *The moduli space of (1,11)-polarized abelian surfaces is unirational*, arXiv:math/9902017, first public version 1999-02-02; *Compositio Mathematica* 126 (2001), 1–23, DOI:10.1023/A:1017518027822. The defining Klein cubic appears in Theorem 0.1.
2. Classical formal implicit-function theorem and parameter-dependent Morse splitting for nondegenerate quadratic directions in odd characteristic (used with the explicit critical section, not as a source of the concrete coefficient identity).
