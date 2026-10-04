# Higher triple lines are the reduced second-type singular locus on the Fermat cubic fourfold
## Finding
For the Fermat cubic fourfold \(X=V(x_0^3+\cdots+x_5^3)\subset\mathbf P^5_{\mathbf C}\), let \(F_2(X)\) be the locus of lines of second type and let \(\mathrm{HTL}(X)\) denote the higher triple lines in the sense of Zhang. Then, set-theoretically,
\[
\mathrm{HTL}(X)=\operatorname{Sing}(F_2(X)_{\mathrm{red}}).
\]
This common locus is the union of exactly \(180\) smooth Fermat plane cubics. Its only mutual intersections are exactly \(405\) points of the line parameter space. Each such point represents a line joining two Eckardt points with disjoint two-coordinate supports; exactly four elliptic components pass through it, and every elliptic component contains exactly \(9\) such points.

Equivalently, the normalization of the reduced higher-triple-line locus is a disjoint union of \(180\) Fermat elliptic curves.

## Assumptions and scope
Work over \(\mathbf C\). The Fermat cubic fourfold is
\[
X=\{x_0^3+x_1^3+x_2^3+x_3^3+x_4^3+x_5^3=0\}\subset\mathbf P^5.
\]
The statement concerns the underlying reduced second-type locus. It does not assert the scheme-theoretic multiplicity of \(F_2(X)\), the local analytic singularity type at the intersections, or transversality of the elliptic branches.

A line of second type is called a higher triple line using Zhang's Definition 2.5: in the normal form of a second-type line, the columns of the matrix of linear forms \(S\) are linearly dependent over the ground field. The proof below identifies that condition on every irreducible component of the Fermat second-type locus.

## Proof
Gounelas and Kouvidakis describe \(F_2(X)_{\mathrm{red}}\) as exactly \(55\) smooth irreducible components: \(45\) Fermat cubic surfaces and \(10\) products of two Fermat plane cubics. Their description can be phrased in coordinate-support language. A second-type line is represented by a two-dimensional vector space spanned by points with disjoint coordinate supports. The relevant support splittings are of type \(2+4\) and \(3+3\).

For a \(2+4\) splitting, the two-coordinate endpoint is an Eckardt point. There are \(\binom{6}{2}\cdot3=45\) such endpoints, because for each coordinate pair the Fermat equation has three projective solutions. The complementary four coordinates trace the corresponding Fermat cubic surface. For a \(3+3\) splitting there are \(\binom{6}{3}/2=10\) unordered partitions, and the two endpoints trace a product of two Fermat plane cubics.

The explicit support descriptions also determine where distinct components meet. A line belongs to more than one of the \(55\) components exactly when at least one ambient coordinate vanishes identically on the line: the zero coordinate can be reassigned across two admissible support blocks, while a line with all six ambient coordinates represented in its two support blocks determines a unique block splitting. Since every one of the \(55\) components is smooth, a point lying on only one component is smooth on the reduced union. A point lying on at least two distinct components is singular, because a regular local ring is a domain whereas the reduced local union has at least two minimal branches. Thus
\[
\operatorname{Sing}(F_2(X)_{\mathrm{red}})
=\{[L]\in F_2(X):\text{some coordinate vanishes identically on }L\}.
\]

It remains to compare this with Zhang's higher-triple condition. Let \(L=\langle p,q\rangle\) be a line in one of the block components, with disjoint support blocks \(A\) and \(B\). The quadratic part of the cubic normal to \(L\) splits according to these blocks. Modulo the line directions, Zhang's pencil represented by \(S\) is block diagonal:
\[
s\,II_p\oplus t\,II_q,
\]
where \(II_p\) and \(II_q\) are the second fundamental forms of the corresponding Fermat factors. Therefore the columns of \(S\) have a constant linear dependence exactly when one of these block second fundamental forms is degenerate.

For a Fermat factor
\[
G(z_1,\ldots,z_r)=z_1^3+\cdots+z_r^3,
\]
the Hessian matrix is diagonal with entries \(6z_i\), so
\[
\det\operatorname{Hess}(G)=6^r\prod_{i=1}^r z_i.
\]
For the nontrivial block sizes \(r=3\) and \(r=4\), the induced projective second fundamental form degenerates precisely on the Hessian section, hence precisely when a coordinate of that block is zero. The two-coordinate Eckardt factor has zero-dimensional projective tangent quotient and introduces no additional condition. Consequently
\[
[L]\in\mathrm{HTL}(X)
\quad\Longleftrightarrow\quad
\text{some coordinate vanishes identically on }L.
\]
Combining this with the previous characterization proves
\[
\mathrm{HTL}(X)=\operatorname{Sing}(F_2(X)_{\mathrm{red}})
\]
set-theoretically.

