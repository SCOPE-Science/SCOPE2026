# Icosahedral excitation: exact three-cycle, geometric-orbit, and six-step entrance census

## Finding
Consider the synchronous three-state Greenberg–Hastings automaton on the ordinary twelve-vertex icosahedral graph, with all twelve vertices labelled as in `graph.json`. Every state becomes periodic within six updates, and the global map satisfies
\[
F^9=F^6.
\]
There is exactly one fixed state (all vertices resting), exactly \(48{,}400\) primitive three-cycle temporal orbits, and no other primitive period. The \(48{,}400\) three-cycles form exactly \(473\) classes under the full \(120\)-element graph automorphism group, including temporal phase shifts. Their spatial orbit-size distribution, measured in temporal orbits per geometric class, is
\[
\begin{array}{c|rrrrrr}
\text{size}&5&20&30&40&60&120\\\hline
\text{classes}&2&4&11&10&99&347.
\end{array}
\]
Exactly \(60\) initial configurations have first periodic entry at time six, and these form a single orbit under spatial automorphisms. The maximal first-entry time is therefore precisely six.

The all-rest state attracts exactly \(18{,}231\) initial configurations; the other \(513{,}210\) enter a three-cycle. The exact counts by first periodic entrance time \(t=0,1,\ldots,6\), separated by eventual period, are
\[
\begin{array}{c|rrrrrrr}
 t&0&1&2&3&4&5&6\\\hline
 \text{period 1}&1&4095&6065&5618&1672&780&0\\
 \text{period 3}&145200&55120&107530&128620&63600&13080&60.
\end{array}
\]
The complete multiset of individual three-cycle basin sizes appears in `direct_output.txt` and is reproduced by `verify_direct.cpp`.

## Assumptions and scope
The graph has vertex set \(V=\{0,1,\ldots,11\}\) and the thirty undirected edges listed explicitly in `graph.json`. Every vertex has five neighbors; this is the standard icosahedral graph. A configuration is a function \(x:V\to\{0,1,2\}\), where \(0\) means resting, \(1\) excited and \(2\) refractory. For every \(v\in V\), the simultaneous update is
\[
(Fx)_v=\begin{cases}
1,&x_v=0\text{ and some }u\sim v\text{ has }x_u=1,\\
0,&x_v=0\text{ and no such }u\text{ exists},\\
2,&x_v=1,\\
0,&x_v=2.
\end{cases}
\]
The first periodic entry time of \(x\) is the least \(t\ge0\) for which \(F^t(x)\) belongs to a periodic orbit. A temporal orbit counts once regardless of its starting phase. A geometric class identifies temporal orbits under graph automorphisms, not under arbitrary recoloring. Basin size means the number of *labelled* initial states entering a particular temporal orbit.

## Proof
**Structure of three-cycles.** On any connected graph under this update, a state on a primitive three-cycle must have every vertex rotating by \(0\mapsto1\mapsto2\mapsto0\). To see this, a vertex that ever takes value \(1\) must take the following values \(2,0\); three-periodicity forces the next value to be \(1\). A vertex that never takes value \(1\) must be constantly \(0\), and a neighbor of a rotating vertex cannot be constantly resting. Connectivity propagates rotation to all vertices. Consequently a configuration \(x\) is on a primitive three-cycle if and only if, for every vertex \(v\), at least one neighbor has value \(x_v+1\pmod3\). This is the **successor-neighbor phase condition**. It forces all three phases to appear, hence excludes fixed states. Conversely that condition makes \(F(x)=x+1\pmod3\) at all vertices, yielding a primitive three-cycle.

**Finite exhaustive certificate.** Encode \(x\) by
\[
\operatorname{code}(x)=\sum_{v=0}^{11}x_v3^v\in\{0,1,\ldots,531440\}.
\]
The independently implemented `verify_direct.cpp` enumerates precisely this complete interval, reconstructs all twelve digits by repeated division by three, applies the explicit neighbor masks and verifies the integer identity \(F^9(x)=F^6(x)\) separately for every state. This proves \(F^9=F^6\), so every orbit has entered a cycle by time six and every recurrent period divides three. The only fixed point is the all-rest state: every nonzero excited or refractory vertex must change on its next update, and an all-rest configuration is fixed.

The same exhaustive algorithm counts \(145{,}200\) configurations periodic with primitive period three. This count is independently certified by `verify_phase.cpp`, which tests the successor-neighbor phase condition for each of the \(3^{12}=531{,}441\) colorings without iterating the dynamical map. Division by three gives \(48{,}400\) temporal three-cycles. The functional-graph algorithm in `enumerate.cpp` also obtains this count by an independent indegree-peeling and cycle-decomposition method.

