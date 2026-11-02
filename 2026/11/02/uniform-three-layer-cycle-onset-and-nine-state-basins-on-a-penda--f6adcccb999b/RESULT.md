# Uniform three-layer cycle onset and nine-state basins on a pendant clique

## Finding
For every integer \(r\ge2\), let \(G_r\) consist of a labelled clique on \(r+1\) vertices, one of which is marked as the hub, and one additional degree-one vertex adjacent only to the hub. Run the synchronous, three-color, successor-contact cyclic cellular automaton on \(G_r\). Write \(F\) for its global transition, \(T\) for the first time at which the full labelled configuration is periodic, and \(p\) for its eventual *least* period. Set
\[
Q_r=3^r-2^{r+1}+1.
\]
Then \(F^5=F^2\); its maximal first-entry time is exactly two, and its only eventual least periods are one and three. The full labelled first-entry census is
\[
\begin{array}{c|ccc}
 &T=0&T=1&T=2\\\hline
p=1&3&3(3\cdot2^r-2)&3(3\cdot2^r-2)\\
p=3&3Q_r&3Q_r&3Q_r
\end{array}.
\]
There are exactly three fixed configurations and \(Q_r\) primitive three-cycle orbits. **Every primitive three-cycle orbit has an individual attraction basin of exactly nine states**, split into precisely three initial states in each of the three entrance-time layers. **Every fixed point has a basin of size \(3(2^{r+1}-1)\)**, split as \(1,3\cdot2^r-2,3\cdot2^r-2\) by first-entry time. Consequently, for independent uniform initial colors, the first-entry time is **exactly uniform on \(\{0,1,2\}\)** conditional on eventual least period three, and
\[
\Pr(p=3)=1-2(2/3)^r+3^{-r}.
\]
In particular, as \(r\to\infty\), eventual period three has probability tending to one, but its first-periodic-entry time remains uniformly distributed over three possible times. The same formulas hold at \(r=1\) with \(Q_1=0\), so that this boundary path graph has only fixed orbits.

## Assumptions and scope
The graph is finite, simple, undirected, with vertices \(h,v_1,\ldots,v_r,\ell\): the set \(\{h,v_1,\ldots,v_r\}\) spans a complete graph, and the leaf \(\ell\) is adjacent only to \(h\). Vertex labels are fixed; the enumeration does not identify colorings under graph automorphisms or under global color shifts. States are in \(\mathbb Z/3\mathbb Z\). Each vertex of color \(c\) changes to \(c+1\pmod3\) at the next synchronous update if and only if at least one of its *open-neighborhood* neighbors already has color \(c+1\); otherwise it remains at \(c\). The initial coloring is arbitrary in the deterministic assertions. Probability assertions use independent uniform colors on every vertex. A basin counts all starting labelled states eventually entering the named periodic orbit, including the states of that orbit. \(T\) counts updates from the initial state, with \(T=0\) for initially periodic states.

## Proof
**1. Core and leaf phase classification.** Color-rotation symmetry allows us to subtract the initial hub color and hence assume \(h=0\) at time zero. Let \(S\subseteq\{0,1,2\}\) be the nonempty set of colors appearing among the other \(r\) clique vertices; let \(L\in\{0,1,2\}\) be the leaf's initial color relative to the hub. Because these other clique vertices have identical neighborhoods apart from themselves, and a successor color never equals a vertex's own color, each nonhub clique update depends only on \(S\) and on the hub color. The complete seven-support, three-leaf-color classification follows by the elementary successor rule:

\[
\begin{array}{c|ccc}
S &L=0&L=1&L=2\\\hline
\{0\}&(0,1)&(2,1)&(1,1)\\
\{1\}&(2,1)&(1,1)&(2,1)\\
\{0,1\}&(2,1)&(1,1)&(2,1)\\
\{2\}&(1,1)&(2,1)&(1,1)\\
\{0,2\}&(1,1)&(2,1)&(1,1)\\
\{1,2\}&(1,3)&(2,3)&(0,3)\\
\{0,1,2\}&(1,3)&(2,3)&(0,3)
\end{array}
\]
Every entry is \((T,p)\), not merely a description of the clique's trajectory. To see the table directly, first suppose \(1,2\in S\): the *clique* has all three colors and every clique vertex advances by one at every subsequent time. In the co-rotating frame with the hub, the leaf phase evolves by \(0\mapsto2\), \(1\mapsto0\), \(2\mapsto2\). Thus leaf phases \(2,0,1\) first enter the rotating three-cycle in times \(0,1,2\), respectively. This applies to every labelled nonhub color word with the same support.

