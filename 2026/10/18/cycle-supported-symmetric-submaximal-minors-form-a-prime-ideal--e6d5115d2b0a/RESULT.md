# Cycle-supported symmetric submaximal minors form a prime ideal

## Finding
For each integer \(n\ge4\), let \(C_n\) be the simple cycle. Let \(A_n\) be the symmetric matrix whose diagonal coordinates are \(a_1,\ldots,a_n\), whose cyclic successive off-diagonal coordinates are \(b_1,\ldots,b_n\), and whose remaining entries are zero. Write \(I_n\) for the ideal of **all** \((n-1)\)-minors in the polynomial ring \(S_n=k[a_1,\ldots,a_n,b_1,\ldots,b_n]\).

**Theorem.** Over any algebraically closed field \(k\) of characteristic zero, the ideal \(I_n\) is prime for all \(n\ge4\). The projective variety \(Y_n=\operatorname{Proj}(S_n/I_n)\subset\mathbb P^{2n-1}\) has dimension \(2n-4\) and contains a dense open subset canonically isomorphic to
\[
U_n=\bigl\{K\in\operatorname{Gr}(2,n):p_{i,i+1}(K)\ne0\text{ for all cyclic }i\bigr\}.
\]
Thus \(Y_n\) is birational to \(\operatorname{Gr}(2,n)\). It is exactly the reduced singular support of the irreducible sparse determinant hypersurface \(H_n=V(\det A_n)\). Along the dense open subset its transverse analytic hypersurface singularity is an ordinary \(A_1\) surface node \(xy-z^2=0\). In particular the infinite family of cycles satisfies the sufficient-direction assertion of Question 16 in Deng--Kretschmer [3]. The stronger assertion for *all* 2-connected graphs is **not** established here.

The codimension-three Cohen--Macaulay property, reducedness of \(I_n\), and degree \(\binom{n+1}{3}\) were already proved for every connected graph in [3, Theorem 1 and Proposition 12]. They are used as prior results, not originality claims.

## Assumptions and scope
The cycle indices are interpreted modulo \(n\). The \(2n\) indicated variables are independent; this is the intrinsic sparse coordinate polynomial ring, so there are no extraneous variables corresponding to absent graph edges. A point has matrix corank at least two if and only if it lies in \(V(I_n)\). A Plücker coordinate \(p_{ij}(K)\) is the determinant of rows \(i,j\) of any basis matrix for a two-plane \(K\); its nonvanishing is independent of the chosen basis. The characteristic-zero assumption is retained for the analytic \(A_1\) description. The irreducibility argument for the reduced variety uses only elementary rank geometry and works over algebraically closed fields in arbitrary characteristic, while the final ideal-theoretic primality invokes radicality in [3].

## Proof
**1. Dense-edge locus and its kernel parameter.** Let \(T\subset\mathbb A^{2n}\) be the open subset where every \(b_i\ne0\). For a vector \(x\) in the kernel of \(A_n\), the three-term recurrence
\[
b_{i-1}x_{i-1}+a_i x_i+b_i x_{i+1}=0
\]
recovers \(x_{i+1}\) from \(x_{i-1},x_i\). Thus a solution is determined by its values at any consecutive two vertices and has dimension at most two. On \(V(I_n)\cap T\) the kernel has dimension exactly two, and each adjacent-coordinate projection \(K\to k^2\) is an isomorphism. Therefore the kernel map lands in \(U_n\).

Conversely, let \(K\in U_n\), choose a basis matrix with row vectors \(v_1,\ldots,v_n\in k^2\), and put \(w_i=\det(v_i,v_{i+1})\ne0\). For any \(q\in k^\times\), set
\[
b_i=\frac q{w_i},\qquad a_i=-\frac{q\det(v_{i-1},v_{i+1})}{w_{i-1}w_i}.
\]
The elementary two-dimensional determinant identity
\[
w_i v_{i-1}-\det(v_{i-1},v_{i+1})v_i+w_{i-1}v_{i+1}=0
\]
shows, after the displayed substitutions, that \(A_n v=0\) for both columns of the basis matrix. (In the identity the coefficient \(w_i\) of \(v_{i-1}\) is positive and the final coefficient \(w_{i-1}\) is positive.) All edge entries are nonzero, so the recurrence implies \(\ker A_n=K\). A basis change multiplies each \(w_i\) and each numerator determinant by the same nonzero factor and is absorbed in the scalar \(q\). The equations force all ratios \(b_iw_i\) to agree; hence the projective matrix is unique for a given \(K\). The inverse is regular on \(U_n\) after clearing denominators by the product \(\prod_iw_i\). Consequently the dense-edge *projective* rank-defect locus is biregular to \(U_n\), which is irreducible of dimension \(2(n-2)\). Its affine cone has dimension \(2n-3\).

**2. Every zero-edge boundary point belongs to that closure.** If exactly one edge coordinate \(b_i\) vanishes, then the support graph is a single path whose remaining edges are nonzero. The same recurrence, beginning at a path endpoint, shows its nullity is at most one; hence no such point is in \(V(I_n)\). If two or more edge coordinates vanish, the matrix splits into path blocks, with nonzero internal edge entries, and each block has nullity at most one. Therefore any point in \(V(I_n)\) with some vanishing edge has at least two singular path blocks. Pick a zero edge on each of two disjoint separating cuts. The point then belongs to at least one of the following closed subsets indexed by distinct cut edges \(i,j\):
\[
Z_{ij}=V\bigl(b_i,b_j,\det B_{ij}^{(1)},\det B_{ij}^{(2)}\bigr),
\]
where the two \(B_{ij}^{(r)}\) are the diagonal path blocks obtained by deleting cycle edges \(i,j\). Indeed, choosing two cuts that separate two singular blocks gives two arcs each containing a singular block, hence both block determinants vanish. Conversely, each \(Z_{ij}\) lies in \(V(I_n)\). Each path determinant, including the size-one determinant, is irreducible because its support graph is connected [3, Proposition 15]. As the two determinants involve disjoint groups of variables, \(Z_{ij}\) is an irreducible complete intersection of codimension four. The open part of \(Z_{ij}\) where every other edge is nonzero and each path block has nullity exactly one is nonempty (take each path block to be the negative weighted Laplacian of that path) and dense.

