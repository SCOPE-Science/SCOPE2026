# Grassmannian reconstruction and uniform nodal germs of cyclic Jacobi determinant hypersurfaces

## Finding
For each integer \(n\ge4\), let \(V_n\) be the vector space of complex symmetric \(n\times n\) matrices with possibly nonzero entries only on the diagonal and the edges of the cycle \(C_n\). Write the diagonal entries as \(a_i\) and the cyclic edge entries \(A_{i,i+1}=A_{i+1,i}=b_i\), with indices modulo \(n\), and put \(H_n=V(\det A)\subset\mathbb P(V_n)\cong\mathbb P^{2n-1}\). Consider the full-edge open subset \(T_n=\{[A]\in H_n:b_1\cdots b_n\ne0\}\).

**Theorem.** The singular locus of \(T_n\), with its reduced scheme structure, is algebraically isomorphic, by \([A]\mapsto\ker A\), to
\[
U_n=\bigl\{K\in\operatorname{Gr}(2,n):p_{12}p_{23}\cdots p_{n-1,n}p_{n,1}\ne0\bigr\}.
\]
In particular this singular locus is nonempty, smooth, irreducible, rational, and of dimension \(2n-4\); it is affine, and its canonical bundle is trivial. Moreover, **at every closed point** \(q\) of this locus,
\[
\widehat{\mathcal O}_{H_n,q}\simeq
\mathbb C[[u,v,w,t_1,\ldots,t_{2n-4}]]/(uw-v^2).
\]
Thus the full-edge singular scheme is reduced, and all its points have transverse ordinary-double-point type and multiplicity two. Any singular points in the boundary \(\{b_1\cdots b_n=0\}\) have ambient codimension at least four, so this is the unique top-dimensional irreducible singular stratum.

The inverse to the kernel map is explicit. For an oriented basis \((x,y)\) of \(K\), let \(p_{ij}=x_i y_j-x_j y_i\), and set \(e_i=p_{i,i+1}\), including \(e_n=p_{n,1}\). Then the matrix with
\[
b_i=e_i^{-1},\qquad a_i=-\frac{p_{i-1,i+1}}{e_{i-1}e_i}
\]
has kernel exactly \(K\). These formulas are projectively independent of the chosen basis.

## Assumptions and scope
The ground field is \(\mathbb C\); all indices are interpreted cyclically. For \(n\ge4\) the \(2n\) matrix coordinates are independent. The scheme-theoretic assertion concerns the open set where every cycle edge is nonzero. No classification of local germs on the zero-edge boundary, nor of possible lower-dimensional singular components entirely in that boundary, is asserted. The result is an algebraic isomorphism of reduced singular loci, not a claim that the original hypersurface is globally smooth or that its entire singular locus is irreducible.

## Proof
**(1) The singular points.** At a matrix of corank at least two, the adjugate vanishes, so all first derivatives of \(\det A\) vanish. If \(A\) has corank one, its adjugate has the form \(czz^{\mathsf T}\) for a nonzero vector \(z\) and scalar \(c\ne0\). The derivatives with respect to the independent diagonal coordinates are \(c z_i^2\). They cannot all vanish in characteristic zero. Thus \(H_n\) is nonsingular at every corank-one point, and its full-edge singular locus consists exactly of full-edge matrices of corank at least two.

**(2) Nullity bound and nonvanishing Pluecker coordinates.** When all \(b_i\ne0\), the equation \(Az=0\) propagates by the second-order recurrence \(b_i z_{i+1}=-a_i z_i-b_{i-1}z_{i-1}\). Hence any solution is determined by two adjacent coordinates. The kernel has dimension at most two, and if its dimension is two, evaluation at any adjacent pair is an isomorphism. For any basis \((x,y)\) of this kernel, this proves \(e_i=p_{i,i+1}\ne0\) for every \(i\).

**(3) Reconstruction and algebraicity.** With \(x,y\) viewed as two solutions, take their oriented two-by-two minors \(p_{ij}\). The two equations obtained by taking determinants of \(b_{i-1}(x_{i-1},y_{i-1})+a_i(x_i,y_i)+b_i(x_{i+1},y_{i+1})=0\) with the middle and last row vectors give
\[
b_{i-1}e_{i-1}=b_i e_i=c,\qquad
 a_i=-c\,p_{i-1,i+1}/(e_{i-1}e_i).
\]
Thus any full-edge corank-two matrix with kernel \(K\) is projectively unique. Conversely, given \(K\in U_n\), these formulas with \(c=1\) define a symmetric cycle matrix. The three-term Pluecker identity for any three vectors in \(\mathbb C^2\) shows that the columns of a basis for \(K\) are in its kernel. As every edge is nonzero, the recurrence bound forces its kernel to be exactly \(K\). Changing the basis by \(g\in\operatorname{GL}_2\) multiplies every \(p_{ij}\) by \(\det g\), and hence multiplies every matrix coordinate by the same nonzero scalar \((\det g)^{-1}\). The inverse map is therefore well defined. Multiplication by \(\prod_i e_i\) makes all its projective coordinates homogeneous polynomial expressions in Pluecker coordinates of equal degree, regular on \(U_n\). The kernel map is regular on a constant-rank locus (for instance by nonvanishing minors), so the two constructions are mutually inverse morphisms.