If \(S\subseteq\{0,1\}\) and \(1\in S\), the nonhub clique colors become all one after one update. The leaf is then at the same color precisely for initial \(L=1\); otherwise it agrees after exactly two updates. If \(S\subseteq\{0,2\}\) and \(2\in S\), the analogous calculation gives first entry at one update for \(L=0,2\), and two updates for \(L=1\). Finally, at \(S=\{0\}\) the initial state is fixed only when \(L=0\); at \(L=2\) the leaf catches the hub in one update, and at \(L=1\) the hub moves first, with the other clique vertices catching up at the second update. These cases prove the table. No longer period or later first entry is possible. For \(r\ge2\), supports containing both 1 and 2 exist, and a configuration with \(S=\{0\},L=1\) proves the sharp time two.

**2. Counting.** For each fixed initial hub color, the number of nonhub color words in which both colors 1 and 2 occur is \(Q_r=3^r-2\cdot2^r+1\), by inclusion-exclusion. Each such word contributes one first-entry configuration at each time \(0,1,2\) for eventual period three, through its three leaf choices. The three initial hub colors multiply every layer count by three. This yields \(N_{0,3}=N_{1,3}=N_{2,3}=3Q_r\).

For eventual fixed points, the only initially fixed words have all clique and leaf colors equal, hence \(N_{0,1}=3\). At fixed initial hub color zero, \(T=1\) has one state from \(S=\{0\}\), \(L=2\); it has \(2^r-1\) states from \(S\subseteq\{0,1\}\) with 1 occurring and \(L=1\); and it has \(2(2^r-1)\) from \(S\subseteq\{0,2\}\) with 2 occurring and \(L\in\{0,2\}\). This totals \(3\cdot2^r-2\); the complementary nonsynchronizing-at-time-one fixed-point trajectories have the same count at \(T=2\). Multiply by three hub colors to obtain the remaining rows. The sum of all six classes is \(3^{r+2}\), as required.

**3. Individual attraction basins.** Any three-cycle has a fully three-colored clique, whose states rotate rigidly. The number of three-color clique configurations is \(3Q_r\), hence the number of primitive three-cycle orbits is \(Q_r\). A given orbit consists of three successive clique phases. For each phase, the three initial leaf colors produce precisely one state at each first-entry time \(0,1,2\) while leaving the clique on that rotating orbit, yielding exactly nine basin states per orbit. No state whose clique omits a color can enter one of those orbits, by step 1. The only fixed states are the three consensus states. By color-rotation equivariance their basins have equal size; the fixed-basin total is \(3+6(3\cdot2^r-2)=9(2^{r+1}-1)\), hence each has size \(3(2^{r+1}-1)\). Similarly, each fixed point's temporal layers have sizes \(1,3\cdot2^r-2,3\cdot2^r-2\). All assertions follow.

## Verification
The proof is size-uniform and does not extrapolate from finite enumeration. The standalone `check_clique_support.py` independently iterates all \(7\times3=21\) possible nonhub-support and relative-leaf-color classes, applies the exact local update to a representative with one copy of each present nonhub color, confirms the displayed \((T,p)\) table, and checks inclusion-exclusion counts over \(r=1,\ldots,15\). The independent `check_clique_direct.cpp` constructs the full labelled graph's neighbor-update map without the support reduction, exhaustively tests every initial coloring for \(r=1,\ldots,11\), and separately checks the size of every individual periodic basin. The compiled program tested exactly 2,391,471 labelled states. Command lines and actual outputs are in `VERIFICATION.md`, `clique_support_output.txt`, and `clique_direct_output.txt`. None of these finite tests substitutes for steps 1–3 of the proof.

## Relationship to prior work
Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs* (arXiv:1610.07320v1, posted 2016-10-24), prove a general irrotationality criterion for synchronization and a graph-diameter bound for **synchronizing** initial colorings (Theorem 3). For the present graph this already implies the eventual fixed/oscillatory distinction and the two-step bound on synchronizing states. Neither that theorem nor its paper's graph-independent cycle-activity statement specifies the nine-element basins of each individual rotating three-cycle or the exact uniform \(\{0,1,2\}\) period-entry clock in the oscillatory sector. Those finer statements are the contribution assessed here. On the intact clique, any fully three-colored initial configuration is periodic immediately. A *single attached leaf* creates two equally populated transient layers without changing the number of distinct primitive three-cycle orbits. The graph is not the friendship-graph windmill, cocktail-party graph, or complete multipartite network appearing in other specific classifications. Identical short iterate identities in other graph families do not imply the labelled basin formulas established here.

## Limitations
The dynamics uses exactly three colors, threshold-one open-neighbor successor contact, and exactly one leaf; the formulas are not asserted for Greenberg–Hastings, inhibitory firefly, threshold-two, or multiple-leaf dynamics. The work does not classify all possible graph families with the same first-entry distribution. Novelty was assessed by comparison with accessible primary literature and published claims, not by a proof that an unindexed equivalent does not exist. Independent validation has not been performed.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first posted 2016-10-24), https://arxiv.org/abs/1610.07320. Definition of CCA and Theorem 3; text and proof in Sections 2 and 4.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (first posted 1993-03-22), https://arxiv.org/abs/patt-sol/9303002. Earlier background on CCA and related excitable media.
