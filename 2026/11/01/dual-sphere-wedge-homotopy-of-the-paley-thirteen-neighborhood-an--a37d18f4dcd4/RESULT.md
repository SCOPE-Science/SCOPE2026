# Dual sphere-wedge homotopy of the Paley-thirteen neighborhood and dominance complexes

## Finding

Let \(P_{13}\) be the quadratic-residue Paley graph on thirteen vertices, and let \(\mathcal N(P_{13})\) and \(\mathcal D(P_{13})\) denote its Lovász open-neighborhood complex and dominance complex, respectively. Their **complete integral homotopy types** are

\[
\mathcal N(P_{13})\simeq\bigvee^{25}S^2,
\qquad
\mathcal D(P_{13})\simeq\bigvee^{25}S^8.
\]

Both statements are established by complete, acyclic discrete-Morse matchings on the defining simplicial complexes. These are homotopy equivalences over the integers, not merely conclusions about homology over a field. The pair of calculations constitutes one classification for the two canonically Alexander-dual graph complexes.

## Assumptions and scope

Write \(V=\mathbb F_{13}=\{0,1,\dots,12\}\), let \(Q=\{1,3,4,9,10,12\}\) be its six nonzero squares, and join distinct \(x,y\in V\) precisely when \(y-x\in Q\). Then \(P_{13}\) is the simple, six-regular, self-complementary Paley graph with strongly regular parameters \((13,6,2,3)\).

For each vertex \(v\), let \(N(v)=\{w:w\sim v\}\) and \(N[v]=N(v)\cup\{v\}\). A nonempty \(\sigma\subseteq V\) belongs to the Lovász neighborhood complex \(\mathcal N(P_{13})\) exactly when \(\sigma\subseteq N(v)\) for some \(v\). It belongs to the dominance complex \(\mathcal D(P_{13})\) exactly when \(V\setminus\sigma\) dominates the graph, equivalently when \(N[v]\not\subseteq\sigma\) for **every** \(v\). The empty face is present in both; face counts reported below exclude it.

Only this thirteen-vertex quadratic-residue graph and these two unfiltered complexes are considered. No all-Paley-graph theorem, claim about other coefficient systems, or graph-family recurrence is asserted.

## Proof

**Graph identification and duality.** Direct enumeration of the six residues verifies that each vertex has degree six, each adjacent pair has two common neighbors, and each nonadjacent pair has three. Multiplication by two, a quadratic nonresidue, sends the graph isomorphically onto its complement. The defining conditions imply the combinatorial Alexander-dual identity

\[
\mathcal D(P_{13})^{\vee}=\mathcal N(\overline{P_{13}}),
\]

in accordance with the general duality theorem of Matsushita and Wakatsuki. Thus the two complexes belong to one dual pair, although the homotopy equivalences below are proved directly and independently.

**Exact face sets.** All \(2^{13}=8192\) subsets are tested against the preceding definitions. The neighborhood complex has \(598\) nonempty simplices, with face vector, by dimensions zero through five,

\[
(13,78,221,195,78,13).
\]

The dominance complex has \(7592\) nonempty simplices, with face vector, by dimensions zero through nine,

\[
(13,78,286,715,1287,1716,1703,1209,520,65).
\]

The exhaustive checker also verifies the stated Alexander-dual relation for every subset, including the empty and full subsets. Both face vectors have Euler characteristic \(26\).

**Acyclic matching construction.** Starting with all nonempty simplices unmatched, process vertices \(v=0,1,\dots,12\) in order. At phase \(v\), traverse remaining face masks in increasing integer order. Whenever a face \(\sigma\) omits \(v\) and both \(\sigma\) and \(\sigma\cup\{v\}\) are still unmatched, pair them and remove both. This specifies a reproducible matching without external certificates or heuristic choices.

For the neighborhood complex, the numbers of pairs at successive phases are

\[
(159,69,21,15,15,3,2,1,1,0,0,0,0).
\]

There are \(286\) pairs, leaving exactly one critical vertex and \(25\) critical two-simplices. For the dominance complex the phase pair counts are

\[
(3656,53,46,16,4,2,2,1,1,1,1,0,0),
\]

giving \(3783\) pairs, one critical vertex, and \(25\) critical eight-simplices.

To certify acyclicity rather than infer it from a face count, the checker constructs the **complete directed Hasse diagram** for each complex. All unmatched codimension-one incidences point downward; all matched incidences are reversed upward. A topological-sort traversal consumes every vertex of each directed graph: respectively \(598\) and \(7592\) vertices, with \(2067\) and \(47528\) codimension-one incidences. Consequently, neither matching has a directed cycle.

The discrete-Morse CW theorem therefore yields, respectively, one zero-cell together with \(25\) cells only in dimension two and one zero-cell together with \(25\) cells only in dimension eight. Since every positive-dimensional cell attaches to the sole zero-cell and no other positive-dimensional cells exist, their CW complexes are precisely the claimed wedges of spheres. This proves the integral homotopy equivalences.

## Verification

The standalone Python 3 standard-library checker `verify_paley13_dual.py` regenerates the graph, tests the \(8192\) subsets, confirms complement isomorphism and Alexander duality, constructs both complete matchings, verifies every directed Hasse edge and topological sorting, and independently computes all mod-two simplicial boundary ranks. It obtains only reduced mod-two Betti number \(25\) in dimension two for the neighborhood complex and \(25\) in dimension eight for the dominance complex; their integral sphere-wedge structure follows from the acyclic matchings, not from these field computations. The recorded successful execution is in `verification_output.txt`.

Running `python3 verify_paley13_dual.py` from a directory containing that file reproduces the entire finite verification. The script uses no remote access, random seeds, optional libraries, or input files.

## Relationship to prior work

Matsushita and Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals* (first arXiv version December 5, 2023), prove the general Alexander-duality equivalence, give methods for dominance homology, and calculate other families. Their duality is used here as known structure, **not** claimed as a new result; their inspected cases and the searched text do not calculate the present graph. Shukla's *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs* (first arXiv version February 13, 2018) classifies degree-at-most-three and four-regular cases. The six-regular Paley graph here lies outside those hypotheses.

Relevant independent exact graph-topology records concern the ordinary clique complex of \(P_{13}\), the neighborhood complex of \(P_{17}\), and the neighborhood complex of \(P_{25}\). Their objects or parameters differ; none of their inspected statements asserts a formula covering the present open-neighborhood or dominance complex. Another known family concerns the third power of a cycle. That graph at thirteen vertices has \(39\) triangles, whereas \(P_{13}\) has \(26\), so they are not isomorphic. The present statement is an exact one-graph computation, not an assertion of uniqueness among all published works.

## Limitations

The proof is exhaustive but finite: it applies to this graph only. The homotopy equivalences provide no calculation for the higher Paley orders. Neither the direct matchings nor the absence of matching search hits establishes universal bibliographic novelty; potentially unindexed or inaccessible equivalent computations remain a residual risk. No independent external audit or validation has been performed.

## References

1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, initially public December 5, 2023. https://arxiv.org/abs/2312.02639
2. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, initially public February 13, 2018. https://arxiv.org/abs/1802.04526
3. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923. DOI:10.1016/j.ejc.2005.04.010. Background definitions and forest results only.
