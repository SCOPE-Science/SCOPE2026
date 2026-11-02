# Sharp aspect-ratio transition in minimum rook-domination exchange graphs

## Finding
Let \(R_{m,n}=K_m\square K_n\), where \(2\le m\le n\). Its vertices are squares of an \(m\)-by-\(n\) board; two squares are adjacent when they share a row or column. Let \(\mathcal J_{m,n}\) have as vertices all minimum dominating subsets of \(R_{m,n}\), joining two such subsets when exactly one occupied square is replaced by one unoccupied square (the **jump** adjacency convention, not necessarily a rook move).

**Rectangular regime.** For \(m<n\), the complete exchange graph is the Hamming graph
\[
\mathcal J_{m,n}\cong\underbrace{K_n\square\cdots\square K_n}_{m\text{ factors}}.
\]
It has \(n^m\) vertices, \(\frac12m(n-1)n^m\) edges, is regular of degree \(m(n-1)\), and has radius and diameter \(m\).

**Square regime.** For each \(n\ge3\), \(\mathcal J_{n,n}\) is connected and has
\[
|V(\mathcal J_{n,n})|=2n^n-n!,\qquad
|E(\mathcal J_{n,n})|=n(n-1)n^n+n!n(n-1)^2,
\]
\[
\operatorname{rad}(\mathcal J_{n,n})=n,\qquad
\operatorname{diam}(\mathcal J_{n,n})=2n-3.
\]
Its entire degree distribution has three strata:

| Degree | Number of vertices | Configuration type |
| --- | --- | --- |
| \(2n(n-1)\) | \(n!\) | permutation placements |
| \((n+2)(n-1)\) | \(2n!\binom n2\) | exactly one doubled column or row |
| \(n(n-1)\) | \(2n^n-n!-2n!\binom n2\) | all remaining placements |

For \(n=2\), the exceptional graph is \(J(4,2)\), with six vertices, twelve edges, radius two, and diameter two.

The degree strata and the sharp diameter characterize a qualitative change at the square-board boundary. In particular, a pair of placements consisting of an entire column and an entire row needs exactly \(2n-3\) replacements, although their unrestricted subset-exchange distance is only \(n-1\).

## Assumptions and scope
All graphs are finite and simple; the rooks are indistinguishable; squares may share a row or column. Domination means that every square is occupied or shares a row or column with an occupied square. The two states connected by a jump each have cardinality \(\gamma(R_{m,n})=m\). A jump may change both coordinates of the moved rook. Distances are graph distances in this **minimum-size jump** graph, not distances in the underlying rook graph, the slide-only exchange graph, or an add/delete graph with spare rooks. The above statements hold for all integers \(2\le m\le n\), with the indicated square boundary case.

## Proof

### 1. Exhaustive encoding of minimum placements
A placement dominates the board if and only if every row is occupied or every column is occupied. Indeed, an empty row and an empty column intersect in an undominated square. Conversely, if one of the two families is completely occupied, every square is dominated. Therefore \(\gamma(R_{m,n})=\min(m,n)=m\).

If \(m<n\), covering all \(n\) columns with \(m\) rooks is impossible. Every optimum has exactly one rook in each row. Such a placement is a function \(f:[m]\to[n]\), and a jump preserves the condition precisely when it changes the value of \(f\) at one argument. This proves the rectangular statement, including all metric and enumerative consequences.

For \(m=n\), every optimum is either a *row placement* \(A_f=\{(i,f(i)):i\in[n]\}\), or a *column placement* \(B_g=\{(g(j),j):j\in[n]\}\), where \(f,g:[n]\to[n]\). The overlap consists exactly of the \(n!\) permutation matrices. These two connected Hamming layers share these configurations, so their union with all jump edges is connected and has \(2n^n-n!\) vertices.

### 2. Degrees and edges
A nonpermutation row placement has \(n(n-1)\) within-row neighbors. A jump from such a placement to a column placement that fails to cover every row is possible exactly when the initial columns consist of \(n-1\) distinct values. Then one column occurs twice: remove either of its two rooks and place a rook in the missing column in one of the \(n-1\) still occupied rows. Hence there are exactly \(2(n-1)\) additional cross-layer neighbors. There are \(n!\binom n2\) row placements with this property: choose the two duplicate rows, the omitted column, the repeated column, and a bijection on the remaining rows. The column-only layer contributes the same number.

A permutation placement has \(n(n-1)\) moves within each layer, all distinct, hence degree \(2n(n-1)\). Every other placement has degree \(n(n-1)\). This proves the three strata. Summing degrees and dividing by two gives the stated edge formula.

### 3. Radius
Every state has a row or column presentation. In the same Hamming layer choose a placement differing in every coordinate. The two occupied-square sets are disjoint; since each jump replaces only one square, their distance is at least \(n\). Hence every eccentricity is at least \(n\). Any permutation placement lies in both Hamming layers, and is within \(n\) jumps of any state. Consequently the radius equals \(n\).

### 4. Sharp upper bound on the diameter
Two states in one Hamming layer are at distance at most \(n\). For a row state \(A_f\) and a column state \(B_g\), passing through a permutation \(p\) takes
\[
2n-s(p)\quad\text{steps,}\qquad
s(p)=\sum_{i=1}^{n}\mathbf{1}_{p(i)=f(i)}+\sum_{j=1}^{n}\mathbf{1}_{p^{-1}(j)=g(j)}.
\]
For a uniformly chosen permutation, \(\mathbb E[s(p)]=2\). We show that \(s(p)\ge3\) for some permutation unless both functions are constant.

