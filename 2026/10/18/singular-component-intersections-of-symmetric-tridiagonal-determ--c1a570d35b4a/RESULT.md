# Singular-component intersections of symmetric tridiagonal determinant hypersurfaces

## Finding
Let \(k\) be an algebraically closed field of characteristic zero, and let \(n\ge3\). Let \(T_n\) be the generic symmetric tridiagonal \(n\times n\) matrix with diagonal coordinates \(a_1,\ldots,a_n\), off-diagonal coordinates \(b_1,\ldots,b_{n-1}\), and zeros elsewhere. Define the degree-\(n\) projective hypersurface
\[
 X_n=V(\det T_n)\subset\mathbb P^{2n-2}_k.
\]
For each \(1\le i<n\), write \(T_{[p,q]}\) for the principal contiguous block on rows and columns \(p,\ldots,q\), and put
\[
 Z_i=V\bigl(b_i,\det T_{[1,i]},\det T_{[i+1,n]}\bigr).
\]
Then \(X_n\) is geometrically integral and normal, and its **reduced singular locus** is exactly \(\bigcup_{i=1}^{n-1}Z_i\). These are precisely its \(n-1\) distinct irreducible components. Each \(Z_i\) is a reduced complete intersection of dimension \(2n-5\) and degree \(i(n-i)\); generically its transverse hypersurface singularity is the ordinary two-dimensional node \(uv-w^2=0\).

For **every nonempty** \(S\subseteq\{1,\ldots,n-1\}\), set \(p=\min S\) and \(q=\max S\). The scheme-theoretic intersection of these *reduced components* in projective space is
\[
 \bigcap_{i\in S} Z_i
 = V\bigl(\{b_j:j\in S\},\det T_{[1,p]},\det T_{[q+1,n]}\bigr).
\]
It is reduced, irreducible, and a complete intersection, with
\[
 \dim\Bigl(\bigcap_{i\in S}Z_i\Bigr)=2n-4-|S|,
 \qquad \deg\Bigl(\bigcap_{i\in S}Z_i\Bigr)=p(n-q).
\]
Thus every nonempty selection of components intersects: their intersection nerve is the full simplex on \(n-1\) vertices. In particular the reduced singular locus has projective degree
\[
 \sum_{i=1}^{n-1}i(n-i)=\binom{n+1}{3}.
\]
The total degree agrees with the classical codimension-three symmetric rank-drop degree; the structural decomposition and intersection formulas are the substantive refinement.

## Assumptions and scope
All statements concern \(n\ge3\) and algebraically closed \(k\) of characteristic zero. All subschemes use the standard homogeneous coordinates \(a_1,\ldots,a_n,b_1,\ldots,b_{n-1}\) on \(\mathbb P^{2n-2}\). The scheme-theoretic intersection assertion refers to the already reduced components \(Z_i\), **not** to a claim that the Jacobian singular scheme itself is reduced. The empty block has determinant one, although the displayed components only involve nonempty end blocks.

## Proof
**1. Irreducible block determinants.** Let \(K_m\) be the determinant of a generic symmetric tridiagonal block of length \(m\), with \(K_0=1\) and \(K_1=a_1\). Expansion in the final row gives
\[
 K_m=a_mK_{m-1}-b_{m-1}^2K_{m-2}.
\]
Inductively \(K_{m-1}\) is irreducible and coprime to \(b_{m-1}^2K_{m-2}\): the variable \(b_{m-1}\) is new and \(K_{m-2}\) has smaller total degree than \(K_{m-1}\). Hence the displayed primitive degree-one polynomial in \(a_m\) is irreducible by Gauss's lemma. This also handles \(m=2\) starting from \(K_1=a_1\). The argument is valid for each contiguous block. Thus \(X_n\) is integral.

**2. No accidental singularities.** The derivative of \(F=\det T_n\) with respect to the diagonal entry \(a_j\) is the \((j,j)\) cofactor. At a corank-one symmetric matrix over \(k\), its adjugate has the form \(c vv^{\mathsf T}\) for some nonzero \(c\) and nonzero kernel vector \(v\). Some diagonal entry \(cv_j^2\) is nonzero. Consequently the projective gradient of \(F\) is nonzero at every corank-one point of \(X_n\); conversely all cofactors and all first derivatives vanish when the corank is at least two. Therefore the singular support is exactly the corank-at-least-two locus.

**3. The cut decomposition.** At any point, deleting all edges \(b_i=0\) splits \(T_n\) into maximal contiguous tridiagonal blocks with all internal off-diagonal entries nonzero. A block of this kind has nullity at most one: its first row determines the second kernel coordinate from the first, and successive rows propagate all coordinates uniquely. Thus the entire matrix has corank at least two precisely when at least two distinct blocks have determinant zero. There is then a zero edge separating two such blocks, and the determinants on both sides of that cut vanish. Conversely these three vanishing conditions force at least one zero eigenvalue on each side. Hence
\[
 \operatorname{Sing}(X_n)_{\mathrm{red}}=\bigcup_{i=1}^{n-1}Z_i
\]
set-theoretically, and the reduced scheme is this union of distinct integral components.

**4. Components and their intersections.** Imposing \(b_i=0\) produces a block diagonal matrix, so \(Z_i\) is cut out by that linear equation and two homogeneous block determinants of degrees \(i\) and \(n-i\). The two determinants involve disjoint variables and define geometrically integral affine cones by Step 1. Their product with unused affine coordinate directions is integral, giving an irreducible reduced homogeneous complete intersection. Thus \(\dim Z_i=2n-5\) and \(\deg Z_i=i(n-i)\).

