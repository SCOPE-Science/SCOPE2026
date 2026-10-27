# Exact quadratic consensus time for proportional group voting on overlap paths

## Finding
For integers \(L\ge 2\), \(k\ge 2\), and \(1\le s\le k/2\), let \(E_1,\ldots,E_L\) be a linear hypergraph path of equally sized groups: every edge has \(k\) vertices, consecutive edges intersect in exactly \(s\) vertices, these intersections within an internal edge are disjoint, and nonconsecutive edges are disjoint. There are \(N=L(k-s)+s\) distinct voters. Each voter holds opinion A or B. Every mixed hyperedge has an independent rate-one exponential clock; when it rings, one of its \(k\) vertices is selected uniformly, and the entire hyperedge adopts that vertex's opinion. There is no rewiring.

Fix any integer \(j\) with \(1\le j<L\). Initially every vertex in \(E_1\cup\cdots\cup E_j\) holds A, and every other vertex holds B. Write \(T\) for the first unanimous time and \(p=s/k\). Then consensus is reached almost surely, and the **exact mean physical consensus time and final A probability** are
\[
\mathbb E[T]=L-j+\frac{1-p}{p}j(L-j),\qquad
\mathbb P(\text{all A at }T)=\frac{j(k-s)+s}{L(k-s)+s}.
\]
In particular, for fixed \(k,s\) and \(j/L\to\theta\in(0,1)\),
\[
\frac{\mathbb E[T]}{L^2}\longrightarrow \frac{k-s}{s}\,\theta(1-\theta).
\]
This is a complete exact outcome-and-first-moment law for the specified polarized-front initial condition, not a claim for all starting configurations.

## Assumptions and scope
The clock normalization is one independent rate-one Poisson process per *mixed* hyperedge. A monochromatic hyperedge is inactive, and no other events occur. Group updates are simultaneous and proportional, not majority updates or independent vertex updates. All overlaps have equal cardinality, nonadjacent groups are disjoint, and at each internal group the two overlap subsets do not intersect. The restriction \(2s\le k\) enforces this geometry and includes the boundary \(2s=k\). No assumption on the number of voters other than the displayed construction is needed.

The initial A set is the union of the first \(j\) complete hyperedges. Consequently the overlap between the \(j\)-th and \((j+1)\)-st edges begins with opinion A. Each distinct vertex in all later groups begins with opinion B. The total number of initial A voters is \(j(k-s)+s\).

## Proof
**Invariant front.** Set \(p=s/k\), \(q=1-p\). There are two front configurations indexed by \(j=1,\ldots,L-1\). In configuration \(R_j\), the first \(j\) groups are entirely A, the later groups are entirely B except that the left overlap of \(E_{j+1}\) contains \(s\) A vertices. Thus precisely \(E_{j+1}\) is mixed with \(s\) A vertices and \(k-s\) B vertices. In configuration \(V_j\), the first \(j-1\) groups are entirely A and groups after \(E_j\) are entirely B, while \(E_j\) contains \(k-s\) A vertices and its right overlap consists of \(s\) B vertices. Thus precisely \(E_j\) is mixed. The initial state is \(R_j\). Some symbolic states coincide as physical colorings when \(k=2s\); this does not change their transition rates or the following equations.

By considering the only active group's chosen opinion, the jumps are
\[
R_j\xrightarrow{p}R_{j+1},\quad R_j\xrightarrow{q}V_j,
\qquad V_j\xrightarrow{p}V_{j-1},\quad V_j\xrightarrow{q}R_j,
\]
where \(R_L\) means all A and \(V_0\) means all B. These are probabilities at the next ring, not continuous-time rates; every transient state has total clock rate exactly one. They follow by direct inspection of the disjoint overlap subsets. This finite chain has an absorbing path from every transient state, with positive probability because \(p>0\), so absorption occurs almost surely and has finite expectation.

**Exact mean.** Write \(U_j=\mathbb E[T\mid R_j]\) and \(W_j=\mathbb E[T\mid V_j]\), with boundary conditions \(U_L=W_0=0\). First-step conditioning gives, for \(1\le j<L\),
\[
U_j=1+pU_{j+1}+qW_j,\qquad
W_j=1+pW_{j-1}+qU_j.
\]
The displayed explicit solutions
\[
U_j=(L-j)+\frac{q}{p}j(L-j),\qquad
W_j=j+\frac{q}{p}j(L-j)
\]
satisfy both recurrences identically and satisfy the boundary conditions. Uniqueness follows from finite expected absorption of the transient chain (equivalently, invertibility of its transient Poisson system). Since the prescribed initial state is \(R_j\), this proves the expected-time formula. With \(j/L\to\theta\) at fixed \(p\), division by \(L^2\) proves the quadratic asymptotic.

