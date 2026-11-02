# A first-run law and geometric near-maximal fill for complete multipartite Cholesky

## Finding

Consider a complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\) and all \(n_i\ge1\). Eliminate its \(N=\sum_i n_i\) vertices in a uniformly random order using **exact** sparse Cholesky factorization of a symmetric positive-definite \(M\)-matrix whose off-diagonal nonzeros are precisely the edges of \(G\). Let \(F\) count the distinct *new* unordered off-diagonal nonzero positions, excluding original edges and diagonals. Put
\[
M=\sum_{i=1}^r\binom{n_i}{2},\qquad (a)_s=a(a-1)\cdots(a-s+1).
\]
Let \(I\) denote the part containing the first eliminated vertex and let \(R\) be the number of consecutive initial eliminated vertices from that part, stopping before the first vertex in another part. Then, **for every permutation**, the exact fill count is
\[
F=M-\binom{n_I}{2}+\binom{n_I-R}{2}.
\tag{1}
\]
The joint law, and therefore the entire fill distribution, is
\[
\Pr(I=i,R=s)=\frac{(n_i)_s(N-n_i)}{(N)_{s+1}},\quad 1\le s\le n_i,
\qquad
\mathbb E[z^F]=\sum_{i=1}^r\sum_{s=1}^{n_i}\frac{(n_i)_s(N-n_i)}{(N)_{s+1}}
 z^{M-\binom{n_i}{2}+\binom{n_i-s}{2}}.
\tag{2}
\]
In particular,
\[
\mathbb EF=\sum_{i=1}^r\binom{n_i}{2}\frac{N-n_i}{N-n_i+2},\quad
\min F=M-\max_i\binom{n_i}{2},\quad
\max F=M-(\min_i n_i-1).
\tag{3}
\]
The minimum and maximum are taken over all vertex orders, not over the part-size vectors.

For fixed \(r\ge2\) and \(r\) equal parts of size \(m\ge3\), let \(M=r\binom m2\). Then
\[
\frac{\mathbb EF}{\min F}=\frac{rm}{(r-1)m+2}\longrightarrow\frac r{r-1},\qquad
\Pr(F=\max F)=\frac{(r-1)m}{rm-1}\longrightarrow\frac{r-1}{r},
\tag{4}
\]
and
\[
\Pr(F=\min F)=\frac{r(m)_{m-1}}{(rm)_{m-1}},\qquad
\frac{M-F}{m}\ \xrightarrow{\ d\ }\ \operatorname{Geom}\!\left(\frac{r-1}{r}\right),\qquad
\frac{\operatorname{Var}(F)}{m^2}\longrightarrow\frac{r}{(r-1)^2}.
\tag{5}
\]
The geometric distribution is supported on \(\{1,2,\ldots\}\) with probability \((r-1)r^{-s}\) at \(s\). Thus, for balanced bipartite graphs, asymptotically half of random orders incur the maximum possible fill, while the optimal fill appears with exponentially small probability.

## Assumptions and scope

The graph has at least two nonempty parts. The matrix is real, symmetric and positive definite, with strictly negative off-diagonal entries exactly on the graph edges and zeros otherwise; for example, \(A=I+L_G\), where \(L_G\) is the unweighted graph Laplacian. The elimination order is a uniformly random permutation of all labeled vertices. Fill means an unordered off-diagonal matrix position first becoming nonzero in a Schur complement, counted once. The result is combinatorial and remains valid for any positive edge weights and positive diagonal augmentation yielding a positive-definite \(M\)-matrix. No dropping, thresholding or incomplete-factorization sampling occurs.

## Proof

**1. Graphical and numerical elimination agree.** For a positive-definite \(M\)-matrix, every pivot \(a_{vv}\) in the Schur complement is positive, and for distinct surviving vertices
\[
a'_{uw}=a_{uw}-a_{uv}a_{vw}/a_{vv}.
\]
All existing off-diagonal entries are nonpositive, while products of two strictly negative incident entries are positive. Thus elimination creates an edge between each nonadjacent pair of neighbors and can never cancel an existing negative edge. This is precisely neighbor-clique completion, with no exceptional cancellations.

**2. Fill is determined by the first monochromatic run.** Suppose the first vertex belongs to part \(i\). Its neighbors are all vertices outside part \(i\); clique completion adds every missing edge *within each other part*. Each subsequent vertex from part \(i\), before any other-part vertex is removed, has a neighbor set that is already a clique and creates no further edges. When the first vertex from a different part is removed, its surviving neighbors include all \(n_i-R\) remaining vertices of part \(i\). Those vertices become a clique, adding \(\binom{n_i-R}{2}\) edges. At this point every surviving pair is adjacent, and there can be no subsequent fill. Initially there are exactly \(M\) missing pairs, so equation (1) follows. It covers the boundary case \(R=n_i\), in which no vertices of the first part remain.