For an arbitrary nonempty set \(S=\{i_1<\cdots<i_s\}\), first impose all \(b_{i_r}=0\). The matrix decomposes into \(s+1\) consecutive blocks. The equations of \(Z_{i_1}\) force the first block determinant to vanish, and those of \(Z_{i_s}\) force the last block determinant to vanish. Once these end determinants vanish, every other left- or right-of-cut determinant appearing among the defining ideals of \(Z_{i_r}\) automatically vanishes because it contains one of those end blocks as a direct summand. This proves the **equality of ideals after imposing the cut variables**, not just equality of point sets. The first and last determinant equations are again in disjoint variable sets and are irreducible; together with the \(s\) independent linear cut equations they form a prime complete intersection. Its codimension in \(\mathbb P^{2n-2}\) is \(s+2\), yielding the asserted dimension and degree \(i_1(n-i_s)\). Nonemptiness follows explicitly, for example by choosing the first and last diagonal entries zero with all other entries zero except a nonzero middle entry, or by choosing nonzero coordinates in an allowed block after the two determinant conditions; for \(n\ge3\) the linear subspace of choices is nontrivial. All subsets therefore appear in the intersection nerve.

**5. Generic transverse nodes and normality.** Fix a cut after position \(i\), and write \(r=n-i\). Choose all internal off-diagonals equal to one. Set the diagonal entries on the left to \(2,\ldots,2,(i-1)/i\), and those on the right to \((r-1)/r,2,\ldots,2\); put the cut entry \(b_i=0\). The determinant of a length-\(m\) tridiagonal block with all diagonal entries two and off-diagonals one is \(m+1\). It follows that both chosen blocks have rank one below full rank, with the relevant end cofactors equal to \(i\) and \(r\), respectively. Vary the last left diagonal coordinate by \(u\), the first right coordinate by \(v\), and the cut coordinate by \(w\). The exact determinant on this transverse slice is
\[
 \det T_n=ir(uv-w^2).
\]
This gives a nondegenerate surface node at the displayed smooth point of \(Z_i\). Since the end cofactors remain nonzero on a dense open of \(Z_i\), the same transverse ordinary-double-point type holds generically. Finally, all singular components have codimension two inside the integral hypersurface \(X_n\). A hypersurface is Cohen--Macaulay, hence satisfies \(S_2\), while the codimension-two singular locus gives \(R_1\); Serre's criterion proves normality.

Summing the complete-intersection degrees gives \(\sum_{i=1}^{n-1}i(n-i)=n(n-1)(n+1)/6\), as asserted.

## Verification
The standalone file `checker.py` uses integer and rational exact arithmetic. It exhaustively checks all nonzero coefficient vectors over \(\mathbb F_3\) for \(n=3,4,5\), comparing the Jacobian criterion, matrix corank and the cut-union criterion. It separately tests every nonempty cut-subset intersection over those finite fields, symbolically verifies determinant factorization identities and irreducibility for sizes \(2\) through \(6\), and checks the explicit transverse-node slices for sizes \(3\) through \(9\). It also samples larger order-six and order-seven matrices over \(\mathbb F_5\). The completed checker prints `VERIFY_OK`. The full all-parameter result rests on the foregoing symbolic proof, not on the finite tests.

## Relationship to prior work
Continuant recurrences and determinant splitting identities are classical and are not claimed as new. Piontkowski's study of symmetric determinantal hypersurfaces records the generic corank-two degree \(\binom{n+1}{3}\), and Kerner--Vinnikov provide a broad framework for symmetric determinant representations and their singularities. The present special linear subspace has **reducible** singular support and a complete cut-indexed scheme-intersection arrangement, neither supplied by their inspected statements. Huang's results on *generic symmetric determinantal multilinear forms* address a different family and an irreducibility statement, not this special tridiagonal family. Benito and collaborators study singularities of cluster algebras using fixed-off-diagonal continuants, explicitly setting their off-diagonal entries equal to minus one; their smoothness and cluster singularity results do not classify the homogeneous hypersurface with independent edge coordinates here. The existing general rank-drop condition is used as a lemma rather than asserted as novel. Potential implicit consequences of broader matrix-rank and continuant theory remain to be assessed independently.

## Limitations
The claim concerns the reduced singular support and *scheme-theoretic intersections of its reduced irreducible components*, not the possible embedded or nonreduced structure of the Jacobian singular scheme. Only generic transverse singularities along components are determined, not every analytic germ on component intersections. The base field is algebraically closed of characteristic zero. The theorem concerns path-pattern symmetric matrices and does not claim an arbitrary tree or graph extension. Bibliographic comparisons identify no explicit statement of the full cut-intersection theorem, but absence from searched sources is not a proof of universal novelty; implicit or unindexed coverage remains possible.

## References
1. D. Kerner and V. Vinnikov, *Determinantal representations of singular hypersurfaces in projective space*, arXiv:0906.3012 (first public preprint 2009-06-16), https://arxiv.org/abs/0906.3012.
2. J. Piontkowski, *Linear Symmetric Determinantal Hypersurfaces*, preprint/PDF, https://www.math.uni-duesseldorf.de/~piontkow/det.pdf, especially Proposition 1.5 on the generic symmetric rank-drop degree.
3. J. Huang, *Determinantal Hypersurface from a Geometric Perspective*, Ph.D. thesis, Caltech (2013), https://thesis.caltech.edu/7656/.
4. A. Benito et al., *Classification of singularities of cluster algebras of finite type: the case of trivial coefficients*, Glasgow Mathematical Journal, Section 3, https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/classification-of-singularities-of-cluster-algebras-of-finite-type-the-case-of-trivial-coefficients/CE916C74775FB8EAB2D048160998F672.
5. E. W. Weisstein, *Continuant*, MathWorld, https://mathworld.wolfram.com/Continuant.html.
