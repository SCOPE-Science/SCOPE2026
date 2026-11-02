# Exact negative type and the nine-vertex obstruction for two-clique chordal sums

## Finding

**Theorem.** For integers \(h\ge2\) and \(a,b\ge1\), let \(G_{h;a,b}\) be the union of two complete graphs on \(h+a\) and \(h+b\) vertices, whose intersection is a complete graph on exactly \(h\) vertices. Keep every edge of the intersection, and put the unit-edge shortest-path metric \(d\) on the total vertex set. This graph is also \(K_h\vee(K_a\sqcup K_b)\), and has \(N=h+a+b\) vertices.

Its supremal negative-type (generalized-roundness) exponent is

\[
\boxed{\wp(G_{h;a,b})=\log_2\!\left(1+\frac1h+\sqrt{\left(\frac1h+\frac1a\right)\left(\frac1h+\frac1b\right)}\right).}
\]

For \(0\le p<\wp\) the metric has **strict** \(p\)-negative type. At \(p=\wp\), negative type still holds but is not strict; at every \(p>\wp\), it fails. The critical snowflake \(d^{\wp/2}\) has an isometric Euclidean realization of minimum dimension \(N-2\), whereas \(d^{p/2}\) for \(0<p<\wp\) requires dimension \(N-1\).

In particular, the original graph metric has \(1\)-negative type exactly when

\[
\boxed{(h-2)ab\le h+a+b.}
\]

**Sharp size boundary inside this family.** Every such two-clique sum with at most eight vertices has \(1\)-negative type. At nine vertices, it fails \(1\)-negative type for exactly two parameter triples up to interchange of the two exclusive parts:

\[
\boxed{(h,a,b)=(4,2,3)\quad\text{or}\quad(5,2,2).}
\]

Thus the first failure within this natural chordal family occurs at nine vertices. The corresponding exact exponents are respectively \(\log_2((5+\sqrt7)/4)\) and \(\log_2(19/10)\), both below one.

## Assumptions and scope

The vertex set is the disjoint union of a shared clique \(H\) of size \(h\), a first exclusive clique \(A\) of size \(a\), and a second exclusive clique \(B\) of size \(b\). Every pair of distinct vertices is adjacent except pairs with one endpoint in \(A\) and one in \(B\). These missing pairs have shortest-path distance exactly two. In particular, this is a finite, simple, unweighted, diameter-two graph. The vertex metric is not a weighted, effective-resistance, or squared-distance metric.

For \(p\ge0\), \(p\)-negative type means that every real vector \(z\) indexed by the vertices with \(\sum_v z_v=0\) satisfies

\[
\sum_{u,v}z_uz_v d(u,v)^p\le0.
\]

Here powers of positive distances are standard, and diagonal entries are zero. Strict negative type means strict inequality for every nonzero zero-sum vector. The expression \(\wp\) is the supremum of admissible nonnegative exponents.

## Proof

Write \(t=2^p\). With respect to the all-ones off-diagonal distance matrix of a complete graph, precisely the \(A\)-to-\(B\) and \(B\)-to-\(A\) entries change from one to \(t\). Hence, for every zero-sum real vector \(z\), with group sums \(\alpha=\sum_{v\in A}z_v\), \(\beta=\sum_{v\in B}z_v\), and shared-clique sum \(-\alpha-\beta\), its powered-distance quadratic form is exactly

\[
Q_p(z)=-\sum_vz_v^2+2(t-1)\alpha\beta.
\]

For fixed group sums, the three within-group quadratic energies are uniquely minimized by a constant coordinate on each group. Decomposing into the three constant components plus the mutually orthogonal within-group zero-sum deviations gives

\[
Q_p(z)=-\sum_{C\in\{H,A,B\}}\sum_{v\in C}(z_v-\overline z_C)^2
-\begin{pmatrix}\alpha&\beta\end{pmatrix}
R_t\begin{pmatrix}\alpha\\\beta\end{pmatrix},
\]

where

\[
R_t=\begin{pmatrix}
\frac1a+\frac1h&\frac1h-(t-1)\\[2pt]
\frac1h-(t-1)&\frac1b+\frac1h
\end{pmatrix}.
\]

Both diagonal entries of \(R_t\) are positive. It is positive semidefinite exactly when

\[
\left(t-1-\frac1h\right)^2\le
\left(\frac1h+\frac1a\right)\left(\frac1h+\frac1b\right).
\]

As \(t\) ranges over \([1,\infty)\), the lower root of the quadratic inequality is strictly below one, because the positive square root exceeds \(1/h\). Therefore admissibility is equivalent to \(t\le t_*\), where

