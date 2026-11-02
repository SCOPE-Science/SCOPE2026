# Forty chordless-cycle obstructions in minimum total-domination exchanges of the dodecahedral graph

## Finding
Let \(D\) be the dodecahedral graph, equivalently the generalized Petersen graph \(\operatorname{GP}(10,2)\). A **total dominating set** \(S\subseteq V(D)\) has the property that every vertex (including each selected vertex) has a neighbor in \(S\). Let \(\mathcal M\) be the family of all minimum-cardinality total dominating sets, and form the **one-vertex-exchange graph** \(R\): its vertices are the members of \(\mathcal M\), and distinct \(S,T\) are adjacent if \(|S\setminus T|=|T\setminus S|=1\). The exchanged vertices need not be adjacent in \(D\).

The minimum cardinality is \(8\) and \(|\mathcal M|=190\). The graph \(R\) has \(360\) edges and is the disjoint union of one connected \(150\)-vertex component and \(40\) isolated vertices. The connected component has radius and diameter \(10\); indeed every one of its vertices has eccentricity \(10\). The degree distribution of \(R\) is \(40\) vertices of degree \(0\), \(120\) of degree \(4\), and \(30\) of degree \(8\).

**Geometric characterization of the frozen configurations.** A member \(S\in\mathcal M\) is isolated in \(R\) if and only if the complementary induced graph \(D[V(D)\setminus S]\) is a chordless cycle on twelve vertices. There are precisely forty such induced twelve-cycles. Of the corresponding isolated sets, thirty induce two disjoint four-vertex paths and ten induce two disjoint three-leaf stars. The full automorphism group of \(D\), of order \(120\), partitions \(\mathcal M\) into five orbits: isolated orbits of sizes \(10,30\), a core orbit of size \(30\), and two core orbits each of size \(60\).

## Assumptions and scope
The labelled graph \(\operatorname{GP}(10,2)\) has vertices \(u_i,v_i\) with \(i\in\mathbb Z/10\mathbb Z\) and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). Thus it has twenty vertices, thirty edges, and degree three at every vertex. For a set \(S\), the total-domination test is \(N(x)\cap S\ne\varnothing\) for every vertex \(x\), where \(N(x)\) is the **open** neighborhood. All subsets and all exchange edges refer to the labelled graph; no quotient by symmetry is taken in the counts. A chordless twelve-cycle means a twelve-vertex induced subgraph that is connected and has every degree equal to two. The claim is only for this finite graph, not all generalized Petersen graphs or all fullerene graphs.

## Proof
The theorem has a finite, exhaustive certificate. Two complete and differently represented algorithms are supplied as standalone executable Python files.

**Minimum cardinality.** Since \(D\) is cubic, \(|N(S)|\le3|S|\). Every total dominating set therefore has at least seven vertices. The first checker examines each of the \(\binom{20}{7}=77{,}520\) seven-element subsets and verifies that none totally dominates. It next examines all \(\binom{20}{8}=125{,}970\) eight-element subsets and finds exactly \(190\) that meet every open-neighborhood constraint. These two complete ranges prove both minimality and the stated configuration count.

**Exact exchange graph.** For each of those \(190\) sets \(S\), every ordered choice of one selected vertex \(x\in S\) and one unselected vertex \(y\notin S\) is examined. The candidate \((S\setminus\{x\})\cup\{y\}\) is joined to \(S\) exactly when it is among the certified \(190\) sets. This is an exhaustive definition of every legal exchange: it does not rely on guessing a pattern of edges. The resulting degrees and edges are counted, and a breadth-first search from every vertex computes all components and eccentricities. These exact checks give the asserted \(360\) edges, component sizes, degree distribution, and common eccentricity \(10\) in the nontrivial component.

**Cycle-complement equivalence.** Every twelve-vertex subset \(C\subseteq V(D)\) is independently examined. A set qualifies precisely when the induced graph \(D[C]\) is connected and every member of \(C\) has two neighbors in \(C\). Exactly \(40\) sets qualify. Checking the complements against the full exchange-degree table establishes the exact set equality
\[
\{S\in\mathcal M:\deg_R(S)=0\}
=\{V(D)\setminus C: D[C]\text{ is an induced twelve-cycle}\}.
\]
Checking the induced selected subgraphs of these forty complements yields thirty copies of \(2P_4\) and ten copies of \(2K_{1,3}\), interpreted as isomorphism types.

