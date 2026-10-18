# Two transverse quadric types on the hollow symmetric determinant

## Finding
Let \(k\) be an algebraically closed field of characteristic different from \(2\). For every integer \(n\ge 5\), let \(H_n\) be the affine space of symmetric \(n\times n\) matrices with zero diagonal and arbitrary off-diagonal entries, and set \(N=\binom n2\). Write \(X_n\subset\mathbb P(H_n)=\mathbb P^{N-1}\) for the determinant-zero hypersurface. Define \(R_n\) to be its projective subvariety of matrices of rank at most \(n-2\), and \(L_i\) to be the projective linear subspace where the \(i\)-th row (equivalently column) vanishes.

**Theorem.** The hypersurface \(X_n\) is geometrically integral, normal and Gorenstein, and
\[
\operatorname{Sing}(X_n)_{\mathrm{red}}=R_n\cup L_1\cup\cdots\cup L_n.
\]
These are exactly its \(n+1\) distinct irreducible components. Their dimensions and codimensions are
\[
\begin{aligned}
\dim R_n&=N-4,&\operatorname{codim}_{X_n}R_n&=2,\\
\dim L_i&=\binom{n-1}{2}-1,&\operatorname{codim}_{X_n}L_i&=n-2.
\end{aligned}
\]
At every rank-\(n-2\) point of \(R_n\) having no zero row, the transverse formal hypersurface is the ordinary quadratic surface cone \(xy-z^2=0\). At every rank-\(n-1\) point of \(L_i\), its transverse formal hypersurface is a nondegenerate quadratic cone in \(n-1\) variables. Both statements use the completed local ring over \(k\); the smooth parameters along the relevant singular stratum are omitted.

Thus the rank-defect component has transverse Hessian rank \(3\), while each zero-row component has transverse Hessian rank \(n-1\). The two types reflect distinct singular mechanisms of a coordinate linear section of the symmetric determinant.

## Assumptions and scope
All statements concern \(n\ge5\) and algebraically closed \(k\) with \(\operatorname{char}k\ne2\). Rank refers to matrix rank over \(k\). The reduced singular locus is classified; no assertion about the primary decomposition or embedded structure of the Jacobian ideal is made. Projective dimensions count the quotient by simultaneous nonzero scalar multiplication.

The characteristic restriction is genuine: in characteristic \(2\), a zero-diagonal symmetric matrix is alternating. Its determinant is identically zero for odd \(n\), and for even \(n\) is the square of a Pfaffian, so the asserted reduced hypersurface picture does not apply. The small sizes \(n=3,4\) are also excluded, as the isotropic Gram parameterization of the corank-two locus need not have the same irreducibility behavior at \(n=4\).

## Proof
**1. Exact Jacobian criterion.** If \(A\in H_n\), for each independent coordinate \(a_{ij}=a_{ji}\) with \(i<j\), the derivative of \(\det A\) is \(2\operatorname{adj}(A)_{ij}\). At rank at most \(n-2\), the adjugate vanishes. At rank \(n-1\), the adjugate is \(c vv^{\mathsf T}\), where \(c\ne0\) and \(v\) spans \(\ker A\). Every off-diagonal derivative vanishes precisely when \(v_iv_j=0\) for every \(i<j\). As \(v\ne0\), this is equivalent to \(v\) being supported in exactly one coordinate. Equivalently one row of \(A\) is zero. Thus the claimed union is the set-theoretic singular locus once \(X_n\) is known to be reduced. In particular, away from the union there are rank-\(n-1\) smooth points.

**2. Irreducibility and dimension of \(R_n\).** Set \(r=n-2\ge3\) and let \(V\) be a nondegenerate quadratic space of dimension \(r\) over \(k\). Its affine isotropic cone \(Q=\{v\in V:\langle v,v\rangle=0\}\) is irreducible because its defining quadratic form has rank \(r\ge3\). The Gram morphism
\[
Q^n\longrightarrow H_n,\qquad (v_1,\ldots,v_n)\longmapsto(\langle v_i,v_j\rangle)_{i,j}
\]
has image exactly the affine rank-at-most-\(r\) locus: every symmetric matrix over an algebraically closed field of characteristic not two admits a factorization as a Gram matrix in an \(r\)-dimensional nondegenerate space if its rank is at most \(r\). Thus its image is closed, being precisely that rank locus, and irreducible.