Suppose instead that \(s(p)\le2\) for every permutation. The mean forces \(s(p)=2\) for every permutation. Define the integer matrix
\[
w_{ij}=\mathbf{1}_{f(i)=j}+\mathbf{1}_{g(j)=i},\quad
c_j=|f^{-1}(j)|,\quad r_i=|g^{-1}(i)|.
\]
Comparing two permutations differing by the exchange of two assigned columns implies that all two-by-two additive differences of \(w\) vanish. Thus \(w_{ij}\) is a row-plus-column matrix. Its row sums are \(1+r_i\), its column sums are \(1+c_j\), and its grand sum is \(2n\). Subtracting the row and column means yields
\[
nw_{ij}=r_i+c_j\qquad\text{for all }i,j.
\]
If \(f\) is nonconstant, each occupied column has \(1\le c_j<n\). For such a column, \(1\le r_i+c_j\le2n-1\), so divisibility by \(n\) forces \(r_i+c_j=n\) for every row. Summing the \(r_i\) gives \(c_j=n-1\). At least two columns are occupied, contradicting \(2(n-1)>n\) for \(n\ge3\). Therefore \(f\) is constant. In each column not used by \(f\), the same displayed equation forces every \(r_i\) to be either zero or \(n\); as their sum is \(n\), \(g\) is constant as well.

Accordingly, if either function is nonconstant, a suitable permutation bridge gives distance at most \(2n-3\). If both are constant, let \(A\) occupy column \(c\) and \(B\) occupy row \(r\). Choose a partial permutation of \(n-1\) cells including \((r,c)\), omitting a second row and a second column. From \(A\), change \(n-2\) rooks to obtain this partial permutation plus one extra rook in column \(c\). In one jump replace that extra rook with a second rook in row \(r\), in the missing column. The resulting column placement reaches \(B\) by changing \(n-2\) rooks. Hence this exceptional pair also has a path of length \(2n-3\). Since \(2n-3\ge n\) for \(n\ge3\), the claimed upper bound follows.

### 5. Sharpness
For the all-in-column placement \(A\), the number of distinct occupied columns begins at one. For the all-in-row placement \(B\), the number of distinct occupied rows ends at one. Both quantities change by at most one per jump. Consider the first state along any path from \(A\) that covers every column. If it is a permutation placement, reaching it takes at least \(n-1\) jumps, and reaching \(B\) then takes at least another \(n-1\). Otherwise it is a column-only state obtained by one jump from a row-only placement: the preceding placement must occupy at least \(n-1\) different columns, and the new state must occupy at least \(n-1\) different rows. Thus at least \(n-2\) jumps precede the crossing and at least \(n-2\) follow it, besides the crossing jump. Every path has length at least \(2n-3\). Together with the construction above, this proves the diameter.

For \(n=2\), every two-square subset of the four-square board is dominating. The exchange graph is the Johnson graph \(J(4,2)\), completing the small case.

## Verification
The supplied independent scripts give finite corroboration, not the proof of the all-parameter assertion. `verify_bruteforce.py` enumerates all cardinality-minimum dominating sets directly from the board adjacency relation, generates every one-square exchange, and checks the graph formulas for square sizes \(2\) through \(5\) and rectangular sizes \((2,3),(2,4),(3,4),(3,5)\). `verify_structural.cpp` independently constructs row and column function placements as bit masks and compares the exact edge count and shortest-path eccentricities on one representative of each row/column symmetry orbit for square sizes \(2\) through \(6\). See `VERIFICATION.md` for commands and recorded output. Both verified runs use exact finite graph operations.

## Relationship to prior work
The jump minimum-domination reconfiguration model appears under the name *jump \(\gamma\)-graph*, and is distinguished from slide \(\gamma\)-graphs and from add/delete dominating-set graphs in the cited survey. Suzuki, Mouawad and Nishimura study add/delete domination reconfiguration rather than this exact minimum-size jump metric. Lakshmanan and Vijayakumar discuss general jump \(\gamma\)-graph realizability, products, and cographs, not this rook-graph degree law or diameter. Mertens gives the rook domination polynomial and explicitly the known count \(2n^n-n!\) of minimum square-board placements; that **count is prior work**, not part of the novelty assertion. The contribution here is the entire jump-graph degree stratification and the exact radius/diameter phase transition, including the nontrivial cross-layer shortcut argument. A direct equivalent in specialized earlier literature remains possible.

## Limitations
The result concerns jump replacements of *minimum* dominating placements only. It does not assert the same diameter for sliding moves or for add/delete models, and does not determine exact distance between every individual pair. Finite checks extend only to the listed board sizes; the infinite-family result follows from the proof. The originality comparison is literature-based and cannot exclude unindexed results or alternate edge-domination terminology; independent external validation has not been performed.

## References
1. A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets* (first public arXiv version January 22, 2014), https://arxiv.org/abs/1401.5714.
2. C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey* (March 12, 2020), https://arxiv.org/abs/2003.05956. In particular §4.3 and §4.4.
3. S. A. Lakshmanan and A. Vijayakumar, *The gamma graph of a graph*, AKCE International Journal of Graphs and Combinatorics 7 (2010), 53–59, https://www.researchgate.net/publication/268019499_The_gamma_graph_of_a_graph.
4. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (first public January 1, 2024), https://arxiv.org/abs/2401.00716; especially equation (3).
5. H.-C. Chen and T.-Y. Ho, *The rook problem on saw-toothed chessboards*, Applied Mathematics Letters 21 (2008), 1234–1237, https://doi.org/10.1016/j.aml.2007.12.003.