**(4) Geometry.** The Grassmannian \(\operatorname{Gr}(2,n)\) is smooth, irreducible, rational, of dimension \(2(n-2)\). Its nonempty open subset \(U_n\) inherits these properties. The complement of \(U_n\) is the support of the effective ample divisor \(\sum_i V(e_i)\), hence \(U_n\) is affine. Since \(K_{\operatorname{Gr}(2,n)}\cong\mathcal O(-n)\) in the Pluecker polarization and \(e_1\) trivializes \(\mathcal O(1)\) on \(U_n\), its canonical bundle is trivial.

**(5) Uniform transverse double points.** Fix any full-edge corank-two matrix \(A\) and its two-dimensional kernel \(K\). Choose a complementary nondegenerate \((n-2)\)-dimensional summand, and use the symmetric Schur complement \(S(A')\in\operatorname{Sym}^2(K^*)\) in a neighborhood of \(A\). There \(\det A'=\det B(A')\det S(A')\), with \(\det B\) a unit. The differential of \(S\) at \(A\) is the restriction map from allowed symmetric matrix variations to \(\operatorname{Sym}^2(K^*)\). Choose two adjacent indices \(i,i+1\); their evaluation rows \(q_i,q_{i+1}\in K^*\) are independent by step (2). Varying \(a_i,a_{i+1},b_i\) gives the three quadratic forms \(q_i^2,q_{i+1}^2,2q_iq_{i+1}\), a basis of \(\operatorname{Sym}^2(K^*)\). Therefore the three entries \((u,v,w)\) of \(S\) extend to formal regular coordinates transverse to \(U_n\), in which the defining equation is a unit times \(uw-v^2\). The Jacobian ideal is formally \((u,v,w)\), so the full-edge Jacobian singular scheme is reduced, with the claimed completed local ring at **every** point of \(U_n\).

**(6) Boundary dimension bound.** If exactly one edge vanishes, the matrix is a single nondegenerate-edge path matrix, whose nullity is at most one by the recurrence argument. If \(k\ge2\) edges vanish, the matrix splits into \(k\) path blocks, each with nonzero internal edges and nullity at most one. Corank at least two requires at least two block determinants to vanish. Since these determinants use disjoint sets of diagonal variables and each is a nonzero, nonconstant polynomial, the corresponding boundary strata have ambient codimension at least \(k+2\ge4\). The full-edge stratum has codimension three; it is therefore the unique largest-dimensional irreducible component of the singular support.

## Verification
The standalone `CHECKER.py` tests the Pluecker inverse formulas using exact integer and rational arithmetic for 84 independently generated kernel planes in dimensions \(4\le n\le9\). For every sample it reconstructs the symmetric cycle matrix, verifies its corank is exactly two, recovers the matrix projectively from its computed nullspace, and checks that the three chosen normal quadratic forms are linearly independent. `CHECKER_OUTPUT.txt` contains the reproducible output. These finite checks are not substituted for the proofs for all \(n\).

## Relationship to prior work
Morier-Genoud, Ovsienko, Schwartz and Tabachnikov study normalized periodic second-order difference equations, frieze patterns and Grassmannian embeddings [1], especially Proposition 3.2.1. Their Grassmannian image obeys **equality** of consecutive Pluecker minors and has dimension \(n-3\), rather than the full nonvanishing-minor open subset \(U_n\) of dimension \(2n-4\). Their work gives important surrounding motivation but not this kernel reconstruction of symmetric sparse determinants or its uniform nodal local equations. Sexton [2] studies minimum ranks with prescribed diagonal patterns on paths and cycles; only the abstract was accessible for comparison. Scott [3] describes Grassmannian cluster structures, without stating the symmetric-cycle-matrix reconstruction in the accessible material. A published treatment of the four-coordinate complement of \(\operatorname{Gr}(2,4)\) [4] determines its product and topology; this handles one instance of \(U_n\) as a Grassmannian open set, but not the identification with the cycle-matrix singular locus or the transverse singularities. The new claim is those isomorphisms and germs, not the standard underlying Grassmannian geometry.

## Limitations
The result concerns the full-edge open locus and provides no complete boundary singularity classification. Existing literature on frieze patterns and minimum rank may contain an equivalent specialization under a different normalization; this remains a historical novelty risk, especially where original full text was inaccessible. The calculation gives formal completed local equations over \(\mathbb C\), not canonical global simultaneous coordinates. No independent mathematical audit is claimed.

## References
[1] S. Morier-Genoud, V. Ovsienko, R. E. Schwartz, S. Tabachnikov, *Linear difference equations, frieze patterns and combinatorial Gale transform*, arXiv:1309.3880v1 (first public 2013-09-16), published *Forum of Mathematics, Sigma* 2 (2014), e22, DOI:10.1017/fms.2014.20; particularly Sections 2, 3 and 6.

[2] W. N. Sexton, *The Minimum Rank of Schemes on Graphs*, Brigham Young University thesis (2014-03-01), https://scholarsarchive.byu.edu/etd/4402/ .

[3] J. S. Scott, *Grassmannians and Cluster Algebras*, arXiv:math/0311148v1 (2003-11-10), *Proceedings of the London Mathematical Society* 92 (2006), 345–380.

[4] *Product structure and integral topology of the four-cycle Schubert complement*, published mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-product-structure-and-integral-topology-of-the-four-cycle-schube--1dab3c8e8faa/RESULT.md .
