# Exact stationary two-point correlations for broadcast voters on regular trees

## Finding
Let \(\mathbb T_d\) be the infinite \(d\)-regular tree, \(d\ge3\). Consider the \(\Lambda\)-broadcast voter dynamics of Astoquillca, González Casanova and dos Santos, started with independent Bernoulli\((p)\) opinions for \(0<p<1\), and let \(\mu_{p,\Lambda}\) be its stationary weak limit. For a finite nonzero measure \(\Lambda\) on \([0,1]\), put
\[
q=\frac{\int_{[0,1]}u\,\Lambda(du)}{\Lambda([0,1])}\in[0,1],\qquad H=2(d-1)^2+(d-2)q.
\]
For distinct vertices \(x,y\) at graph distance \(k\), define \(C_k=\operatorname{Cov}_{\mu_{p,\Lambda}}(\eta(x),\eta(y))\). Then
\[
\frac{C_1}{p(1-p)}=\frac{2(d-1)+(d-2)q}{H},\qquad
\frac{C_k}{p(1-p)}=\frac{2+(d-2)q}{H}(d-1)^{-(k-2)}\quad(k\ge2).
\]
In particular, \(C_k>0\); every \(C_k\) strictly increases with \(q\); and \(C_{k+1}/C_k=1/(d-1)\) for all \(k\ge2\). The geometric decay rate is independent of \(\Lambda\), although the short-range amplitudes depend on its normalized first moment. Moreover, if \(h=C_1/[p(1-p)]\), then
\[
q=\frac{2(d-1)((d-1)h-1)}{(d-2)(1-h)}.
\]
Thus a known one-site density and a single nearest-neighbor covariance identify the normalized first moment of the broadcast measure.

## Assumptions and scope
The graph is the infinite homogeneous tree of integer degree \(d\ge3\); the model has binary opinions and no spontaneous mutation; every broadcasting vertex uses the same finite, nonzero measure \(\Lambda\). Time is rescaled by the positive total mass \(\Lambda([0,1])\), which does not change the stationary law. The notation \(\mu_{p,\Lambda}\) refers specifically to the long-time weak limit from product Bernoulli\((p)\) initial data, whose existence follows from the published stationary-measure construction. The claim applies to each fixed pair of distinct vertices and every real \(p\in(0,1)\), not to an arbitrary invariant measure of the interacting process.

## Proof
The graphical construction and moment duality in [1, Sections 3.2--3.4] identify the expectation of the product of two opinions at time \(t\) with the corresponding product evaluated at the positions of two coordinated, coalescing ancestral walkers. Given independent Bernoulli\((p)\) initial opinions, the conditional expectation is \(p\) after ancestral coalescence and \(p^2\) if the ancestral sites remain distinct. Hence, with \(\tau\) denoting the first meeting time of the two dual walkers,
\[
\operatorname{Cov}(\eta_t(x),\eta_t(y))=p(1-p)\,\Pr_{x,y}(\tau\le t).
\]
As \(t\to\infty\), weak convergence to \(\mu_{p,\Lambda}\) and monotone convergence give \(C_k=p(1-p)h_k\), where \(h_k=\Pr(\tau<\infty\mid\operatorname{dist}(Y^1_0,Y^2_0)=k)\), and \(h_0=1\).

The two-walker distance, stopped at zero, is a birth-and-death chain with one additional direct-coalescence transition. All rates below are divided by \(\Lambda([0,1])\). When the distance is at least three, the two lineages have no common-neighbor broadcast source, so total inward and outward rates are \(2\) and \(2(d-1)\), respectively. At distance one, jumping along their connecting edge coalesces them at rate \(2\), and moving outward occurs at rate \(2(d-1)\). At distance two, the unique intermediate vertex broadcasts to both occupied neighbors simultaneously at rate
\[
\frac{1}{\Lambda([0,1])}\int_{[0,1]}u\,\Lambda(du)=q.
\]
The two single-lineage jumps toward the midpoint each have rate \(1-q\), and the total outward rate is \(2(d-1)\). This follows directly by summing the generator's subset rates [1, equations (3.4)--(3.5)]; no moment above the normalized first is involved for two lineages.

