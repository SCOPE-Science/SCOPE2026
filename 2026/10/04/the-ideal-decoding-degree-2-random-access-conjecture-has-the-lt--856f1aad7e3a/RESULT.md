# The ideal-decoding degree-\(2\) random-access conjecture has the LT limit
## Finding

For every \(a\in(0,1)\), let \(G_k(x,y)\) be the recovery-complete construction of Boruchovsky–Elishco–Gabrys–Gruica–Tamo–Yaakobi, with \(x\) distinct weight-\(2\) columns on each pair support and \(y\) copies of each weight-\(1\) information column, and choose \(y/x\to a(k-1)/(2(1-a))\) as \(x\to\infty\). Then, under ideal linear decoding, \[\lim_{k\to\infty}\lim_{x\to\infty}\frac{T_{\max}(G_k(x,y))}{k}=\int_0^1\frac{-\log(1-t)}{a+2(1-a)t}\,dt.\] Consequently this construction has the same degree-\(2\) asymptotic objective as the binary fully symmetric LT ensemble under peeling. Its unique optimal weight-\(1\) mass is \(a_\star=0.155473700361088\ldots\), with optimal normalized expectation \(0.793933444597171\ldots\), thereby proving the explicit degree-\(2\) ideal-ratio conjecture of Hofmeister–Bitar–Yaakobi.

## Assumptions and scope

For each integer \(k\ge 2\), use the recovery-complete generator matrix \(G_k(x,y)\) of Boruchovsky, Elishco, Gabrys, Gruica, Tamo, and Yaakobi. It has \(y\) copies of every standard basis column and \(x\) distinct weight-\(2\) columns on each unordered pair of coordinates. The field may grow with \(k\) and \(x\), as allowed by the construction.

Fix \(a\in(0,1)\). The total probability mass on weight-\(1\) columns is
\[
a_k=\frac{ky}{ky+\binom{k}{2}x}.
\]
Thus \(a_k\to a\) for fixed \(k\) precisely when
\[
\frac{y}{x}\to \frac{a(k-1)}{2(1-a)}.
\]
The inner limit below is taken along integer pairs \((x,y)\) with this ratio and along fields large enough for the recovery-complete construction.

The random-access expectation \(T_{\max}\) is for ideal linear-span decoding, not peeling decoding.

## Proof

Write
\[
\beta=2(1-a).
\]
Poissonize the read process at total rate \(k\). If \(\tau\) is the discrete number of reads until the target information symbol is recoverable, the continuous stopping time is the sum of \(\tau\) independent exponential holding times of mean \(1/k\). Hence
\[
\mathbb E[\tau]/k=\mathbb E[T_{\mathrm{Pois}}],
\]
so Poissonization preserves the normalized expectation exactly.

For fixed \(k\), pass first to \(x\to\infty\). A particular weight-\(2\) column copy then has vanishing chance to be sampled twice on every bounded time interval. Repeated samples from the same pair support are therefore distinct columns in the limit. This passage is valid also in expectation: the target's own weight-\(1\) column is sampled at asymptotic rate \(a\), so the stopping-time tail is uniformly bounded by \(e^{-ar}\).

In the limiting process, every vertex has an independent direct-mark Poisson process of rate \(a\), and every unordered edge support has an independent Poisson process of rate
\[
\lambda_k=\frac{\beta}{k-1}.
\]
Recovery completeness gives an exact graph criterion for the target vertex. A direct mark in its connected edge component recovers that marked vertex and then propagates along all sampled tree edges. A simple cycle recovers all of its cycle vertices, after which recovery propagates along attached trees. Two distinct columns on the same pair support recover both endpoints and act as a length-\(2\) cycle.

Conversely, if the target edge component is a simple tree and contains no marked vertex, then the target is not recoverable. Indeed, for each sampled edge column, both endpoint coefficients are nonzero. Root the tree at the target and assign a nonzero dual coordinate at the root; recursively choose each child coordinate so that the dual vector annihilates the unique edge column joining it to its parent. This produces a dual vector supported on the tree, nonzero at the target, annihilating all sampled columns in that component. Columns outside the component have disjoint support. Hence the target basis vector is not in the sampled span.

Therefore the target is unrecovered at time \(r\) exactly when its component is an unmarked simple tree. If that component has \(j\) vertices, choose its other \(j-1\) vertices, choose one of the \(j^{j-2}\) labeled trees, require one arrival on each of its \(j-1\) tree edges, no arrivals on any other internal or outgoing edge, and no direct marks on its vertices. Thus
\[
U_k(r)=
\sum_{j=1}^k
\binom{k-1}{j-1}j^{j-2}
\left(\frac{\beta r}{k-1}\right)^{j-1}
\exp\!\left(
-arj-\frac{\beta r}{k-1}
\left(\binom{j}{2}+j(k-j)\right)
\right),
\]
with the convention \(1^{-1}=1\).

For every fixed \(j\),
\[
\binom{k-1}{j-1}
\left(\frac{\beta r}{k-1}\right)^{j-1}
\longrightarrow
\frac{(\beta r)^{j-1}}{(j-1)!},
\]
and the exponential factor tends to \(e^{-jr(a+\beta)}\). For fixed \(r>0\), the contribution from components of size greater than \(J\) is at most \(e^{-ar(J+1)}\), because all vertices in such a component must be unmarked. Hence
\[
U_k(r)\longrightarrow
u(r):=
\sum_{j\ge1}
\frac{j^{j-2}}{(j-1)!}
(\beta r)^{j-1}e^{-jr(a+\beta)}.
\]

