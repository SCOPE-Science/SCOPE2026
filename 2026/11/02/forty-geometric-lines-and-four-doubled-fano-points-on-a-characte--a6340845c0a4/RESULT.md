# Forty geometric lines and four doubled Fano points on a characteristic-five quartic

## Finding
Let \(X\subset\mathbb P^3_{\mathbb F_5}\) be the quartic defined by
\[
F=x_0^2x_1x_2+x_1^2x_2^2+x_0x_1^2x_3+x_0x_2^2x_3+x_0^2x_3^2+x_1x_2x_3^2=0.
\]
For this **literal displayed polynomial**, the Fano scheme of lines \(\mathcal F=F_1(X)\subset\operatorname{Gr}(2,4)\) is finite. Its geometric reduced support has **exactly 40 points**, all rational over \(\mathbb F_{25}\). Exactly four of these lines are rational over \(\mathbb F_5\), and the other 36 form 18 conjugate pairs. As a scheme, \(\mathcal F\) has **length 44**: exactly the four coordinate lines
\[
(x_2=x_3=0),\quad(x_1=x_3=0),\quad(x_0=x_2=0),\quad(x_0=x_1=0)
\]
are nonreduced points, each of local length two; the remaining 36 points are reduced. Consequently, for every integer \(n\geq1\),
\[
\#\mathcal F(\mathbb F_{5^n})=\begin{cases}4& n\text{ odd},\\40& n\text{ even},\end{cases}
\qquad
Z(\mathcal F,T)=\frac1{(1-T)^4(1-T^2)^{18}}.
\]
Here the zeta function counts closed points, and hence is unchanged by the nilpotent structure. The source displaying this six-term equation attributes 48 lines to its characteristic-five reduction; the exact calculation above pertains to the equation **as printed** and does not identify why the source count differs.

## Assumptions and scope
The ground field has characteristic five; geometric statements mean base change to \(\overline{\mathbb F}_5\). A line is a two-dimensional vector subspace of the four-dimensional coordinate vector space. The Fano scheme is the closed subscheme of the Grassmannian cut out by the five coefficients of \(F\) restricted to its universal line. “Length” means the dimension of its coordinate algebra after base change to an algebraic closure, summed over all support points. No claim is made about a different intended or corrected equation.

## Proof
Write a line in unique reduced-row-echelon form, with pivot columns \(0\leq i<j\leq3\). The resulting six disjoint Schubert cells cover all geometric lines. Substitute
\[
(x_0,x_1,x_2,x_3)=(r_0U+s_0V,\ldots,r_3U+s_3V)
\]
into \(F\), and set the five coefficients of the binary quartic equal to zero. A reduced exact Gröbner-basis calculation over \(\mathbb F_5\) gives the dimensions of the corresponding zero-dimensional affine coordinate algebras in pivot order \((01),(02),(03),(12),(13),(23)\):
\[
26,\quad9,\quad4,\quad0,\quad1,\quad1.
\]
These are upper bounds on the numbers of distinct geometric points in the respective cells. They are computed from the standard monomials not divisible by the Gröbner-basis leading terms; the standalone code explicitly reconstructs the five equations and these numbers.

Enumerate all two-planes over \(\mathbb F_{25}=\mathbb F_5[\alpha]/(\alpha^2-2)\) in reduced-row-echelon form. A degree-four polynomial in one variable vanishes identically if it vanishes at the five distinct elements of \(\mathbb F_5\); thus five evaluations give an exact, not probabilistic, line-membership test. The numbers of distinct lines found in the six cells are
\[
25,\quad9,\quad4,\quad0,\quad1,\quad1.
\]
On the open \((01)\)-cell, the line \(x_2=x_3=0\) has Zariski tangent dimension one in the Fano scheme. Its local length is therefore at least two. Together with 24 other distinct points, this exhausts the entire cell-algebra dimension 26; there are no further geometric points. Each other cell already has as many distinct points as its coordinate-algebra dimension, so it too contains no additional points. This proves the total of 40 over the algebraic closure, rather than merely a finite-field lower bound.

For the scheme structure, work in the full four-parameter open Plücker chart around each of these 40 points, rather than only in its possibly lower-dimensional Schubert cell. The five quartic-coefficient equations have Jacobian rank four at 36 points and rank three at precisely the four coordinate lines displayed above. At each exceptional coordinate line, translate the four local chart variables so the point is the origin, write \(\mathfrak m\) for their maximal ideal, and compute
\[
\dim_{\mathbb F_5}\frac{\mathbb F_5[z_1,\ldots,z_4]}{I+\mathfrak m^2}
=
\dim_{\mathbb F_5}\frac{\mathbb F_5[z_1,\ldots,z_4]}{I+\mathfrak m^3}=2.
\]
Because the global line scheme has finite support, its local rings are Artinian. Equality of these two successive truncation lengths yields \(\mathfrak m^2=\mathfrak m^3\), and Nakayama's lemma gives \(\mathfrak m^2=0\). Each exceptional local ring therefore has length two and is isomorphic, after algebraic closure, to the dual numbers. The other 36 points have zero-dimensional tangent space and reduced length one. Total length: \(36+4\cdot2=44\).

Finally, complete enumeration over \(\mathbb F_5\) gives four lines, whereas every geometric line was already constructed over \(\mathbb F_{25}\). Frobenius thus has four fixed points and eighteen two-cycles, proving the closed-point census and zeta formula.

## Verification
Run `python verify.py` with SymPy 1.14 or a compatible 1.x release. It constructs \(\mathbb F_{25}\) exactly, enumerates all finite-field reduced-row-echelon lines, computes Gröbner-basis standard-monomial counts in all six cells, checks the full Grassmannian tangent ranks, computes the two local jet-quotient dimensions at all four exceptional points, and enumerates Frobenius cycles. The packaged `verify.stdout` ends with `VERIFY_OK`. All comparisons and ranks are exact, not floating point. The local-algebra inference uses the mathematical Nakayama argument above, not finite-field point-count extrapolation.

## Relationship to prior work
Veniani, *The maximum number of lines lying on a K3 quartic surface*, Example 7.6, writes the six-term polynomial displayed here and states that its reduction modulo five contains 48 lines. The present claim is a direct, equation-specific comparison: the complete reduced set has 40 points, and the Fano scheme has length 44. The discrepancy may reflect a transcription or intended-model issue; no conclusion about a different polynomial is drawn. Veniani's later *Lines on K3 quartic surfaces in characteristic 3* gives a distinct equation with 56 lines in characteristic five (Example 5.5), not this line-scheme classification. Classical quartic line bounds and other finite-field line configurations concern different objects and do not imply the specific Gröbner and local-structure computations established here.

## Limitations
The assertion is for the literal polynomial and characteristic five only; it does not invalidate independent geometric results about other quartics. The finite-field enumeration on its own would not prove geometric completeness; that conclusion requires the Gröbner-basis upper bounds and the tangent-space multiplicity argument. The local length calculation concerns the line Fano scheme, not singularity multiplicities of the quartic surface. Historical-priority verification is provisional, and no independent external audit has been performed.

## References
1. D. C. Veniani, *The maximum number of lines lying on a K3 quartic surface*, arXiv:1502.04510 (first posted 2015-02-16), Example 7.6. https://arxiv.org/abs/1502.04510 ; full text https://arxiv.org/html/1502.04510
2. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, Manuscripta Mathematica 167 (2022), 675–701, first published online 2021-02-07, especially Example 5.5. https://doi.org/10.1007/s00229-021-01284-9
