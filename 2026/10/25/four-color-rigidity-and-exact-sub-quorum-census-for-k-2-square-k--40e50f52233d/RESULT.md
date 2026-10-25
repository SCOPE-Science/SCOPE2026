# Four-color rigidity and exact sub-quorum census for \(K_2\square K_n\)

## Finding
For every integer \(n\ge2\), define \(R_n=K_2\square K_n\), consisting of two \(n\)-cliques with a perfect matching between corresponding columns. The sub-quorum coloring number satisfies
\[
\psi_{sq}(R_n)=\min\{n,4\}.
\]
For every \(n\ge4\), a sub-quorum coloring uses four colors if and only if the following hold (up to renaming the colors): the two row palettes are disjoint and each has exactly two colors; the colored column sets \(I\) and \(J\) in the two rows are nonempty, disjoint, and of even size; within each row the two colors each occupy precisely half of that row's selected columns. All unlisted vertices are uncolored.

There are exactly
\[
Q_n=\sum_{\substack{a,b\ge1\\2a+2b\le n}}\binom n{2a}\binom{n-2a}{2b}\frac12\binom{2a}{a}\frac12\binom{2b}{b}
=\frac{n!}{4}\sum_{\substack{a,b\ge1\\2a+2b\le n}}\frac1{(a!)^2(b!)^2(n-2a-2b)!}
\]
four-color sub-quorum partitions on the labeled vertex set, with color names disregarded. In particular \(Q_4=6\), \(Q_5=30\), \(Q_6=180\), \(Q_7=840\), and
\[
\sum_{n\ge0}Q_n\frac{t^n}{n!}=\frac{e^t}{4}\left(\sum_{a\ge1}\frac{t^{2a}}{(a!)^2}\right)^2.
\]

## Assumptions and scope
All graphs are finite, undirected, and simple. Label vertices of \(R_n\) by \((r,j)\) with \(r\in\{0,1\}\) and \(j\in[n]\). Vertices in the same row are adjacent, and \((0,j)\) is joined to \((1,j)\). A partial coloring \(f:S\to\{1,\ldots,k\}\) is onto its color set and is sub-quorum if for every \(v\in S\),
\[
2|N[v]\cap f^{-1}(f(v))|\ \ge\ |N[v]\cap S|.
\]
The quantity \(\psi_{sq}\) maximizes \(k\), allowing vertices outside \(S\) to stay uncolored. A coloring count treats the graph's rows and columns as labeled, but identifies colorings differing only by a global permutation of color names. Thus it counts partitions of the colored support, not named-color assignments.

## Proof
Let \(s_r\) be the number of colored vertices in row \(r\), and let \(t_r\) be the number of distinct colors represented there. For a row color \(c\), let \(a_{r,c}\ge1\) be its multiplicity. At a vertex of that color, the colored closed neighborhood consists of the entire colored part of its row, plus possibly its matching partner. If \(\varepsilon\in\{0,1\}\) says that partner is colored and \(\eta\in\{0,1\}\) says it has color \(c\), then \(\eta\le\varepsilon\) and the sub-quorum inequality reads
\[
2(a_{r,c}+\eta)\ge s_r+\varepsilon.
\]
It follows that \(2a_{r,c}\ge s_r-1\) for every represented row color. If \(t_r\ge3\), summing \(a_{r,c}\ge\lceil(s_r-1)/2\rceil\) over those colors shows that \(s_r=3\), \(t_r=3\), and all three row colors occur once. Indeed \(s_r\ge3\lceil(s_r-1)/2\rceil\) is impossible when \(s_r\ge4\). A singleton-colored vertex in this row has three colored vertices in its row's closed neighborhood; it can satisfy the inequality only if its matching partner is colored with the same color. Therefore, the opposite row contains these three partners with three distinct colors. Applying the same argument there gives exactly three colored vertices and the same palette in both rows. In particular, every coloring with at least four distinct colors has at most two distinct colors in each row; there can be at most four colors in all.