**Symmetry.** A graph-isomorphism backtracking enumeration finds all \(120\) automorphisms of the base graph. Each is applied to each selected set, yielding five orbits with the indicated sizes; their degrees are constant, as required by automorphism invariance.

**Independent reconstruction of the finite data.** The second checker builds the graph directly from the three generalized-Petersen edge rules above, using twenty integer bit positions rather than a library graph object. It independently enumerates the exact seven- and eight-element subsets, builds all exchanges by bit operations, performs breadth-first searches, and counts and checks all induced twelve-cycles. Both implementations give the same finite statements. As the domain is finite and every eligible subset, replacement, and graph distance is covered, this is a complete exhaustive computational proof rather than inference from a sample.

## Verification
Execute `python verify_dodeca_total_direct.py` with Python 3.10 or later and NetworkX 3.x. Execute `python verify_dodeca_total_gp.py` with Python 3.10 or later and no third-party packages. The first prints `DODECAHEDRON_DIRECT_TOTAL_DOMINATION_PASS`; the second prints `DODECAHEDRON_GP_BITSET_PASS`. Both exit with an assertion error if any critical invariant differs. The programs include the graph definitions and enumeration logic; no downloaded datasets, hidden certificates, or unsupplied scripts are required. Exact counts and computations are reproducible by rerunning the included files.

## Relationship to prior work
Cockayne, Dawes, and Hedetniemi introduced total domination in 1980. Henning's 2000 paper develops bounds for graphs with large total domination number. Cao, Lin, and Shi (2009) determine the total domination number of generalized Petersen graphs \(\operatorname{GP}(n,2)\); in particular, the minimum cardinality \(8\) in \(\operatorname{GP}(10,2)\) is not new. Zhao and collaborators (2020) study other numerical total-domination invariants of generalized Petersen graphs. Alikhani, Fatehi, and Mynhardt (2017) investigate **addition/deletion** reconfiguration for total dominating sets of size at most a threshold, which is not the fixed-minimum-cardinality **one-for-one exchange** operation used here.

The asserted new part is the complete exchange-graph decomposition, its uniform eccentricity, and the characterization of isolated optima by induced twelve-cycles. Neither an extremal cardinality nor a list of all optimal vertex subsets by itself supplies these exchange invariants. The prior-work comparison is a qualified priority assessment, not a proof of global novelty.

## Limitations
This is an exact single-graph theorem; no analogous claim is made for other cubic polyhedra or generalized Petersen parameters. Complete computations supply a finite certificate, not a general structural theorem for infinite families. An older or unindexed catalogue of dodecahedral minimum total dominating sets, induced cycles, or equivalent reconfiguration configurations might already encode part of the result; the possibility remains a priority risk. No independent human validation has been performed.

## References
- E. J. Cockayne, R. M. Dawes and S. T. Hedetniemi, *Total domination in graphs*, Networks 10 (1980), 211–219. DOI: `10.1002/net.3230100304`. The source specifies the season of publication but not a verified calendar day.
- M. A. Henning, *Graphs with large total domination number*, Journal of Graph Theory 35 (2000), 21–45. First published 2000-08-09. DOI: `10.1002/1097-0118(200009)35:1<21::AID-JGT3>3.0.CO;2-F`.
- J. Cao, W. Lin and M. Shi, *Total Domination Number of Generalized Petersen Graphs*, Intelligent Information Management 1 (2009), 14–17. Published online July 2009. DOI: `10.4236/iim.2009.11003`.
- S. Alikhani, D. Fatehi and C. M. Mynhardt, *On k-Total Dominating Graphs*, 2017, `arXiv:1711.04363v1`.
- T. Zhao et al., *The Numerical Invariants concerning the Total Domination for Generalized Petersen Graphs*, Journal of Mathematics (2020), article 5473675. DOI: `10.1155/2020/5473675`.
