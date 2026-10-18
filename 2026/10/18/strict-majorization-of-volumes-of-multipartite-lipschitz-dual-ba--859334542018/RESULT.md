# Strict majorization of volumes of multipartite Lipschitz dual balls

## Finding
Let \(k\ge2\), let \(n_1,\ldots,n_k\ge1\) be integers, and put \(N=\sum_i n_i\). On a disjoint union of \(k\) parts of these sizes assign distance \(1\) between different parts and distance \(t\in[1,2]\) between distinct vertices in one part. Write \(Q_{t,\mathbf n}\) for the dual unit ball of the associated real Lipschitz-free space, normalized by fixing any one vertex value to zero, and \(V_t(\mathbf n)\) for its \((N-1)\)-dimensional Lebesgue volume in those anchored coordinates. Then
\[
\boxed{V_t(\mathbf n)=N+\sum_{i=1}^k n_i(n_i-1)\int_1^t r^{n_i-2}(2-r)^{N-n_i}\,dr.}
\tag{1}
\]
The summands for singleton parts are defined to be zero. The endpoint is the finite binomial-tail formula
\[
\boxed{V_2(\mathbf n)=N\left(1+\sum_{i=1}^k\frac{\sum_{j=0}^{n_i-2}\binom{N-1}{j}}{\binom{N}{n_i}}\right),}
\tag{2}
\]
with an empty numerator sum equal to zero.

For every fixed \(N\ge k\ge2\) and every \(1<t\le2\), \(V_t\) is **strictly Schur-convex** on unordered positive-integer \(k\)-partitions of \(N\): if \(\mathbf n\) strictly majorizes \(\mathbf m\), then \(V_t(\mathbf n)>V_t(\mathbf m)\). Consequently, the balanced part-size vector, whose sizes differ by at most one, uniquely minimizes \(V_t\) up to permutation, and \((N-k+1,1,\ldots,1)\) uniquely maximizes it up to permutation. In degenerate cases with only one unordered composition both descriptions coincide. At \(t=1\), every volume equals \(N\), so the inequality is not strict.

For fixed \(k\ge3\), along balanced compositions as \(N\to\infty\),
\[
\boxed{\frac{V_2(\mathbf n_{\mathrm{bal}})}{N}\longrightarrow\frac{k-1}{k-2}.}
\tag{3}
\]
For two balanced parts, the distinct critical law is
\[
\boxed{V_2(\mathbf n_{\mathrm{bal}})\sim \sqrt{\frac\pi8}\,N^{3/2}.}
\tag{4}
\]
For every fixed \(k\ge2\), the maximal composition obeys
\[
\boxed{V_2(N-k+1,1,\ldots,1)\sim2^{N-1}(k-1)!\,N^{2-k}.}
\tag{5}
\]
Thus the volume ordering holds for every interpolation parameter, while balanced and maximally concentrated part sizes have sharply different volume-growth rates at the graph-metric endpoint.

## Assumptions and scope
All scalar fields and normed spaces are real. Distinct vertices in different parts have metric distance one; within a part of size at least two the distance is \(t\). The triangle inequality follows from \(t\le2\) and \(t\ge1\). Fix a vertex \(o\) and identify Lipschitz potentials modulo constants with \(f(o)=0\). The dual ball is
\[
Q_{t,\mathbf n}=\left\{f(o)=0:\ |f(x)-f(y)|\le1\text{ across parts},\quad|f(x)-f(y)|\le t\text{ inside a part}\right\}.
\]
Volumes are calculated with respect to the \(N-1\) nonbasepoint potential coordinates; changing the anchor acts by a unimodular integer matrix of determinant \(\pm1\). Intrinsic Euclidean volume in the zero-sum hyperplane is \(V_t/\sqrt N\), not \(V_t\) itself, because the anchored-to-centered Gram matrix has determinant \(1/N\).

For positive integer compositions \(\mathbf n,\mathbf m\) of equal \(N\) and equal length \(k\), \(\mathbf n\) *strictly majorizes* \(\mathbf m\) if their decreasing rearrangements are different and all leading partial sums for \(\mathbf n\) are at least the corresponding sums for \(\mathbf m\).

