# Sharp \(\ell_1\) snowflake threshold and cut rigidity for equal-block multipartite metrics

## Finding
Let integers \(r,n\ge2\) be given. Partition a set \(M\) into \(r\) labeled blocks \(A_1,\ldots,A_r\), each of size \(n\). For any real \(1\le t\le2\), define the metric \(d_t\) by assigning distance \(t\) to two distinct points in the same block and distance \(1\) to points in different blocks. Its least distortion into real \(\ell_1\), with no restriction on target dimension, is exactly
\[
\boxed{c_{\ell_1}(M,d_t)=\max\left\{1,\frac{n-1}{n}t\right\}.}
\]
Consequently \((M,d_t)\) embeds isometrically in real \(\ell_1\) if and only if \(t\le n/(n-1)\). For the snowflaked shortest-path metric of the unweighted balanced complete multipartite graph, \(t=2^\alpha\), the exact isometric exponent range is
\[
\boxed{0\le\alpha\le\log_2\!\left(\frac n{n-1}\right).}
\]
These constants and thresholds are independent of the number of blocks \(r\).

There is a supporting-cut rigidity statement. If \(t\ge n/(n-1)\), every nonzero cut with positive coefficient in **any** cut decomposition of an optimally scaled real \(\ell_1\) metric must select equally many points in every block. If \(t>n/(n-1)\), every optimal noncontracting embedding has image distance exactly \(t\) on each within-block pair and exactly \((n-1)t/n\) on each cross-block pair.

## Assumptions and scope
All metrics and embeddings are real. The integers \(r,n\) range independently over \(\{2,3,\ldots\}\), and \(t\in[1,2]\). The triangle inequality follows from \(t\le2\). The distortion of an injective map \(f:M\to\ell_1^N\) is the product of its largest and reciprocal smallest distance ratios. Equivalently, the optimal distortion is the least \(D\ge1\) for which some image metric \(\rho\) satisfies \(d_t\le\rho\le Dd_t\) on all pairs, after a common positive rescaling. A finite real \(\ell_1\) metric is a nonnegative combination of cut semimetrics \(\delta_S(x,y)=|\mathbf1_S(x)-\mathbf1_S(y)|\). This follows by threshold-sweeping each real coordinate; conversely, nonnegative cut sums embed explicitly into real \(\ell_1\). There is no target-dimension restriction.

## Proof
**1. A sharp identity for every cut.** For any subset \(S\subseteq M\) put \(a_i=|S\cap A_i|\), and \(x_i=a_i/n\). Let \(U(S)\) be the mean of \(\delta_S\) over all unordered distinct pairs belonging to one common block, and let \(W(S)\) be its mean over all unordered cross-block pairs. Elementary counting gives
\[
U(S)=\frac{2}{r n(n-1)}\sum_{i=1}^r a_i(n-a_i),
\quad W(S)=\frac{2}{r(r-1)n^2}\sum_{i<j}\bigl[a_i(n-a_j)+(n-a_i)a_j\bigr].
\]
Subtract and expand the squares. The exact **variance identity** is
\[
\boxed{W(S)-\frac{n-1}{n}U(S)
=\frac{2}{r(r-1)n^2}\sum_{i<j}(a_i-a_j)^2.}\tag{1}
\]
The right side is nonnegative, and vanishes if and only if \(a_1=\cdots=a_r\). By linearity, every finite real \(\ell_1\) metric \(\rho\) has corresponding pair means \(U(\rho),W(\rho)\) satisfying
\[
W(\rho)\ge\frac{n-1}{n}U(\rho),\tag{2}
\]
with equality if and only if every positive-weight nontrivial cut in a cut decomposition has equal block counts. This conclusion is independent of the choice of decomposition.

**2. Universal lower bound.** Suppose \(d_t\le\rho\le Dd_t\) is any noncontracting real \(\ell_1\) embedding metric. All within-block source distances are \(t\), so \(U(\rho)\ge t\); all cross-block source distances are \(1\), so \(W(\rho)\le D\). Equation (2) yields \(D\ge(n-1)t/n\). The definition of distortion also requires \(D\ge1\). Thus \(D\ge\max\{1,(n-1)t/n\}\).

**3. Explicit matching embeddings.** Choose independently and uniformly one vertex from every block; let \(S\) be the cut consisting of those \(r\) selected vertices. Define the real cut metric
\[
B=\frac n2\,\mathbb E\,\delta_S.
\]
Two distinct vertices in one block are separated with probability \(2/n\); two vertices in different blocks are separated with probability \(2(n-1)/n^2\). Therefore \(B\) equals \(1\) within blocks and \((n-1)/n\) across blocks. Define also the cut metric
\[
P=\frac12\sum_{i=1}^r\delta_{A_i},
\]
which vanishes within blocks and equals \(1\) across blocks. For \(t\le n/(n-1)\), the metric
\[
\rho_t=tB+\left(1-\frac{n-1}{n}t\right)P
\]
is a nonnegative cut combination and equals \(d_t\) on every pair: an isometric real \(\ell_1\) realization. For \(t>n/(n-1)\), take \(\rho_t=tB\), which equals \(t\) within blocks and \((n-1)t/n\) across blocks. Consequently \(d_t\le\rho_t\le[(n-1)t/n]d_t\), attaining the lower bound. The expectation is a finite average over exactly \(n^r\) cuts, so this is a finite-dimensional construction.

