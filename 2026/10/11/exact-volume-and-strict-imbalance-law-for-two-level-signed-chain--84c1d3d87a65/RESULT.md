# Exact volume and strict imbalance law for two-level signed-chain polytopes

## Finding
For integers \(p,q\geq1\), let \(n=p+q\) and define the full-dimensional polytope
\[
\mathcal C_{p,q}=\left\{(x,y)\in\mathbb R^p\times\mathbb R^q:
 |x_i|\leq1,\ |y_j|\leq1,\ |x_i+y_j|\leq1\text{ for all }i,j\right\}.
\]
These are the singleton and two-element signed-chain inequalities for the complete height-two poset with \(p\) minimal and \(q\) maximal elements, in the signed-chain construction motivated by Beck and Hlavacek. The displayed halfspace definition, not any convention about chains, is the mathematical definition used here.

**Exact volume theorem.** With \(\operatorname{Vol}_n\) denoting ordinary Euclidean coordinate volume and with any expression multiplied by \(p(p-1)\) (or \(q(q-1)\)) omitted when that parameter is \(1\),
\[
\boxed{\operatorname{Vol}_n(\mathcal C_{p,q})=
 n+1+p(p-1)\int_1^2 s^{p-2}(2-s)^{q+1}\,ds
       +q(q-1)\int_1^2 s^{q-2}(2-s)^{p+1}\,ds.}
\]
This is a finite rational formula: for nonnegative integers \(a,b\),
\[
\int_1^2s^a(2-s)^b\,ds
=\sum_{j=0}^{a}\frac{(-1)^j2^{a-j}\binom aj}{b+j+1}.
\]

**Strict imbalance theorem.** At every fixed \(n\geq2\), the volume is symmetric in \(p,q\) and strictly increases as \(|p-q|\) increases along the permitted integer pairs. Consequently it is smallest at the balanced split (uniquely up to interchanging the two parts) and largest at \(\{p,q\}=\{1,n-1\}\), where
\[
\boxed{\operatorname{Vol}_n(\mathcal C_{1,n-1})=\frac{2^{n+1}-2}{n}.}
\]
For every fixed positive integer \(p\), its unbalanced high-dimensional asymptotic is
\[
\boxed{\operatorname{Vol}_{p+q}(\mathcal C_{p,q})
 \sim \frac{2^{p+q}(p+1)!}{q^p}\qquad(q\to\infty).}
\]
The ratio in this asymptotic tends to \(1\); neither \(p\) nor the coordinate scaling varies with \(q\).

## Assumptions and scope
The parameters \(p,q\) are integers at least \(1\). Euclidean volume uses the usual Lebesgue measure on the actual \(p+q\) coordinate axes, not normalized lattice volume and not the volume of a polar polytope. All inequalities are closed; boundaries have measure zero. The polytope contains an open neighborhood of the origin and is full-dimensional. If a signed-poset convention differs on chains of length two, the theorem remains precisely about the explicitly defined halfspace body above.

The graph interpretation is also literal: after the coordinate change \(y_j\mapsto-y_j\), \(\mathcal C_{p,q}\) is the rooted unit-Lipschitz polytope of the graph obtained by adjoining a universal root to \(K_{p,q}\), fixing the root potential at zero. The root-edge inequalities give the coordinate bounds, and the cross edges give the difference bounds. This identification is an equality of explicit polytopes, not an appeal to an external spectral or volume theorem.

## Proof
**1. Exact range decomposition.** Reflect the second group, setting \(v_j=-y_j\), and translate all coordinates by \(1\). Their new values \(u_i,v_j\) lie in \([0,2]\), and all cross-group differences have absolute value at most \(1\). Reflections and translations have absolute Jacobian determinant \(1\).

Let \(m\) and \(M\) be the minimum and maximum across the \(n\) coordinates, and put \(s=M-m\). If \(s\leq1\), every cross-group difference is at most \(1\). Up to measure-zero ties, choosing which coordinates realize the two extremes gives the volume
\[
 n(n-1)\int_0^1s^{n-2}(2-s)\,ds=n+1.
\]
Indeed the minimum can range over an interval of length \(2-s\) and the \(n-2\) remaining coordinates range independently inside the span of length \(s\).

Suppose \(s>1\) and the point satisfies all cross-group constraints. The minimum and maximum cannot lie in different groups, because that pair would differ by more than \(1\). If they both lie in the first group, there are \(p(p-1)\) ordered choices for the two extreme coordinates. Their \(p-2\) companions each range over the interval of length \(s\). Each second-group coordinate must lie in
\[
 [M-1,m+1],
\]
which has length \(2-s\) and is contained in \([0,2]\) for \(1<s\leq2\). The minimum \(m\) ranges over an interval of length \(2-s\). The total contribution is therefore
\[
 p(p-1)\int_1^2 s^{p-2}(2-s)^{q+1}\,ds.
\]
Interchanging the groups supplies the remaining term. The three cases are pairwise disjoint outside null sets and exhaust all feasible points. Expanding \(s^a=(2-(2-s))^a\) and substituting \(t=2-s\) evaluates the integrals as the displayed finite rational sums.

