# Optimal simultaneous facet-center interpolation on Euclidean hypercubes

## Finding

Fix an integer \(d\ge3\). Equip the finite set
\[
V_d=\{-1,1\}^{d}\subset\mathbb R^d
\]
with its inherited **Euclidean**, not Hamming or graph, distance. Set
\[
F_d=\{s e_i:1\le i\le d,\ s\in\{-1,1\}\},\qquad S_d=V_d\cup F_d,
\]
where each \(s e_i\) is the centroid of the corresponding \((d-1)\)-dimensional facet. Let \(\operatorname{Lip}_0(X)\) denote real-valued functions on a finite metric set, modulo constants, with the Lipschitz seminorm. Consider all real-linear right inverses of restriction
\[
T:\operatorname{Lip}_0(V_d)\longrightarrow\operatorname{Lip}_0(S_d).
\]
The **unrestricted** minimum operator norm is
\[
\boxed{\lambda_d=
\frac{2}{2^{d-1}\sqrt{d-1}}
\sum_{k=0}^{d-1}\binom{d-1}{k}\sqrt{k}.}
\]
It is attained **simultaneously at every facet center** by the positive operator
\[
(T_*f)(v)=f(v)\quad(v\in V_d),\qquad
(T_*f)(s e_i)=2^{-(d-1)}\sum_{v\in V_d:\ v_i=s}f(v).
\]
The constants obey \(1<\lambda_3<\lambda_4<\cdots<\sqrt2\), with
\[
\lambda_3=\frac12+\frac1{\sqrt2},\qquad
\lim_{d\to\infty}\lambda_d=\sqrt2,\qquad
\lambda_d=\sqrt2\left(1-\frac1{8(d-1)}+O((d-1)^{-2})\right).
\]
In particular, ordinary arithmetic averaging over the vertices of each facet is globally optimal even when competitors may use **all** \(2^d\) vertex values, arbitrary real signed coefficients, and no symmetry. This is a simultaneous statement for all \(2d\) new points, not merely a one-point extension result.

## Assumptions and scope

All dimensions are integers \(d\ge3\). The domain and target are real scalar Lipschitz spaces modulo constants with **ambient Euclidean chord distances**. The operator norm is the supremum of the target Lipschitz seminorm over source functions with seminorm at most one. Linear extensions on the quotient correspond to constant-preserving linear extension formulas on unquotiented finite function spaces, once constants are anchored at a fixed vertex.

The side length of this cube is two; scaling the whole configuration uniformly leaves the operator norm unchanged. No result for arbitrary target Banach spaces, non-Euclidean metrics, other face dimensions, or uniqueness of the complete set of optimizers is claimed.

## Proof

**1. The binomial distances.** Put \(N=d-1\), and let \(K\) have binomial distribution \(\operatorname{Bin}(N,1/2)\). Define
\[
A_N=\mathbb E\sqrt K,\quad B_N=\mathbb E\sqrt{K+1},\quad
S_N=2A_N,\quad U_N=2B_N.
\]
For a vertex \(v\) lying on the facet centered at \(c=s e_i\), the average of \(\|v-w\|_2\) over the \(2^N\) vertices \(w\) of that facet is \(S_N\); here exactly \(K\) of the remaining coordinates disagree. The center-to-vertex distance is \(\sqrt N\). For \(v\) on the opposite facet, the corresponding average is \(U_N\), while \(\|v-c\|_2=\sqrt{N+4}\).

**2. Lower bound for every real-linear extension.** Let \(T\) be arbitrary. Average its conjugates over the finite signed-permutation isometry group of the cube, acting on source and target. The resulting extension \(\bar T\) has norm at most \(\|T\|\), because the conjugations are isometric and the operator norm is convex. It still preserves the original vertex values and constants.

