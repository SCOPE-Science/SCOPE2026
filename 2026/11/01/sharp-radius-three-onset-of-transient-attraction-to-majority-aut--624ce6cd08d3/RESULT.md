# Sharp radius-three onset of transient attraction to majority-automaton two-cycles

## Finding
For every integer radius \(r\ge1\) and ring length \(n\ge 2r+1\), let \(F_{r,n}\) be the synchronous binary majority cellular automaton on \(\mathbb Z/n\mathbb Z\), with each cell replacing its state by the strict majority of the \(2r+1\) sites at offsets \(-r,\ldots,r\), counting its own current state once. A primitive two-cycle means two different configurations \(y,z\) with \(F(y)=z\) and \(F(z)=y\). A *transient predecessor* of a periodic configuration \(y\) is an \(x\) with \(F(x)=y\) but \(x\) not itself periodic.

**Sharp interaction-radius threshold.** If \(r=1\) or \(r=2\), every configuration in any primitive two-cycle has precisely one one-step preimage: its companion in that cycle. Hence no transient initial configuration ever enters a primitive two-cycle. Radius \(3\) is the smallest radius for which this isolation fails, already on a ring of ten cells.

**Exact exponential incoming multiplicity.** Put \(Y=0011001110\) and \(Z=1000111001\). For every integer \(m\ge1\), let \(y_m\) and \(z_m\) be the corresponding binary strings repeated \(m\) times on the labelled ring of length \(10m\). They constitute a primitive two-cycle under \(F_{3,10m}\). For each of its two configurations,
\[
\# F_{3,10m}^{-1}(y_m)=\# F_{3,10m}^{-1}(z_m)=2^m.
\]
Exactly one preimage of each is periodic, and the other \(2^m-1\) are transient states that first enter that two-cycle after one update. The union of both one-step entrance shells therefore has \(2(2^m-1)\) distinct configurations. In particular the ten-cell example is a direct counterexample to the universal no-incoming-transients assertion of Tosic and Agha (2004, Lemma 5); its assertion is not merely unresolved.

## Assumptions and scope
All binary configurations are spatially labelled: rotations and complementation are not quotiented out. The ring neighborhoods are genuinely \(2r+1\) distinct sites because \(n\ge2r+1\). Periodic means temporally periodic from the initial update (not eventually periodic). The phrase *enter after one update* excludes those already periodic at time zero. The result neither counts the full basins of the specified cycle nor claims that all radius-three primitive cycles exhibit incoming transients.

## Proof
**1. Cycles at radii one and two.** Nakar and Ron (2022, Section 1.4, page 6) give a complete classification of temporally periodic binary words for these two radii. The only primitive two-cycle words, up to shifts and binary complement, are repetitions of \(01\) for radius one, and repetitions of \(0011\), \(001101\) and \(001011\) for radius two. The other listed radius-two word, \(01\), is fixed. We use their classification only as an already established premise; a separate finite-state proof below computes preimage cardinalities.

For a fixed target of spatial period \(d\), write its bits \(b_0,\ldots,b_{d-1}\). Construct a finite directed graph whose states are \((k,s)\), where \(k\in\mathbb Z/d\mathbb Z\) is an output phase and \(s\in\{0,1\}^{2r}\) is an input window. From \((k,s_0\cdots s_{2r-1})\) to \((k+1,s_1\cdots s_{2r-1}a)\), draw an edge if the majority of those \(2r+1\) input bits equals \(b_{k+r}\). Each labelled input word of length divisible by \(d\) mapping to the repeated target is exactly a closed walk in this graph that starts in phase zero. This is a bijection because consecutive windows overlap in exactly \(2r-1\) cells.

Exhaustive generation of the at most \(d2^{2r+1}\) possible transitions gives exactly one cyclic strongly connected component for each target at \(r=1,2\). Each is one directed simple cycle of length \(d\), with no other directed cycles in the graph. Specifically, the recurrent vertex/edge sizes are \((2,2)\) for \(01\) at radius one and \((4,4),(6,6),(6,6)\) for the three radius-two target types. Thus every such repeated target has exactly one preimage, its temporal companion. Shifts and binary complementation commute with majority update, so the conclusion holds for every primitive cycle configuration. If a longer transient trajectory entered one of these cycles, its final step would contradict this unique-predecessor statement. That proves isolation at both radii for every admissible ring length.