## Proof
**Exact range decomposition.** The map taking anchored potentials to coordinates relative to any one selected vertex is a linear map of determinant \(\pm1\). Apart from a null set, every admissible potential has a unique minimum and maximum. Denote their spread by \(r\). For \(r\le1\), choose the minimum vertex in \(N\) ways and set its value to zero. Every other potential independently belongs to \([0,1]\), and all inequalities are satisfied. The \(N\) pieces contribute volume \(N\).

Suppose \(r>1\). The minimizing and maximizing vertices must lie in the same part \(A_i\); otherwise the cross-part constraint would force \(r\le1\). Choose the ordered pair of extremes \((a,b)\in A_i^2\) with \(a\ne b\), shift \(f(a)=0\), and write \(f(b)=r\), where \(1<r\le t\). Each of the remaining \(n_i-2\) vertices in \(A_i\) lies independently in \([0,r]\). Every vertex outside \(A_i\) must lie in the intersection \([-1,1]\cap[r-1,r+1]=[r-1,1]\), an interval of length \(2-r\). Conversely, each such assignment satisfies every distance constraint: all vertices within the distinguished part have spread at most \(r\le t\); the outside vertices have spread at most \(2-r\le1\); and every cross-part difference is at most one. The change of variables from potentials to \(r\) and the free coordinates has absolute Jacobian one. Hence one ordered extreme pair contributes \(\int_1^t r^{n_i-2}(2-r)^{N-n_i}\,dr\), and summing the \(n_i(n_i-1)\) ordered pairs proves (1), including its boundaries by continuity. For \(n_i=1\), no such pair exists.

**Endpoint.** Substitute \(r=2u\) and express the upper incomplete beta integral in (1) as the lower binomial tail with \(N-1\) trials. This gives, for \(2\le s\le N-1\),
\[
s(s-1)\int_1^2r^{s-2}(2-r)^{N-s}\,dr
=\frac{N}{\binom Ns}\sum_{j=0}^{s-2}\binom{N-1}{j},
\]
which proves (2). The case \(s=1\) contributes zero.

**Strict convexity and global extremizers.** Fix \(N\) and \(t>1\) and put \(F(s)=s(s-1)\int_1^t r^{s-2}(2-r)^{N-s}\,dr\) for integers \(1\le s\le N-1\), with \(F(1)=0\). For \(2\le s\le N-2\), write \(u=2-r\) and \(d=r-u=2(r-1)\). The integrand's second discrete difference is
\[
r^{s-3}u^{N-s-1}\left[2u^2+4sud+s(s+1)d^2\right]>0
\]
for all \(1<r<t\). Therefore \(F(s+1)-2F(s)+F(s-1)>0\). A transfer of one unit from a smaller part to a part at least as large strictly increases \(\sum_iF(n_i)\). By the standard integer majorization transfer characterization this proves strict Schur-convexity. Repeated transfers attain exactly the most concentrated and balanced compositions, establishing both extremizers. When \(t=1\), all integrals vanish and equality holds.

**Asymptotics.** For a part size \(s/N\to p\in(0,1/2)\), substitute \(r=1+y/N\) into its summand. The normalized summand is
\[
\frac{F(s)}N=\frac{s(s-1)}{N^2}\int_0^N\left(1+\frac yN\right)^{s-2}\left(1-\frac yN\right)^{N-s}dy.
\]
The integrand tends pointwise to \(e^{(2p-1)y}\). Its logarithm is concave in \(y\), with derivative at zero eventually bounded above by a negative constant, so dominated convergence gives \(F(s)/N\to p^2/(1-2p)\). Along balanced \(k\ge3\) compositions, \(p=1/k\), yielding (3).

For balanced \(k=2\), let \(s\) be either part size, within one of \(N/2\). The binomial sum in (2) is \(2^{N-2}(1+o(1))\) by the central limit theorem for \(\operatorname{Bin}(N-1,1/2)\), while \(\binom Ns=2^N\sqrt{2/(\pi N)}(1+o(1))\) by Stirling's formula. Substituting two contributions into (2) yields (4). For the maximal vector, only its large part \(s=N-k+1\) contributes. Equation (2) becomes \(V_2=N[1+(2^{N-1}-O_k(N^{k-1}))/\binom N{k-1}]\). With fixed \(k\), \(\binom N{k-1}\sim N^{k-1}/(k-1)!\), proving (5).

