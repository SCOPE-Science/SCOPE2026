# Exact Cartesian-product law for the two-body Bézout mixed-volume coefficient

## Finding
Let \(m\ge2\), let \(d_1,\ldots,d_m\) be positive integers with \(n=\sum_i d_i\), and let \(K_i\subset\mathbb R^{d_i}\) be compact convex sets with nonempty interior. Put \(K=K_1\times\cdots\times K_m\). For every full-dimensional compact convex \(D\subset\mathbb R^d\), \(d\ge2\), define
\[
\beta_d(D)=\sup_{L,M}\frac{V_d(L,M,D[d-2])\operatorname{vol}_d(D)}{V_d(L,D[d-1])V_d(M,D[d-1])},
\]
where the supremum runs over nonempty compact convex \(L,M\) with positive denominator and \(V_d\) is the standard normalized mixed volume. Then the **exact** product rule is
\[
\boxed{\displaystyle\beta_n(K)=\frac{n}{n-1}\max\left\{1,\max_{i:d_i\ge2}\frac{d_i-1}{d_i}\beta_{d_i}(K_i)\right\}.}
\]
The maximum over an empty index set is omitted. The same identity holds for invertible affine images of \(K\). In particular, if every factor has dimension at most two, then
\[
\boxed{\beta_n(K)=\frac{n}{n-1}.}
\]
This includes arbitrary products of planar convex sets and segments, including products of polygons and parallelotopes. The sharp constant is witnessed by two line segments lying in different factor subspaces, or by full-dimensional approximations of those segments.

## Assumptions and scope
All dimensions are integers, \(m\ge2\), each \(d_i\ge1\), and the factors \(K_i\) have positive \(d_i\)-volume. A convex set used as \(L\) or \(M\) may have lower dimension; restricting the supremum to full-dimensional sets gives the same value by replacing \(L\) and \(M\) with \(L+\varepsilon B\) and \(M+\varepsilon B\) and taking \(\varepsilon\downarrow0\). A one-dimensional factor has no separately defined two-body coefficient. All volumes are Euclidean Lebesgue volumes in the indicated dimensions; \(D[j]\) means \(j\) identical mixed-volume arguments. The theorem concerns two test bodies, not an arbitrary number of mixed-volume arguments.

## Proof
**1. Reduction to products of projections.** Let \(E_i\) denote the coordinate factor subspace and \(L_i,M_i\) the coordinate projections of \(L,M\). Set \(\widehat L=\prod_iL_i\), \(\widehat M=\prod_iM_i\). Since \(L\subseteq\widehat L\) and \(M\subseteq\widehat M\), mixed-volume monotonicity gives
\[
V_n(L,M,K[n-2])\le V_n(\widehat L,\widehat M,K[n-2]).
\]
On the other hand,
\[
V_n(L,K[n-1])=V_n(\widehat L,K[n-1]),\qquad
V_n(M,K[n-1])=V_n(\widehat M,K[n-1]).
\]
Indeed, the surface-area measure of a Cartesian product is supported on normals living in one factor subspace at a time: outside sets of boundary Hausdorff codimension at least two, exactly one factor is on its boundary. In such a normal direction, the support functions of \(L\) and \(\widehat L\) agree by the definition of coordinate projection. The integral formula \(nV_n(L,K[n-1])=\int h_L\,dS_K\) gives the asserted identities, and similarly for \(M\). Therefore it suffices to bound the quotient for \(\widehat L,\widehat M\).

**2. Exact product coefficients.** Write \(v_i=\operatorname{vol}_{d_i}(K_i)>0\), and define nonnegative numbers
\[
 a_i=\frac{d_i V_{d_i}(L_i,K_i[d_i-1])}{v_i},\qquad
 b_i=\frac{d_i V_{d_i}(M_i,K_i[d_i-1])}{v_i},
\]
and, for \(d_i\ge2\),
\[
 c_i=\frac{d_i(d_i-1)V_{d_i}(L_i,M_i,K_i[d_i-2])}{v_i}.
\]
For \(d_i=1\), set \(c_i=0\). Expanding the coefficients of \(t\), \(s\), and \(ts\) in the Minkowski volume polynomial
\[
\operatorname{vol}_n(K+t\widehat L+s\widehat M)
=\prod_{i=1}^{m}\operatorname{vol}_{d_i}(K_i+tL_i+sM_i)
\]
yields, with \(v=\operatorname{vol}_n(K)=\prod_i v_i\),
\[
\frac{n V_n(\widehat L,K[n-1])}{v}=\sum_i a_i,\qquad
\frac{n V_n(\widehat M,K[n-1])}{v}=\sum_i b_i,
\]
\[
\frac{n(n-1)V_n(\widehat L,\widehat M,K[n-2])}{v}
=\sum_{i\ne j}a_i b_j+\sum_i c_i.
\]
By the defining supremum, for \(d_i\ge2\),
\[
 c_i\le\frac{d_i-1}{d_i}\beta_{d_i}(K_i)a_i b_i.
\]
For a vanishing factor denominator the inequality follows by continuity from positive perturbations. Denote the coefficient on the right by \(\gamma_i\), with \(\gamma_i=0\) for one-dimensional factors, and put \(\Gamma=\max\{1,\gamma_1,\ldots,\gamma_m\}\). Since \(a_i,b_i\ge0\),
\[
\sum_{i\ne j}a_i b_j+\sum_i c_i
\le\Gamma\sum_{i,j}a_i b_j
=\Gamma\bigl(\sum_i a_i\bigr)\bigl(\sum_j b_j\bigr).
\]
The first-step reduction and normalization therefore give \(\beta_n(K)\le n\Gamma/(n-1)\).

