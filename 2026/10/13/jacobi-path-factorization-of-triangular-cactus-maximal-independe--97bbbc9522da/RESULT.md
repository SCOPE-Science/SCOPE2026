# Jacobi-path factorization of triangular-cactus maximal-independent-set polynomials

## Finding

For every integer \(n\ge 2\), form the triangular chain \(T_n\) from \(n\) triangles with vertex sets \(\{c_{i-1},c_i,\ell_i\}\), \(1\le i\le n\), where consecutive triangles meet only at the designated vertex \(c_i\), and all other vertices are distinct. Let
\[
I_n(x)=\sum_{S\subseteq V(T_n)\atop S\text{ maximal independent}}x^{|S|}.
\]
Let \(P_n\) be the path on vertices \(1,\ldots,n\), and let \(\mathcal M(P_n)\) be its matchings. For \(M\in\mathcal M(P_n)\), write \(b(M)\) for the number of endpoints of \(P_n\) that are not incident with any edge of \(M\). Then
\[
\boxed{I_n(x)=\sum_{M\in\mathcal M(P_n)} 2^{b(M)}x^{n-|M|}.}
\]
Let \(J_n\) be the real symmetric \(n\)-by-\(n\) tridiagonal matrix with zero diagonal and off-diagonal entries \(a_i=(J_n)_{i,i+1}=(J_n)_{i+1,i}\), where \(a_1=1/2\), \(a_2=\sqrt3/2\) if \(n\ge3\), and \(a_i=1\) for \(3\le i\le n-1\). If \(\lambda_{n,1},\ldots,\lambda_{n,\lfloor n/2\rfloor}\) are its positive eigenvalues, then they are distinct, belong to \((0,2)\), and
\[
\boxed{I_n(x)=4x^{\lceil n/2\rceil}\prod_{j=1}^{\lfloor n/2\rfloor}(x+\lambda_{n,j}^{2}).}
\]
In particular, the \(\lfloor n/2\rfloor\) nonzero complex zeros of \(I_n\) are **distinct real numbers in \((-4,0)\)**; the remaining zero is \(0\), of multiplicity \(\lceil n/2\rceil\). The positive consecutive coefficients are strictly log-concave (when there are at least three of them) and consequently unimodal. The corresponding spectral factorization for \(n=1\) is not asserted: \(I_1(x)=3x\).

## Assumptions and scope

All graphs are finite, simple and undirected. A vertex set is maximal independent exactly when it is independent and dominating. The chain is the *linear* triangular cactus with pairwise different cut vertices in any internal triangle, not an arbitrary branched triangle cactus. The path matching endpoint multiplicities require \(n\ge2\); no assertion is made about other polygonal cactus families, nor about roots of general independent-domination polynomials. Complex roots are understood with algebraic multiplicity.

## Proof

**1. Tile-matching bijection.** Fix a maximal independent set \(S\) of \(T_n\). The private vertex \(\ell_i\) has neighbors exactly \(c_{i-1}\) and \(c_i\). To dominate \(\ell_i\), the set \(S\) must contain a vertex of its triangle. Since that triangle is a clique, exactly one of \(c_{i-1},c_i,\ell_i\) is selected. Conversely, if an independent set has exactly one selected vertex in every triangle, then every vertex is adjacent to, or itself is, a selected vertex, and the set is maximal independent.

For each selected interior cut vertex \(c_i\) with \(1\le i<n\), place a dimer covering positions \(i,i+1\) of a length-\(n\) line. This vertex is the unique selected vertex in both corresponding triangles. Every triangle not covered by a dimer contributes a monomer. Its chosen vertex must be \(\ell_i\) if \(1<i<n\), but a monomer at position \(1\) has the two choices \(\ell_1\) or \(c_0\), and one at position \(n\) has the two choices \(\ell_n\) or \(c_n\). Distinct dimers do not meet, so they form a matching of \(P_n\). Conversely, from any matching and endpoint choices, select its interior cut vertices and the indicated monomer vertices. Each triangle has exactly one selected vertex, and no edge joins two selected vertices, proving the bijection. A matching of size \(|M|\) covers \(2|M|\) triangles but contributes only \(|M|\) selected vertices; the remaining \(n-2|M|\) monomers each contribute one vertex. Thus \(|S|=n-|M|\), and each unmatched endpoint independently has two choices. Summation gives the first displayed polynomial identity.

**2. Matching recurrence.** Write \(f_r(t)=\sum_{M\in\mathcal M(P_r)}t^{|M|}\), for \(r\ge0\), with \(f_0=f_1=1\). Splitting matchings according to whether their last edge is used proves \(f_r=f_{r-1}+tf_{r-2}\) for \(r\ge2\). Since \(2^{b(M)}=(1+\mathbf1_{\{1\notin V(M)\}})(1+\mathbf1_{\{n\notin V(M)\}})\) for \(n\ge2\), expanding the two factors and deleting isolated unmatched endpoints yields
\[
 p_n(t):=x^{-n}I_n(x)\big|_{t=x^{-1}}=f_n(t)+2f_{n-1}(t)+f_{n-2}(t).
\]
Here \(p_n\) is a polynomial in the formal variable \(t\), not a Laurent series. Directly \(p_2(t)=4+t\), \(p_3(t)=4+4t\), and the preceding recurrence implies \(p_n=p_{n-1}+tp_{n-2}\) for every \(n\ge4\).