On the dense open set where the vectors span \(V\), two Gram representations differ by an orthogonal transformation. The generic fiber therefore has dimension \(r(r-1)/2\). Since \(\dim Q=r-1\), the affine image has dimension
\[
n(r-1)-\frac{r(r-1)}2=\binom n2-3=N-3.
\]
It contains nonzero rank-\(r\) matrices without zero rows: choose any spanning collection of nonzero isotropic vectors (possible because the isotropic cone spans a nondegenerate space when \(r\ge3\)); the Gram matrix has rank \(r\), and no row can vanish since the vectors span \(V\). Projectivization gives \(\dim R_n=N-4\).

**3. The linear strata.** Each \(L_i\) is cut out by the \(n-1\) off-diagonal entries in row \(i\), hence has projective dimension \(N-(n-1)-1=\binom{n-1}{2}-1\). It has a dense open subset of rank \(n-1\): the complementary \((n-1)\times(n-1)\) hollow symmetric block may be taken as the matrix having zero diagonal and every off-diagonal entry \(1\), whose determinant is \((-1)^{n-2}(n-2)\) in characteristic zero. In arbitrary odd characteristic the same conclusion follows by choosing a generic invertible hollow block, for example a direct sum of nondegenerate \(2\times2\) blocks and, if the block order is odd, one nondegenerate \(3\times3\) hollow block (determinant \(2\)). Therefore no \(L_i\) lies in \(R_n\), and the \(L_i\) are pairwise distinct. Together with Step 2 and the Jacobian criterion, these exhaust the irreducible components of the reduced singular locus.

**4. Transverse quadrics on \(R_n\).** At a rank-\(n-2\) point with kernel \(K\) of dimension \(2\), the standard Schur-complement expansion gives, up to a unit, the determinant of a \(2\times2\) symmetric matrix on \(K\), whose linear term is the restriction of an arbitrary hollow symmetric perturbation to \(K\). The restriction map \(H_n\to\operatorname{Sym}^2K^*\) is surjective whenever \(K\) contains no coordinate vector. To prove this, suppose an element in its dual kernel existed. It would give a nonzero symmetric matrix on \(k^n\), of rank at most \(2\), with image contained in \(K\), and with all off-diagonal entries zero. A nonzero diagonal matrix of rank at most \(2\) has at least one coordinate vector in its image, contradicting the assumption on \(K\). But \(e_i\in K\) exactly when row \(i\) vanishes. Therefore, at every rank-\(n-2\) point with no zero row, the restricted normal determinant is the nondegenerate ternary quadratic \(xy-z^2\), with other local coordinates smooth. The Schur-complement coordinate change is formally invertible and yields the asserted completed-local-ring model.

**5. Transverse quadrics on \(L_i\).** At a rank-\(n-1\) point of \(L_i\), rearrange indices and write
\[
A=\begin{pmatrix}0&u^{\mathsf T}\\u&B\end{pmatrix},
\]
with \(B\) invertible and hollow. The exact block-determinant identity yields
\[
\det A=-\det(B)\,u^{\mathsf T}B^{-1}u.
\]
The coordinates of \(u\) are precisely the independent directions normal to \(L_i\). Since \(B^{-1}\) is symmetric nondegenerate and \(2\) is invertible, a formal linear change of \(u\) over the completed local ring diagonalizes this quadratic form, with \(B\) varying as smooth parameters. The transverse Hessian has rank \(n-1\).

