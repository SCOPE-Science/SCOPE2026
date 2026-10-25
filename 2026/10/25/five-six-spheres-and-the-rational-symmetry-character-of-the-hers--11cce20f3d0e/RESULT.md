# Five six-spheres and the rational symmetry character of the Herschel spanning-path containment complex

## Finding
Let \(H\) be the eleven-vertex Herschel graph specified in the next section. Let \(K(H)\) be the abstract simplicial complex on the graph's eighteen edges whose faces are precisely the edge sets contained in at least one Hamiltonian path. There is an integral homotopy equivalence
\[
K(H)\simeq \bigvee^{5} S^{6}.
\]
The full graph automorphism group is \(\operatorname{Aut}(H)\cong S_3\times C_2\). Its representation on the sole nonzero reduced rational homology group is
\[
\widetilde H_6(K(H);\mathbb Q)
\cong (\operatorname{sgn}\oplus\operatorname{Std})\boxtimes\mathbf1
\;\oplus\; \operatorname{Std}\boxtimes\varepsilon,
\]
where \(\operatorname{sgn}\) and \(\operatorname{Std}\) are the sign and two-dimensional standard \(S_3\)-representations, and \(\varepsilon\) is the nontrivial \(C_2\)-character. In particular, its subspace fixed by all graph automorphisms is zero.

## Assumptions and scope
Use graph vertices \(0,1,\ldots,10\). For each \(j\in\{0,\ldots,5\}\), join \(5+j\) to the two members of \(\{0,1,2\}\setminus\{j\bmod3\}\) and to \(3+(j\bmod2)\). These are exactly eighteen distinct edges, all between \(\{0,1,2,3,4\}\) and \(\{5,6,7,8,9,10\}\). This model has three degree-four vertices, eight degree-three vertices, is planar and three-connected, and has the characteristic spectrum and twelve symmetries of the classical Herschel graph.

Index the graph edges lexicographically from \(0\) to \(17\), and encode a subset by the sum of its corresponding powers of two. Hamiltonian path means an *undirected* simple path traversing each graph vertex exactly once. A face is allowed to be a disconnected subgraph: it must merely be a subset of the edge set of some spanning path. The empty set is included combinatorially; the simplicial realization contains the nonempty faces. All homotopy and homology statements use ordinary finite simplicial realizations. The homology statement holds integrally; the representation statement is over \(\mathbb Q\).

## Proof
**Exhaustive facets.** A depth-first enumeration of all ordered simple paths visiting eleven vertices, from every possible first vertex, finds \(444\) oriented Hamiltonian paths, hence \(222\) distinct undirected ten-edge Hamiltonian paths. A separate Held–Karp subset recurrence reproduces the oriented count. Every Hamiltonian path is visited, since the recursion branches over every unused neighbor of the current endpoint. The \(222\) edge sets are exactly the facets of \(K(H)\), because they all have cardinality ten. Generating all their subsets gives \(37,454\) nonempty faces, with numbers in cardinalities one through ten:
\[
(18,153,796,2742,6402,9913,9738,5694,1776,222).
\]
The unreduced Euler characteristic is \(6\).

**A complete acyclic matching.** Process the eighteen lexicographically indexed graph-edge vertices in this order:

`6,12,16,13,9,11,5,0,2,4,14,3,15,1,10,8,17,7`.

Initially declare all nonempty simplices unpaired. At each vertex index \(v\), pair every remaining face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), when both remain; remove both faces from subsequent consideration. Each pair differs by a single vertex, so these are codimension-one face–coface pairs. The algorithm yields exactly \(18,724\) pairs and six unmatched simplices: one vertex and five six-dimensional simplices. To **verify global acyclicity**, direct each codimension-one incidence from its higher to its lower face, except direct matched incidences upward. Topologically sorting this *entire* directed Hasse graph succeeds on all \(37,454\) vertices and all \(237,072\) incidences. Consequently, the matching is an acyclic discrete-Morse matching. The finite discrete-Morse theorem gives a CW complex homotopy equivalent to \(K(H)\) with exactly one zero-cell and five six-cells, and no cells in other dimensions. Every six-cell attaching map then has the one-point four/five-skeleton as target and is nullhomotopic, giving the asserted wedge. This is an integral homotopy statement, not an inference from numerical Betti numbers.

**The group action and its trace.** Distinct degree-four vertices are exactly \(0,1,2\). Vertices \(3,4\) are intrinsically distinguished among degree-three vertices because all their neighbors have degree three, whereas each right-side vertex has two degree-four neighbors. An automorphism therefore permutes \(0,1,2\) and independently may swap \(3,4\). Once those images are chosen, each other vertex is determined by its missing degree-four neighbor and its unique neighbor among \(3,4\). Every one of the \(3!\cdot2=12\) possibilities preserves adjacency. Thus the full automorphism group is \(S_3\times C_2\).