The outward drift in the region of distance at least three and the gambler's-ruin limit yield \(\Pr_k(\tau_2<\infty)=(d-1)^{-(k-2)}\), where \(\tau_2\) is the hitting time of distance two. Any route from distance \(k\ge3\) to coalescence passes through two; therefore
\[
h_k=(d-1)^{-(k-2)}h_2\qquad(k\ge2).
\]
First-step equations at distances one and two are, respectively,
\[
2d\,h_1=2+2(d-1)h_2,
\qquad
(2d-q)h_2=q+2(1-q)h_1+2(d-1)h_3.
\]
Substitute \(h_3=h_2/(d-1)\) and solve this nonsingular two-by-two linear system. Its determinant after normalization is \(H=2(d-1)^2+(d-2)q>0\), and the claimed expressions for \(h_1,h_2\) result. This also gives the exact formula at \(q=0\), namely \(h_k=(d-1)^{-k}\), the classical uncoordinated-tree collision probability.

For strictly positive integer \(d-2\), differentiation of the rational expressions gives
\[
\frac{\partial h_1}{\partial q}=\frac{2(d-2)^2(d-1)}{H^2}>0,
\qquad
\frac{\partial h_2}{\partial q}=\frac{2(d-2)((d-1)^2-1)}{H^2}>0.
\]
The same strict sign extends to \(h_k\) for \(k\ge3\). Solving the formula for \(h_1\) for \(q\) proves the displayed inverse relation; its denominator is nonzero because \(h_1<1\) for \(d\ge3\).

## Verification
The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It verifies the backward generator equations for multiple degrees, first-moment parameters and distances, and independently solves finite Dirichlet truncations. The checked truncation satisfies \(0\le h_k-h_k^{(K)}\le h_K\), matching the analytical strong-Markov bound for absorption at distant level \(K\). Run `python verify.py` from the directory containing this document. These finite diagnostics are not an infinite-state proof; that proof is given above.

## Relationship to prior work
Astoquillca, González Casanova and dos Santos [1] introduce the broadcast dynamics, its coordinated coalescing dual, the stationary-measure construction and general uniqueness/identifiability by a finite moment profile, including trees. They do not state the explicit homogeneous-tree two-point covariance or its first-moment inversion. The present calculation specializes their dual to two walkers and solves its distance process, yielding new explicit pair-level information. In particular, the global identification of the full moment profile from the full stationary measure in their Theorem 2.5 is not an identification of the first moment from one nearest-neighbor covariance.

The classical uncoordinated collision probability on regular trees is standard; see Durrett [2, Example 7.4.3] and the classical voter/coalescing-walk duality in Aldous and Fill [3, Section 14.3]. Astoquillca [4] studies different voter-model variants, not this coordinated-broadcast two-point calculation. The new content is the complete \(q\)-dependent stationary two-point profile and its recovery formula, not the established graphical duality, stationary existence or classical \(q=0\) limit.

## Limitations
The result determines two-point correlations but not higher-order marginals; the latter can depend on higher moments of \(\Lambda\). It is restricted to infinite homogeneous trees of degree at least three, fixed spatially homogeneous broadcast rates, and stationary laws obtained from i.i.d. Bernoulli initial data. A general unpublished representation of coordinated coalescence could in principle subsume these explicit formulas; no independent priority certification is asserted. The finite rational tests do not certify the infinite-state argument independently.

## References
[1] J. Astoquillca, A. González Casanova and R. S. dos Santos, *The broadcast voter model: Stationary measures*, arXiv:2610.04530v1 (first public 2026-10-03), Sections 2--5. https://arxiv.org/abs/2610.04530

[2] R. Durrett, *Dynamics on Graphs*, Chapter 7, Section 7.4, Example 7.4.3 (version accessed 2026-10-16). https://sites.math.duke.edu/~rtd/DoG/Chapter7.pdf

[3] D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Section 14.3 (manuscript). https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch14.S3.html

[4] J. Astoquillca, *On the stationary measures of two variants of the voter model*, Journal of Theoretical Probability 39, article 34 (2026), https://doi.org/10.1007/s10959-025-01474-1.