**Entrance times and basins.** For each encoded state, `verify_direct.cpp` forms the exact ten-term list \(x,Fx,\ldots,F^9x\). Its first periodic entry time is the least \(0\le t\le6\) with \(F^{t+3}x=F^t x\). At this time the eventual primitive period is one if \(F^{t+1}x=F^t x\), otherwise three. The algorithm tabulates all \(531{,}441\) states, producing the displayed table. The state with code \(3156\), represented in vertex order \(0,1,\ldots,11\) by \((0,2,2,2,2,0,1,1,0,0,0,0)\), first enters a three-cycle at exactly time six; the complete orbit is reproduced in the verification instructions. Thus six is sharp. Grouping the eventual periodic code \(\min(F^6x,F^7x,F^8x)\) yields exact individual basin sizes.

**Full symmetry quotient.** The two explicit permutations in `aut_generators.txt` preserve every edge, and their composition closure contains exactly \(120\) permutations, checked independently in `verify_symmetry.py`. There are no additional graph automorphisms: each automorphism sends a chosen vertex to one of twelve positions, then induces one of at most ten symmetries of its induced five-neighbor cycle. The five distance-two vertices are uniquely determined by pairs of neighbors on that cycle, and the unique distance-three antipode is then fixed. Hence \(|\operatorname{Aut}(G)|\le120\), so equality holds. Applying the two generating permutations together with temporal phase normalization partitions the \(48{,}400\) temporal cycles into precisely \(473\) classes with the claimed sizes; `symmetry_classes.csv` gives one representative and the orbit size for each class. The \(60\) states at first entry time six are exactly one spatial orbit, also checked by this program.

These are finite exact statements, not extrapolations from a sample. Exhaustiveness follows from one-to-one base-three encoding of all twelve-digit configurations, the tested identity on every code, and the verified full automorphism group.

## Verification
The package contains `graph.json`, `enumerate.cpp`, `verify_direct.cpp`, `verify_phase.cpp`, `verify_symmetry.py`, `aut_generators.txt`, `stats.txt`, `direct_output.txt`, `phase_output.txt`, `symmetry_output.txt`, and `symmetry_classes.csv`. From the directory containing these files, compile the three C++ programs with a conforming C++17 compiler and run them, then run the Python 3 symmetry verifier. The expected count checks are \(531{,}441\) states, \(48{,}400\) primitive three-cycles, \(473\) geometric cycle classes, maximal first-entry time six, and \(60\) extremal states. Exact reproduced output files are supplied; no random testing or floating-point approximation is involved. `VERIFICATION.md` provides commands and checksums. The second dynamical implementation operates on bit masks and tests a direct iterate identity, rather than relying on the functional-graph decomposition of the first implementation.

## Relationship to prior work
Gravner, Lyu and Sivakoff (2016), Theorem 3, give an irrotationality criterion and limiting activity for three-color excitation on arbitrary connected finite graphs. Doba (2018), Theorems 1–2, analyzes persistent excitation by phase differences and maximum cycle density. On a triangulated sphere such as the icosahedron, those qualitative results substantially explain the period-one/period-three dichotomy; **that dichotomy by itself is not asserted to be new**. Neither inspected primary work supplies this labelled icosahedral orbit census, the \(473\)-class full-symmetry quotient, the exact basin distributions or the sharp uniform six-step identity. Previous graph-specific counts on other finite networks do not imply these numbers without additional computation or combinatorics. The phase-coloring interpretation links recurrent excitations to directed three-phase local-domination constraints rather than ordinary proper graph coloring.

## Limitations
This is an exact finite-graph classification, not a theorem for an arbitrary family of polyhedral graphs. The proof of the global six-step bound and the numerical counts is a completely enumerated finite-state certificate whose conclusion depends on replay of the supplied, short standalone programs and their precise labelled graph input. The analytic three-phase characterization alone does not prove the entrance bound. General irrotationality, maximum-cycle-density and three-color model results are prior work. No stochastic excitation, different threshold, asynchronous update, or alternative graph is covered. Equivalent earlier unindexed tabulations cannot be excluded by the literature comparison.

## References
1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first posted 2016-10-24), especially Theorem 3. https://arxiv.org/abs/1610.07320
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126, especially Theorems 1 and 2. https://doi.org/10.25088/ComplexSystems.27.2.101
3. NetworkX documentation, *icosahedral_graph*: twelve vertices and thirty edges, https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.icosahedral_graph.html
4. E. W. Weisstein, *Icosahedral Graph*, MathWorld, https://mathworld.wolfram.com/IcosahedralGraph.html
