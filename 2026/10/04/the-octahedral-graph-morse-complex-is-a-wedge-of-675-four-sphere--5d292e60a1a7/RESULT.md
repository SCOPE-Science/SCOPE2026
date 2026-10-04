# The octahedral graph Morse complex is a wedge of \(675\) four-spheres

## Finding
Let \(O\) be the octahedral graph on vertex set \(\{0,1,2,3,4,5\}\), with all edges present except \(01\), \(23\), and \(45\). Thus \(O=K_{2,2,2}\), equivalently \(K_6\) with a perfect matching removed.

For a graph, a primitive gradient vector field is a pair \((v,vw)\) consisting of a vertex and an incident edge. The ordinary Morse complex \(\mathcal M(O)\) has these primitive fields as vertices and has one simplex for every gradient discrete vector field. Then

\[
\mathcal M(O)\simeq \bigvee^{675} S^4.
\]

The complete nonempty face vector of \(\mathcal M(O)\), from dimensions \(0\) through \(4\), is

\[
(24,228,1072,2496,2304).
\]

## Assumptions and scope
The graph is regarded as a one-dimensional finite simplicial complex, and \(\mathcal M(O)\) means the ordinary Morse complex of gradient vector fields, not the generalized Morse complex. A discrete vector field uses each cell in at most one regular pair and is gradient precisely when it has no nontrivial closed \(V\)-path.

The claim is a finite exact homotopy computation for this single graph. No formula is asserted for all complete multipartite graphs, all cocktail-party graphs, or all Platonic graphs.

## Proof
There are \(12\) graph edges and therefore \(24\) primitive gradient fields \((v,vw)\), one for each incidence of a vertex with an edge.

For a graph, a collection of primitive fields can be read as a partial orientation: choosing \((v,vw)\) orients the edge from \(v\) toward \(w\). The discrete-vector-field condition is exactly that each vertex is the tail of at most one chosen edge and each underlying edge is chosen at most once. A \(V\)-path alternates from a chosen tail across its selected edge to the opposite endpoint, so a nontrivial closed \(V\)-path is exactly a directed cycle in this partial orientation. Hence the simplices of \(\mathcal M(O)\) are exactly the partial orientations satisfying those three finite conditions.

The standalone verifier enumerates this set without sampling. Each of the six graph vertices has five choices: no outgoing edge or one of its four neighbors. Thus all \(5^6=15625\) possible tail assignments are visited. Assignments that select the same underlying edge twice or contain a directed cycle are rejected. The surviving simplices give the face vector

\[
(24,228,1072,2496,2304).
\]

Next fix the verifier's deterministic order on the \(24\) primitive fields. Starting from all nonempty faces, for each primitive field \(p\) in order, pair every still-unmatched face \(\sigma\) not containing \(p\) with \(\sigma\cup\{p\}\) whenever the latter is also a still-unmatched face. The verifier then constructs every cover relation in the complete nonempty face poset, orients unmatched Hasse edges downward and matched Hasse edges upward, and performs an exhaustive directed-cycle test. The resulting matching is acyclic. It contains \(2724\) pairs and leaves exactly one critical \(0\)-simplex and \(675\) critical \(4\)-simplices.

Forman's discrete Morse theorem, in the special case quoted as Theorem 7 by Donovan and Scoville, implies that a simplicial complex with an acyclic matching having one critical \(0\)-cell, \(k\) critical \(n\)-cells, and no other critical cells is homotopy equivalent to a wedge of \(k\) copies of \(S^n\). Applying it here gives

\[
\mathcal M(O)\simeq \bigvee^{675}S^4.
\]

## Verification
Run `python3 verify_octahedral_morse.py`. The program reconstructs the graph and the full Morse complex from definitions, checks the face vector, verifies acyclicity of the complete matched Hasse diagram, and independently computes simplicial boundary ranks over \(\mathbb F_2\).

The required boundary ranks are

\[
(23,205,867,1629),
\]

which give mod-\(2\) homology dimensions

\[
(1,0,0,0,675).
\]

The Euler characteristic is \(676\), also agreeing with a wedge of \(675\) four-spheres. A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Donovan, Lin, and Scoville introduced their 2019 study by noting that explicit homotopy types of Morse complexes were known only for a small collection of complexes, and they computed several families using strong collapses. Scoville and Zaremsky later gave general connectivity bounds. Their Theorem 4.4 gives only a connectivity lower bound from the edge count and maximum degree; for the octahedral graph it yields only \(1\)-connectedness. In the same paper they recall Kozlov's exact complete-graph computation, but \(O\) is \(K_6\) with a perfect matching removed, so that theorem does not determine this Morse complex.

Donovan and Scoville's 2022 exact homotopy computations concern extended stars, paths, cycles, Dutch windmills, and related matching/generalized-Morse constructions. Their full text supplies the Morse-complex definition and the discrete-Morse wedge criterion used above, but does not state an octahedral-graph computation.

Exact database searches were also run under the aliases “octahedral graph,” “\(K_6\) minus a perfect matching,” “acyclic discrete vector fields,” and “complex of discrete Morse functions.” The closest same-graph-family database hit concerns a different acyclic-orientation invariant and does not imply a Morse-complex homotopy type.

## Limitations
This is an exact finite result for one canonical graph. The exhaustive verifier proves the finite combinatorial certificate but does not establish a family theorem. The literature comparison is strong enough to separate the claim from the inspected exact and general Morse-complex results, but an unindexed or differently phrased prior computation remains a residual bibliographic risk.

## References
1. Connor Donovan, Maxwell Lin, and Nicholas A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440v1, first submitted 2019-09-25.
2. Nicholas A. Scoville and Matthew C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1, first submitted 2020-04-22; Proc. Amer. Math. Soc. Ser. B 9 (2022), 135-149.
3. Connor Donovan and Nicholas A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, first submitted 2022-07-27.
4. Dmitry N. Kozlov, *Complexes of Directed Trees*, J. Combin. Theory Ser. A 88 (1999), 112-122, DOI:10.1006/JCTA.1999.2984.
