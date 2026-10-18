# All minimum hop total Roman dominating functions of Cartesian rook graphs
## Finding
For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\), with vertices the \(m\times n\) cells and two cells adjacent precisely when they share a row or a column. Under the hop total Roman convention of Ahangar, Chellali, Sheikholeslami, and Soroudi, every zero-labeled cell must have a label-two vertex at graph distance exactly two, and the graph induced by all positive-labeled cells must have no isolated vertices. Then
\[
\gamma_{\mathrm{htR}}(R_{m,n})=\begin{cases}4,&m=2,\\5,&m=3,\\6,&m\ge4.\end{cases}
\]
More strongly, the *entire set of minimizing functions* consists exactly of the applicable six geometric families described below. Consequently, the number \(N_{m,n}\) of minimum functions on fixed labeled vertices is
\[
N_{m,n}=\begin{cases}
9,&m=n=2,\\
n,&m=2<n,\\
18,&m=n=3,\\
3n,&m=3<n,\\
6\binom m2\binom n2+6n\mathbf 1_{\{m=4\}}+6m\mathbf 1_{\{n=4\}},&m\ge4.
\end{cases}
\]
In particular, for \(m,n\ge5\) all minima are supported on three or four vertices in a single axis-aligned \(2\times2\) rectangle; exactly six minimizing functions occur per rectangle. The exceptional narrow and four-wide cases are specified exhaustively below.

## Assumptions and scope
Graphs are simple and undirected, and \(m,n\) are integers with \(2\le m\le n\). A *hop total Roman dominating function* on a graph \(G\) is a map \(f:V(G)\to\{0,1,2\}\) with both properties:

1. For every \(v\) with \(f(v)=0\), some \(u\) has \(f(u)=2\) and \(d_G(u,v)=2\).
2. The induced graph on \(\{v:f(v)>0\}\) has no isolated vertex.

Its weight is \(w(f)=\sum_{v\in V(G)}f(v)\). The symbol \(\gamma_{\mathrm{htR}}(G)\) denotes the minimum weight, and \(N_{m,n}\) counts functions on the *labeled* vertex set of \(R_{m,n}\), not equivalence classes under automorphisms. The Cartesian rook graph has distance exactly two precisely for cells in different rows and different columns.

The following six configurations are defined for arbitrary \(m,n\), and a family is part of the minimum classification **if and only if** its indicated weight equals \(\gamma_{\mathrm{htR}}(R_{m,n})\):

- **All-one:** label every cell \(1\), of weight \(mn\); one function.
- **One defender:** choose a cell, label it \(2\), label the other cells in its row or column \(1\), and label all remaining cells \(0\); weight \(m+n\), count \(mn\).
- **Two defenders in one row:** choose the row and two distinct columns, label those two cells \(2\), the other cells of that row \(1\), and all other cells \(0\); weight \(n+2\), count \(m\binom n2\).
- **Two defenders in one column:** choose the column and two distinct rows, label those two cells \(2\), the other cells of that column \(1\), and all other cells \(0\); weight \(m+2\), count \(n\binom m2\).
- **Two opposite defenders:** choose two rows and two columns, label one pair of diagonally opposite corners \(2\) and the other two corners \(1\), labeling all other cells \(0\); weight \(6\), count \(2\binom m2\binom n2\).
- **Three defenders in an L:** choose two rows and two columns, label three corners of their \(2\times2\) rectangle \(2\), all other cells \(0\); weight \(6\), count \(4\binom m2\binom n2\).

The six descriptions have disjoint label-two cardinalities or incidence patterns, including at tied weights; no double counting occurs.

## Proof
**Step 1: Each of the six displayed families is feasible.** If no cell has label \(2\), the all-one function is feasible because the rook graph has no isolated vertices. With one defender \((r,c)\), every cell outside row \(r\) and column \(c\) is at distance two from it, while every cell in its row or column was made positive. The positive cross is connected. For two defenders in a common row (respectively column), any cell outside that row (column) is at distance two from at least one of the two defenders, since their columns (rows) differ, and the entire occupied row (column) is a positive clique. For opposite defenders in a \(2\times2\) rectangle, the only cells without a distance-two defender are the other two corners, both made positive; the four selected corners induce a four-cycle. For an L of three defenders, each remaining cell has a defender in a different row and different column: a row-column cross containing all three occupied corners would have to be centered at their common corner, which is already positive. Those three positive cells induce a path, hence have no isolated vertices.

**Step 2: A sharp lower bound by the number of label-two cells.** Write \(t\) for the number of vertices labeled \(2\). If \(t=0\), all cells must be positive, so the weight is at least \(mn\), with equality only for the all-one function. If \(t=1\), let its cell be \((r,c)\). Every other cell in row \(r\) or column \(c\) cannot lie at distance two from that defender; all \(m+n-2\) such cells must be positive. Hence \(w(f)\ge m+n\), with equality only in the one-defender cross family.

