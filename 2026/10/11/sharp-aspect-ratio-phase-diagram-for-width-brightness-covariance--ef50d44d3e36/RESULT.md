# Sharp aspect-ratio phase diagram for width–brightness covariance of orthotopes

## Finding

Let \(d\ge2\) be an integer and \(K=\prod_{i=1}^d[0,a_i]\subset\mathbb R^d\) an orthotope with \(a_i>0\). For one and the same uniformly random normal \(U\in S^{d-1}\), let \(W(U)\) be the length of the projection of \(K\) onto the line spanned by \(U\), and let \(B(U)\) be the \((d-1)\)-volume of its projection onto \(U^\perp\). Write
\[
V=\prod_{i=1}^d a_i,\quad Q=\left(\sum_i a_i\right)\left(\sum_i a_i^{-1}\right),\quad
\mu_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\quad
\beta_d=\mu_d^2-\frac{2}{\pi d}>0,\quad T_d=\frac{1-2/\pi}{\beta_d}>d^2.
\]
Then the **exact mixed covariance** is
\[
\boxed{\operatorname{Cov}(W,B)=V\left(1-\frac2\pi-\beta_d Q\right).}
\]
In particular, its sign depends on the side lengths only through \(Q\), and the sign is positive, zero, or negative exactly as \(Q<T_d\), \(Q=T_d\), or \(Q>T_d\).

More strongly, fixing **only the aspect ratio** \(R=\max_i a_i/\min_i a_i\ge1\) gives the entire sharp range
\[
\boxed{
\left(d-2+\sqrt R+R^{-1/2}\right)^2
\le Q\le
 d^2+\left\lfloor\frac{d^2}{4}\right\rfloor\left(R+R^{-1}-2\right).
}
\]
Every intermediate value occurs among orthotopes of aspect ratio exactly \(R\). If \(R>1\), the left equality holds precisely, up to permutation and common scale, at the side lengths
\(1,R,\sqrt R,\ldots,\sqrt R\); the right equality holds precisely at two-level side lengths \(1\) and \(R\) occurring in groups whose cardinalities differ by at most one. For \(d=2\), the two bounds coincide.

Define the **sharp universal-positive threshold** \(R_-(d)\) and **sharp universal-negative threshold** \(R_+(d)\) by
\[
\begin{gathered}
k_d=\left\lfloor\frac{d^2}{4}\right\rfloor,\qquad
z_d=2+\frac{T_d-d^2}{k_d},\qquad
R_-(d)=\frac{z_d+\sqrt{z_d^2-4}}{2},\\
s_d=\sqrt{T_d}-(d-2),\qquad
R_+(d)=\left(\frac{s_d+\sqrt{s_d^2-4}}2\right)^2.
\end{gathered}
\]
They satisfy \(1<R_-(d)\le R_+(d)\), with equality only when \(d=2\). For fixed \(R\), the covariance is strictly positive for **all** such boxes if \(1\le R<R_-(d)\), and strictly negative for **all** such boxes if \(R>R_+(d)\). For \(d\ge3\) and \(R_-(d)<R<R_+(d)\), there exist boxes with positive, zero, and negative covariance, all with that same aspect ratio. At either threshold the relevant extremal family has exactly zero covariance and all nonextremizers have the corresponding strict sign. In the plane, the two thresholds coincide and there is no coexistence interval.

Finally,
\[
\lim_{d\to\infty}R_-(d)=\frac{z_\infty+\sqrt{z_\infty^2-4}}2,
\quad z_\infty=2+4(\pi-3),
\qquad
\lim_{d\to\infty}\frac{R_+(d)}{d^2}=(\sqrt{\pi-2}-1)^2.
\]
The limiting constants are approximately \(2.08727767287\) and \(0.00468586705\), respectively. Thus the coexistence window spans a bounded-to-quadratic pair of aspect-ratio scales as the dimension increases.

## Assumptions and scope

The random normal is Haar-uniform on the complete unit sphere; the two projections use the *same* normal, not independent normals. Width and brightness are ordinary Euclidean measures with no unit-area or unit-volume normalization. All edge lengths are strictly positive and \(d\) is any fixed integer at least two. The extremal assertions quantify over all positive orthotopes whose maximum-to-minimum edge ratio equals the prescribed \(R\). Reflection, translation, and permutation of axes leave the conclusions unchanged. There is no claim for general parallelotopes, other convex bodies, or nonuniform directional sampling.

## Proof

**Projection identities.** Each edge of \(K\) contributes independently to its support-function difference, so
\[
W(U)=\sum_{i=1}^d a_i|U_i|.
\]
The Cauchy projection formula applied to the pairs of opposite facets (or direct orthogonal projection of those facets) gives
\[
B(U)=\sum_{i=1}^d\left(\prod_{j\ne i}a_j\right)|U_i|
=V\sum_{i=1}^d a_i^{-1}|U_i|.
\]
For uniform \(U\), its squared coordinates have the Dirichlet law with all parameters \(1/2\). Beta integration yields
\[
\mathbb E|U_i|=\mu_d,\qquad \mathbb E|U_i|^2=\frac1d,\qquad
\mathbb E|U_iU_j|=\frac2{\pi d}\quad(i\ne j).
\]
Thus
\[
\mathbb E(WB)=V\left[1-\frac2\pi+\frac{2Q}{\pi d}\right],
\qquad
\mathbb EW\,\mathbb EB=V\mu_d^2 Q.
\]
Subtracting proves the covariance formula. To justify \(\beta_d>0\) without a gamma inequality, condition on \(|U_1|^2=x\). Then \(\mathbb E(|U_2|\mid |U_1|^2=x)\) is a positive constant times \(\sqrt{1-x}\); this is strictly decreasing in \(x\). Since \(|U_1|\) is strictly increasing in \(x\), their covariance is strictly negative. But this covariance equals \(2/(\pi d)-\mu_d^2\). At equal edge lengths, \(B\) is a positive multiple of \(W\) and \(\operatorname{Var}(W)>0\); substituting \(Q=d^2\) shows \(T_d>d^2\).

