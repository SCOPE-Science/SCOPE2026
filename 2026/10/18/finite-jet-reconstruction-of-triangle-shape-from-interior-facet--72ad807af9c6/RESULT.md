# Finite-jet reconstruction of triangle shape from interior facet-distance ratios

## Finding

Let \(S\) be a nondegenerate Euclidean \(d\)-simplex, \(d\ge2\), with facets \(F_1,\ldots,F_m\), \(m=d+1\), and positive facet \((d-1)\)-volumes \(A_i\). Put \(p_i=A_i/\sum_j A_j\). Choose \(X\) uniformly in \(S\) by \(d\)-dimensional volume. Write \(D_i(X)\) for the perpendicular Euclidean distance from \(X\) to the **affine supporting hyperplane** of \(F_i\), and order these distances as \(D_{(1)}<D_{(2)}<\cdots<D_{(m)}\) almost surely. Let \(R=D_{(2)}/D_{(1)}\).

The complete ordered list of supporting-facet distances has the same rank order as independent exponential waiting times of respective rates \(A_i\); in particular its ordered facet labels have the classical Plackett–Luce probability
\[
\Pr(i_1,\ldots,i_m)=\prod_{j=1}^{m}\frac{A_{i_j}}{\sum_{k=j}^{m}A_{i_k}}.
\]
The *unlabeled scalar* ratio has the exact survival law, for every \(y\ge0\),
\[
\boxed{H_S(y):=\Pr(R>1+y)=\sum_{i=1}^{m}\frac{p_i}{1+(1-p_i)y}.}
\]
Thus the law depends only on the unordered normalized facet-area profile. More strongly, its first \(d=m-1\) right derivatives at \(y=0\) uniquely recover the complete multiset \(\{p_1,\ldots,p_m\}\). In dimension two, **only the first and second right derivatives suffice to recover every triangle up to similarity and reflection**.

For triangles, the realizable laws are precisely the displayed rational functions corresponding to triples \(p_i>0\), \(\sum_i p_i=1\), and \(\max_i p_i<1/2\). Every such triple comes from a unique triangle similarity class up to reflection. Additionally, every nondegenerate triangle and every \(y>0\) obey the sharp stochastic envelope
\[
\boxed{\frac{3}{3+2y}\le H_S(y)<\frac{2}{2+y}.}
\]
The lower equality holds precisely for the equilateral triangle, and the upper bound is approached by a sequence of increasingly degenerate isosceles triangles, but never attained by a genuine triangle.

## Assumptions and scope

The simplex is full-dimensional and nondegenerate; the sampling law is uniform Euclidean volume. A **facet distance** means distance to the entire affine hyperplane containing a facet, which differs in general from distance to the finite facet or to the boundary of the simplex. The ratio is well-defined almost surely because interior points have positive distances and ties occur only on lower-dimensional sets. All facet-area profiles are considered up to a common multiplicative factor, and the facet labels are discarded in the inverse statement. The triangle shape is identified modulo scaling, rigid motions, and reflection.

## Proof

**1. The exponential reduction.** Let \(v_i\) be the vertex opposite \(F_i\), and let \(\lambda_i(X)\) be the associated barycentric coordinate. The altitude of \(v_i\) above the hyperplane of \(F_i\) equals \(h_i=d\operatorname{Vol}_d(S)/A_i\), by the simplex-volume formula. Thus
\[
D_i(X)=h_i\lambda_i(X)=\frac{d\operatorname{Vol}_d(S)}{A_i}\lambda_i(X).
\]
The barycentric coordinates of a uniform point have the Dirichlet law with all parameters equal to one. Equivalently, with independent unit-rate exponential variables \(E_i\), their vector is distributed as \((E_i/\sum_jE_j)_{i=1}^m\). Consequently the ratios and rank order of \(D_i\) agree with those of \(T_i=E_i/A_i\), which are independent exponential variables of rates \(A_i\). Successive use of the memoryless property gives the displayed Plackett–Luce ranking law; this last ranking mechanism itself is classical.

**2. Two-smallest ratio law.** Write \(A=\sum_jA_j\). Let \(I\) be the index of the first exponential clock, and let \(T_{(1)}\) and \(T_{(2)}\) denote the first two times. Standard competing-exponential calculations, or direct integration of the joint density, give \(\Pr(I=i)=A_i/A=p_i\); independently of \(I\), \(T_{(1)}\) has exponential rate \(A\). Conditional on \(I=i\) and \(T_{(1)}=t\), the gap \(T_{(2)}-T_{(1)}\) is exponential of rate \(A-A_i\) and independent of \(t\). Therefore
\[
\Pr\left(\frac{T_{(2)}}{T_{(1)}}>1+y\mid I=i\right)
=\int_0^\infty A e^{-At}e^{-y(A-A_i)t}\,dt
=\frac1{1+(1-p_i)y}.
\]
Averaging with weights \(p_i\) proves the exact law for every \(y\ge0\), including \(y=0\).