## Verification
The standard-library script `check_volumes.py` independently counts lattice points in dilations of the rational metric's dual polytope. Because the directed-incidence constraint matrix is totally unimodular, after multiplying the potential coordinates by the denominator of \(t\), all vertices have integral coordinates. The leading Ehrhart coefficient recovered by exact finite differences is the scaled Euclidean-coordinate volume. Ten exact volume checks for \(t=3/2\) and \(t=2\) agree with (1), including both bipartite and multipartite examples.

Additional exact checks compared (1) and (2) for 492 multipartitions and the predicted strict majorization inequality for 2230 comparable distinct unordered pairs, each at both \(t=3/2\) and \(t=2\). Execution produces `EXACT_MULTIPARTITE_VOLUME_PASS ehrhart=10 endpoints=492 majorization_pairs=2230`. These finite computations are independent corroborations; the unlimited-dimensional and real-parameter claims are proved analytically above. For example, at \(N=6,k=3,t=2\), the balanced vector \((2,2,2)\) has volume \(36/5\), while the maximizer \((4,1,1)\) has volume \(62/5\).

## Relationship to prior work
Aliaga (2021 preprint, primary MSC 46B20) establishes an extreme-point support theorem for Lipschitz-free Banach spaces, not an interior-volume formula. Alexander, Fradelizi, García-Lirola and Zvavitch (2019 preprint), *Geometry and volume product of finite dimensional Lipschitz-free spaces*, evaluate the equilateral unit-ball volume and investigate global volume products. Their equilateral \(t=1\) reference value is used here and is not new. Higashitani, Jochemko and Michałek (2018 preprint) classify facets of symmetric edge polytopes of complete multipartite graphs, including the graph-metric endpoint; their combinatorial facet theorem is credited rather than presented as new. D'Alì, Juhnke-Kubitzke and Koch (2023 preprint) treat lattice-point enumerations for broader regular-matroid polytopes, without a complete-multipartite dual-volume extremum over part-size profiles.

More specific previously recorded calculations concern complete bipartite metrics, one lengthened distance in an equilateral metric, and complete split graphs. Moreover, an exact signed-chain-polytope volume theorem for a two-level poset identifies, after a coordinate reflection and adding a universal root, precisely the complete tripartite graph \(K_{1,p,q}\) at \(t=2\); it includes a strict imbalance law for this subfamily. **That entire three-part endpoint subfamily is known, not newly claimed here.** The new generality includes all-part sizes at \(k\ge3\), strict majorization across all such profiles and the full continuous deformation \(1<t<2\). A separate treatment of the identical interpolated complete-multipartite metrics counts facets for \(1<t<2\), not continuous volumes or their strict majorization ordering. Likewise, exact Euclidean inradius and graph-spread calculations for complete multipartite symmetric edge polytopes optimize the most distant dual point, not the total dual volume. The contribution here is the single general volume identity (1), its all-partition strict Schur-convexity, and the sharp balanced/concentrated asymptotics across all \(k\ge2\).

## Limitations
The volume uses anchored coordinate Lebesgue measure, not unnormalized intrinsic Euclidean volume or the volume of the primal Lipschitz-free unit ball. The graph consists of complete multipartite parts with one shared within-part distance; no claim is made for general graphs, arbitrary missing-edge lengths, or independently weighted parts. The strict inequality requires \(t>1\) and a genuinely distinct pair of part-size profiles related by majorization. The case \(k=2\) includes previously studied volume values and should not be mistaken for a new bipartite volume formula. The stated asymptotics hold for fixed \(k\); they do not claim uniformity when \(k\) grows with \(N\). Prior equivalent formulations under root-polytope, graph-potential, or transportation-norm terminology may remain outside the inspected literature; independent scientific assessment is not asserted.

## References
1. Matthew Alexander, Matthieu Fradelizi, Luis C. García-Lirola, Artem Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1, first public 2019-11-24, https://arxiv.org/abs/1911.10642.
2. Akihiro Higashitani, Katharina Jochemko, Mateusz Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, first public 2018-07-20, https://arxiv.org/abs/1807.07678.
3. A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933v1, https://arxiv.org/abs/2307.04933.
4. *Exact volume and strict imbalance law for two-level signed-chain polytopes*, accessible 2026 mathematical research record (complete \(K_{1,p,q}\) endpoint subfamily); its graph interpretation and integral formula were compared directly.
5. Ramón J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219v1, first public 2021-02-01, MSC primary 46B20, https://arxiv.org/abs/2102.01219.