**Sharp range at fixed aspect ratio.** Scale the minimum edge to \(1\) and relabel so the first and last edges are \(1\) and \(R\). Put \(z_i=\log a_i\), with endpoints fixed at \(0\) and \(L=\log R\). Then
\[
Q(z)=\sum_{i,j}e^{z_i-z_j}.
\]
This is convex as a function of the free logarithms, and strictly convex when the endpoints are distinct. It is unchanged when all free logarithms are replaced by \(L-z_i\), since this reflection interchanges the two fixed endpoint values and interchanges the two factors in \(Q\). Convexity at the midpoint of a configuration and its reflected configuration therefore forces the unique free-coordinate minimum at \(z_i=L/2\), giving the stated \(Q_{\min}\). A convex function on the logarithmic cube attains its maximum at a vertex. Strict convexity in each free coordinate excludes nonvertices for \(R>1\). A vertex has \(k\) edges of length \(1\) and \(d-k\) of length \(R\), giving
\[
Q=d^2+k(d-k)(R+R^{-1}-2).
\]
The integer maximum of \(k(d-k)\) is \(\lfloor d^2/4\rfloor\), giving \(Q_{\max}\) and its equality cases. The connected parameter cube maps continuously to the real line under \(Q\); hence all values between the extrema occur. The \(d=2\) statement follows directly with no free coordinates.

**Thresholds and dimensions.** Both extremal functions of \(R\) are continuous and strictly increasing for \(R>1\), start at \(d^2\), and diverge. Their unique crossings of \(T_d>d^2\) are obtained by solving the displayed quadratics for \(R_-\) and \(\sqrt{R_+}\). Since \(Q_{\min}\le Q_{\max}\), one has \(R_-\le R_+\), with strict inequality for \(d\ge3\) because the distinct configurations attain different \(Q\) values whenever \(R>1\). The exact sign classification and endpoint equalities follow. Finally, the gamma-ratio expansion
\[
\mu_d^2=\frac2{\pi d}+\frac1{\pi d^2}+O(d^{-3})
\]
gives \(T_d=(\pi-2)d^2(1+O(d^{-1}))\). Substitute this into the two quadratic crossing equations to obtain both asymptotic limits.

## Verification

The standalone file `verify.py` independently evaluates the spherical mixed covariance from uniform Gaussian directions, checks the sharp formulas on random and binary side-length configurations in dimensions \(2\) through \(12\), verifies threshold substitution, and compares high-dimensional limits. Running `python verify.py` using the Python standard library produced `VERIFY_OK 6436`. The sampled directions and finite checks are supplementary; the statements for all dimensions and all orthotopes follow only from the preceding proof.

For orientation, \(R_-(2)=R_+(2)\approx1.52017\), \(R_-(3)\approx1.72913\), and \(R_+(3)\approx1.88197\). A cube has strictly positive covariance, whereas the \(1\times1\times2\) box has strictly negative covariance under the same-normal coupling.

## Relationship to prior work

Kabluchko–Litvak–Zaporozhets (2015) derive width moments and Gaussian representations for regular polytopes, including cubes; their general formulas supply a well-established background for the one-dimensional marginal computations. Finch (2011) obtains low-dimensional cube and tetrahedron width moments. Both were inspected in their mathematical sections: neither asserts this joint width–hyperplane-brightness aspect-ratio classification. The known general covariance-of-spherical-coordinate identity makes the mixed-covariance expansion a relatively elementary step. The substantive result here is the complete all-dimensional *sharp* phase diagram with both different extremal geometries and both high-dimensional threshold scales, not the assertion that a second mixed moment can be computed.

Abas (2026) gives general weighted-box width-distribution and moment tools, and a separate width–brightness treatment for three-dimensional polytopes. Their accessible abstracts indicate relevant stronger marginal machinery, but their complete manuscripts could not be inspected. Those results could imply the covariance identity by polarization; whether they or other sources already include the sharp joint aspect-ratio phase diagram remains a historical-comparison risk.

## Limitations

All findings concern axis-orthogonal boxes and a shared direction. The sign of covariance does not determine the full joint law, and it is not an invariant for arbitrarily oriented parallelotopes. The finite verifier is neither an exhaustive enumeration of continuous parameters nor an independent mathematical certification. The exact covariance identity can be obtained from familiar spherical moments; novelty and value rest on the full optimized sign classification. Incomplete access to newer weighted-projection manuscripts leaves a residual originality risk.

## References

1. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first public 2015-11-26, https://arxiv.org/abs/1511.08479 .
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first public 2011-10-04, https://arxiv.org/abs/1110.0671 .
3. O. Abas, *Width distributions for rectangular boxes*, arXiv:2608.03305, 2026, https://arxiv.org/abs/2608.03305 (abstract inspected; complete text unavailable).
4. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, 2026, https://arxiv.org/abs/2609.26202 (abstract inspected; complete text unavailable).
