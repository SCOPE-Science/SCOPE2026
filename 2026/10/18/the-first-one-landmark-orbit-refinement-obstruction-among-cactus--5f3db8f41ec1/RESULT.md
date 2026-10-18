# The first one-landmark orbit-refinement obstruction among cactus graphs

## Finding

**Theorem (sharp first obstruction).** Let \(G\) be a finite simple connected cactus graph, meaning that every biconnected block is either an edge or a cycle. Start ordinary synchronous counting colour refinement with a singleton colour on a selected vertex \(r\) and one common colour on all other vertices. For every \(|V(G)|\leq8\) and every choice of \(r\), the stable colour classes are exactly the orbits of \(\operatorname{Aut}(G)_r\). At order \(9\), there is precisely **one isomorphism type of rooted pair \((G,r)\)** for which this fails.

The unique rooted obstruction is the pentagon \(r-u_1-u_2-u_3-u_4-r\) together with one triangle attached only at \(u_1\) and a second triangle attached only at \(u_4\). The marked vertex is \(r\). Its stable colouring has class sizes \(1,2,6\), whereas the rooted automorphism-orbit sizes are \(1,2,2,4\).

## Assumptions and scope

All graphs here are finite, simple, undirected and connected. The statement is *within-graph orbit recovery*: it does **not** assert that colour refinement identifies a graph among arbitrary nonisomorphic graphs. A block is a maximal biconnected subgraph, with bridges treated as edge blocks. A rooted isomorphism sends the uniquely coloured vertex to the uniquely coloured vertex. A strict refinement round splits at least one colour class; stability means that no class splits. Other initial vertex colours are not allowed in the theorem.

For a partition \(\pi_t\), the next partition is induced by the keys \((\pi_t(v),[\pi_t(w):w\sim v])\), with all neighbour-colour multiplicities counted. Colour names themselves are immaterial. The orbit partition of the root stabilizer always refines the stable partition; orbit-exactness is the reverse containment.

## Proof

**1. A complete finite recursion.** Write \(\mathcal C_n\) for the isomorphism types of connected cactus graphs with \(n\) vertices. Start at \(\mathcal C_1=\{K_1\}\). For each \(2\leq n\leq9\), each \(1\leq k<n\), each \(H\in\mathcal C_{n-k}\), and each \(v\in V(H)\), add \(k\) fresh vertices. If \(k=1\), join the new vertex to \(v\) by one bridge; if \(k\geq2\), arrange the fresh vertices and \(v\) in a cycle of length \(k+1\). Remove duplicate outputs by exact graph isomorphism.

This enumeration is exhaustive: the block-cut incidence tree of any nonsingleton cactus has a leaf block. Removing all vertices of such a block except its one attachment vertex leaves a smaller connected cactus; reversing the deletion is exactly one allowed construction. For a cactus with only one block, choose any vertex as the retained root of that block. The induction supplies every isomorphism class, and no construction leaves the cactus family. A second, differently organized exhaustive recursion builds every \(n+1\)-vertex cactus by attaching one vertex to a nonempty set of old vertices and then discarding noncacti. The latter is complete because deleting a non-articulation vertex of a leaf block (or any vertex when there is only one block) leaves a connected cactus.

**2. Exact rooted-orbit tests.** For each unrooted representative from either recursion, individually colour **every** vertex in turn. Iterate refinement until the number of classes does not increase. For each stable class \(B\), select \(a\in B\) and check, for every \(b\in B\), whether a graph automorphism fixes the marked vertex and sends \(a\) to \(b\). One implementation uses two differently pointed copies and exact graph isomorphism. The other uses a separate exhaustive backtracking bijection search, checking adjacency, nonadjacency, degree and stable-colour preservation at each assignment. Thus a positive orbit comparison is witnessed by a bijective automorphism, and a negative one has exhausted all such candidates. Since every automorphism preserves refinement colours, all the classwise positive tests are equivalent to orbit-exactness.

Both recursions return the same complete sequence of unrooted cactus isomorphism counts for \(n=1,\ldots,9\):

\[
(1,1,2,4,9,23,63,188,596).
\]