Fix a point of this open part. The kernel has basis \(u,v\) supported on the two disjoint paths. On either path, a nonzero kernel vector has nonzero endpoint values, again by the endpoint recurrence. The standard tangent space to the symmetric rank-at-most-\(n-2\) locus at a rank-\(n-2\) matrix is the kernel of the restriction map \(\delta A\mapsto(\delta A)|_{\ker A}\in\operatorname{Sym}^2(\ker A)^*\). Within the cycle-sparse linear space this restriction is **surjective**: a diagonal variation at a vertex of each path independently gives the two diagonal quadratic forms \(u^2\) and \(v^2\), while varying either cut edge gives a nonzero mixed \(uv\) term. Thus the restricted degeneracy variety is smooth of codimension three at this point. The mixed equation in its tangent space is a nonzero scalar times \(\delta b_i\) plus a nonzero scalar times \(\delta b_j\); consequently it has a tangent direction with both \(\delta b_i\) and \(\delta b_j\) nonzero. Smoothness implies the germ meets the locus with both cut edges nonzero: equivalently neither edge function vanishes identically on the unique local branch, and their product is nonzero at its generic point. Hence the generic point of each \(Z_{ij}\), and so all of \(Z_{ij}\), lies in the closure of the dense-edge rank-defect locus. The boundary is exhausted by these subsets, proving \(V(I_n)\) irreducible of codimension three.

**3. Reducedness upgrades irreducibility to primality.** Deng--Kretschmer [3, Theorem 1] prove that the ideal of all submaximal minors of every sparse generic symmetric matrix is radical, over any field. In the present smaller polynomial ring (omitting the absent off-diagonal indeterminates), this applies verbatim. Since the zero set of \(I_n\) over algebraically closed \(k\) is irreducible, the radical ideal \(I_n\) is prime. This establishes the theorem uniformly in \(n\).

**4. Hypersurface singularity.** The gradient of \(\det A_n\) with respect to \(a_i\) is the \((i,i)\)-cofactor. At rank \(n-1\), the adjugate is a nonzero rank-one matrix \(czz^{\mathsf T}\) with \(z\ne0\), so at least one diagonal cofactor is nonzero. At rank at most \(n-2\), all cofactors vanish. Thus the reduced singular support is exactly \(Y_n\). At a general point of the dense-edge locus, the restriction map to \(\operatorname{Sym}^2\ker A\) is surjective already using the two diagonals and intervening edge at any adjacent pair of vertices. The leading normal term of the determinant is the determinant of the resulting symmetric two-by-two matrix. Over characteristic zero, formal/analytic coordinates put the transverse hypersurface into the ordinary quadratic node \(xy-z^2=0\). This statement concerns generic points, not arbitrary boundary points.

## Verification
A standalone exact-arithmetic check in `verify_cycle.py` exercises the recurrence parameterization and rank for \(4\le n\le8\), and for every pair of cut edges constructs two singular path blocks with nonzero internal edges and checks that the restriction of sparse matrix perturbations to the two-dimensional kernel spans a three-dimensional space. All 80 tested cut-edge pairs satisfy the predicted rank-three transversality, and all five dense-edge witnesses have corank exactly two. Running the checker prints `VERIFY_OK`. These finite tests are consistency checks only; the argument above treats every integer \(n\ge4\) and uses the external published radicality theorem explicitly.

## Relationship to prior work
Boocher [1] develops pruning of sparse nonsymmetric determinantal resolutions, giving the historical archive foundation for this line. Conca--Welker [2] study coordinate sections of symmetric determinantal loci and graph criteria. Deng--Kretschmer [3, Theorem 1] establish radicality and Cohen--Macaulayness for connected graph supports, and [3, Proposition 12] already gives the codimension and degree quoted above. Crucially, [3, Question 16] explicitly asks whether 2-connectivity forces primality of the submaximal-minor ideal, and reports computer evidence only through size six. The present claim proves that question for the family of *all cycle graphs*, with a Grassmannian parameterization and a boundary-closure proof; it neither claims the pre-existing general radicality/degree results nor settles the general graph question.

## Limitations
Primality is asserted over algebraically closed characteristic-zero fields. The proof does not classify the nonreduced Jacobian singular scheme, all boundary analytic germs, or the general 2-connected graph case. An equivalent general theorem published elsewhere might subsume this cycle-family conclusion; the literature comparison is substantial but not an independent exhaustive certification. The node statement is generic. Computational tests over finitely many matrix sizes alone would not prove the theorem.

## References
[1] Adam Boocher, *Free Resolutions and Sparse Determinantal Ideals*, arXiv:1111.0279, first posted 2011-11-01, https://arxiv.org/abs/1111.0279.

[2] Aldo Conca and Volkmar Welker, *Lovasz-Saks-Schrijver ideals and coordinate sections of determinantal varieties*, arXiv:1801.07916, 2018, https://arxiv.org/abs/1801.07916.

[3] Jiahe Deng and Andreas Kretschmer, *Ideals of submaximal minors of sparse symmetric matrices*, arXiv:2211.07020 (2022), Theorem 1, Proposition 12, Proposition 15 and Question 16, https://arxiv.org/html/2211.07020v1.