The component count is now combinatorial. A generic higher triple line has exactly one identically zero coordinate and therefore has actual nonzero support sizes \(2+3\). Choose the two-coordinate Eckardt endpoint in \(45\) ways and choose the zero coordinate among its four complementary coordinates. This gives
\[
45\cdot4=180
\]
irreducible higher-triple curves. On each, the moving endpoint is a Fermat plane cubic, so every component is a smooth elliptic curve. The same count is visible from the \(10\) product components, each of which contains \(18\) vertical or horizontal Fermat cubic branches of the higher-triple locus.

Two such elliptic components meet only when a second coordinate vanishes identically. Then the line has support type \(2+2\) and joins two Eckardt points on disjoint coordinate pairs. Choose the unordered pair of disjoint coordinate pairs and the two cubic-root labels:
\[
\frac{\binom{6}{2}\binom{4}{2}}{2}\cdot3^2=45\cdot9=405.
\]
For a fixed elliptic component, the moving Fermat cubic meets its coordinate triangle in \(3\cdot3=9\) points, so it contains exactly \(9\) deep points. Conversely, each deep line admits four choices of which one of its two zero coordinates is assigned to which adjacent \(2+3\) branch, so exactly four elliptic components pass through it. The incidence check
\[
180\cdot9=405\cdot4
\]
confirms both counts. A third vanishing coordinate would force one endpoint to have support of size at most one, which cannot lie on a Fermat cubic, so there is no deeper stratum and no other component intersection.

## Verification
The accompanying script `artifacts/verify_fermat_htl.py` independently checks the finite parts of the argument. It symbolically computes
\[
\det\operatorname{Hess}(z_1^3+z_2^3+z_3^3)=216z_1z_2z_3
\]
and
\[
\det\operatorname{Hess}(z_1^3+z_2^3+z_3^3+z_4^3)=1296z_1z_2z_3z_4,
\]
then enumerates the \(45\) cubic-surface components, \(10\) product components, \(180\) elliptic higher-triple components, and \(405\) deep points. It also verifies that every higher-triple curve lies on one cubic-surface component and one product component, that each cubic-surface component contains \(4\) such curves, each product component contains \(18\), each curve contains \(9\) deep points, and each deep point lies on \(4\) curves. The recorded run terminates with `VERIFY_OK`.

The infinite-geometric step is the block-Hessian equivalence in the proof; the finite script is a check of the Hessian formulas and incidence arithmetic, not a substitute for that argument.

## Relationship to prior work
Zhang introduced higher triple lines, proved the Hessian description for higher triple lines through an Eckardt point, and explicitly asked how higher triple lines relate to singularities of \(F_2(X)\) in dimension at least four. For the Fermat cubic fourfold, Zhang noted at least \(45\) one-parameter families of higher triple lines.

Gounelas and Kouvidakis determined the complete reduced second-type locus of the Fermat cubic fourfold: \(45\) Fermat cubic surfaces and \(10\) products of Fermat plane cubics, and noted that this locus is singular and non-normal. Their component classification does not identify its singular locus with Zhang's higher triple lines or give the \(180\)-curve and \(405\)-point incidence refinement above.

The result here combines those two structures with the block-Hessian criterion to give a complete special-case answer to Zhang's question for the Fermat cubic fourfold.

## Limitations
The equality is set-theoretic for the reduced second-type locus. No assertion is made about the nonreduced scheme structure of \(F_2(X)\), branch multiplicities, local analytic equations at the \(405\) deep points, or whether the four branches meet transversely. The originality check found no prior statement of the equality or the \(180/405\) incidence description in the sources inspected, but literature search cannot logically prove nonexistence of an independently discovered equivalent formulation.

## References
1. Y. Zhang, *Hilbert Scheme of a Pair of Skew Lines on Cubic Hypersurfaces*, arXiv:2501.01682v1, 3 January 2025; revised version 18 April 2025. https://arxiv.org/abs/2501.01682
2. F. Gounelas and A. Kouvidakis, *The Fermat cubic and monodromy of lines*, arXiv:2302.09562v1, 19 February 2023; *New York Journal of Mathematics* 31 (2025), 650--667. https://arxiv.org/abs/2302.09562
3. F. Gounelas, *The universal cover of the second-type locus of a cubic*, arXiv:2608.08909v1, 9 August 2026. https://arxiv.org/abs/2608.08909
