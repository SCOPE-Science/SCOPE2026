# The Icosian eight-edge switch graph is a Petersen line-graph double cover

## Finding

Let \(D\) be the dodecahedral graph, and let \(\mathcal H\) denote its undirected Hamiltonian cycles, identified by their edge sets. For an even integer \(L\), construct \(\mathcal R_L(D)\) on \(\mathcal H\), joining distinct cycles precisely when their symmetric difference is a **single alternating simple cycle** of length at most \(L\). Here alternating means that consecutive edges belong alternately to the two Hamiltonian cycles.

**Theorem.** The smallest \(L\) for which \(\mathcal R_L(D)\) is connected is \(8\). At this threshold the graph has \(30\) vertices, \(60\) edges, degree \(4\) at every vertex, and diameter \(4\). More precisely,

\[
\mathcal R_8(D)\cong K_2\times L(P),
\]

where \(P\) is the Petersen graph, \(L(P)\) is its line graph, and \(\times\) is the graph direct (tensor, or Kronecker) product. Thus \(\mathcal R_8(D)\) is the connected bipartite double cover of the line graph of the Petersen graph.

The isomorphism can be chosen so that the antipodal automorphism of \(D\) exchanges the two sheets. The quotient by its action on Hamiltonian cycles is precisely \(L(P)\). The \(30\)-cycle enumeration itself is established older work and is not asserted to be new.

## Assumptions and scope

All graphs are undirected and simple, except that the Cartesian notions of a product are not used. The graph \(D\) is the generalized Petersen graph \(GP(10,2)\). Use twenty labeled vertices \(u_i,v_i\), with \(i\in\mathbb Z/10\mathbb Z\), and its thirty edges

\[
u_iu_{i+1},\quad u_iv_i,\quad v_iv_{i+2}\qquad(i\in\mathbb Z/10\mathbb Z).
\]

In the verification files \(u_i\) is numbered \(i\), while \(v_i\) is numbered \(10+i\). Cycles are identical when they use the same undirected edges, without regard to starting vertex or orientation. An edge of \(\mathcal R_L(D)\) is **one** symmetric-difference alternating cycle, not an arbitrary union of cycles and not the usual two-edge Hamilton-cycle switch. The product \(K_2\times L(P)\) joins \((a,e)\) to \((1-a,f)\) exactly when the Petersen edges \(e,f\) share an endpoint.

## Proof

The result is a finite, exact, exhaustive classification with a small independently replayable certificate. Here are the reduction, exhaustiveness argument, and structural identification; the complete integer data and their recomputation are supplied in `certificate.json`, `verify_cycle_dfs.py`, and `verify_matching_alt.py`.

**1. Completeness of the Hamilton-cycle list.** Start an oriented path at vertex \(0\), repeatedly append every unused neighbor of its last vertex, and accept at twenty vertices only if the endpoint is adjacent to \(0\). For each undirected Hamiltonian cycle, exactly two such rooted traversal sequences exist; accepting only sequences with the second vertex numerically smaller than the last retains exactly one. No admissible extension is pruned. `verify_cycle_dfs.py` implements this complete recursion and yields exactly \(30\) distinct twenty-edge masks. This agrees with Schwenk's established enumeration of Hamilton cycles of \(GP(10,2)\); the earlier count is used as context, not as the new conclusion.

**2. The sharp lower bound.** For Hamiltonian cycles \(H,H'\), their symmetric difference has degree zero or two at each underlying vertex. Every nonempty component is a simple cycle alternating between edges of \(H\) and \(H'\), hence has even length. The dodecahedral graph has neither a four-cycle nor a six-cycle: the supplied exact six-cycle search exhausts every simple path of the required length and closes it only when the final vertex is adjacent to the first (likewise for length four). Consequently every permitted alternating cycle has at least eight edges. In particular \(\mathcal R_L(D)\) is edgeless for \(L<8\).

**3. The eight-edge exchange census.** On the complete list of \(\binom{30}{2}\) pairs of Hamiltonian cycles, calculate the exact set symmetric difference. An eight-edge difference is checked to be connected and degree two on its eight participating vertices; it is therefore a single alternating eight-cycle. There are exactly \(60\) such pairs, and all thirty cycles have four neighbors. Exhaustive breadth-first search from **every** vertex gives connectivity and diameter \(4\). These are exhaustive finite statements, not extrapolation from sampling.

**4. The antipodal quotient.** The map \(\alpha:u_i\mapsto u_{i+5},\ v_i\mapsto v_{i+5}\) is an involutive automorphism of \(D\). Its induced action pairs the thirty Hamiltonian cycles into fifteen two-element orbits, with no fixed cycle. The eight-edge exchange graph is bipartite, with fifteen vertices in each part, and \(\alpha\) interchanges the two parts. On the quotient \(Q\) of these fifteen orbits, each exchange edge has a partner exchanged by \(\alpha\), and every quotient edge has exactly two lifts. The quotient has fifteen vertices, thirty edges and constant degree four.