At \(c=e_1\), invariance under the stabilizer of \(c\) implies that \((\bar T f)(c)\) is a combination of the two uniform facet means:
\[
(\bar T f)(e_1)=a\operatorname{Av}_{v_1=1}f(v)
+b\operatorname{Av}_{v_1=-1}f(v),\qquad a+b=1,
\]
for arbitrary **real** \(a,b\); positivity is not assumed. Define on the vertex set
\[
f(v)=\bigl\|(v_2,\ldots,v_d)-(1,\ldots,1)\bigr\|_2.
\]
Euclidean coordinate deletion and the reverse triangle inequality show that \(f\) is \(1\)-Lipschitz. At \(v_*=(1,\ldots,1)\), \(f(v_*)=0\). Both uniform facet means of \(f\) equal \(S_N\), so \((\bar T f)(e_1)=S_N\), irrespective of \(a,b\). Since \(\|e_1-v_*\|_2=\sqrt N\),
\[
\|T\|\ge\|\bar T\|\ge\frac{S_N}{\sqrt N}.
\]
This argument covers nonpositive, asymmetric and otherwise unrestricted real-linear extensions.

**3. Upper bound for simultaneous facet averaging.** Associate to each vertex its point mass and to each facet center the uniform probability measure on the vertices of that facet. The operator \(T_*\) integrates vertex functions against these measures. For any pair of target points the Lipschitz operator ratio equals the Kantorovich–Rubinstein dual norm of the difference of their measures divided by their Euclidean distance. In the finite setting this follows directly by taking the supremum over all source functions of Lipschitz constant at most one.

For two original vertices, the ratio is one. For a vertex and a facet center, the difference is a point mass minus a positive probability measure, whose transport cost is exactly the mean distance from the vertex. By Step 1 the possible ratios are \(S_N/\sqrt N\) and \(U_N/\sqrt{N+4}\).

For opposite facet centers \(s e_i,-s e_i\), the uniform facet distributions can be coupled by flipping coordinate \(i\), at cost two. Every source-support vertex and target-support vertex differ in coordinate \(i\), so two is also the minimum possible cost. The center distance is two; their ratio is one.

For facet centers \(s e_i,t e_j\) with \(i\ne j\), their uniform distributions agree on the vertices satisfying both signed coordinate constraints. Each has mass \(1/2\) remaining on a disjoint subcube. Any point of the first residual subcube differs from any point of the second in **both** coordinates \(i,j\), costing at least \(2\sqrt2\); matching the remaining coordinates attains this distance. Thus the exact transport cost is \(\sqrt2\), equal to the distance between the centers. Their ratio is again one. This exhausts every target-pair type. Consequently,
\[
\|T_*\|=\max\left\{1,\frac{S_N}{\sqrt N},\frac{U_N}{\sqrt{N+4}}\right\}.
\]

**4. The off-facet inequality.** For every integer \(N\ge2\),
\[
\frac{U_N}{\sqrt{N+4}}\le\frac{S_N}{\sqrt N},
\quad\text{equivalently}\quad
B_N\le\sqrt{\frac{N+4}{N}}\,A_N.
\]
Here is a uniform proof for \(N\ge4\), followed by exact small cases. Set \(m=N/2\). The elementary identity
\[
\sqrt t=\sqrt m+\frac{t-m}{2\sqrt m}
-\frac{(\sqrt t-\sqrt m)^2}{2\sqrt m}
\]
and \((\sqrt t-\sqrt m)^2\le(t-m)^2/m\) for \(t\ge0\) give
\[
A_N\ge\sqrt{N/2}\left(1-\frac1{2N}\right),
\]
since \(\mathbb EK=m\) and \(\operatorname{Var}(K)=N/4\). Jensen's inequality gives \(B_N\le\sqrt{N/2+1}\). The desired comparison follows from
\[
\left(1-\frac1{2N}\right)^2-\frac{N+2}{N+4}
=\frac{N-4}{N(N+4)}+\frac1{4N^2}\ge0
\quad(N\ge4).
\]
For \(N=2\), direct binomial expansion yields
\[
A_2=\frac{2+\sqrt2}{4},\qquad
B_2=\frac{1+2\sqrt2+\sqrt3}{4}<\sqrt3 A_2.
\]
For \(N=3\), it yields
\[
A_3=\frac{3+3\sqrt2+\sqrt3}{8},\qquad
B_3=\frac{3+3\sqrt2+3\sqrt3}{8}<\sqrt{7/3}\,A_3.
\]
Both strict inequalities can be checked by squaring, or with the rational bounds \(7/5<\sqrt2<3/2\), \(17/10<\sqrt3<7/4\), and \(3/2<\sqrt{7/3}\). Also \(S_N/\sqrt N>1\) for \(N\ge2\): the pointwise inequality \(\sqrt k\ge k/\sqrt N\) is strict for \(0<k<N\), an event of positive probability. Therefore \(\|T_*\|=S_N/\sqrt N\), equal to Step 2's lower bound. This proves optimality.