By the rooted-tree generating function, this series is the unique \(u(r)\in(0,1]\) satisfying
\[
u(r)=\exp\!\left(-ar-\beta r(1-u(r))\right).
\]
Moreover \(U_k(r)\le e^{-ar}\), so dominated convergence yields
\[
\lim_{k\to\infty}\lim_{x\to\infty}
\frac{T_{\max}(G_k(x,y))}{k}
=
\int_0^\infty u(r)\,dr.
\]

Put \(t=1-u(r)\). The fixed-point equation gives
\[
r(t)=\frac{-\log(1-t)}{a+\beta t}.
\]
This function is strictly increasing: after differentiating, the numerator is
\[
\frac{a}{1-t}
+
\beta\left(\frac{t}{1-t}+\log(1-t)\right)>0.
\]
As \(r\) goes from \(0\) to \(\infty\), \(t\) goes from \(0\) to \(1\). Integration by parts therefore gives
\[
\int_0^\infty u(r)\,dr
=
\int_0^1 r(t)\,dt
=
\int_0^1
\frac{-\log(1-t)}{a+2(1-a)t}\,dt.
\]

This is exactly the degree-\(2\) objective \(f(p)\) of Hofmeister, Bitar, and Yaakobi with \(p_1=a\) and \(p_2=1-a\). Their strict-convexity result makes its optimum unique. Their KKT equations reduce to
\[
\frac{1}{2b}\operatorname{{Li}}_2\!\left(\frac{2b}{1+b}\right)
=
\frac{1}{2b(1+b)}
\log\!\left(\frac{1+b}{1-b}\right),
\qquad b=1-a.
\]
The unique solution is
\[
a_\star=0.155473700361088\ldots,
\qquad
1-a_\star=0.844526299638912\ldots,
\]
and the common objective value is
\[
0.793933444597171\ldots.
\]
Thus the ideal-decoded recovery-complete construction has exactly the limiting ratio and expectation conjectured in the 2026 source.

## Verification

The bundled `artifacts/verify.py` uses only the Python standard library. It independently evaluates the finite-\(k\) expectation obtained by integrating the exact tree-component survival formula:
\[
E_k(a)=
\sum_{j=1}^k
\binom{k-1}{j-1}j^{j-2}
\left(\frac{\beta}{k-1}\right)^{j-1}
\frac{(j-1)!}{A_{k,j}^j},
\]
where
\[
A_{k,j}=aj+\frac{\beta}{k-1}
\left(\binom{j}{2}+j(k-j)\right).
\]
At \(a=a_\star\), it checks monotone numerical convergence of this exact finite-\(k\) expression toward the stated integral for \(k=20,50,100,200,500\).

The verifier also computes the dilogarithm by its defining power series, solves the KKT equation by bisection, checks \(a_\star\) and the objective to high numerical accuracy, and prints `VERIFY_OK`.

The finite computations are consistency checks. The limit theorem itself is established by the tree-component characterization, the explicit finite-\(k\) formula, and dominated convergence.

## Relationship to prior work

Boruchovsky et al. introduced the recovery-complete matrices \(G_k(x,y)\), proved the cycle and repeated-edge recovery rules, and derived a finite-\(k\) asymptotic expression under the large-\(x\) no-repeat-copy regime. They explicitly noted that optimizing the unequal vertex/edge sampling probabilities is analytically cumbersome and left that optimization as future work. Their symmetric specialization gives the earlier limit \(\pi^2/12\).

Hofmeister, Bitar, and Yaakobi later analyzed binary fully symmetric codes through their equivalence with LT codes. For maximum degree \(2\), they found the unique peeling-optimal masses \(p_1\approx0.15547\) and \(p_2\approx0.84453\), with normalized expectation about \(0.7939\). They explicitly conjectured that the ideal weight-\(1\)/weight-\(2\) ratios in the Boruchovsky et al. construction tend to those same masses and that its normalized ideal-decoding expectation tends to the same optimum.

The proof above resolves that stated conjecture. Its mechanism also explains why ideal cycle decoding does not improve the first-order limit over degree-\(2\) peeling: a uniformly chosen target lies asymptotically in a finite unmarked tree whenever it is still unresolved; cyclic finite components have vanishing mass, while macroscopic components contain direct marks with overwhelming probability.

Wang and Yaakobi study exact finite-parameter random-access algorithms and bounds and several small-\(k\) constructions, but do not derive this recovery-complete large-\(k\) limit.

## Limitations

The result concerns the iterated regime in which the per-support multiplicity first tends to infinity and then the dimension tends to infinity, with a positive limiting weight-\(1\) mass \(a\). It does not quantify the finite-\(x\) correction, and it does not address the boundary \(a=0\), where the direct-mark exponential domination used above disappears. The field size is allowed to grow as required by the recovery-complete construction.

The theorem is specific to weight \(1\) and weight \(2\). Higher-weight fully symmetric families have hypergraph rather than graph recovery geometry, so the argument does not automatically extend to the better degree distributions known for larger maximum degree.

The originality conclusion is based on exact-claim, parameter, alias, and implication searches plus full-text inspection of the closest sources. An equivalent argument under random-graph or fountain-code terminology could exist outside the searched literature.

## References

1. Christoph Hofmeister, Rawad Bitar, and Eitan Yaakobi, *Random Access Expectation in DNA Storage and Fountain Codes*, arXiv:2605.10919v1, first public version 2026-05-11.
2. Avital Boruchovsky, Ohad Elishco, Ryan Gabrys, Anina Gruica, Itzhak Tamo, and Eitan Yaakobi, *Making it to First: The Random Access Problem in DNA Storage*, arXiv:2501.12274v1, first public version 2025-01-21; later published in IEEE Transactions on Information Theory.
3. Chen Wang and Eitan Yaakobi, *Random Access in DNA Storage: Algorithms, Constructions, and Bounds*, arXiv:2601.07053v1, first public version 2026-01-11.
