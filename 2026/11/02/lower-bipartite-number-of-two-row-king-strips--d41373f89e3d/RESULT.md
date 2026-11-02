# Lower bipartite number of two-row king strips

## Finding
Let \(H_n=K_2\boxtimes P_n\) be the strong product of a two-vertex clique and an \(n\)-vertex path, with \(n\ge1\). Identify its vertices with the two cells in each of \(n\) consecutive columns, with all distinct cells in equal or adjacent columns adjacent. A selected subset is *inclusion-maximal induced bipartite* if its induced graph is bipartite but adjoining any omitted vertex destroys bipartiteness. Its lower bipartite number is the minimum size of such a subset. The exact result is
\[
\boxed{\operatorname{LB}(K_2\boxtimes P_n)=2\left\lceil\frac n3\right\rceil\quad(n\ge1).}
\]
This is a sharp formula for every strip length, including the small endpoints, of a natural bounded-width subfamily of king graphs. The proof gives an exact local test for *all* inclusion-maximal induced bipartite subsets.

## Assumptions and scope
Graphs are finite and simple. The path \(P_n\) has \(n\) vertices, and the strong product is the usual king-move adjacency between two rows. Cardinality counts vertices, not connected components. The formula concerns *inclusion-maximal* induced bipartite sets, not maximum-cardinality induced bipartite sets. It is restricted to height two and does not assert an answer for arbitrary rectangular king graphs.

## Proof
**Characterization.** Fix a selected set \(S\). Let \(t_i\in\{0,1,2\}\) be its number of cells in column \(i\). Every two consecutive columns induce a complete graph on four vertices. Hence if \(t_i+t_{i+1}\ge3\), the selected graph contains a triangle and is not bipartite. Conversely, if \(t_i+t_{i+1}\le2\) for each adjacent pair, selected cells in any column number at most two, and the only possible occupied adjacent-column interactions are between singletons. All components of the selected graph are therefore isolated two-cell edges and paths of singletons (possibly isolated vertices), hence bipartite. This also handles \(n=1\), for which the unique maximal set uses both cells.

For an empty column \(i\), adding any cell preserves bipartiteness precisely when every existing neighboring column has occupancy at most one; accordingly, maximality requires an adjacent column occupied twice. For a column occupied once, adding its other cell breaks bipartiteness precisely when an adjacent column is occupied once (neighboring occupancy two is already forbidden). A twice-occupied column has no omitted cell. Therefore a word is maximal exactly when
\[
\begin{array}{ll}
\text{(i)}&t_i+t_{i+1}\le2\quad(1\le i<n);\\
\text{(ii)}&t_i=0\Longrightarrow\text{some available neighbor has occupancy }2;\\
\text{(iii)}&t_i=1\Longrightarrow\text{some available neighbor has occupancy }1.
\end{array}
\]
Every such occupancy word represents \(2^{\#\{i:t_i=1\}}\) different labeled vertex sets, because each singleton column independently chooses its row.

**Lower bound.** Let \(p,q,r\) be the numbers of columns occupied twice, once, and zero times, respectively. Put \(s=2p+q\), the number of selected vertices, and \(n=p+q+r\). Condition (ii) implies \(r\le2p\), since each twice-occupied column has at most two neighboring empty columns. Thus
\[
n\le3p+q=s+p.
\]
Condition (iii) additionally excludes \(q=1\), because a singleton column needs another singleton column as a neighbor. Write \(n=3k+j\) with \(j\in\{0,1,2\}\). If \(j=0\) and \(s\le2k-1\), then \(p\le k-1\), giving \(n\le s+p\le3k-2\), a contradiction. If \(j=2\) and \(s\le2k+1\), then \(p\le k\) and \(n\le3k+1\), also impossible. If \(j=1\) and \(s\le2k+1\), then \(p\le k\). For \(p\le k-1\), the bound becomes \(n\le3k\). For \(p=k\), we have \(q=s-2k\le1\); since \(q=1\) is forbidden, \(q=0\), and then \(n\le3k\). In every case \(s\ge2\lceil n/3\rceil\).

**Constructions.** The following occupancy words meet all three conditions and attain the lower bound, with \(k\ge0\):
\[
\begin{array}{ll}
n=3k:&(0,2,0)^k\quad(k\ge1),\\
n=3k+1:&(2,0,0)^k,2,\\
n=3k+2:&(2,0,0)^k,2,0.
\end{array}
\]
Every zero in these words is adjacent to a two, and there are no singleton columns. Their numbers of selected vertices are respectively \(2k\), \(2k+2\), and \(2k+2\). This matches the lower bound, proving the theorem.

## Verification
The standalone script `verify_kings_strip.py` independently constructs the actual king-strip adjacency graph and exhaustively tests every vertex subset for induced bipartiteness and inclusion-maximality at orders \(1\le n\le8\). These comprise 87,380 directly tested vertex subsets. An independent occupancy-word routine enumerates all words through \(n=12\), checking the local conditions and minimum cardinality against the theorem. The direct and occupancy enumerations agree in every overlapping case. The all-order proof is the counting argument above, not extrapolation from tests.

## Relationship to prior work
Bachstein and Goddard introduced and investigated the lower bipartite number and studied rook graphs. Their 2023 paper explicitly lists king graphs among directions of interest, but its accessible text does not state this two-row-strip formula. Madsen, Nielsen and Skjernaa (2002) study general enumeration and counting of maximal induced bipartite subgraphs without a comparable strip-specific exact lower number. Cao (2020) develops general maximal induced subgraph enumeration methods. This result addresses the original lower-bipartite invariant, rather than a renamed ordinary dominating number.

## Limitations
The two-row result does not settle the higher-width king-graph problem. There is no assertion that the result is unpublished in inaccessible literature; the full 2023 publisher PDF was not inspectable, leaving a publication-priority risk. Direct computations corroborate small cases and do not substitute for the proof. Independent mathematical audit has not been performed.

## References
1. A. Bachstein and W. Goddard, *The Lower Bipartite Number of a Graph*, Mathematica Pannonica **29** (2023), 49–56. doi:10.1556/314.2023.00003. First public online date 2023-02-07; primary MSC2020 05C69.
2. B. A. Madsen, J. M. Nielsen, and B. Skjernaa, *On the Number of Maximal Bipartite Subgraphs of a Graph*, BRICS Report Series RS-02-17 (2002). doi:10.7146/brics.v9i17.21735.
3. Y. Cao, *Enumerating Maximal Induced Subgraphs*, arXiv:2004.09885 (2020).