**2. Radius-three witness and lower bound.** A direct seven-bit majority calculation on the three ten-bit strings
\[
Y=0011001110,\quad Z=1000111001,\quad P=1001011001
\]
gives \(F(Y)=Z\), \(F(Z)=Y\), and \(F(P)=Y\). Since \(P\ne Z\), the string \(P\) is a nonperiodic predecessor of the two-cycle. These identities remain valid when a complete ten-cell pattern is repeated. Indeed each local update depends only on seven successive symbols, which already occur in the period-ten extension.

Moreover every independent concatenation of \(m\) blocks selected from \(Z\) and \(P\) maps in one update to \(Y^m\); this is checked locally across all four possible neighboring pairs of blocks and yields \(2^m\) distinct preimages.

**3. Matching upper bound.** For the target \(Y\) and radius three, the phase-window graph has exactly one cyclic strongly connected component, with 17 vertices and 18 internal directed edges. Its only phase-zero vertices are \((0,41)\) and \((0,49)\), where the six-bit window is encoded least-significant-bit first. The exact ten-step return-path multiplicity matrix between these two states is
\[
M=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Every closed input walk lies in that component. The number of phase-zero closed walks of length \(10m\) is therefore \(\operatorname{tr}(M^m)=2^m\). This matches the constructed lower bound and rules out all additional predecessors, regardless of their spatial period. The cyclic-component and return-matrix assertions are verified by the standalone exhaustive finite-graph checker, which constructs each possible local transition, computes all strongly connected components, and performs exact integer path counting. The code and its recorded output accompany the theorem.

Finally, the target \(Z\) is the bitwise complement of \(Y\) rotated through five sites. Both operations commute with the majority rule, so its preimage count is identical. The only periodic predecessor of a primitive two-cycle state is its temporal companion. The exact numbers of transient one-step predecessors and the sharp radius threshold follow.

## Verification
Run `python3 VERIFY.py` using Python 3.8 or later; no external packages are needed. The checker exhausts the phase-window graphs for the four radius-one/two primitive target types, establishes their sole simple-cycle strongly connected components and one-by-one return matrices, then obtains the 17-vertex, 18-edge radius-three recurrent graph and its exact two-by-two ten-step matrix. It independently evaluates the three displayed ten-cell update identities, all \(2^m\) explicit block mosaics for \(1\le m\le5\), and direct microscopic predecessor counts for rings of size 3–12 at radius one, 5–12 at radius two, and 7–10 at radius three. The last line of the recorded successful replay is `RADIUS_THRESHOLD_CERTIFICATE_OK`.

The direct finite-size enumerations are corroboration, not a substitute for the all-size finite-state transfer argument.

## Relationship to prior work
The period-at-most-two result of Goles–Olivos and the complete small-radius catalogue of periodic configurations in Nakar–Ron (2022, especially Section 1.4) are prior work, not new results here. Liu–Chen (original arXiv posting 2002, revised 2003), Section 4, analyze the symbolic attractor patterns for the radius-two infinite majority cellular automaton. Their radius-two attractor analysis is consistent with the unique-incoming-predecessor statement and motivates seeking the first genuinely attracting oscillations.

Tosic–Agha (2004), Lemma 5 on page 8, explicitly states that any finite or infinite threshold cellular automaton either lacks proper cycles or has no transient states entering cycles. The ten-cell radius-three witness disproves that assertion in the parallel majority setting, which falls under the stated scope. Their paper does not give the radius-three ten-bit precursor or an exact exponential preimage law. The principal scientific contribution here is therefore the sharp threshold and explicit infinite preimage multiplicity, not the already published catalog of two-cycle words.

## Limitations
The predecessor count concerns a particular natural period-ten oscillator at radius three, not every oscillator or every transient-depth shell. The proof of the lower-radius exclusion uses the published complete periodic-word classification; it is not asserted to rederive that classification. Strongly connected components are finite mathematical certificates verified by a reproducible enumerator; independent mathematical auditing has not been performed. Historical unindexed calculations of radius-three predecessors may exist, although targeted statement/implication searches found none.

## References
1. P. T. Tosic and G. A. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004, LNCS 3305, 861–870. DOI: 10.1007/978-3-540-30479-1_89. Author-hosted full text: https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf . See Lemma 5, page 8.
2. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972 (first posted 2022-05-18), Section 1.4. https://arxiv.org/pdf/2205.08972 .
3. R.-F. Liu and C.-C. Chen, *Analytic Proof of the Attractors of a Class of Cellular Automaton*, arXiv:nlin/0209005 (first posted 2002-09-02), Section 4. https://arxiv.org/pdf/nlin/0209005 .
4. J. A. Aledo, S. Martínez, and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015). DOI: 10.1155/2015/594294.