**3. Exact distribution and expectation.** The event \(I=i,R=s\) requires \(s\) successive draws from part \(i\), then a draw outside that part. Sampling without replacement gives the first formula in (2); summing the associated monomials gives the polynomial. Alternatively, an initially missing pair from part \(i\) becomes fill if and only if the earliest eliminated vertex among that pair and all \(N-n_i\) vertices outside part \(i\) is an outsider. That probability is \((N-n_i)/(N-n_i+2)\). Sum the indicator expectations to obtain (3). For fixed initial part size \(n_i\), the number of missing edges left unfilled is
\[
M-F=\binom{n_i}{2}-\binom{n_i-R}{2}=\frac{R(2n_i-R-1)}2.
\]
This increases (weakly) with \(R\), has minimum \(n_i-1\) at \(R=1\), and maximum \(\binom{n_i}{2}\) at \(R=n_i-1\) or \(R=n_i\). Both values are attainable, so optimizing over the first part proves the extrema in (3).

**4. Balanced families and the limiting law.** If all parts have size \(m\), the formula for the expectation in (3) yields \(\mathbb EF=r\binom m2 (r-1)m/((r-1)m+2)\), proving the first identity in (4). For \(m\ge3\), maximum fill is equivalent to \(R=1\); conditioning on the initial vertex gives its probability \((r-1)m/(rm-1)\). Minimum fill is equivalent to \(R\ge m-1\). The exact no-outsider-before-position-\(m-1\) probability is \(r(m)_{m-1}/(rm)_{m-1}\), proving the first formula in (5). For each fixed integer \(s\ge1\),
\[
\Pr(R\ge s)=\frac{(m-1)_{s-1}}{(rm-1)_{s-1}}=\frac{r(m)_s}{(rm)_s}\longrightarrow r^{-(s-1)}.
\]
For every permitted \(s\), each without-replacement factor is at most \(1/r\), giving \(\Pr(R\ge s)\le r^{-(s-1)}\). Thus \(R\) converges to the asserted geometric law and has uniformly bounded moments of every fixed order. Since
\[
\frac{M-F}{m}=R-\frac{R(R+1)}{2m},
\]
we obtain the distributional limit and second-moment convergence, giving the variance limit in (5). For \(r=2\) the minimum-fill probability simplifies to \(2(m+1)/\binom{2m}{m}\), which decreases exponentially.

## Verification

The included standalone \(\texttt{verify.py}\) uses only the Python standard library and executes 2,231 grouped exact assertions. It compares the predicted fill-count distribution with exhaustive uniform-permutation graphical elimination for every part-size vector with 2–5 parts, each size from 1 to 4, and total order at most 7. It independently compares graphical fill against exact-rational Schur complements of \(I+L_G\) for four further examples; it also checks normalization, extremal values, moments and balanced-family identities at several larger parameters. Run \(\texttt{python3 verify.py}\). Finite enumeration checks are diagnostics, **not** proofs of the unbounded identities; the preceding argument proves those identities for all admissible sizes.

## Relationship to prior work

Neighbor-clique completion, fill graphs and sparse Cholesky elimination are classical. Chen, Liang and Biros [1] state this exact-elimination principle and develop an **approximate sampled-clique factorization**; their object is not the fill count of a uniform exact-elimination order. Fahrbach and colleagues [2] study minimum-degree orderings and general elimination/fill graphs, which do not report a complete random-order distribution for the graph family here. Classical minimum-fill research, including Kloks [3], is relevant to the deterministic minimum but does not by its bibliographic description settle the uniform random-order law. The claims here concern the joint first-run distribution, exact full fill polynomial and resulting geometric near-maximal-fill phenomenon, not novelty of the clique-completion rule itself or a generic minimum-fill characterization.

## Limitations

These are exact results for complete multipartite graph patterns and noncancelling positive-definite \(M\)-matrices. They do not describe approximate or randomized incomplete Cholesky, arithmetic complexity, peak active memory or running time. The precise random-order law may have a prior formulation not located in the checked literature; bibliographic evidence is not a proof of publication priority. One historical minimum-fill paper was available only as bibliographic information, not full text. Independent scientific audit has not been performed.

## References

1. Chao Chen, Tianyu Liang, George Biros, *RCHOL: Randomized Cholesky Factorization for Solving SDD Linear Systems*, arXiv:2011.07769 (first posted 2020-11-16), https://arxiv.org/abs/2011.07769 . Sections 1–2 explain exact clique completion and the distinct approximate sampling algorithm.
2. Matthew Fahrbach, Gary L. Miller, Richard Peng, Saurabh Sawlani, Junxing Wang, Shen Chen Xu, *On Computing Min-Degree Elimination Orderings*, arXiv:1711.08446 (2017), https://arxiv.org/abs/1711.08446 . Graph-elimination and fill formalism.
3. Ton Kloks, *Minimum fill-in for chordal bipartite graphs* (1993), bibliographic listing: https://research.tue.nl/en/publications/minimum-fill-in-for-chordal-bipartite-graphs/ . The technical text was not accessible for inspection.
