# A corner-product law and convex-order rigidity for random boundary polygons

## Finding

Let \(P\subset\mathbb R^2\) be a fixed strictly convex polygon with \(m\ge3\) vertices, perimeter \(L\), interior angles \(0<\theta_j<\pi\), and successive side lengths \(\ell_j>0\). For each integer \(N\ge3\), let \(H_N\) be the convex hull of \(N\) independent points drawn uniformly in boundary arclength. Write \(A_N=\operatorname{Area}(P)-\operatorname{Area}(H_N)\), \(c_j=\tfrac12\sin\theta_j\), and \(\mu=\sum_{j=1}^m c_j\).

**Theorem.** There exist mutually independent unit-rate exponential random variables \(E_1,F_1,\ldots,E_m,F_m\) for which
\[
\frac{N^2}{L^2}A_N\ \xrightarrow[N\to\infty]{\mathrm d}\ S_P=\sum_{j=1}^m c_j E_jF_j.
\]
Every fixed positive integer moment converges. In particular,
\[
\lim_{N\to\infty}\frac{N^2\mathbb EA_N}{L^2}=\mu,
\qquad
\lim_{N\to\infty}\operatorname{Var}\!\left(\frac{N^2 A_N}{L^2}\right)=3\sum_{j=1}^m c_j^2.
\]
More strongly, with \(\ell_*=\min_j\ell_j\), a constant \(C_P<\infty\) exists such that for every \(N\ge3\),
\[
\left|\mathbb EA_N-\frac{L^2\mu}{(N+1)(N+2)}\right|
\le C_P\exp(-N\ell_*/L).
\]
Thus the complete algebraic-order expansion of the expectation depends only on the interior angles and perimeter; dependence on individual side lengths is exponentially small. The law has the Laplace transform
\[
\mathbb Ee^{-sS_P}=\prod_{j=1}^m
\frac{e^{1/(sc_j)}}{sc_j}E_1\!\left(\frac1{sc_j}\right),\quad s>0,
\]
where the function \(E_1(z)=\int_z^\infty e^{-u}u^{-1}\,du\) is the exponential integral (not an exponential random variable).

Let \(c_*=\max_j c_j\) and let \(k_*\) count its occurrences. The limiting law has the sharp heavy tail
\[
\Pr(S_P>t)\sim k_*\sqrt\pi\,(t/c_*)^{1/4}
\exp\!\left(-2\sqrt{t/c_*}\right)\quad(t\to\infty).
\]
Its mean-normalized version obeys the convex-order inequality
\[
\frac1m\sum_{j=1}^m E_jF_j\ \le_{\mathrm{cx}}\ \frac{S_P}{\mu},
\]
meaning the expectation of every convex test function on the left does not exceed that on the right whenever both expectations exist. The inequality is strict for every strictly convex test function with finite expectations unless all \(\sin\theta_j\) coincide; in that equal-sine case the two laws agree. Consequently,
\[
\frac{\operatorname{Var}(S_P)}{(\mathbb ES_P)^2}
=3\frac{\sum_j\sin^2\theta_j}{(\sum_j\sin\theta_j)^2}
\ge\frac3m,
\]
with equality precisely when the sines coincide (including all parallelograms when \(m=4\)). Independently, at fixed \(m\) and \(L\),
\[
\mu\le\frac m2\sin\!\left(\frac{2\pi}{m}\right),
\]
with equality exactly for equiangular polygons. The two rigidity statements concern different optimizations and need not have identical equality classes.

## Assumptions and scope

"Strictly convex polygon" means a nondegenerate convex polygon with consecutive, non-collinear edges and every interior angle strictly between zero and \(\pi\); no smoothness or rationality is assumed. Side indices are cyclic. The perimeter is the sum of Euclidean edge lengths. The exponentials \(E_j,F_j\) in the theorem are independent for each fixed polygon; the number of corners \(m\) is fixed as \(N\to\infty\). All limits concern boundary sampling, not uniform sampling in the polygon's interior. No joint \(m,N\to\infty\) assertion is made.

## Proof