**3. Jacobi characteristic polynomial.** For \(n\ge2\), define \(q_n(z)=\tfrac14z^n p_n(-z^{-2})\). The preceding initial values give \(q_2=z^2-\tfrac14\) and \(q_3=z^3-z\). For every \(n\ge4\), the recursion becomes \(q_n=zq_{n-1}-q_{n-2}\). On the other hand, expanding \(\det(zI-J_n)\) along the last row and column gives exactly these two initial polynomials and, for \(n\ge4\), the same recursion because \(a_i^2=1\) for \(i\ge3\). Hence
\[
\det(zI-J_n)=\tfrac14 z^n p_n(-z^{-2})
\]
identically as polynomials for all \(n\ge2\). This is an identity over \(\mathbb Q[z]\), despite the square-root entries of \(J_n\).

**4. Roots and factorization.** The matrix \(J_n\) is real symmetric, hence has only real eigenvalues. All off-diagonal entries are positive. An eigenvector is uniquely determined up to scalar by its first coordinate via the three-term row recurrence (and its first coordinate cannot vanish unless the entire vector vanishes); consequently every eigenvalue is simple. The sign-change diagonal matrix \(\mathrm{diag}(1,-1,1,-1,\ldots)\) conjugates \(J_n\) to \(-J_n\), so eigenvalues occur in distinct opposite pairs, with one additional simple zero precisely for odd \(n\). Nonnegativity, irreducibility and the inequalities \(J_n\mathbf1\le2\mathbf1\), strict at the first vertex, imply \(\rho(J_n)<2\): equality would force all coordinates of a Perron eigenvector attaining its maximum to propagate their maximum to the first vertex, where the strict row inequality is impossible. The same upper bound is immediate for \(n=2\). Thus the positive eigenvalues all lie in \((0,2)\), and
\[
\det(zI-J_n)=z^{n-2m}\prod_{j=1}^{m}(z^2-\lambda_{n,j}^2),\qquad m=\lfloor n/2\rfloor.
\]
Substitute this into the determinant identity to obtain \(p_n(t)=4\prod_{j=1}^{m}(1+\lambda_{n,j}^2t)\) and hence the stated factorization of \(I_n(x)\). Because the positive eigenvalues are distinct, their squares are distinct and nonzero, and therefore the nonzero polynomial roots are simple and lie in \((-4,0)\). The nonzero coefficient string is the coefficient sequence of a product of positive linear factors; Newton's inequalities yield strict ordinary log-concavity at each interior index and hence unimodality. The case \(m=1\) has no interior coefficient to test.

## Verification

Run the enclosed `verify.py` using Python 3 (standard library only). Its independently constructed triangular-chain graphs are exhaustively checked against the matching and Jacobi formulas for \(1\le n\le9\): the total number of candidate vertex subsets inspected is \(699048\). The code also compares every coefficient of the matching-tiling recurrence, the pre-existing bivariate generating-function recurrence, and the tridiagonal determinant recurrence for \(2\le n\le80\), using exact integer and rational arithmetic; the captured output is in `verification_output.txt`. Finite checks are corroboration, not the proof for arbitrary \(n\). The infinite statement follows from the bijection and determinant argument above.

## Relationship to prior work

Jahari and Alikhani (2019) enumerated the **total numbers** of independent dominating sets in triangular cactus chains, with a Fibonacci recurrence. Klamsakul and collaborators (2022), Theorem 1, already determined the **complete cardinality enumerator** through the known bivariate generating function
\[
\sum_{n\ge0}I_n(x)u^n=\frac{(1+ux)^2}{1-ux-u^2x}.
\]
No novelty is claimed for that generating function, its coefficients, the total-count recurrence, or the minimum size. The contribution assessed here is the explicit boundary-weighted matching bijection, the precise Jacobi tridiagonal spectral representation, and the resultant simple negative real-root and log-concavity theorem **simultaneously for all \(n\ge2\)**. These are substantive consequences of the earlier enumerator, not independent alternative counts. General matching-polynomial real-rootedness and elementary Jacobi-matrix facts are classical background; the object-specific reduction is the new ingredient. Literature search and comparison do not exclude an equivalent unindexed prior reduction.

## Limitations

The result is for linear triangular cactus chains only. It does not establish any general real-rootedness property for non-linear cactus structures, other polygon lengths, or arbitrary graphs. The uniform root theorem is proved algebraically, but the historical originality assessment is not an exhaustive guarantee against unpublished, unindexed, or differently named results. No independent external audit has been performed.

## References

1. S. Jahari and S. Alikhani, *Counting independent dominating sets in linear polymers*, arXiv:1910.05272 (first public 2019-09-29), Section 2. https://arxiv.org/abs/1910.05272
2. N. Klamsakul, P. Thengarnanchai, M. Suebtangjai, P. Kaewperm, N. Songsuwan, and P. Kaemawichanurat, *Maximal Independent Sets in Polygonal Cacti*, arXiv:2202.11294 (first public 2022-02-23), Theorem 1 and its proof. https://arxiv.org/abs/2202.11294
3. M. Dod, *The Independent Domination Polynomial*, arXiv:1602.08250 (2016), foundational terminology. https://arxiv.org/abs/1602.08250
