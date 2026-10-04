# A one-sided block criterion for bipartite sequential orderability
## Finding
Let \(G=(A,B;E)\) be a finite simple bipartite graph with a fixed proper edge-colouring. If \(\deg_G(a)\ge 3\) for every \(a\in A\), then the edges of \(G\) admit a global total order such that the incident-colour sequences at the endpoints of every edge are distinct. Consequently, every finite simple \(d\)-regular bipartite graph is sequentially orderable under every proper edge-colouring for every integer \(d\ge 3\).

Here “sequentially orderable” means that, after fixing a proper edge-colouring and choosing one global total order of all edges, each vertex reads the colours on its incident edges in the induced order, and the two resulting sequences are different at the endpoints of every edge.

## Assumptions and scope
Let \(G=(A,B;E)\) be finite, simple, and bipartite. The edge-colouring is proper, so the colours incident with any vertex are pairwise distinct. The hypothesis is one-sided: only vertices of \(A\) are required to have degree at least \(3\). No connectedness or regularity assumption is needed for the theorem.

The threshold is natural. In degree \(2\), a properly two-edge-coloured even cycle can fail sequential orderability, so a universal statement with only a degree-
\(2\) lower bound is false.

## Proof
Fix an arbitrary order \(a_1,\ldots,a_m\) of the vertices in \(A\). We shall order all edges in consecutive blocks
\[
E(a_1),E(a_2),\ldots,E(a_m),
\]
where the internal order of each block \(E(a_i)\) will be chosen later.

Consider a vertex \(b\in B\). Because \(G\) is simple, at most one edge incident with \(b\) lies in any block \(E(a_i)\). Therefore the colour sequence seen at \(b\) depends only on the fixed order \(a_1,\ldots,a_m\), and is completely independent of all choices of internal block orders. Denote this fixed sequence by \(s_b\).

Now fix \(a\in A\) and write \(d=\deg_G(a)\). Properness gives \(d\) pairwise distinct incident colours. Hence the \(d!\) possible internal orders of \(E(a)\) produce exactly \(d!\) distinct colour sequences at \(a\).

Each neighbour \(b\in N(a)\) can forbid at most one of these \(d!\) possibilities, namely the unique permutation equal to \(s_b\), if \(s_b\) even has the same length and colour set. Thus at most \(d\) internal orders are forbidden. For \(d\ge3\),
\[
d!>d.
\]
So at least one internal order of \(E(a)\) avoids \(s_b\) for every \(b\in N(a)\).

These choices can be made independently for every \(a\in A\), because changing an internal order in an \(A\)-block never changes any sequence \(s_b\) on the \(B\)-side. Concatenate the chosen blocks. For every edge \(ab\), the sequence at \(a\) was chosen to differ from the fixed sequence at \(b\). Thus the resulting global edge order distinguishes the endpoints of every edge.

For a \(d\)-regular bipartite graph with \(d\ge3\), either bipartition class may be used as \(A\), giving the stated corollary.

## Verification
The proof above is deductive and does not depend on computation. The embedded `verify.py` separately stress-tests the construction by exhaustive enumeration of all labeled regular bipartite adjacency matrices and all proper edge-colourings in four finite strata: \(K_{3,3}\), all \(3\)-regular bipartite graphs with four vertices per side, all such graphs with five vertices per side, and \(K_{4,4}\). It checks \(67,404\) proper colourings in total and verifies that the block construction always produces distinct endpoint sequences.

## Relationship to prior work
Gorzkowska and Kwaśny introduced this sequential-orderability problem for a fixed proper edge-colouring. Their September 2026 preprint proves the connected regular case for degree at least \(6\) and leaves the regular degrees \(3,4,5\) among the remaining cases. The present block argument settles every bipartite regular graph in those degrees and, more generally, every finite simple bipartite graph having one bipartition class of minimum degree at least \(3\).

A separately indexed September 2026 result proves the regular bipartite case for degree at least \(5\) using a local-lemma argument. The theorem here strictly contains that range and replaces the probabilistic step by independent local permutation choices.

## Limitations
The argument uses simplicity essentially: a right-side vertex must have at most one incident edge in each left-side block. It also uses properness so that the \(d!\) internal edge orders yield \(d!\) distinct local colour sequences. The result does not settle the remaining nonbipartite regular cases of degrees \(3,4,5\).

The primary preprint's abstract, metadata, and theorem-level public summaries were available, but direct full-text retrieval from the queried public arXiv endpoints was unavailable during the comparison. Thus an unindexed or body-only observation of the same bipartite block argument remains a bibliographic residual risk; the searches located no such statement.

## References
1. Aleksandra Gorzkowska and Jakub Kwaśny, “Distinguishing adjacent vertices by ordering edges,” arXiv:2609.11832, first public version 2026-09-10.
2. “A local-lemma criterion for sequential edge orderings in bipartite graphs,” public indexed research record dated 2026-09-18; its stated range is finite simple \(d\)-regular bipartite graphs with \(d\ge5\).
