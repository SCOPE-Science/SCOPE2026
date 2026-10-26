# Four-periodic classification of upper-dominating sets in prism graphs

## Finding
Let \(P_n=C_n\square K_2\) be the ordinary circular prism on the labelled vertices \(t_i,b_i\), with indices \(i\) in \(\mathbb Z/n\mathbb Z\), where \(n\ge3\). A *minimal dominating set* is a vertex set that dominates every vertex and ceases to dominate after any one of its elements is deleted. Write \(\Gamma(P_n)\) for the largest size of such a set, and \(U_n\) for the number of distinct vertex subsets attaining this largest size.

**Theorem.** For every integer \(n\ge3\),
\[
\Gamma(P_n)=n,\qquad
U_n=2+2\mathbf1_{2\mid n}+4\mathbf1_{4\mid n}.
\]
More precisely, *all* minimal dominating sets of size \(n\) belong to the following disjoint classes:

1. **Layer sets (always):** the entire top or entire bottom \(n\)-cycle (two sets).
2. **Alternating sets (only for even \(n\)):** one vertex of each rung, alternating between top and bottom on successive rungs (two sets).
3. **Paired-rung sets (only when \(4\mid n\)):** choose both vertices of two consecutive rungs, neither vertex of the next two rungs, and repeat cyclically (four distinct phases).

Hence \(U_n=2\) for odd \(n\), \(U_n=4\) for \(n\equiv2\pmod4\), and \(U_n=8\) for \(n\equiv0\pmod4\). Counts refer to distinct subsets in the fixed labelled graph, not symmetry orbits.

## Assumptions and scope
All graphs are finite, simple and undirected; \(C_n\) is the simple \(n\)-cycle for \(n\ge3\). The Cartesian product has the vertical rung edges \(t_ib_i\) and two horizontal cycles \(t_it_{i+1}\), \(b_ib_{i+1}\), with indices modulo \(n\). This graph is connected and cubic, with \(2n\) vertices. A vertex subset \(S\) dominates when each vertex outside \(S\) has a neighbor in \(S\). Minimality is inclusion-minimality, whereas maximizing its cardinality defines upper domination. No assertions are made here about all smaller minimal dominating sets, domination polynomials or ladders with open ends.

## Proof
**Tightness lemma for regular graphs.** Let \(G\) be any connected \(d\)-regular graph of positive degree and order \(N\), and \(S\) a minimal dominating set. Partition \(S=I\sqcup F\), where \(I\) contains vertices isolated in \(G[S]\), and every vertex of \(F\) has a neighbor in \(S\). Minimality supplies, for each \(f\in F\), an *external private neighbor* \(p(f)\notin S\) adjacent to \(f\) and no other vertex of \(S\). Indeed \(f\) itself cannot be private, since it has a neighbor in \(S\). The chosen vertices \(p(f)\) are distinct. Put \(Q=\{p(f):f\in F\}\) and \(R=V(G)\setminus(S\cup Q)\). No vertex of \(I\) is adjacent to a vertex of \(S\) (by definition), or to a vertex of \(Q\) (by the private-neighbor property). Hence every one of the \(d|I|\) edges incident with \(I\) ends in \(R\), implying \(d|I|\le d|R|\) and
\[
2|S|=2(|I|+|F|)\le N.
\]
This reproves the known regular-graph upper bound, which is used here rather than claimed as a new general result.

If equality holds, \(|I|=|R|\), so every vertex of \(R\) has *all* \(d\) neighbors in \(I\). Thus \(I\cup R\) and \(F\cup Q\) have no edges between them. Connectedness forces either \(I=\varnothing\) or \(F=\varnothing\). If \(F=\varnothing\), the set \(S\) is independent and has half the vertices; regularity forces its complement also to be independent, making \(S\) one class of a bipartition. If \(I=\varnothing\), then \(Q=V\setminus S\), and each outside vertex has exactly one neighbor in \(S\). Each selected vertex has at least one chosen private neighbor, so counting the \(|S|\) crossing edges forces every selected vertex to have exactly one outside neighbor. Therefore all edges across \((S,V\setminus S)\) form a perfect matching. Conversely an independent bipartition side, or either side of such a perfect-matching cut in a positive-degree regular graph, is dominating and minimal: in the second case each selected vertex has its uniquely matched outside private neighbor. It follows that for the connected cubic prism, the sets of size \(n\) are exactly independent bipartition sides and sides of perfect-matching cuts.