Suppose a coloring has exactly four colors. It must use two colors in each row and the two palettes must be disjoint. For every colored vertex its matching partner (if colored) has a different color. Writing \(a\) and \(b\) for the two color multiplicities in a fixed row, with \(s=a+b\), the inequalities imply \(2a\ge s+\varepsilon_a\) and \(2b\ge s+\varepsilon_b\) for all vertices of the respective colors. Since \(2a+2b=2s\), necessarily \(a=b=s/2\), and all corresponding \(\varepsilon\)'s vanish. Thus the two colored row supports have even positive size and do not meet in a column. Conversely, if these conditions hold, every colored closed neighborhood lies entirely within its row and contains exactly twice as many colored vertices as the color multiplicity; each inequality holds with equality. Four colors are therefore possible exactly when \(n\ge4\).

For \(n=3\), coloring both vertices in each of the three matching columns with one column-specific color provides three valid colors: every selected closed neighborhood contains four vertices, two of its color. Four colors are impossible by the preceding characterization. For \(n=2\), the graph is a four-cycle; two nonadjacent singletons realize two colors. Three or four colors are impossible: with at most four colored vertices, three distinct colors require either three isolated labels on a three-vertex induced path (its middle vertex violates sub-quorum) or full support with at least two singleton color classes (each has three colored vertices in its closed neighborhood and violates sub-quorum). This proves the number formula for all stated orders.

To enumerate four-colorings, write \(|I|=2a\), \(|J|=2b\) for integers \(a,b\ge1\) and \(2a+2b\le n\). Choose \(I\) and \(J\) as \(\binom n{2a}\binom{n-2a}{2b}\) disjoint subsets. Each row has \(\binom{2a}{a}/2\) unordered equipartitions into two nonempty color classes, and analogously for the other row. These choices are unique when color names are forgotten. The coefficient formula follows; multiplication of exponential generating functions gives the displayed product identity.

## Verification
Run `python3 verify.py` with Python 3.9 or later. The self-contained program reconstructs the matched-clique graph and checks the local sub-quorum inequalities directly, enumerating every uncolored/partition assignment modulo permutations of color labels using restricted-growth sequences. For \(n=2,3,4,5\) it reports respectively \(52,877,21147,678570\) assignments inspected and maximum color counts \(2,3,4,4\); for \(n=4,5\) it independently finds exactly \(6\) and \(30\) optimal partitions and checks every optimum against the proved structural characterization. It also evaluates the exact count formula through \(n=12\). Successful execution terminates with `VERIFY_OK`. These finite checks corroborate, but do not replace, the infinite proof.

## Relationship to prior work
Ma, Sahbi, and Zhang, *Sub-quorum colorings of graphs*, arXiv:2609.25128, introduced a broad structural treatment of this partial-coloring invariant, including degree bounds, algorithmic results, complete multipartite graphs, rectangular grid strips, and hypercubes. The initial public arXiv submission dates to September 20, 2026. Definition 2.2 is used here. This result instead treats the line graph of a complete bipartite graph with one part of size two, a graph of two matched cliques; it establishes a four-color plateau and classifies/counts all optimizers. It does not follow by substituting the rectangular *grid* results, which concern Cartesian products of paths, or complete multipartite cases. The 2013 quorum-coloring framework concerns total colorings and introduced the partial variant as a problem. We do not claim those definitions or general inequalities as new.

## Limitations
The classification treats the two-row rook graph only, not arbitrary rook boards or other graph products. Its exact count identifies color permutations; named colors would introduce an additional factor of \(4!\) for four-color optima. The result has been checked against accessible literature and mathematical research records, not independently certified for historical priority. The verifier is exhaustive only for the displayed finite orders; no external audit has been performed.

## References
1. H. Ma, R. Sahbi, and W. Zhang, *Sub-quorum colorings of graphs*, arXiv:2609.25128 (initial submission September 20, 2026), https://arxiv.org/html/2609.25128v4 .
2. S. M. Hedetniemi, S. T. Hedetniemi, R. Laskar, and H. M. Mulder, *Quorum colorings of graphs*, AKCE International Journal of Graphs and Combinatorics 10 (2013), https://repub.eur.nl/pub/37620/EI2012-20.pdf .
3. R. Sahbi, A. Belkina, and M. Bennadji, *Sub-quorum colorings of some infinite families of caterpillars*, arXiv:2609.39619, https://arxiv.org/abs/2609.39619 .