**1. Exact corner decomposition on the high-probability event.** Let \(G_N\) be the event that every open side contains at least one sampled point; with probability one, no point is a vertex. A union bound gives
\[
\Pr(G_N^c)\le\sum_{j=1}^m(1-\ell_j/L)^N\le m e^{-N\ell_*/L}.
\]
At corner \(j\), measure \(U_{N,j}\) and \(V_{N,j}\) along its two incident edges from the corner to the closest sample on that edge, truncating to the full edge length if the side is empty. On \(G_N\), the polygon missing from the sampled convex hull is exactly the union of the \(m\) corner triangles whose vertices are the original corner and the nearest samples on its two edges. Indeed the sampled boundary points on any occupied side occur on the segment joining that side's two extreme samples, and the strict convexity of \(P\) makes the hull's remaining connecting edges precisely the chords across consecutive corners. Hence
\[
 A_N=\sum_{j=1}^m\frac12\sin\theta_j\,U_{N,j}V_{N,j}
 \qquad\text{on }G_N.
\]
Both sides of this formula are bounded by a constant depending only on \(P\), for all outcomes and \(N\). Consequently, replacing \(A_N\) by the sum of corner products changes its expectation by at most \(C_Pe^{-N\ell_*/L}\); the same exponentially small bound holds for every fixed moment after its natural polynomial rescaling.

**2. Exact integration and all algebraic orders.** If the two incident edge lengths at corner \(j\) are \(a,b\), the survival identity for \(0\le u<a,\ 0\le v<b\) is
\[
\Pr(U_{N,j}>u,\ V_{N,j}>v)
=\left(1-\frac{u+v}{L}\right)^N.
\]
Here the two arclength intervals lie on disjoint edges and \(a+b\le L\). Tail integration followed by two elementary antiderivatives gives the exact identity
\[
\mathbb E[U_{N,j}V_{N,j}]
=\frac{L^2}{(N+1)(N+2)}
\left[1-\left(1-\frac aL\right)^{N+2}
-\left(1-\frac bL\right)^{N+2}
+\left(1-\frac{a+b}{L}\right)^{N+2}\right].
\]
Every bracket correction is exponentially small with a polygon-dependent rate. Combining with Step 1 yields the asserted uniform expectation estimate. In particular the coefficient of \(N^{-k}\) for any fixed \(k\ge2\) can be read from the Taylor expansion of \(1/((N+1)(N+2))\), without new shape parameters.

**3. The independent corner-product limit and moment control.** Take any fixed nonnegative numbers assigned to the \(2m\) incident corner germs. For all sufficiently large \(N\), the corresponding arclength neighborhoods of sizes \(Lt_i/N\) are pairwise disjoint. The probability that all these neighborhoods contain no sampled point equals
\[
\left(1-\frac{\sum_i t_i}{N}\right)^N
\longrightarrow e^{-\sum_i t_i}.
\]
Joint survival convergence identifies the \(2m\) limiting distances as independent rate-one exponentials. The continuous mapping theorem and Step 1 give the stated limit of scaled area. Moreover, for any corner distance \(U\) truncated at its edge length,
\[
\Pr(NU/L>t)\le e^{-t}\quad(t\ge0).
\]
The same holds for \(V\). Hölder's inequality then bounds every fixed moment of \((NU/L)(NV/L)\) uniformly in \(N\). Finite sums inherit uniform bounds in every order. Applying uniform integrability to powers yields convergence of all moments. Finally \(\mathbb E(E_jF_j)=1\) and \(\operatorname{Var}(E_jF_j)=4-1=3\).

**4. Transform and sharp tail.** Conditioning on \(E_j=u\) gives
\[
\mathbb E e^{-sc_jE_jF_j}
=\int_0^\infty\frac{e^{-u}}{1+sc_ju}\,du
=\frac{e^{1/(sc_j)}}{sc_j}E_1\!\left(\frac1{sc_j}\right).
\]
For independent unit exponentials \(E,F\), the single-product tail is
\[
\Pr(EF>z)=\int_0^\infty e^{-u-z/u}\,du
=2\sqrt z K_1(2\sqrt z)
\sim\sqrt\pi\,z^{1/4}e^{-2\sqrt z}.
\]
The final estimate follows directly from Laplace's method at the unique saddle \(u=\sqrt z\) (and does not depend on the Bessel notation). To pass to a finite sum, use the elementary subexponential convolution argument: cut the convolution at \(h(t)=t^{1/3}\) from both endpoints. Contributions where one summand is at most \(h\) reproduce the other summand's tail with relative error \(o(1)\), because \(h=o(\sqrt t)\). Where both summands exceed \(h\) and their sum exceeds \(t\), the sum of square-root exponents is larger than the dominant endpoint exponent by a constant multiple of \(\sqrt h\); the extra stretched-exponential factor dominates polynomial prefactors. Iterating proves that the tail of the sum is asymptotic to the sum of the individual tails. Only corners with largest \(c_j\) survive that comparison, giving the stated prefactor and exponent.