**2. Strict imbalance.** In the two integrals put \(t=(2-s)/s\). A direct Jacobian computation gives
\[
\operatorname{Vol}_n(\mathcal C_{p,q})-(n+1)
 =2^n\int_0^1\frac{p(p-1)t^{q+1}+q(q-1)t^{p+1}}{(1+t)^{n+1}}\,dt.
\]
Fix \(n\), put \(a=n/2\), \(d=(p-q)/2\), and \(\lambda=-\log t\) for \(0<t<1\). The numerator is precisely
\[
 2t^{a+1}\left[\bigl(a(a-1)+d^2\bigr)\cosh(\lambda d)
 +(2a-1)d\sinh(\lambda d)\right].
\]
Here \(a\geq1\). The bracket is even in \(d\) and strictly increasing with \(|d|\) for positive \(|d|\): every factor of its two summands is nonnegative and either \(d^2\) or \(d\sinh(\lambda d)\) increases strictly. Integrating against the positive denominator proves the strict imbalance assertion for all distinct permitted values of \(|p-q|\). For \(p=1\), conditioning on its one coordinate gives \(2\int_0^1(2-t)^{n-1}\,dt=(2^{n+1}-2)/n\), proving the endpoint maximum formula.

**3. Fixed-part asymptotic.** For fixed \(p\) and increasing \(q\), the constant term \(n+1\) is polynomial and the first excess term is \(O_p(q^{-1})\). In the second excess term, substitute \(t=2-s\) and then \(u=qt/2\):
\[
 q(q-1)\int_1^2s^{q-2}(2-s)^{p+1}\,ds
 =2^{p+q}q^{-p}\left(1-\frac1q\right)
 \int_0^{q/2}u^{p+1}\left(1-\frac uq\right)^{q-2}\,du.
\]
The integrand converges pointwise to \(u^{p+1}e^{-u}\). For all sufficiently large \(q\), \((1-u/q)^{q-2}\leq e^{-u/2}\) on the integration range, giving an integrable dominating function. Dominated convergence yields the limit \(\Gamma(p+2)=(p+1)!\). The polynomial and smaller terms are negligible relative to the exponential main term. This proves the claimed asymptotic.

## Verification
The standalone `verify.py` is executable with Python 3 and uses `fractions.Fraction` for the exact identities. It checks \(36\) ordered parameter pairs with \(1\leq p,q\leq6\) by two different exact integrations: the range-extrema formula above and a conditional decomposition by positive/negative extrema of the first group. It also checks volume symmetry, normalized-volume integrality in those cases, and strict imbalance for total dimensions \(4\) through \(12\). When SciPy and NumPy are installed, seven independent halfspace-to-vertex-to-convex-hull calculations compare volumes to the exact answer in dimensions \(2\) through \(5\). All checks passed on the packaged code before writing this result. The finite computations do not constitute the proof for all parameters: that proof is the range decomposition, hyperbolic monotonicity, and dominated convergence above.

Some exact examples: \(\operatorname{Vol}(\mathcal C_{1,1})=3\), \(\operatorname{Vol}(\mathcal C_{1,2})=14/3\), \(\operatorname{Vol}(\mathcal C_{2,2})=6\), \(\operatorname{Vol}(\mathcal C_{2,3})=41/5\), and \(\operatorname{Vol}(\mathcal C_{3,3})=49/5\).

## Relationship to prior work
Beck and Hlavacek introduce signed order and signed chain polytopes and their type-B context [1, Definitions 1.5–1.6 and 6.4–6.5]; their Sections 5–6 emphasize Gorenstein and antichain properties rather than the volume profile of complete two-level posets. The present statement evaluates the specified two-level halfspace body's volume and gives a strict imbalance law and a fixed-part asymptotic. Even at \(p=q=2\), its volume is \(6\), whereas the signed order polytope for the corresponding ordinal sum has volume \(2^4(2!2!)/4!=8/3\), so the classical order–chain volume coincidence cannot be assumed here.

The polytope is also a rooted graph Lipschitz polytope, in the general terminology of Gordon and Petrov [2]; their inspected results concern face structures and generic metrics, not this complete bipartite cone-graph volume formula. The survey and comparison of Lipschitz polytopes with symmetric edge polytopes in D’Alì, Delucchi, and Michałek [3] develops metric duality, facets, Ehrhart counts, and volume for the symmetric edge polytopes themselves, rather than an evaluated volume of the present polar body. Tsuchiya's volume theorem [4] concerns twinned chain polytopes defined as convex hulls of two ordinary chain polytopes, a different operation from the simultaneous signed-chain inequalities here. These distinctions are mathematical comparisons, not claims that every conceivable equivalent source has been exhausted.

## Limitations
No assertion is made about a general signed poset, an arbitrary graph, Ehrhart coefficients, or the number of vertices of this body. The proof is an ordinary Euclidean-volume proof and does not provide a complete combinatorial classification of the facets. One older or differently named Lipschitz-polytope volume identity could imply this result; the available primary-source comparisons did not establish such coverage. The exact choice of a two-element signed-chain convention in the originating paper is not required by this theorem because the halfspace body is defined independently and explicitly.

## References
[1] M. Beck and M. Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409v1, publicly posted 2023-11-08, especially Sections 1–2 and 6, https://arxiv.org/abs/2311.04409.

[2] Y. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848v1, https://arxiv.org/abs/1608.06848.

[3] A. D’Alì, E. Delucchi, and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, Electronic Journal of Combinatorics 29 (2022), article P3.24, https://d-nb.info/1273981944/34.

[4] A. Tsuchiya, *Volume, Facets and Dual Polytopes of Twinned Chain Polytopes*, arXiv:1512.08332v2, Theorem 1.3, https://arxiv.org/abs/1512.08332.
