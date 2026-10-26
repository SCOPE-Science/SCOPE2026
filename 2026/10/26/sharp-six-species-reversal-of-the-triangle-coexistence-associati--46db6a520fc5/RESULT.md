# Sharp six-species reversal of the triangle–coexistence association

## Finding

For the homogeneous symmetric competitive Lotka–Volterra system on a connected simple graph, the smallest vertex count at which a **single degree-preserving two-edge switch** can create a triangle while **lowering the stable-coexistence threshold** is six. There is a six-vertex pair with identical degrees, whose triangle count increases from zero to one and whose average local clustering increases from zero to \(7/18\), but whose exact stable-coexistence threshold falls from the unique root \(\rho\in(11/25,9/20)\) of
\[
1-2\rho-\rho^2+\rho^3=0
\]
to
\[
\sigma=\frac{\sqrt{17}-1}{8}.
\]
In particular, \(\rho>11/25>2/5>\sigma\). For all connected simple graphs on at most five vertices, increasing the triangle count while preserving the degree multiset cannot decrease this threshold, even if more than one edge switch is allowed.

## Assumptions and scope

Let \(G\) be an undirected simple connected graph with vertices numbered \(0,\ldots,n-1\) and symmetric zero-diagonal adjacency matrix \(A\). At fixed \(\tau\geq0\), consider
\[
\dot x_i=x_i\left(1-x_i-\tau\sum_j A_{ij}x_j\right),\qquad x_i>0.
\]
Define the **stable-coexistence threshold** \(\tau_*(G)\) to be the first parameter encountered when increasing \(\tau\) continuously from zero at which the positive coexistence branch ceases to be strictly positive or ceases to be linearly asymptotically stable. Thus the definition includes both a boundary collision and loss of linear stability; it does not assert anything about restabilization beyond the first event.

Put
\[
\begin{aligned}
E(G_0)&=\{02,03,04,12,13,35\},\\
E(G_1)&=\{03,04,05,12,13,23\}.
\end{aligned}
\]
Here an unordered pair \(ij\) denotes the edge between vertices \(i\) and \(j\). The rewiring removes \(02,35\) and inserts \(05,23\). Both graphs are connected, and their sorted degree multiset is \((1,1,2,2,3,3)\).

## Proof

**Stable equilibrium criterion.** At a strictly positive equilibrium, \(B(\tau)x=\mathbf 1\), with \(B(\tau)=I+\tau A\). Its Jacobian is \(-\operatorname{diag}(x)B(\tau)\), similar to the negative symmetric matrix \(-\operatorname{diag}(\sqrt{x})B(\tau)\operatorname{diag}(\sqrt{x})\). Hence strict linear stability holds exactly when \(B(\tau)\) is positive definite. While this is true, the equilibrium is unique and equals \(B(\tau)^{-1}\mathbf 1\); it is biologically feasible exactly when every coordinate is positive. Consequently the first failure of either property gives \(\tau_*(G)\).

**Before rewiring.** Direct determinant and Cramer calculations for \(G_0\) give
\[
\det B_0(\tau)=P(\tau)Q(\tau),\quad
P=1-2\tau-\tau^2+\tau^3,\quad Q=1+2\tau-\tau^2-\tau^3,
\]
and
\[
x_0=x_3=\frac{1-\tau-\tau^2}{Q},\qquad
x_1=x_2=\frac1Q,\qquad
x_4=x_5=\frac{1+\tau}{Q}.
\]
All coordinates are strictly positive for \(0\leq\tau\leq1/2\) whenever the inverse exists, since \(Q>0\) and \(1-\tau-\tau^2>0\) on this interval. On \([0,1/2]\), \(P\) is strictly decreasing from \(1\) to \(-1/8\), while \(Q>0\). Thus its unique zero \(\rho\in(11/25,9/20)\) is the first singular parameter of the symmetric matrix \(B_0\). Continuity of its eigenvalues from the positive identity implies \(B_0\succ0\) for all \(\tau<\rho\); at \(\rho\) it loses strict positive definiteness without the positive coexistence values vanishing. Therefore \(\tau_*(G_0)=\rho\).

**After rewiring.** Put \(D=1+\tau-5\tau^2-3\tau^3+4\tau^4\). Direct Cramer calculations for \(G_1\) yield \(\det B_1=(1-\tau)D\) and
\[
\begin{aligned}
x_0&=\frac{(1-\tau)(1-\tau-4\tau^2)}{D},\\
x_1=x_2&=\frac{(1+\tau)(1-2\tau)}{D},\\
x_3&=\frac{1-2\tau-\tau^2+4\tau^3}{D},\\
x_4=x_5&=\frac{1-3\tau^2}{D}.
\end{aligned}
\]
At \(\tau=2/5\), the six leading principal minors of \(B_1\), in the vertex order given above, are respectively
\[
1,\ 1,\ 21/25,\ 321/625,\ 1281/3125,\ 957/3125,
\]
so \(B_1(2/5)\succ0\). By convex interpolation with the identity, \(B_1(\tau)\succ0\) on \([0,2/5]\), and in particular \(D>0\). On this interval, all numerators except possibly that of \(x_0\) remain positive; for \(x_3\), use \(1-2\tau-\tau^2+4\tau^3\geq1-2\tau-\tau^2\geq1/25\). The first vanishing coordinate is \(x_0\), at the unique positive zero of \(1-\tau-4\tau^2\), namely \(\sigma=(\sqrt{17}-1)/8<2/5\). Therefore \(\tau_*(G_1)=\sigma\). The edge switch creates exactly triangle \(123\), with local clustering contributions \(1,1,1/3\) at its three vertices and zero elsewhere, so mean clustering rises from \(0\) to \(7/18\).