**5. Two distinct sharp rigidity principles.** Let \(Y_j=E_jF_j\), \(w_j=c_j/\mu\), and let \(\sigma\) range over all permutations of \(\{1,\ldots,m\}\). For every fixed vector \((Y_j)\), permutation averaging gives
\[
\frac1{m!}\sum_\sigma\sum_jw_{\sigma(j)}Y_j=\frac1m\sum_jY_j.
\]
Jensen's inequality and exchangeability of the \(Y_j\) yield the convex-order assertion. Since these variables have continuous, nondegenerate independent distributions, strict convexity yields strict inequality unless \(w_1=\cdots=w_m\), equivalent to equal \(\sin\theta_j\). The variance inequality is also Cauchy–Schwarz and has the same equality condition. Finally \(\sum_j\theta_j=(m-2)\pi\), so strict concavity of sine on \((0,\pi)\) gives
\[
\sum_j\sin\theta_j\le m\sin((m-2)\pi/m)=m\sin(2\pi/m),
\]
with equality exactly for equal interior angles. This proves the fixed-perimeter leading-loss extremum.

## Verification

The standalone standard-library program `verify.py` checks 16 exact rational instances of the double-survival integral against a binomial expansion, 983 successful independently computed hull-area-versus-corner-triangle identities on triangles and irregular quadrilaterals/pentagons, and the mean and variance of 140,000 independently generated product-sum samples for a four-corner example. Its actual successful output is: `VERIFY_OK exact_integrals=16 hull_geometry=983 product_samples=140000 moment_estimates=(1.99856,2.99274)`. Execute with `python verify.py` from the directory containing this file. None of these finite computations substitutes for the analytical limit, convex order, or tail argument.

## Relationship to prior work

Reitzner, Schütt, and Werner [1] study random convex hulls generated from the boundary of a simple polytope and give expected missing-volume asymptotics with an unspecified dimension/shape constant; their printed general error exponent is singular at dimension two. The present planar result instead makes the all-order mean coefficient explicit and determines the limiting distribution, its sharp upper tail, and convex-order and angle-rigidity consequences. Prochno, Schütt, Sonnleitner, and Werner [2] analyze polygonal boundary samples for **Hausdorff distance** and use corner Poisson limits; those corner limits provide natural precedents, but the area-product functional and its distributional/convex-order conclusions do not follow merely from their Hausdorff formulas. Schütt and Werner [3] study randomly inscribed polytopes for general convex bodies via curvature and surface area, not this explicit polygon-corner law. The full statements were compared, not merely their titles.

## Limitations

The polygon and its number of sides are fixed; neither a growing-side-count limit nor a dimension-three analogue is proved. The exponentially small expectation bound is a polygon-dependent big-O, not an exact closed finite-\(N\) expected area. The limiting tail is taken after the sampling limit \(N\to\infty\), not simultaneously with large \(t\). Equality for convex order is equal **sines** of interior angles, which is less restrictive than equiangularity; confusing these conditions would be false. Independent mathematical checking has not been performed. Priority overlap remains possible in older stochastic-geometry, extreme-value, or random-spacing literature not wholly searchable by abstracts or metadata.

## References

1. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917, first publicly submitted 14 November 2019; *Discrete & Computational Geometry* 69 (2023), 453–504. https://arxiv.org/abs/1911.05917
2. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870, first publicly submitted 3 April 2024. https://arxiv.org/abs/2404.02870
3. C. Schütt and E. M. Werner, *Polytopes with vertices chosen randomly from the boundary of a convex body*, *Geometric Aspects of Functional Analysis*, Lecture Notes in Mathematics 1807 (2003), 241–422. https://case.edu/artsci/math/werner/publications/rpbd.pdf