Suppose \(t=2\). If the defenders share a row, every other cell in that row must be positive, giving \(w(f)\ge n+2\); equality forces the stated full-row configuration. Analogously, a common column gives \(w(f)\ge m+2\), with equality only for the full-column configuration. If the two defenders occupy different rows and different columns, the two other corners of their \(2\times2\) rectangle have no defender at distance two and so must be positive; thus \(w(f)\ge 6\), with equality only for the opposite-defenders pattern.

If \(t\ge3\), then \(w(f)\ge2t\ge6\). Equality requires exactly three label-two cells and no label-one cells. For \(m,n\ge4\), these three positive cells must have no isolated vertex. Any three-vertex rook subgraph with no isolated vertex is either a triangle (three cells of one row or column) or a path of length two (three corners of a \(2\times2\) rectangle). A triangle in one row cannot be feasible when \(n\ge4\): an unoccupied cell in that row is zero and has no defender at distance two. The analogous column triangle is excluded since \(m\ge4\). Thus, at weight \(6\) and \(m,n\ge4\), equality requires an L of three label-two cells. By Step 1 these L configurations all work. The smaller widths \(m\le3\) attain weight below \(6\), so no function with \(t\ge3\) can be optimal there.

**Step 3: Minimum and classification.** Steps 1–2 give
\[
\gamma_{\mathrm{htR}}(R_{m,n})=\min\{mn,m+n,n+2,m+2,6\}.
\]
Under \(2\le m\le n\), this minimum is \(4\) for \(m=2\), \(5\) for \(m=3\), and \(6\) for \(m\ge4\). Equality in every lower-bound case is fully classified in Step 2; all these equality patterns were proved feasible in Step 1. It follows that every minimum function belongs to exactly one of the six listed families whose weight equals this minimum. Counting the choices for each family yields the announced \(N_{m,n}\) formula; for \(m,n\ge5\), only the two rectangle families compete and contribute \((2+4)\binom m2\binom n2\). The formula for \(m\ge4\) includes the exceptional tied full-column family when \(m=4\), and the tied full-row family when \(n=4\). The \(2\times2\) case also has the all-one and one-defender ties. This completes the proof.

## Verification
The companion standalone `verify.py` builds the rook graph adjacency directly, computes all graph distances by breadth-first search, and applies the defining two conditions to each candidate assignment. For every board in the explicit test suite
\[
(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(4,6),(5,5),(5,6),(6,6),
\]
it checks every labeling of weight at most \(6\), combining exhaustive ternary enumeration for small order with independent enumeration by disjoint label-one and label-two supports for larger order. Where the graph has more than six vertices, a labeling with no defenders cannot be feasible at weight at most six, because every vertex would have to be positive. The program therefore omits only that provably irrelevant regime. It excludes all weights below the claimed optimum, verifies the count at the minimum, and tabulates the geometric types of minimizing labelings.

The recorded replay result is `VERIFY_OK cases= 13 candidate_labelings_tested= 4516156`. Computation verifies these finite boards only; the parameter-uniform result comes from the proof above. The program uses only the Python standard library.

## Relationship to prior work
The defining article of Abdollahzadeh Ahangar, Chellali, Sheikholeslami, and Soroudi introduces hop total Roman domination and treats complexity, paths and cycles, and extremal numerical cases. Its publicly accessible full HTML text does not give the two-parameter rook-graph extremizer enumeration proved here. A later 2-hop Roman study by Akwu and collaborators demands *two* label-two vertices at distance two from each zero and does not impose the same total-positive-support condition; even its treatment of products therefore concerns a different parameter. Related complete-prism Roman \(\{3\}\)-domination uses labels up to \(3\) and a *neighbor-sum* threshold, not this distance-two defender condition. Likewise, ordinary total Roman domination and perfect Roman domination use distinct rules and do not mathematically imply this minimum-set classification. The distinguishing contribution here is the six-family description of *all minimum functions* on every rectangular rook graph, including the exact multiplicities and width transition.

## Limitations
The theorem enumerates only minimum-weight hop total Roman functions, not their full weight polynomial, and applies only to Cartesian products of two complete graphs with both orders at least two. It does not address arbitrary Hamming graphs or products of three or more cliques. The finite replay does not independently certify every integer size, and no independent human or external mathematical review has been performed. Searches cannot exclude an equivalent result in literature using a different name or not indexed by the consulted sources.

## References
1. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, and M. Soroudi, “Hop total Roman domination in graphs,” *AKCE International Journal of Graphs and Combinatorics* 20 (2023), 73–78; first online 30 March 2023. DOI:10.1080/09728600.2023.2184288.
2. A. D. Akwu and collaborators, “2-Hop Roman Domination of Some Product Graphs,” DOI:10.37560/matbil2549141a (2026). This uses two distance-two defenders, without the same total-support requirement.
3. N. Ebrahimi, H. Abdollahzadeh Ahangar, M. Chellali, and S. M. Sheikholeslami, “Graphs with small or large Roman \(\{3\}\)-domination number,” *RAIRO - Operations Research* 57 (2023), 1195–1208, DOI:10.1051/ro/2023058. This investigates the neighbor-sum Roman \(\{3\}\) variant.