\[
t_*=1+\frac1h+\sqrt{\left(\frac1h+\frac1a\right)\left(\frac1h+\frac1b\right)}.
\]

This proves the exponent formula, inclusivity, and strictness below the endpoint. At the endpoint, \(R_{t_*}\) has rank one. The within-group deviations are strictly penalized, and its one-dimensional kernel is attained by group sums \(\alpha=\sqrt{1/h+1/b}\), \(\beta=\sqrt{1/h+1/a}\), with coordinates constant within each group and shared-clique sum \(-\alpha-\beta\). For \(t>t_*\), the same group-sum direction makes \(Q_p(z)>0\). It is therefore an explicit witness above the threshold. The kernel dimension on the zero-sum hyperplane is exactly one at the threshold and zero strictly below; Schoenberg's centered-Gram criterion then gives the two Euclidean dimension statements.

For \(p=1\), put \(t=2\). Expanding the determinant inequality and multiplying by \(hab>0\) gives exactly \((h-2)ab\le h+a+b\). This is valid also for \(h=2\), where the condition is automatic.

For the minimal-order claim, a violation requires \(h\ge3\). Define \(F(h,a,b)=(h-2)ab-(h+a+b)\). Increasing \(a\) by one increases \(F\) by \((h-2)b-1\ge0\). Thus a violation at fewer than eight vertices would persist after enlarging one exclusive part to obtain eight vertices. For \(N=8\), the maximum values of \(F\) for \(h=3,4,5,6\) (using \(ab\le\lfloor(N-h)^2/4\rfloor\)) are respectively \(-2,0,-2,-4\); no violation occurs. For \(N=9\), testing \(h=3,4,5,6,7\) via the same product bound, and then enumerating the integer pairs for the two viable overlaps, gives exactly \((4,2,3)\) and \((5,2,2)\) up to exchange. The rational zero-sum vector constant on each group, with group sums \(\alpha=\beta=1\) and total \(-2\) on \(H\), has \(Q_1=1/6>0\) in the first graph and \(Q_1=1/5>0\) in the second, independently confirming failure.

## Verification

Execute `python3 verify.py` using Python 3 and the standard library only. The checker reconstructs every powered-distance entry from the full vertex metric with rational values of \(t=2^p\), forms an independent centered Euclidean Gram matrix, and tests positive semidefiniteness by exact rational Schur complements. This is compared to the displayed two-dimensional criterion across 1,320 graph/power instances. It also checks 10,469 integer instances of the \(1\)-negative-type criterion and exhaustively verifies the within-family nine-vertex boundary. All listed tests passed. Numerical or finite checking is not used to infer the universal theorem; the preceding proof supplies that inference.

## Relationship to prior work

Sánchez (2011, arXiv:1108.0451) gives a general distance-matrix characterization of supremal negative type for finite metrics and calculates complete bipartite graph examples. The present formula specializes the general negative-type definition to a different chordal family and adds a closed overlap-parameter classification and exact nine-vertex boundary. The graph construction is the union of two cliques along a **shared clique of size at least two**, not a one-vertex bouquet. Formulas for one-vertex clique bouquets and for complete multipartite graph metrics do not imply the stated common-clique threshold by merely identifying their graph parameters.

Faver, Kochalski, Murugan, Verheggen, Wesson and Weston (arXiv:1201.6669) discuss negative type and the rank of Euclidean realizations, with particular attention to additive metrics and ultrametrics. The present graphs have triangles and need not be tree-additive. Deza and Maehara's earlier work on transformed graph distances provides a potentially stronger general spectral framework, but the relevant complete manuscript was not available for direct statement-by-statement comparison. A concealed equivalent formula in that work or elsewhere is an unresolved originality risk.

## Limitations

The classification is for exactly two maximal cliques, meeting in a nonempty complete separator of size at least two, with unit-edge shortest-path distance. It is not a result about arbitrary chordal graphs, sums of three or more cliques, weighted edge lengths, arbitrary Hilbert distortion, or \(L^1\)-embeddability. It does not establish historical uniqueness or constitute independent scientific validation. The claim about the smallest obstruction is **only within the specified two-clique family**, not among all connected or all chordal graphs.

## References

1. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451, first public version 2011-08-02. https://arxiv.org/abs/1108.0451
2. T. Faver, K. Kochalski, M. K. Murugan, H. Verheggen, E. Wesson, and A. Weston, *Roundness properties of ultrametric spaces*, arXiv:1201.6669. https://arxiv.org/abs/1201.6669
3. M. Deza and H. Maehara, *Metric transforms and Euclidean embeddings*, Trans. Amer. Math. Soc. **317** (1990), 661–671. https://doi.org/10.1090/S0002-9947-1990-0974513-6 (full text not inspected).