**3. Finite derivatives determine facet areas.** Define the computable right-derivative coefficients
\[
M_k=\frac{(-1)^k}{k!}H_S^{(k)}(0+)=\sum_{i=1}^m p_i(1-p_i)^k,
\qquad 1\le k\le m-1.
\]
Set the power sums \(s_j=\sum_i p_i^j\), with \(s_1=1\). Binomial expansion gives
\[
M_k=\sum_{j=0}^k(-1)^j\binom{k}{j}s_{j+1}.
\]
Its coefficient of the previously unknown \(s_{k+1}\) is \((-1)^k\). Therefore the \(m-1\) coefficients \(M_1,\ldots,M_{m-1}\) recursively determine \(s_2,\ldots,s_m\). Newton identities then determine all elementary symmetric functions of \(p_1,\ldots,p_m\), and hence the monic polynomial \(\prod_{i=1}^m(z-p_i)\). Its multiset of roots is the unique normalized facet-area multiset. This proof allows repeated roots, corresponding to repeated facet areas; no genericity assumption is needed.

**4. Triangle reconstruction and feasibility.** For \(m=3\), the elementary symmetric polynomials are explicitly
\[
e_1=1,\qquad e_2=\frac{M_1}{2},\qquad e_3=\frac{M_2-M_1/2}{3}.
\]
Thus the three normalized side lengths are exactly the positive roots of
\[
\boxed{z^3-z^2+\frac{M_1}{2}z-\frac{M_2-M_1/2}{3}=0.}
\]
They satisfy the strict triangle inequalities if and only if \(\max_i p_i<1/2\). Conversely every positive triple summing to one with that inequality specifies a nondegenerate Euclidean triangle by the side-side-side construction, unique up to similarity and reflection. Its uniform-point ratio law is the formula in the finding. Therefore both the inverse and realizability assertions hold.

To see why **two** local derivatives encode genuinely more information than one, take \(a=1/12\). The two triples \((1/3+a,1/3-a,1/3)\) and \((1/3+a/\sqrt3,1/3+a/\sqrt3,1/3-2a/\sqrt3)\) both satisfy strict triangle inequalities, are not permutations, yet have equal sums of squares, hence equal \(M_1\) and equal first derivative. Their second derivative distinguishes them.

**5. Sharp stochastic bounds.** For fixed \(y>0\) write \(f_y(p)=p/[1+(1-p)y]\), with
\[
f_y''(p)=\frac{2y(1+y)}{(1+y-yp)^3}>0
\qquad (0\le p\le1/2).
\]
Jensen's inequality at the common mean \(1/3\) gives \(\sum_i f_y(p_i)\ge3f_y(1/3)=3/(3+2y)\), with equality exactly when all sides are equal. Every feasible normalized triangle side triple is majorized by \((1/2,1/2,0)\), because its largest entry is strictly below \(1/2\) and its total sum is one. Strict convexity and Karamata's inequality yield
\[
\sum_i f_y(p_i)<2f_y(1/2)+f_y(0)=\frac2{2+y}.
\]
Letting \(p_1=p_2=(1-\varepsilon)/2\), \(p_3=\varepsilon\), with positive \(\varepsilon\) tending to zero, shows sharpness of this unattained upper envelope. This completes the proof.

## Verification

The standalone `check_facet_ratio.py` constructs Euclidean supporting-hyperplane unit normals independently of the barycentric altitude formulas. It samples four two- or three-dimensional simplices (including a scalene right triangle, a nonregular isosceles triangle, an equilateral triangle, and an irregular tetrahedron), with \(230000\) uniform points per case. It compares four predicted survival thresholds and each first-facet probability against empirical frequencies, checks the direct distance/altitude identity to numerical tolerance, and tests the triangle extremal bounds on \(1500\) random valid profiles. Independent exact-rational computations recover power sums and annihilating polynomials for four rational area profiles. The command `python check_facet_ratio.py` completed with output `SIMPLEX_FACET_RATIO_OK geometry_cases=4 samples=920000 exact_jets=4 extremal_profiles=1500`. These experiments corroborate, but do not replace, the infinite-parameter proofs above.

## Relationship to prior work

The normalized-independent-exponential representation of uniform simplex coordinates is a pre-existing result, explicitly developed in the probabilistic section of Anderson, Goyal, and Rademacher. Exponential-clock ranking is the classical Plackett–Luce model. Neither fact alone is presented here as new. The assessed contribution is their geometric application to the **unlabeled two-smallest supporting-facet distance ratio**, its explicit complete distribution, **finite-jet inverse recovery**, and the exact triangle realizability and sharp stochastic extremal bounds. Prior geometric-probability literature on distances between independent interior points of triangles concerns a different observable. Existing unlabeled projection-width triangle inverse laws use random directional widths rather than this random interior supporting-line statistic. These comparisons do not constitute an exhaustive historical-priority guarantee.

## Limitations

For \(d\ge3\), normalized facet areas do not in general identify the Euclidean simplex up to similarity, so only the facet-area multiset is recovered. The finite-jet assertion concerns exact population derivatives, not an estimator from finitely many samples; derivative estimation can be ill-conditioned when several areas nearly coincide. The claim concerns supporting hyperplanes, not distances to finite facets, arbitrary convex polytopes, nonuniform sampling, or shapes other than simplices. Independent mathematical validation and definitive historical priority assessment remain outstanding.

## References

1. J. Anderson, N. Goyal, and L. Rademacher, *Efficient Learning of Simplices*, arXiv:1211.2227 (first public version 2012-11-09); particularly the full-text probabilistic section on uniform simplex sampling. https://arxiv.org/html/1211.2227v3
2. R. L. Plackett, *The Analysis of Permutations*, Applied Statistics 24 (1975), 193–202, doi:10.2307/2346567. The classical ranking model; original full text not inspected.
3. F. Tong, M. Ahmadi, and J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498 (first public 2013-11-29). https://arxiv.org/abs/1312.2498