**Fixation probability.** Let \(M_t\) be the number of A voters. Conditional on a group of size \(k\) having \(a\) A voters, the group update changes the A count to \(k\) with probability \(a/k\) or zero with probability \(1-a/k\), so its expected count after the update is \(a\). Therefore the bounded process \(M_t\) is a martingale in continuous time. At almost-sure absorption it equals either zero or \(N\). Bounded convergence gives \(N\mathbb P(\text{all A})=M_0=j(k-s)+s\), proving the second formula. The martingale proof does not assert any unconditional uniform-time approximation.

## Verification
The standalone `verify.py` constructs the *labeled* vertices and hyperedges, performs the exact mixed-hyperedge transitions directly from bitmasks, enumerates every reachable state, and solves the full transient absorbing-chain linear systems using `fractions.Fraction`. It independently compares both quantities with the theorem for all \(L=2,\ldots,7\), \(k=2,\ldots,8\), every positive \(s\) satisfying \(2s\le k\), and every \(j=1,\ldots,L-1\). All 336 tests pass, including the degenerate overlap geometry \(k=2s\). Symbolic substitution into the recurrence verifies the formulas at arbitrary admissible parameters; the finite computation alone is not the general proof.

For example, \(L=5\), \(k=4\), \(s=1\), \(j=2\) gives \(N=16\), \(\mathbb E[T]=21\) time units and probability \(7/16\) of unanimous A. With just two groups, \(L=2\) and \(j=1\), the mean reduces to \(k/s\).

## Relationship to prior work
Golovin, Mölter and Kuehn's proportional hyperedge-voting model supplies the simultaneous whole-group update mechanism and documents long-lived stochastic opinion coexistence. Their article studies adaptive hypergraphs and moment-closure approximations, not this exact fixed-overlap hyperpath first-passage law. Papanikolaou and collaborators study majority-oriented group influence and magnetization drift, not the neutral proportional clock used here. Chung and Tsiatas formulate a broad hypergraph-coloring Markov framework, especially for memoryless interactions, but do not provide the present polarized-front quadratic mean and fixation formulas. Classical voter and language-contact models supply qualitative random-walk and quadratic-in-group-count analogies; these are not asserted to be new.

The innovation claimed is the exact invariant-front reduction and closed \(L,k,s,j\)-dependent physical-time and fixation formulas for the explicitly defined proportional all-at-once hypergraph process. General Markov-chain solvability and the underlying first-step method are prior mathematical tools.

## Limitations
The result assumes a fixed linear overlap path, identical group sizes, disjoint adjacent overlaps, neutral proportional whole-group updates, no rewiring, and a single polarized front. Arbitrary hypergraph colorings may contain multiple active groups; they are not covered. The source's empirical/mean-field conclusions for random evolving hypergraphs are not implied. No independent external validation or exhaustive global publication-priority claim is made. Earlier work establishes general voter-model random-walk methods, so novelty attaches only to the precise family-specific closed formulas rather than those general techniques.

## References
1. A. Golovin, J. Mölter, C. Kuehn, *Polyadic Opinion Formation: The Adaptive Voter Model on a Hypergraph*, arXiv:2308.03640 (first posted 2023-08-07); *Annalen der Physik* 536 (2024), 2300342, DOI:10.1002/andp.202300342. Full open-access text: https://onlinelibrary.wiley.com/doi/full/10.1002/andp.202300342 .
2. N. Papanikolaou, G. Vaccario, E. Hormann, R. Lambiotte, F. Schweitzer, *Consensus from group interactions: An adaptive voter model on hypergraphs*, arXiv:2201.06421 (2022); *Physical Review E* 105, 054307. Full preprint: https://arxiv.org/pdf/2201.06421 .
3. F. Chung, A. Tsiatas, *Hypergraph Coloring Games and Voter Models* (2012), https://cseweb.ucsd.edu/~atsiatas/voter.pdf .
4. J. Kim et al., *Competition between group interactions and nonlinearity in voter dynamics on hypergraphs*, arXiv:2407.11261 (2024); node-level group-constrained voter dynamics distinct from whole-edge propagation.