**Sharpness in vertex count.** Exhaustively classifying connected simple graphs with at most five vertices by sorted degree multiset and triangle count leaves only two degree families with any variation in triangle count. In each family the two triangle-count levels each consist of a single isomorphism class. Their exact thresholds are:

| Number of vertices | Sorted degrees | Triangles | Stable-coexistence threshold |
| --- | --- | --- | --- |
| 5 | \((1,2,2,2,3)\) | 0 | \((\sqrt3-1)/2\) |
| 5 | \((1,2,2,2,3)\) | 1 | \(1/2\) |
| 5 | \((2,2,2,3,3)\) | 0 | \(1/3\) |
| 5 | \((2,2,2,3,3)\) | 1 | \(1/2\) |

For up to four vertices no degree multiset supports differing triangle counts. An exhaustive finite certificate enumerates all \(2^{\binom n2}\) labeled graphs at each \(2\leq n\leq5\), filters connected graphs by graph traversal, and compares their canonical relabelings. The corresponding five-vertex representative edge sets and exact polynomial identities appear in `verify.py`. The threshold values in the table follow by direct Cramer's-rule equilibrium formulas and symmetric-matrix definiteness: in the four graph orderings above, the first boundary/loss is respectively \((\sqrt3-1)/2\), \(1/2\), \(1/3\), \(1/2\). Exact positive-definiteness witnesses are supplied at \(3/8\), \(1/2\), \(1/3\) for the first three; for the fourth the matrix at \(1/2\) is positive semidefinite and singular, so strict positive definiteness holds below \(1/2\) by convex interpolation. Every coexistence coordinate remains positive until the asserted first event. This establishes the table and rules out a smaller connected degree-preserving triangle-increase counterexample.

## Verification

Run `python verify.py` using Python 3.9 or newer, with no third-party packages. The program reconstructs all six-vertex determinant and Cramer polynomial identities by permutation expansion; independently checks exact rational principal-minor certificates and the degree/triangle/clustering claims; verifies four five-vertex representative calculations; and exhaustively scans all connected labeled simple graphs on two through five vertices. Counts are \(1,4,38,728\) connected labeled graphs at orders \(2,3,4,5\). This is exhaustive **only for the explicitly bounded finite census**; the six-vertex exact formulas and stability proof establish the continuous-parameter result.

## Relationship to prior work

Mooij, Baudena, von der Heydt, Miele, and Kryven (arXiv:2603.17584, March 18, 2026; June 2026 revision) derive universal graph bounds for competitive coexistence and report a positive clustering–stability association under degree-preserving rewiring in simulated networks and ecological data. Their complete accessible text describes positive correlations rather than a universal per-switch monotonicity theorem. The present result does **not** dispute those statistical associations. It identifies the sharp small-graph boundary at which the tempting universal monotonic inference fails, within their identical ODE and graph-rewiring framework. Mooij and coauthors (arXiv:2404.14031) provide earlier degree-based sufficient bounds, which do not compare the two same-degree graphs or imply the sharp reversal. No previously inspected source supplies this exact six-vertex counterexample and minimum-size classification; this is a best-knowledge comparison, not a guarantee of historical priority.

## Limitations

The result concerns undirected simple connected networks with identical competitive coefficients and unit carrying capacities. It compares triangle count and mean local clustering for a specific **two-edge switch**, not arbitrary triangle additions or general ecology models. Only the onset of failure of strictly positive **linearly asymptotically stable** coexistence is classified; behavior after that onset is not analyzed. The minimality statement is restricted to connected graphs on at most five vertices and the stated degree-preserving triangle-increase comparison; it is supported by a finite exhaustive checker, not an infinite enumerative argument. The source's positive population-level correlations may remain valid. Independent historical-priority verification has not been performed.

## References

1. M. N. Mooij, M. Baudena, A. S. von der Heydt, L. Miele, and I. Kryven, *A dynamic mechanism for prevalence of triangles in competitive networks*, arXiv:2603.17584v1 (first posted 2026-03-18), https://arxiv.org/abs/2603.17584 . Open-access full text: https://arxiv.org/html/2603.17584v2 .
2. M. N. Mooij, M. Baudena, A. S. von der Heydt, and I. Kryven, *Stable coexistence in indefinitely large systems of competing species*, arXiv:2404.14031 (first posted 2024-04-22), https://arxiv.org/abs/2404.14031 .
