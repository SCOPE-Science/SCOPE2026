# Integral homotopy and cyclic character of the Desargues dominance complex

## Finding

Let \(G\) be the 20-vertex Desargues graph \(GP(10,3)\), and let \(\mathcal D(G)\) be the simplicial complex whose faces are vertex subsets with dominating complements. Then there is an integral homotopy equivalence

\[
\mathcal D(G)\simeq\bigvee^{13}S^9.
\]

For the natural order-ten rotation \(\rho\), the traces of \(\rho^k\) on \(\widetilde H_9(\mathcal D(G);\mathbb Q)\), for \(0\le k\le9\), are exactly

\[
(13,-1,3,-1,3,-11,3,-1,3,-1).
\]

In particular, as a rational \(C_{10}\)-representation,

\[
\widetilde H_9(\mathcal D(G);\mathbb Q)
\cong\mathbb Q\oplus\varepsilon^{\oplus4}\oplus\mathbb Q(\zeta_{10})^{\oplus2},
\]

where \(\varepsilon(\rho)=-1\) and \(\mathbb Q(\zeta_{10})\) denotes the faithful four-dimensional rational cyclotomic representation. All other reduced integral homology vanishes; \(\widetilde H_9(\mathcal D(G);\mathbb Z)\cong\mathbb Z^{13}\).

## Assumptions and scope

The graph is finite, simple, and undirected. Its vertex set is \(\{u_i,v_i:i\in\mathbb Z/10\mathbb Z\}\), and its 30 edges are

\[
\{u_i,u_{i+1}\},\quad\{u_i,v_i\},\quad\{v_i,v_{i+3}\},\qquad i\in\mathbb Z/10\mathbb Z.
\]

Indices are interpreted modulo ten, and each undirected edge is included once. A set \(T\subseteq V(G)\) dominates if \(T\cap N_G[x]\ne\varnothing\) for each vertex \(x\), with \(N_G[x]\) the *closed* neighborhood of \(x\). Define

\[
\mathcal D(G)=\{\sigma\subseteq V(G):V(G)\setminus\sigma\text{ dominates }G\}
=\{\sigma: N_G[x]\not\subseteq\sigma\text{ for all }x\}.
\]

The empty face is included, and geometric realization uses only nonempty faces. The rotation sends \(u_i\mapsto u_{i+1}\) and \(v_i\mapsto v_{i+1}\); it preserves the closed-neighborhood conditions and induces a simplicial \(C_{10}\)-action.

## Proof

**Exhaustive enumeration.** Encode each subset \(\sigma\) by its 20-bit indicator \(m\), and each closed neighborhood by the bit mask \(b_x\). Check the exact predicate \((m\mathbin{\&}b_x)\ne b_x\) for every \(x\). The packaged standalone program evaluates the complete range \(0\le m<2^{20}\), with a downward-closed recurrence equivalent to the predicate; it enumerates precisely \(434220\) nonempty faces. Their face numbers in dimensions zero through thirteen are

\[
(20,190,1140,4825,15184,36390,66800,93120,96400,71356,35680,11105,1880,130).
\]

**Exact acyclic Morse matching.** In the fixed vertex order \(u_0,\ldots,u_9,v_0,\ldots,v_9\), process each pivot vertex in turn. Pair every still-unmatched nonempty face \(\sigma\) not containing the pivot with \(\sigma\cup\{v\}\), provided both are faces and unmatched. The executable implementation constructs all \(217103\) pairs. It checks the directed Hasse diagram obtained by reversing precisely the matched covering arrows, leaving all unmatched covering arrows directed downward. There are \(3663080\) covering incidences between nonempty faces. A complete topological sort visits all \(434220\) nodes, which establishes acyclicity, not merely absence of short cycles. Exactly one unmatched vertex and thirteen unmatched nine-dimensional faces remain. By the acyclic-matching theorem of discrete Morse theory, \(\mathcal D(G)\) is homotopy equivalent to a CW complex with precisely one zero-cell and thirteen nine-cells. Every nine-cell attaches to the point, yielding the asserted wedge *integrally*. No field-dependent rank calculation is used to infer the homotopy type.

**Cyclic character.** For each \(0\le k\le9\), let \(p=\rho^k\). A simplex fixed setwise by \(p\) is a union of its vertex orbits. Enumerate all such unions, reject any failing the closed-neighborhood condition, and take the sign \(\operatorname{sgn}(p|_\sigma)\) of the induced permutation of its ordered vertices. The nonempty-chain Lefschetz number is

\[
L(p)=\sum_{\substack{\varnothing\ne\sigma\in\mathcal D(G)\\p\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(p|_\sigma).
\]

Because the only nonzero reduced homology is in odd degree nine, \(L(p)=1-\operatorname{tr}(p|\widetilde H_9)\). Exact integer evaluation yields the ten trace values stated in the Finding. The four irreducible rational \(C_{10}\)-representations are the trivial representation, the sign representation, and the degree-four cyclotomic representations of orders five and ten. Comparing their rational characters gives multiplicities \(1,4,0,2\), respectively, establishing the claimed decomposition. This is a rational representation classification, not a claim of integral-module splitting.

## Verification

Run `python3 verify_desargues.py` with Python 3.9 or newer. The program uses only the standard library. Its assertions reproduce every face, every proposed matching pair, all directed covering incidences and the complete topological-order acyclicity test, all ten signed Lefschetz traces, and the rational character. An alternate model constructs the canonical bipartite double cover of the Petersen graph \(KG(5,2)\), verifies an explicit 20-vertex graph isomorphism, and independently reconstructs the full face vector. The expected concise results are 434220 nonempty faces, 217103 matching pairs, 1 critical zero-cell and 13 critical nine-cells, 3663080 covering incidences, and the trace vector above. This is a finite exhaustive mathematical certificate; it is not an external independent audit.

## Relationship to prior work

Matsushita and Wakatsuki [1], publicly available on 2023-12-05, define dominance complexes and prove a general combinatorial Alexander-duality relationship with neighborhood complexes of complement graphs. Their graph-family calculations and general relationships do not present this particular Desargues-graph integral homotopy calculation or the order-ten character. Earlier work of Matsushita [2] discusses the same closed-neighborhood avoidance model and its connectivity, but does not determine this exact space. The Desargues graph has separately studied ordinary independence, matching, cut and graph-metric complexes; those constructions have different faces or vertex universes and their homotopy classifications do not imply this dominance-complex classification. A lack of indexed matching results is not proof of historical priority.

## Limitations

The result is for the precisely defined Desargues graph and its indicated cyclic automorphism subgroup. It does not determine a uniform family of generalized Petersen dominance complexes, the full automorphism-group action, or the integral \(\mathbb Z[C_{10}]\)-module structure. The finite certificate establishes the claimed homotopy equivalence once its exhaustive exact operations are reproduced. Unindexed equivalent earlier work remains possible; no claim of external verification or priority certification is made.

## References

1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639 (first posted 2023-12-05), https://arxiv.org/abs/2312.02639.
2. T. Matsushita, *Dominance complexes and vertex cover numbers of graphs*, arXiv:2009.04145, https://arxiv.org/abs/2009.04145.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