**5. Identification of the quotient.** Enumerating all triples of mutually adjacent vertices in \(Q\) gives exactly ten triangles. Each vertex of \(Q\) belongs to precisely two of these triangles, and each edge belongs to precisely one. Form a ten-vertex graph \(P'\) whose vertices are these triangles and whose edges correspond to their common vertices of \(Q\). The data show that \(P'\) is cubic, and the supplied explicit mapping of its ten triangle-indices to the ten two-element subsets of a five-element set sends its edges exactly to disjointness. Thus \(P'\cong KG(5,2)\), the Petersen graph. Every vertex of \(Q\) is the intersection of its two associated triangles, and adjacency in \(Q\) means incidence at a common triangle; hence \(Q\cong L(P')\cong L(P)\). The mapping is recorded explicitly in `certificate.json`, rather than asserted from numerical spectral coincidences.

**6. Recovery of the full switch graph.** Label each Hamilton cycle by its quotient vertex and its bipartite color. The antipodal map exchanges the colors, and each quotient edge has exactly one lift incident to each preimage. Therefore two Hamilton cycles are adjacent exactly when their quotient vertices are adjacent and their colors differ. This is precisely the direct-product adjacency defining \(K_2\times L(P)\). Since \(P\) has triangles in its line graph and is connected, its double cover here is connected; direct all-source breadth-first search independently verifies diameter four. Combining with step 2 proves the sharp threshold.

The proof is computer-assisted for a **fixed twenty-vertex graph**. It does not claim an infinite-family theorem or treat partial enumeration as exhaustive; the two fully specified finite search spaces are exhausted.

## Verification

Run these standalone programs from the extracted package with Python 3.9 or newer:

```
python3 verify_cycle_dfs.py
python3 verify_matching_alt.py
```

The first enumerates rooted Hamiltonian cycles without pruning, checks all pairwise symmetric differences, reconstructs the antipodal quotient, checks triangle incidence and the Petersen strongly regular parameters, and verifies the exact double-cover adjacency. The second independently enumerates all \(36\) perfect matchings of the cubic graph and keeps those whose complements are connected two-factors; it finds \(30\) Hamiltonian cycles and \(6\) other two-factors. It then reconstructs the exchange graph and exhibits an isomorphism to \(KG(5,2)\) by backtracking over all ten quotient-triangle labels. It independently verifies the two-sheet lift.

Every operation is exact integer/set arithmetic; there is no numerical tolerance, random search, third-party package, or external file dependency. The JSON certificate lists each Hamiltonian-cycle edge mask, all exchange adjacencies, the antipodal map, the quotient edges/triangles, and the Petersen labeling. Its values may be recreated with the first verifier.

## Relationship to prior work

Schwenk (1989) determined the **number** of Hamiltonian cycles of generalized Petersen graphs \(GP(n,2)\), which already includes the cardinality \(30\) at \(n=10\). Hopkins (2004) demonstrated the dodecahedron's uniqueness of Hamiltonian tours up to spatial symmetry and described the four faces with four chosen edges. Neither establishes adjacency of the thirty individual tours under shortest alternating-cycle switching, the diameter of that exchange graph, or the Petersen line-graph double-cover structure.

Sierksma (1998) studied interchange graphs on Hamiltonian cycles of **complete graphs** and their traveling-salesperson polytope, not the constrained thirty-cycle system in \(D\). Takaoka (2018) examined Hamiltonian-cycle reconfiguration by two-edge replacement, a distinct and strictly shorter operation that cannot act on this graph without a four-cycle. The exact graph identification and threshold stated here are the proposed new result; counts of Hamilton cycles and general graph-cover facts are acknowledged background.

## Limitations

This is a finite exact classification for the dodecahedron, not a result about all generalized Petersen graphs. The identification does not assert geometric realization of individual flips on the surface beyond the combinatorial alternating-cycle definition. The result has not undergone independent scholarly audit. A mathematically equivalent description might exist in older graph-transformation, icosian, or edge-coloring literature that is absent from the inspected sources. The finite certificate proves the stated combinatorial facts but does not prove bibliographic novelty.

## References

1. A. J. Schwenk, *Enumeration of Hamiltonian Cycles in Certain Generalized Petersen Graphs*, Journal of Combinatorial Theory, Series B **47** (1989), 53–59. DOI: 10.1016/0095-8956(89)90064-6. Author-supplied full text available at https://www.researchgate.net/publication/220077067_Enumeration_of_Hamiltonian_cycles_in_certain_generalized_Petersen_graphs.
2. B. Hopkins, *Hamiltonian Paths on Platonic Graphs*, International Journal of Mathematics and Mathematical Sciences **2004** (2004), 1613–1616. DOI: 10.1155/S0161171204307118. First published July 18, 2004. Full text available at https://www.researchgate.net/publication/26533752_Hamiltonian_paths_on_Platonic_graphs.
3. G. Sierksma, *Interchange Graphs and the Hamilton Cycle Polytope*, Discrete Applied Mathematics **81** (1998), 217–224. DOI: 10.1016/S0166-218X(97)00086-3.
4. A. Takaoka, *Complexity of Hamiltonian Cycle Reconfiguration*, Algorithms **11** (2018), 140. DOI: 10.3390/a11090140.