**4. Rigidity.** If \(t\ge n/(n-1)\) and an embedding attains \(D=(n-1)t/n\), the inequalities
\[
D\ge W(\rho)\ge\frac{n-1}{n}U(\rho)\ge\frac{n-1}{n}t=D
\]
are all equalities. Equality in (1), with nonnegative cut coefficients, forces every supporting cut to have \(a_1=\cdots=a_r\). Equality \(U(\rho)=t\) and each within-block image distance at least \(t\) force all such distances to equal \(t\). Equality \(W(\rho)=D\) and each cross-block distance at most \(D\) force all such distances to equal \(D\). The strict supercritical statement follows. At the threshold \(D=1\), every optimal embedding is isometric and the same cut support equality applies.

For \(t=2^\alpha\) with \(0\le\alpha\le1\), this is exactly the snowflake of the unit-edge shortest-path metric of \(K_{n,\ldots,n}\), proving the stated exponent condition. This finishes the proof.

## Verification
The proof holds for all listed integers and real parameters, not merely checked examples. The standalone `check_metric.py` uses only Python's standard library and exact `Fraction` arithmetic. It enumerates every cut for the seven small parameter pairs \((r,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3)\), checking identity (1) and its equality criterion, and then checks every pair of vertices of explicit finite cut constructions for six rational parameter choices per pair. The successful replay printed `CHECK_OK {'cut_identity_assertions': 15792, 'balanced_cut_equalities': 344, 'exact_embedding_pairs': 1164}`. Separately, independent finite cut-cone linear programs for six small parameter pairs and four parameter values attained the formula to standard numerical tolerance; these calculations are corroboration, not proof for arbitrary parameters.

At \(n=2\), all \(t\in[1,2]\) yield isometric embeddings; at \(n=3,t=2\), the distortion is \(4/3\); and at \(n=4,t=2\), it is \(3/2\). The full sharp transition occurs at the noninteger value \(t=n/(n-1)\) whenever \(n\ge3\).

## Relationship to prior work
Abraham, Filtser, Gupta and Neiman (first public arXiv 14 August 2017) study general graph-metric embeddings with bounds governed by shortest-path decomposition depth. Their inspected results do not provide the exact two-level metric formula or supporting-cut equality condition. The paper's later published corrigendum withdraws a separate theorem; no claim here relies on that theorem. The cut-cone decomposition used in the proof is classical, not claimed to be new. Obata's 2022 first-public preprint on complete-multipartite graph quadratic embeddings gives a necessary conditional-negative-type obstruction at the ordinary graph-metric endpoint. A separately recorded full powered-metric negative-type classification implies the *numerical obstruction* \(t\le n/(n-1)\) for isometric real \(\ell_1\) embeddings, since every real \(\ell_1\) metric is conditionally negative definite. Thus no standalone priority is claimed for the cutoff as a negative-type bound; the contribution here is its sufficiency for \(\ell_1\), the full optimal bilipschitz distortion beyond it, and the cut-support rigidity.

Higashitani, Jochemko and Michałek (first public arXiv 20 July 2018) calculate faces and arithmetic invariants of symmetric edge polytopes for complete multipartite graphs. At \(t=2\) the relevant Lipschitz-free ball is such a symmetric edge polytope, but its facet-count statement does not determine the distortion of the underlying metric into \(\ell_1\) or the whole snowflake interval. Published studies of the same two-level multipartite metric give facet-count transitions and relative projection constants of Lipschitz-free subspaces, not this optimal metric distortion or isometric threshold. Mori's 2026 exact \(K_{2,n}\) result optimizes the **worst weighted graph metric** on that graph, which is a different invariant from the present fixed homogeneous metric.

An already recorded exact result for \(K_{3,n}\) includes the \(r=2,n=3,t=2\) boundary value \(4/3\). The present contribution is the all-block, all-size, continuously parameterized formula, its sharp snowflake threshold and equality characterization, not a claim of priority for that boundary value. No mathematical claim of independent novelty certification is made.

## Limitations
All blocks must have the same cardinality; arbitrary unequal block sizes, independently varying within-block distances, and arbitrary weighted shortest-path metrics are not covered. The result concerns least distortion into real \(\ell_1\), not Banach–Mazur distances of Lipschitz-free spaces, their projection constants, or minimal embedding dimension. The proof classifies supporting cuts only in the sharp and supercritical regimes, not all cut decompositions below the isometry threshold. Equivalent older formulations in unindexed cut-cone or hypermetric literature remain a bibliographic risk, and independent mathematical validation has not been performed.

## References
1. I. Abraham, A. Filtser, A. Gupta and O. Neiman, *Metric Embedding via Shortest Path Decompositions*, arXiv:1708.04073v1, 14 August 2017, https://arxiv.org/abs/1708.04073. The later 2023 corrigendum is DOI 10.1137/23M1546245.
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, 20 July 2018, https://arxiv.org/abs/1807.07678.
3. N. Obata, *Complete Multipartite Graphs of Non-QE Class*, arXiv:2206.05848v1, 12 June 2022, especially Theorems 1.1–1.2 on quadratic-embedding obstructions, https://arxiv.org/abs/2206.05848.
4. D. Avis and M. Deza, *The cut cone, \(L_1\) embeddability, complexity, and multicommodity flows*, Networks 21 (1991), 595–617, DOI 10.1002/net.3230210602.
5. H. Mori, *The exact value of \(c_1(K_{2,n})\)*, arXiv:2602.23745v1, 27 February 2026. The author defines \(c_1(G)\) by optimizing over edge weights, unlike the fixed metric here.
6. *Sharp facet jumps for interpolated complete-multipartite Lipschitz-free balls*, published mathematical finding, 11 October 2026.
7. *Sharp optimal projection constants for clustered finite metric free spaces*, published mathematical finding, 11 October 2026.