**5. Strict monotonicity and limit.** Let \(Y_1,Y_2,\ldots\) be independent Bernoulli random variables with success probability \(1/2\). The formula is
\[
\lambda_{N+1}=2\mathbb E\sqrt{\frac{Y_1+\cdots+Y_N}{N}},
\]
where \(\lambda_{N+1}\) is the value in cube dimension \(N+1\). Given \(N+1\) Bernoulli observations, randomly delete one, and condition on all \(N+1\) observations. The expected mean of the remaining \(N\) values equals the mean of all \(N+1\). Jensen's inequality for the strictly concave square-root function proves strict increase: the deletion mean is nonconstant with positive probability whenever the original sample contains both zeros and ones. The bounded law of large numbers gives convergence to \(2\sqrt{1/2}=\sqrt2\). A Taylor expansion around \(1/2\), using variance \(1/(4N)\), vanishing third centered moment, fourth centered moment \(O(N^{-2})\), and exponentially small binomial tails away from \(1/2\), yields the stated \(\sqrt2(1-1/(8N)+O(N^{-2}))\) expansion. All steps concern every integer \(N\ge2\), not a finite search.

## Verification

The accompanying `verify.py` uses the Python standard library. It enumerates every vertex–center pair and every center–center pair in cube dimensions \(3\) through \(8\). It compares all vertex–center ratios with the exact binomial predictions and checks center–center transport formulas against center distances. It also checks that the coordinate-deletion witness has the predicted facet expectation for seven real signed coefficient choices. The replay completed successfully: **7,152 vertex–center pairs and 365 center–center pairs**. Those computations corroborate the finite formulas; Step 2, Step 4 and Step 5 are the arguments for unrestricted optimality and all-dimensional scope.

## Relationship to prior work

Bruè–Di Marino–Stra (2018) construct linear Lipschitz extensions through random projections and give general norm estimates. Their random-measure viewpoint is relevant, but their full text does not give these exact cubical facet-center interpolation constants. Basso (first preprint 2023, revised 2024) surveys explicit extension estimates under general metric hypotheses; those bounds do not identify the sharp Euclidean facet-center configuration.

A separately indexed result on **a Euclidean cube's vertices plus its single center** derives a binomial one-point norm. Restricting to one facet in dimension \(d\) gives the same numerical necessary lower bound as its \((d-1)\)-dimensional center case. That earlier one-point statement **does not imply** that the minimum can be attained simultaneously at all \(2d\) facet centers: this requires the cross-center couplings and, crucially, the opposite-facet vertex inequality in Steps 3–4. Available summaries of that record do not state or imply the present compatibility theorem. Its complete text was not accessible, which is an explicitly retained bibliographic risk.

Known sharp interpolation results on simplex-face centroids, polytope edge midpoints, and the cube's single center treat different target configurations. No claim is made that the symmetry-averaging method itself is new.

## Limitations

The result is confined to real scalar linear extension on the explicitly specified finite Euclidean metric configuration and to \(d\ge3\). It does **not** claim a classification of all minimizing operators, sharp constants for square edge midpoints, general cubical faces of other codimensions, or Banach-valued data. Existing literature outside the materials inspected could provide equivalent coverage; an independent mathematical audit has not been performed.

## References

1. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533 (first public 2018-01-23). Full text: https://arxiv.org/html/1801.07533v1.
2. G. Basso, *Lipschitz extension theorems with explicit constants*, arXiv:2310.13554 (first public 2023-10-20). Full text: https://arxiv.org/html/2310.13554v3.
3. *Exponential snowflake threshold for linear extension from hypercube vertices*, public research-index summary dated 2026-10-11; complete material not accessed. The one-point statement is used only for overlap comparison, not as a premise of the proof.
