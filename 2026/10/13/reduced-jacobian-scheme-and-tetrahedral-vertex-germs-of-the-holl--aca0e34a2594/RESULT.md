# Reduced Jacobian scheme and tetrahedral vertex germs of the hollow quartic

## Finding
Let \(a,b,c,d,e,f\) be independent homogeneous coordinates on \(\mathbb P^5_{\mathbb C}\), and set
\[
M=\begin{pmatrix}0&a&b&c\\a&0&d&e\\b&d&0&f\\c&e&f&0\end{pmatrix},\quad
F=\det M=a^2f^2+b^2e^2+c^2d^2-2abef-2acdf-2bcde.
\]
Let \(X=V(F)\) and let \(\Sigma\subset X\) be the **scheme-theoretic projective singular locus**, defined by the homogeneous partial derivatives of \(F\) (equivalently, by the corresponding saturated Jacobian ideal).

**Theorem.** The entire projective singular scheme \(\Sigma\) is reduced. Its eleven irreducible components are the eight coordinate planes and three smooth quadrics previously identified for the underlying reduced singular support. Each occurs with scheme multiplicity one, and \(\deg\Sigma=14\).

More precisely, in the chart \(a=1\), set \(w=f-be-cd\). The polynomial change of coordinates \((b,c,d,e,f)\leftrightarrow(b,c,d,e,w)\) gives
\[
F=w^2-4bcde,\qquad
\mathcal I_{\Sigma\cap\{a\ne0\}}=(w,bcd,bce,bde,cde).
\]
Writing \((x_1,x_2,x_3,x_4)=(b,c,d,e)\), this ideal has the **scheme-theoretic primary decomposition**
\[
(w,bcd,bce,bde,cde)
=\bigcap_{1\le i<j\le4}(w,x_i,x_j).
\]
Every other off-diagonal-coordinate chart has the same structure after a permutation of the four indices of \(M\). Therefore this is a complete local description of the projective singular scheme, including all component intersections.

At each of the six coordinate vertices of \(\mathbb P^5\), the completed local ring of \(\Sigma\) is
\[
\widehat{\mathcal O}_{\Sigma,p}\simeq
\mathbb C[[b,c,d,e]]/(bcd,bce,bde,cde).
\]
Its tangent cone is the affine cone over the one-skeleton of a tetrahedron. It is reduced and Cohen--Macaulay of dimension \(2\), with Hilbert--Samuel series
\[
\sum_{q\ge0}\dim_{\mathbb C}(\mathfrak m^q/\mathfrak m^{q+1})t^q
=\frac{1+2t+3t^2}{(1-t)^2},
\]
and Hilbert--Samuel multiplicity \(6\).

## Assumptions and scope
The ground field is \(\mathbb C\). The result is about the **Jacobian scheme** of this particular zero-diagonal \(4\times4\) determinant, not just the set of singular points. The six off-diagonal chart opens cover \(\mathbb P^5\). The isomorphism on a chart is polynomial, not merely formal or étale. The vertex Hilbert--Samuel series is for the local singular scheme, not for the ambient determinant hypersurface.

## Proof
**(1) Exact affine presentation.** On \(a=1\), the identity
\[
F=(f-be-cd)^2-4bcde
\]
is immediate on expanding the determinant. Set \(w=f-be-cd\). Its inverse is \(f=w+be+cd\); therefore this is a polynomial automorphism of the five-dimensional affine chart. The five derivatives in the new coordinates are
\[
\partial_w F=2w,\quad
\partial_b F=-4cde,\quad
\partial_c F=-4bde,\quad
\partial_d F=-4bce,\quad
\partial_e F=-4bcd.
\]
The ordinary chain rule shows that these five derivatives generate the same ideal as the derivatives in the original five chart coordinates \(b,c,d,e,f\). The homogeneous derivative \(\partial_a F\) imposes no additional scheme equation on \(X\): Euler's identity \(4F=aF_a+bF_b+cF_c+dF_d+eF_e+fF_f\), with \(a=1\), makes \(F_a\) redundant modulo \(F\) and the five chart derivatives. Also \(F=w^2-4b(cde)\) itself belongs to the five-derivative ideal, so this is indeed the full local homogeneous Jacobian ideal.

**(2) Radicality and primary decomposition.** A monomial in \(b,c,d,e\) lies in \((bcd,bce,bde,cde)\) precisely when its support involves at least three distinct variables. It lies in every pair ideal \((x_i,x_j)\) precisely when its support meets every two-element set, equivalently when it has at least three distinct variables. Hence
\[
(bcd,bce,bde,cde)=\bigcap_{i<j}(x_i,x_j).
\]
All six component ideals are prime; the displayed local Jacobian ideal is radical with no embedded primary component.