For each of the twelve automorphisms, act on the indexed eighteen graph edges. A face contributes to the oriented simplicial chain trace precisely if its edge set is preserved; its contribution is the sign of the induced permutation of its ordered vertices. The alternating sum of these traces is the ordinary Lefschetz number. Since the only nonzero ordinary homology is one copy of \(\mathbb Q\) in degree zero and five copies in degree six, subtracting one from this alternating face trace yields the degree-six homology character. Grouping by conjugacy classes indexed by (type of \(S_3\) permutation, nontrivial \(C_2\)-flip or not), the resulting values are
\[
\begin{array}{c|rrrrrr}
\text{class} &(1,0)&((12),0)&((123),0)&(1,1)&((12),1)&((123),1)\\\hline
\chi_6 &5&-1&-1&1&-1&1 .
\end{array}
\]
The displayed representation has exactly this character: if \(s(g)\) denotes the sign character of \(S_3\), \(t(g)\) its two-dimensional standard character, and \(\epsilon(c)\in\{1,-1\}\), then \(\chi_6(g,c)=s(g)+t(g)(1+\epsilon(c))\). Since rational finite-group representations are semisimple and characters determine their isomorphism classes, this proves the decomposition. Averaging the twelve character values gives zero, hence there are no invariant rational classes.

## Verification
The self-contained Python 3 script `verify.py` uses only the standard library. Execute from the extracted directory with `python3 verify.py`. It derives the graph directly from the displayed incidence rule, enumerates spanning paths in two distinct ways, regenerates every face, constructs the toggle matching, and topologically sorts the full reversed Hasse graph. It also computes signed fixed-simplex traces for all twelve graph automorphisms and checks the entire character table and decomposition. The script terminates with `VERIFY_OK` only if all assertions pass. The expected certificate summary is \(222\) undirected paths, \(37,454\) nonempty faces, \(18,724\) matched pairs, one critical zero-cell, five critical six-cells, and \(237,072\) Hasse incidences. The verifier was also rerun with different Python hash seeds, giving identical output.

## Relationship to prior work
The Herschel graph is a classical smallest non-Hamiltonian polyhedral graph, described for example in H. S. M. Coxeter's *Regular Polytopes* (1948) and in C. Lawson-Perfect's graph-and-symmetry discussion (2013). The available dated public graph depiction by David Eppstein was uploaded on 13 October 2009; that verified public-access date is used for the source's cohort assignment, **not** asserted as the original discovery date of the graph. The path complex here uses *Hamiltonian spanning paths*, which exist despite non-Hamiltonicity.

J. Jonsson's 2003 non-Hamiltonian-graph complex \(\Gamma_n\) considers all non-Hamiltonian graphs on a fixed complete \(n\)-vertex ground set. It has a different face condition: all edge subsets of the Herschel graph belong to \(\Gamma_{11}\), but only certain subsets belong to the present spanning-path complex. General results about \(\Gamma_n\) therefore do not give the claimed homotopy type. Likewise, the ordinary independence complex of the Herschel graph uses *graph vertices* as simplicial vertices, whereas the present complex uses *graph edges*. The previously determined Petersen Hamiltonian-path containment complex has a different underlying graph and does not imply this exact class or its \(S_3\times C_2\)-character. General discrete-Morse theory supplies the proof method, not these enumerated invariants.

## Limitations
This is an exact computation for one specified finite graph and its automorphism action, not a theorem about all planar or all non-Hamiltonian graphs. The character statement is rational, although the homotopy classification is integral. The entire computation can be rerun using the included checker; it has not received an independent mathematical audit. The author's freely indexed version of Jonsson's related 2003 paper was not retrievable in full during literature inspection, and its book-length survey was available only in preview; an unindexed equivalent result remains possible. This does not establish publication priority. No unsupported claims about the graph's earliest historical discovery are made.

## References
1. H. S. M. Coxeter, *Regular Polytopes*, Methuen, 1948, p. 8 (classical non-Hamiltonian polyhedral graph, bibliographic attribution).
2. David Eppstein, *Herschel graph.svg*, publicly uploaded 13 October 2009, https://commons.wikimedia.org/wiki/File:Herschel_graph.svg (dated accessible graph model).
3. Christian Lawson-Perfect, *An enneahedron for Herschel*, The Aperiodical, posted 1 October 2013, https://aperiodical.com/2013/10/an-enneahedron-for-herschel/ (graph construction and symmetry; its informal assertion about absence of a spanning path is not used).
4. Jakob Jonsson, *On the topology of simplicial complexes related to 3-connected and Hamiltonian graphs*, Journal of Combinatorial Theory A 104 (2003), 169–199, https://doi.org/10.1016/j.jcta.2003.07.001 (different non-Hamiltonian graph-property complex).
5. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete-Morse theorem).
