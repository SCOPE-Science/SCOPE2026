# Sharp quasi-total Roman domination and exact optimizers of rook graphs

## Finding

For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\) be the rook graph whose vertices are cells \((i,j)\) of an \(m\)-by-\(n\) rectangle; distinct cells are adjacent if they share a row or a column. Define a **quasi-total Roman dominating function** (QTRDF) as a map \(f:V(R_{m,n})\longrightarrow\{0,1,2\}\) such that every \(0\)-labeled vertex is adjacent to a \(2\)-labeled vertex, and every \(2\)-labeled vertex is adjacent to some positively labeled vertex. The weight is \(\omega(f)=\sum_{v}f(v)\).

**Theorem.** The minimum weight is
\[
\gamma_{qtR}(R_{m,n})=2m.
\]
Write \(S_{\ge2}(m,j)\) for the number of partitions of \(m\) labeled elements into \(j\) unlabeled blocks, each of size at least two; let \((n)_{\underline j}=n!/(n-j)!\). Put
\[
F_m(n)=\sum_{j=1}^{\lfloor m/2\rfloor}(n)_{\underline j}S_{\ge2}(m,j)
=m!\,[u^m](e^u-u)^n.
\]
The number of distinct minimum QTRDFs, with labeled rows and columns, is
\[
\boxed{N_{m,n}=(1+\mathbf{1}_{m=n})F_m(n)+9\mathbf{1}_{m=n=2}+54\mathbf{1}_{m=n=3}.}
\]
In particular, for \(m<n\), every minimum function consists of precisely \(m\) label-\(2\) cells, one in each row, such that each occupied column contains at least two such cells; all other cells are labeled \(0\). For \(m=n\ge4\), the only other minimum functions are transposes, supported in one cell of each column with no singly occupied row. The two orientations are disjoint. Small square boards have the additional equality cases described below.

## Assumptions and scope

The graph is simple and finite. Rows and columns are distinguishable, so two labelings that are related by a graph automorphism still count as distinct. The theorem applies to every integer pair \(2\le m\le n\), including the two exceptional square sizes. The requirement on a label \(2\) is to have a **positive-labeled neighbor**; label-\(1\) vertices have no support requirement. This is quasi-total Roman, not total Roman domination.

## Proof

**1. Forced-ones bound.** Let \(T=f^{-1}(2)\), with \(k=|T|\), and let \(a\) and \(b\) be the numbers of rows and columns containing a cell of \(T\), respectively. Any cell outside these \(a\) rows and \(b\) columns has no neighbor of label \(2\), hence it must be labeled \(1\). Therefore
\[
\omega(f)\ \ge\ 2k+(m-a)(n-b)\ \ge\ 2k+(m-k)(n-k)
\tag{1}
\]
whenever \(k\le m\). If a label-\(2\) vertex is not adjacent either to another label \(2\) or to one of these forced \(1\) vertices, further positive labels are required. The forced block is disjoint in row and column coordinates from every cell of \(T\), so **none of its cells is adjacent to any label-\(2\) cell**. Consequently the forced labels \(1\) never support a label \(2\).

**2. Excluding weights below \(2m\).** If \(k=0\), every vertex is labeled \(1\), with weight \(mn\ge2m\); equality occurs only for \(m=n=2\). Now assume \(1\le k\le m\). When \(k\le m-3\), the bound (1), with \(d=m-k\ge3\), gives
\[
\omega(f)\ge2k+(m-k)^2=2m+d(d-2)>2m.
\]
When \(k=m-2\), inequality (1) yields weight at least \(2m\). Equality forces \(n=m\) and \(a=b=k\), so the \(k\) cells of \(T\) lie in different rows and columns and are pairwise nonadjacent. As just noted, their forced label-\(1\) block does not support them, so another positive label is necessary; hence equality is impossible for \(k\ge1\).

For \(k=m-1\), (1) becomes \(\omega(f)\ge2m-2+(n-m+1)\). For \(n\ge m+2\) this is at least \(2m+1\). For \(n=m+1\), weight \(2m\) could occur only when \(a=b=m-1=k\), making the \(k\) labels \(2\) a pairwise nonadjacent rook placement; the forced \(1\) labels cannot support them, and an additional positive label increases the weight. For \(n=m\), put \(k=m-1\). If \(a=b=k\), there is exactly one forced \(1\) and the \(k\) pairwise nonadjacent labels \(2\) need extra support. A further label \(1\) can be adjacent to at most two of those \(k\) labels \(2\). Thus every function of this type has weight at least \(2m-1+\lceil k/2\rceil\); equality at \(2m\) is possible only when \(k\le2\), corresponding to the \(2\times2\) and \(3\times3\) cases. If exactly one of \(a,b\) equals \(k-1\) and the other equals \(k\), the forced block has two cells, so the base weight is \(2m\). Here \(T\) has precisely one adjacent pair and \(k-2\) isolated label-\(2\) vertices. All isolated labels need extra support; hence this is possible only for \(k=2\), on a \(3\times3\) board. Any smaller \(a\) or \(b\) forces at least three ones and weight above \(2m\).