**(3) Global conclusion.** Any of the six off-diagonal coordinates can play the role of \(a\) via a permutation of the four matrix indices. Thus the projective Jacobian scheme has radical local ideal in an open cover of \(\mathbb P^5\), hence is reduced as a scheme. These local components glue to exactly eight coordinate planes \(P\) (one nonzero choice in each of \(\{a,f\},\{b,e\},\{c,d\}\)) and three smooth quadrics
\[
Q_A=V(a,f,be-cd),\quad
Q_B=V(b,e,af-cd),\quad
Q_C=V(c,d,af-be).
\]
Indeed, the six pair components on the \(a\ne0\) chart give four such planes and the restrictions of \(Q_B,Q_C\). The same verification on all six charts exhausts the components. Consequently the saturated Jacobian ideal is the **intersection of the eleven distinct homogeneous prime ideals** for these surfaces. Its projective degree is \(8\cdot1+3\cdot2=14\).

**(4) Deepest singularities.** The coordinate point \(p=[1:0:0:0:0:0]\) corresponds to the maximal ideal \((w,b,c,d,e)\) in the chart. Quotienting by \(w\) and completing gives the displayed Stanley--Reisner ring. Its squarefree faces are the empty face, four vertices and six edges of the complete graph on four vertices. Every nonzero monomial has support of size at most two, so the standard-graded Hilbert series is \((1+2t+3t^2)/(1-t)^2\). This is also the associated-graded ring at the chart origin, proving the Hilbert--Samuel assertion; the multiplicity is \(1+2+3=6\). The simplicial complex is connected and pure of dimension one, so by Reisner's criterion its Stanley--Reisner ring is Cohen--Macaulay over \(\mathbb C\). The six coordinate vertices are equivalent under permutations of the matrix indices.

## Verification
The standalone `verify.py` reconstructs the determinant using exact symbolic arithmetic, checks the change of variables, checks all five chart derivatives modulo \(w\), checks the squarefree primary-intersection criterion on every monomial through degree \(8\), and checks the Hilbert series in those degrees. Its recorded output is in `verification_output.txt`. The general equality of ideals and global reducedness use the exact symbolic proof above; finite monomial checks are supplementary and not offered as an infinite certificate.

## Relationship to prior work
Helmer and Sturmfels (arXiv:1603.06544, Section 4, equation (35)) identify the second-hypersimplex discriminant as this zero-diagonal symmetric determinant. Al Ahmadieh and Vinzant (arXiv:2105.13444, Example 6.5) identify the same quartic as a linear slice of Cayley's hyperdeterminant; Devriendt, Friedman, Reinke and Sturmfels (arXiv:2401.03684, Example 3.6) give the squared-Grassmannian description. The published study *Eleven singular surfaces on the smallest squared Grassmannian* proves the underlying eleven-component **reduced support**, the generic transverse node type, normality, and a sign-quotient presentation; it explicitly does **not** determine the complete Jacobian scheme or the exceptional local types at component intersections. The present theorem adds the radical **scheme** structure at every point and a precise Cohen--Macaulay multiplicity-six model at each coordinate vertex. Those assertions do not follow merely from the previously reported support decomposition or generic nodes; they require the new local Jacobian ideal computation. The quartic equation and sign-quotient construction are not claimed as new.

## Limitations
The theorem concerns the \(4\times4\) case and characteristic zero; no extension to larger matrices or characteristic \(2\) is claimed. The coordinate-vertex model describes the singular **scheme**, not the full analytic classification of the hypersurface near all intersections. Earlier exact presentations of the quartic make the derivative computation accessible; an equivalent scheme-theoretic assertion in unindexed literature remains a historical novelty risk. The numerical check samples degrees only through \(8\); the full scheme identity is proved algebraically.

## References
1. M. Helmer and B. Sturmfels, *Nearest Points on Toric Varieties*, arXiv:1603.06544 (first posted 2016-03-21), Section 4, equation (35).
2. A. Al Ahmadieh and C. Vinzant, *Characterizing principal minors of symmetric matrices via determinantal multiaffine polynomials*, arXiv:2105.13444 (2021), Example 6.5.
3. K. Devriendt, H. Friedman, B. Reinke and B. Sturmfels, *The Two Lives of the Grassmannian*, arXiv:2401.03684 (2024), Example 3.6.
4. *Eleven singular surfaces on the smallest squared Grassmannian*, published mathematical research record (2026), identifier `6ce60a96126e`, publicly available at `https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-eleven-singular-surfaces-on-the-smallest-squared-grassmannian--6ce60a96126e`.
5. R. Stanley, *Combinatorics and Commutative Algebra*, second edition, Birkhäuser, 1996 (Stanley--Reisner rings and Hilbert series).