**3. Sharpness of every candidate coefficient.** Fix different factors \(i\ne j\). Take \(L\) to be a nondegenerate line segment contained in \(E_i\), and \(M\) one contained in \(E_j\). Only \(a_i,b_j\) can be nonzero, so the volume-polynomial identity gives the quotient exactly \(n/(n-1)\). This proves the cross-factor lower bound.

For any index \(i\) with \(d_i\ge2\), take \(L,M\subset E_i\), identifying them with arbitrary factor test bodies \(L_i,M_i\). All other projections are singletons. The same coefficient identity gives
\[
\frac{V_n(L,M,K[n-2])v}{V_n(L,K[n-1])V_n(M,K[n-1])}
=\frac{n}{n-1}\frac{d_i-1}{d_i}
\frac{V_{d_i}(L_i,M_i,K_i[d_i-2])v_i}{V_{d_i}(L_i,K_i[d_i-1])V_{d_i}(M_i,K_i[d_i-1])}.
\]
Taking the factor supremum proves the other lower bounds and hence equality in the boxed formula. A nonsingular linear map preserves all quotients because numerator and denominator have the same overall determinant scaling.

**4. Planar-factor consequence.** The sharp planar Bézout inequality \(\beta_2(D)\le2\) for every planar convex \(D\) is Theorem 6.1 of Soprunov–Zvavitch, arXiv:1507.00765v3. Thus each \(d_i=2\) factor has \(\gamma_i\le1\), while \(d_i=1\) gives \(\gamma_i=0\). The general formula immediately yields \(n/(n-1)\), with equality from the cross-factor witnesses.

## Verification
The standalone `verify.py` script uses only the Python standard library. Run `python3 verify.py` in the directory containing it. It checks exact rational coefficient extraction for products of truncated bivariate polynomials, independent integer-determinant evaluations of zonotope volumes, and sharpness and upper bounds for segment tests against unit boxes in dimensions two through seven. It prints `VERIFY_OK 8054` on the checked version. The proof above, not the finite tests, establishes the theorem for arbitrary convex factors and all dimensions.

## Relationship to prior work
Artstein-Avidan, Florentin and Ostrover (arXiv:1306.1315, Theorem 1.1) establish the same coefficient \(n/(n-1)\) for positive-semidefinite mixed discriminants, but explicitly note that the analogous inequality fails for arbitrary triples of convex bodies when \(n\ge3\). Their Proposition 5.1 proves the sharp planar inequality and characterizes its equality case; their paper does not classify product bodies in higher dimensions. Soprunov and Zvavitch's *Bezout Inequality for Mixed volumes* (first public version July 2, 2015; arXiv:1507.00765) establishes the coefficient-one inequality for a simplex, the sharp planar universal coefficient two (Theorem 6.1), and a dimension-independent coefficient two when the two test bodies are zonoids (Lemma 5.2 and Theorem 5.6). Their projection discussion (Section 4) shows that parallelotopes violate the coefficient-one inequality but does not determine their best general-test-body coefficient in dimensions above two. Saroglou, Soprunov and Zvavitch (arXiv:1512.05442) characterize simplices among polytopes by the coefficient-one property. Xiao (arXiv:1704.00883) proves the general bound \(\beta_n(D)\le n\); it does not, in the inspected statements, give a factorwise sharp product law. The present formula determines the best constant for every Cartesian product from those of its factors and supplies a shape-independent sharp constant for any number of one- and two-dimensional factors. Its tools are classical, so independent checking against older equivalent tensorization formulations is warranted.

## Limitations
No analogous exact formula is asserted for arbitrary Minkowski sums, nonproduct bodies, more than two test bodies, or products with unspecified factor coefficients. No factor coefficient \(\beta_{d_i}(K_i)\) is calculated here for general factors of dimension three or higher. For the special case of products of simplices, classical multihomogeneous Bézout estimates may furnish related bounds, and this note does not claim novelty for those earlier general principles. Independent literature validation has not been performed. The computational tests are finite and do not certify the infinite-dimensional breadth of the analytic proof.

## References
1. S. Artstein-Avidan, D. Florentin and Y. Ostrover, *Remarks about Mixed Discriminants and Volumes*, arXiv:1306.1315 (first public 2013-06-06), https://arxiv.org/html/1306.1315v1 .
2. I. Soprunov and A. Zvavitch, *Bezout Inequality for Mixed volumes*, arXiv:1507.00765 (first public 2015-07-02), revised v3 (2016-12-08), https://arxiv.org/html/1507.00765v3 .
3. C. Saroglou, I. Soprunov and A. Zvavitch, *Characterization of simplices via the Bezout inequality for mixed volumes*, arXiv:1512.05442 (2015-12-17), https://arxiv.org/html/1512.05442v1 .
4. J. Xiao, *Bézout type inequality in convex geometry*, arXiv:1704.00883 (2017-04-04), https://arxiv.org/html/1704.00883v1 .
5. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded edition, Cambridge University Press (2014), for mixed-volume monotonicity and the first-variation formula.
