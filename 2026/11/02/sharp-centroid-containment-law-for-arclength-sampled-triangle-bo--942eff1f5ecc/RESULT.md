# Sharp centroid-containment law for arclength-sampled triangle boundaries

## Finding
Let \(T\) be any nondegenerate Euclidean triangle with sides \(s_1,s_2,s_3>0\), perimeter \(L=s_1+s_2+s_3\), and area centroid \(G\). Choose \(X_1,X_2,X_3\) independently and uniformly by arclength on \(\partial T\). Put \(p_i=s_i/L\), and write \(e_2=\sum_{i<j}p_ip_j\), \(e_3=p_1p_2p_3\). The exact probability of strict containment is
\[
\mathbb P\!\left(G\in\operatorname{int}\operatorname{conv}\{X_1,X_2,X_3\}\right)
=\left(\frac13+\frac{4\log2}{9}\right)e_2
 +\left(\frac{8\log2}{3}-1\right)e_3. \tag{1}
\]
The same formula holds for non-strict containment because the ambiguous events have probability zero. More generally, (1) holds for any three side-sampling probabilities \(p_i\geq0\) summing to one, conditional on each chosen side carrying uniform arclength, even when the probabilities are not proportional to side lengths.

The right side is strictly Schur-concave in \((p_1,p_2,p_3)\) on the positive simplex. For genuine triangles, the complete sharp range is
\[
\frac1{12}+\frac{\log2}{9}
<\mathbb P(G\in\operatorname{conv}\{X_1,X_2,X_3\})
\leq\frac2{27}+\frac{20\log2}{81}. \tag{2}
\]
The upper equality holds exactly for equilateral triangles. The lower endpoint is unattained, but is approached precisely when the normalized side-length triple converges, up to relabeling, to \((1/2,1/2,0)\). Every value in this half-open interval is realized. The sharp upper probability coincides with the established probability for three *area*-uniform points inside any triangle to contain its centroid; the distinction between perimeter sampling and area sampling is fundamental away from equilateral shapes.

There is a uniform quantitative form of the upper inequality:
\[
\frac2{27}+\frac{20\log2}{81}-P(T)
\geq\left(\frac16+\frac{2\log2}{9}\right)
\sum_{i=1}^3(p_i-1/3)^2. \tag{3}
\]
The constant in (3) is certified valid, but is not claimed optimal.

## Assumptions and scope
A triangle is nondegenerate if its three vertices are not collinear. All three samples are independent with normalized one-dimensional Hausdorff measure on its entire boundary; vertices have probability zero. The target point is the *area centroid* \(G=(A+B+C)/3\), not the perimeter centroid (Spieker center). Equation (1) admits a separate side-weight interpretation: first choose one of the three sides with prescribed probability \(p_i\), then choose uniformly on that side. The strict Schur statement applies to all positive sampling triples, while only triples with \(p_i<1/2\) arise from nondegenerate Euclidean side lengths. Throughout, \(\log\) denotes the natural logarithm.

## Proof
**Step 1: reduction to two universal conditional constants.** An invertible affine transformation maps any nondegenerate triangle to the reference triangle with vertices \(A=(0,0)\), \(B=(1,0)\), \(C=(0,1)\). It maps the area centroid to \(g=(1/3,1/3)\) and preserves uniform *fractional position along each fixed side*. Consequently, the probability conditional on any prescribed pattern of side labels is independent of triangle shape. Let \(b\) be the probability of containing \(g\) when two points lie on one chosen side and the third lies on a different chosen side. Let \(c\) be the analogous probability when one point is drawn independently on each of the three sides. Three points on the same side have a collinear hull and cannot contain \(g\). Permuting the vertices shows that these two values are independent of the chosen side labels.

**Step 2: two samples on one side.** Consider \(X=(s,0)\), \(Y=(t,0)\), \(Z=(0,u)\), where \(s,t,u\) are independent uniform variables on \((0,1)\). The horizontal section of their triangle at height \(1/3\) exists only if \(u\geq1/3\). Its horizontal coordinates range between \((1-1/(3u))s\) and \((1-1/(3u))t\). For it to contain \((1/3,1/3)\), the number \(k(u)=u/(3u-1)\) must lie between \(s\) and \(t\); this is possible exactly when \(u\geq1/2\). Thus
\[
 b=\int_{1/2}^1 2k(u)(1-k(u))\,du
 =\int_{1/2}^1\frac{2u(2u-1)}{(3u-1)^2}\,du
 =\frac19+\frac{4\log2}{27}. \tag{4}
\]
The conditions and equality boundaries are understood almost surely, so no endpoint issue arises.

**Step 3: one sample on each side.** In barycentric coordinates relative to \((A,B,C)\), draw independent \(u,v,w\sim\operatorname{Unif}(0,1)\) and form the three columns
\[
M=\begin{pmatrix}
1-u&0&w\\
u&1-v&0\\0&v&1-w
\end{pmatrix}.
\]
The determinant \(\det M=(1-u)(1-v)(1-w)+uvw\) is positive in the open cube. The centroid lies in the sampled triangle exactly when all components of \(M^{-1}(1,1,1)^\top/3\) are nonnegative. Three times the Cramer numerators are
\[
 N_0=1-v-2w+3vw,\qquad N_1=1-w-2u+3uw,\qquad N_2=1-u-2v+3uv.
\]
The event \(N_0<0\) forces \(0<v<1/2\) and \(w>(1-v)/(2-3v)>1/2\). The two cyclic counterparts force respectively \(w<1/2<u\) and \(u<1/2<v\); hence no two of the three bad events can occur simultaneously. Each bad event has probability
\[
 j=\int_0^{1/2}\left(1-\frac{1-v}{2-3v}\right)dv
 =\frac13-\frac{2\log2}{9}.
\]
Therefore
\[
 c=1-3j=\frac{2\log2}{3}. \tag{5}
\]