For orders \(1\) through \(8\), all root choices pass, a total of \(2153\) tested rootings of one representative of each unrooted type. At order \(9\), precisely one of the \(596\cdot9=5364\) rootings fails. Therefore there is one and only one rooted isomorphism type of failure. The two complete executable enumerations, with their exact outputs, are included in the verification materials; the argument above establishes why their finite search spaces cover the theorem's full quantified domain.

**3. The obstruction and its inequivalent orbits.** Name the two extra triangle vertices at \(u_1\) by \(a,b\), and those at \(u_4\) by \(c,d\). Immediately after the first strict refinement there are exactly three cells

\[
\{r\},\qquad \{u_1,u_4\},\qquad \{u_2,u_3,a,b,c,d\}.
\]

Indeed, \(u_1,u_4\) have degree \(4\) and each sees one marked neighbour and three vertices in the final six-cell; each of the remaining six vertices has degree \(2\) and sees one vertex from the degree-four cell and one from the six-cell; \(r\) sees the two degree-four vertices. The partition is equitable and stable. The rooted graph has a reflection swapping \(u_1\) with \(u_4\) and \(u_2\) with \(u_3\), and the two triangle pairs may be independently interchanged. The sole five-cycle is invariant under all graph automorphisms, so no vertex in \(\{u_2,u_3\}\) can be sent to a triangle-only vertex. Hence the four orbit classes are exactly \(\{r\}\), \(\{u_1,u_4\}\), \(\{u_2,u_3\}\), and \(\{a,b,c,d\}\), strictly refining the stable three-cell partition.

## Verification

Running \(`python check_neighbor_augmentation.py`\) and \(`python check_leaf_block.py`\) with the dependency in `requirements.txt` reproduces the complete two-method census through order nine and the lone exception. The recorded output files `check_neighbor_augmentation.txt` and `check_leaf_block.txt` were generated by executing these programs. The routines explicitly assert both the graph-count sequence and the vector \((0,0,0,0,0,0,0,0,1)\) of failed rooted representatives. Graph-isomorphism grouping is exact, not a heuristic fingerprint: degree and block-size keys only prefilter potential duplicates.

The external cactus counting sequence A000083 independently matches the unrooted totals. It does **not** supply any of the rooted refinement results. The finite enumeration *is* an exhaustive proof of the sharp cutoff because every graph and every possible root in the claimed finite domain is covered by the proved recursions; it is not being extrapolated to larger orders.

## Relationship to prior work

Arvind--Köbler--Rattan--Verbitsky define refinability and the colour-refinement/automorphism hierarchy for arbitrary graphs; their general results do not enumerate singly individualized cacti or imply the nine-vertex uniqueness statement. Verbitsky--Zhukovskii describe universal covers of unicyclic graphs and analyse colour refinement on sparse random graph cores; their results are about a different class or an asymptotic distribution and do not determine this first finite multi-cycle cactus obstruction. Classical cactus enumeration counts the graphs but not their pointed refinement-orbit discrepancies. The present theorem supplies a sharp first failure of a one-vertex individualization heuristic in a natural family strictly beyond the one-cycle case.

## Limitations

The exact result stops at order nine; it is not a structural characterization for all pointed cacti and is not a theorem about arbitrary additional vertex colours. The implementation requires Python and NetworkX, and the two programs share a graph-isomorphism library for *unrooted duplicate elimination* although their constructions and pointed-automorphism checks differ. Previous specialized descriptions of this same cutoff may exist outside the inspected literature. No independent scientific audit or publication-priority certification has been performed.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public 2015-02-04), especially Sections 2 and 8. https://arxiv.org/abs/1502.01255
2. O. Verbitsky, M. Zhukovskii, *Canonical Labeling of Sparse Random Graphs*, STACS 2025, DOI:10.4230/LIPIcs.STACS.2025.75, especially Sections 2.2--2.5. https://doi.org/10.4230/LIPIcs.STACS.2025.75
3. OEIS A000083, *Number of mixed Husimi trees with n nodes; or polygonal cacti with bridges*, https://oeis.org/A000083 (enumeration cross-check, not a refinement result).