When \(k=m\), weight \(\le2m\) forces every other cell to have label \(0\). The \(m\) defended cells must touch every row or every column; otherwise an untouched row/column intersection is an undefended zero. For \(m<n\), only covering every row is possible, so there is exactly one \(2\) per row. Its positive-neighbor requirement is equivalent to each occupied column having at least two labels \(2\). For \(m=n\), covering all columns gives the transposed family. They are disjoint since their intersection would have precisely one \(2\) in every occupied row and every occupied column, leaving every \(2\) isolated. For \(k>m\), weight \(2k>2m\).

**3. Existence and counts.** Placing one \(2\) in each row, all in the first column, and assigning zero elsewhere yields a valid QTRDF of weight \(2m\). Hence the lower bound is sharp. The nonexceptional row-oriented minimum configurations correspond bijectively to maps from the \(m\) labeled rows to the \(n\) named columns in which no nonempty fiber has size one. Partitioning rows into \(j\) fibers of size at least two and injectively assigning those fibers to columns gives \((n)_{\underline j}S_{\ge2}(m,j)\), summed over \(j\). The same count applies in the transposed square case. The exponential generating function follows by independently choosing in each named column an empty row subset or a subset of size at least two.

For \(2\times2\), there are \(2F_2(2)=4\) all-\(0,2\) configurations, eight configurations with one \(2\), its opposite cell forced \(1\), and one of its two neighbors labeled \(1\), and the single all-ones function: \(N_{2,2}=4+8+1=13\). For \(3\times3\), there are \(2F_3(3)=6\) all-\(0,2\) configurations, and exactly \(54\) configurations with two labels \(2\) and two labels \(1\). Of the latter, \(36\) arise from choosing two different rows, two different columns, one of the two bijections between them for the label-\(2\) pair, and one of the two cross-corners as a support label \(1\); the remaining label \(1\) is the unique vertex outside all selected rows and columns. The other \(18\) configurations place the pair of labels \(2\) in the same row (\(9\) configurations) or the same column (\(9\) configurations), and label by \(1\) the two cells outside the occupied rows and columns. Therefore \(N_{3,3}=6+36+18=60\), and all equality cases have been exhausted.

## Verification

The accompanying `verify.py` constructs the rook graph independently from its adjacency definition, enumerates all labelings of weight at most \(2m\) by choosing their label-\(2\) locations, retaining the mathematically compulsory label-\(1\) sites, and enumerating all additional label-\(1\) positions consistent with the weight cap. It tests both quasi-total Roman conditions directly. Thus its finite enumerations are exhaustive **within the stated weight cap**, not merely sampled. The program independently computes the proposed associated-Stirling count by dynamic programming over the number of processed named columns. It agrees on eleven boards, including all stated exceptions, and confirms five larger patterns through complete defender-map enumeration. Its output is in `verification_output.txt`. These finite checks corroborate, but are not used as substitutes for, the proof for arbitrary board dimensions.

## Relationship to prior work

Quasi-total Roman domination was defined by Cabrera-García, Cabrera-Martínez, and Yero in a March 2019 arXiv preprint, and further general bounds were obtained by Cabrera Martínez, Hernández-Gómez, and Sigarreta in 2021. Neither establishes the optimizer structure or exact count for Cartesian products of complete graphs. Mertens computed the **ordinary** domination polynomial of rook graphs in 2024, which enumerates dominating sets without the extra positive-neighbor requirement on each label \(2\); this does not determine the quasi-total Roman optimizer coefficient. The graph \(R_{m,n}\) is also the line graph of \(K_{m,n}\); the nonexceptional optimal configurations therefore correspond to specially constrained total edge-dominating sets, an equivalence used in the literature comparison.

## Limitations

The theorem concerns optimum quasi-total Roman functions only; it does not enumerate functions of every weight, and it makes no claim about an independent external audit. The bibliographic comparison covered relevant accessible foundational and rook-graph literature and semantic mathematical records. An equivalent optimizer enumeration via total edge domination or another unindexed formulation remains a residual originality risk. The computations cover finitely many explicitly listed boards, while the all-size conclusion rests on the proof above.

## References

1. S. Cabrera-García, A. Cabrera-Martínez, and I. G. Yero, *Quasi-total Roman domination in graphs*, arXiv:1903.09789 (first public preprint 23 March 2019); later *Results in Mathematics* 74 (2019), article 173.
2. A. Cabrera Martínez, J. C. Hernández-Gómez, and J. M. Sigarreta, *On the Quasi-Total Roman Domination Number of Graphs*, *Mathematics* 9 (2021), 2823, doi:10.3390/math9212823.
3. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (1 January 2024); *Journal of Integer Sequences* 27 (2024), article 24.3.7.