**Step 4: combination.** Side labels are independent with probabilities \(p_i\). There are three permutations of a specified two-on-one/one-on-another label pattern, and six permutations of one-on-each-side. Therefore
\[
P=3b\sum_{i\neq j}p_i^2p_j+6c\,p_1p_2p_3.
\]
Since \(\sum_{i\neq j}p_i^2p_j=e_2-3e_3\), inserting (4) and (5) gives precisely (1).

**Step 5: majorization, sharp range, and stability.** Both coefficients in (1) are strictly positive: \(1/3+4\log2/9>0\) and \(8\log2/3-1>0\) because \(\log2>3/8\). On the positive simplex, a nontrivial two-coordinate averaging increases \(e_2\) strictly and does not decrease \(e_3\). The strict Schur-concavity follows. Every genuine triangle has \(0<p_i<1/2\), and conversely every such probability triple gives valid triangle side lengths. The uniform triple \((1/3,1/3,1/3)\) uniquely maximizes (1), yielding the right side of (2). On the closure of the triangle-side domain, \((1/2,1/2,0)\) and its permutations majorize every admissible triple, and are the only minimizers; substituting gives the left endpoint. The family \(p_1=p_2=(1-t)/2\), \(p_3=t\), \(0<t\leq1/3\), continuously connects the limiting lower endpoint with the upper endpoint, proving attainability of every intermediate value. Finally \(e_2=\frac13-\frac12\sum_i(p_i-1/3)^2\), while \(e_3\leq1/27\) by AM–GM. Subtracting (1) from its value at the uniform triple proves (3).

**Step 6: comparison with area-uniform sampling.** The three triangles formed by joining the area centroid to the original sides have equal area. A point sampled uniformly from the original triangle projects radially from \(G\) onto a uniformly selected side and, conditional on its side, has a uniform fractional side position (constant Jacobian after integrating the radial scale). Since whether \(G\) is contained in a sampled triangle depends only on the three rays from \(G\), this reduces the known area-uniform probability to formula (1) at \(p_i=1/3\). This recovers exactly the pre-existing constant \(2/27+20\log2/81\); that constant alone does not determine the arclength-weighted shape law.

## Verification
The standalone `checker.py` uses a separately implemented geometric orientation test on full Euclidean coordinates for five differently shaped triangles, deterministic random seeds, independent midpoint quadrature for (4) and (5), random tests of the sign-disjointness argument, and random Schur balancing and stability comparisons. The program prints `ALL_CHECKS_PASSED` upon completion. Its finite tests corroborate the exact algebra; they are not proofs of the continuum assertions. The analytic derivations in Steps 1–6 constitute the proof.

## Relationship to prior work
Prékopa, *On the number of vertices of random convex polyhedra* (1972), §5, obtains the area-uniform triangle-centroid constant and relates radial projection to boundary sampling in the regular-simplex model. Halász–Kleitman (1974) study the interior-uniform point-containment extremum. Ionaşcu (first public arXiv version December 15, 2016), *Random triangles in planar regions containing a fixed point*, treats arbitrary area-sampling regions and points via induced angular boundary densities, including the known equilateral-centroid constant; its arbitrary-triangle section uses a density weighted by distances to the sides, not the constant-per-unit-length perimeter distribution. Reitzner–Schütt–Werner (first arXiv version November 14, 2019) investigate hulls of boundary-uniform samples but concentrate on large-sample face-number and volume asymptotics, not fixed-centroid containment for three samples. These general approaches motivate the question and are explicitly credited. The distinct new assertion is the complete arclength-weighted side-length formula with strict shape majorization and its sharp range; the historical possibility of an unlocated earlier derivation remains.

## Limitations
The assertion concerns exactly three independent boundary points on a Euclidean triangle and the *area centroid*. It does not give the distribution of the area of their sampled triangle or probabilities for arbitrary interior target points, general polygons, or correlated sampling. The stability coefficient in (3) is not asserted to be optimal. Although relevant full texts and indexed result summaries were compared, the historical priority judgment is provisional rather than a certificate of novelty. No independent mathematical audit has been performed.

## References
1. A. Prékopa, *On the number of vertices of random convex polyhedra*, Periodica Mathematica Hungarica 2 (1972), 259–282, especially pp. 19–21, https://rutcor.rutgers.edu/~prekopa/number.pdf.
2. S. Halász and D. J. Kleitman, *A note on random triangles*, Studies in Applied Mathematics 53 (1974), 225–237, https://doi.org/10.1002/sapm1974533225.
3. E. J. Ionaşcu, *Random triangles in planar regions containing a fixed point*, arXiv:1612.08619, first submitted 2016-12-15, https://arxiv.org/abs/1612.08619.
4. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917, first submitted 2019-11-14, https://arxiv.org/abs/1911.05917.