**6. Geometric integrality and normality.** The homogeneous determinant on \(H_n\) is nonzero, since an invertible hollow matrix exists in every order at least \(2\) in odd characteristic by the block construction of Step 3. The hypersurface has smooth points (for instance a direct sum of a rank-two hollow \(3\times3\) path block and an invertible hollow block of order \(n-3\)); its kernel has two nonzero coordinates, so a gradient derivative is nonzero by Step 1. The singular locus found above has codimension at least \(2\) inside the hypersurface. If the determinant had multiple irreducible factors, the respective projective hypersurface components would intersect in codimension \(1\) inside \(X_n\) (and any repeated factor would be singular at its general point), a contradiction. Thus it is irreducible and squarefree, so \(X_n\) is integral. Hypersurfaces are Cohen–Macaulay, hence satisfy \(S_2\); codimension-at-least-two singularities imply \(R_1\), giving normality by Serre's criterion. Finally every projective hypersurface is Gorenstein.

## Verification
The companion `verify.py` is self-contained and uses exact rational arithmetic. It checks explicit rank-\(n-2\), zero-row rank-\(n-1\), and smooth rank-\(n-1\) witnesses for \(n=5,6\), including all off-diagonal determinant derivatives and the full Hessian ranks. It also checks the all-ones-off-diagonal determinant formula for orders \(5\) through \(10\). Run with `python verify.py`; expected terminal marker `VERIFY_OK`. These tests are not the proof for arbitrary \(n\), which is supplied above.

## Relationship to prior work
Symmetric determinantal varieties, their linear sections, and their rank strata are classical; the rank-drop part of this singular-locus description is familiar from the unrestricted determinant. The new distinction is the extra \(n\) row-vanishing components produced by imposing **all** diagonal entries zero, their complete irreducible-component count for \(n\ge5\), and the two simultaneous transverse quadratic types. The exact claim is specific to the hollow (zero-diagonal) linear section and is not a classification of arbitrary sparse symmetric matrices.

Nie–Ranestad–Sturmfels (2006) examine rank loci in linear spaces of symmetric matrices for semidefinite programming, but do not give this hollow all-rank component decomposition. Huang (2013) studies singularities of **multilinear determinantal forms** attached to symmetric matrices, a different ambient parameter space. Cunha–Ramos–Simis (2018) study a diagonal-cloning degeneration and zeros in a triangular corner, rather than zeroing the entire main diagonal. Conca–Welker (2018) and Deng–Kretschmer (2022) treat coordinates zeroed at **off-diagonal** positions while diagonal entries remain variables; the latter studies submaximal-minor ideals rather than the present Jacobian of a determinant with forced-zero diagonal. These distinctions are substantive, not evidence of impossibility of an equivalent treatment elsewhere.

## Limitations
No claim is made that the Jacobian singular scheme is reduced, that all singular points have ordinary-double-point transverse type, or that the small-size cases satisfy the component formula. The proof applies in every characteristic other than two. The mathematical originality assessment cannot rule out an unindexed treatment under the language of graph adjacency determinants or specialized coordinate sections. General algebraic-geometry results on determinants are used; no independent review is claimed.

## References
- J. Nie, K. Ranestad, B. Sturmfels, *The algebraic degree of semidefinite programming*, arXiv:math/0611562, first posted 2006-11-19, https://arxiv.org/abs/math/0611562.
- J. Huang, *Determinantal hypersurface from a geometric perspective*, PhD thesis, Caltech, 2013, https://thesis.caltech.edu/7656/01/52.pdf.
- R. Cunha, Z. Ramos, A. Simis, *Symmetry preserving degenerations of the generic symmetric matrix*, arXiv:1802.08067, first posted 2018-02-20, https://arxiv.org/html/1802.08067v2.
- A. Conca, V. Welker, *Lovász–Saks–Schrijver ideals and coordinate sections of determinantal varieties*, arXiv:1801.07916, first posted 2018-01-24, https://arxiv.org/abs/1801.07916.
- J. Deng, A. Kretschmer, *Ideals of submaximal minors of sparse symmetric matrices*, arXiv:2211.07020, first posted 2022-11-13, https://arxiv.org/abs/2211.07020.