**Independent sides.** Any independent set of \(n\) vertices must contain exactly one vertex on each of the \(n\) rungs, since each rung is an edge. The horizontal edges force the chosen layer to alternate with the rung index. Such an alternating assignment closes around the cycle if and only if \(n\) is even, and then there are exactly two assignments.

**Perfect-matching cuts.** Color the vertices of \(S\) black and the others white. Each vertex must have precisely one differently colored neighbor. If some rung is bichromatic, its rung edge is already that crossing edge for both endpoints. Consequently both horizontal neighbors of both endpoints have their respective same colors, forcing each adjacent rung to be bichromatic with the same orientation. Induction around the cycle implies that every rung is bichromatic with the same orientation: these are exactly the two layer sets.

Otherwise all rungs are monochromatic. Write \(c_i\in\{0,1\}\) for the color of both vertices on rung \(i\). The vertical edge is now internal to a color class, so the unique-crossing-neighbor rule requires that exactly one of \(c_{i-1}\) and \(c_{i+1}\) differs from \(c_i\), for every \(i\). Equivalently, every maximal constant run in the cyclic binary word \((c_i)\) has length exactly two. Indeed a run of length one gives two differing neighbors; a run of length at least three gives an interior position with none. The runs alternate colors, so their total number must be even and \(4\mid n\). Conversely when \(4\mid n\), the four cyclic phases of \(0011\) repeated satisfy the rule and determine four distinct sets. There are no additional cuts.

The top-layer set has size \(n\) and is minimal dominating, so the general bound is attained. Summing the pairwise disjoint types proves the theorem. \(\square\)

## Verification
The accompanying self-contained Python 3 program `verify.py` independently constructs the prism adjacency relation and tests domination and inclusion-minimality directly, without using the proof's cut classification. It enumerates every \(n\)-vertex subset for \(3\le n\le10\), comparing the complete list with the three explicit families. It also enumerates *every* subset of cardinality greater than \(n\) for \(3\le n\le8\), finding no minimal dominating set. Run with `python3 verify.py`; the expected plain-text transcript is `verify_output.txt`. This is finite corroboration, not an infinite proof; the latter is the argument above.

## Relationship to prior work
Sahbi (2026), arXiv:2610.03785v1 (first made public 2026-09-30), determines the upper-domination number for *rectangular* Cartesian grids using classical bipartite identities and does not present the circular-prism extremal-set enumeration. Southey and Henning (2013) establish the general regular-graph upper bound and characterize equality graph families; that general bound is expressly credited here. The new assessed claim is the explicit complete **vertex-subset** classification and its four-periodic *number* for the circular prisms, including nonbipartite odd prisms. The general bound alone does not enumerate these vertex subsets. Zverovich and Zverovich (1999) study upper-domination-perfect graphs, with prism examples in their structural theory, not an identified table of the cardinality-specific counts above. The accessible OEIS entry A290379 counts *all* minimal dominating sets of *open* ladders, a different graph and different enumeration.

## Limitations
The result concerns only inclusion-minimal dominating sets of *maximum* size, not those of other sizes. The original 2013 equality-classification paper could not be inspected in full text; its abstract was available and its coverage of the general bound was credited. Likewise the 1999 prism-related structural article was only available through its abstract. Their uninspected proofs could contain related classifications; equivalence of the exact four-periodic labeled-set enumeration was not established. No independent mathematical audit has been carried out. Exhaustive tests cover only the explicitly listed small sizes.

## References
1. R. Sahbi, *Upper Domination in Rectangular Grid Graphs and Its Relation to Sub-Quorum Colorings*, arXiv:2610.03785v1, first submitted 2026-09-30, https://arxiv.org/abs/2610.03785.
2. J. Southey and M. A. Henning, *Edge Weighting Functions on Dominating Sets*, Journal of Graph Theory 72 (2013), 346–360, DOI:10.1002/jgt.21649.
3. I. E. Zverovich and V. E. Zverovich, *A semi-induced subgraph characterization of upper domination perfect graphs*, Journal of Graph Theory 31 (1999), 29–49, DOI:10.1002/(SICI)1097-0118(199905)31:1<29::AID-JGT4>3.0.CO;2-G.
4. OEIS A290379, *Number of minimal dominating sets in the n-ladder graph*, https://oeis.org/A290379 (distinct open-ladder comparison).
