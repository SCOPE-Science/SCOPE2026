# Exact locating-dominating bipartitions and their reconfiguration on matched cliques

## Finding
For each integer \(n\ge4\), let \(G_n=K_n\square K_2\), with two distinguished \(n\)-cliques \(A=\{u_1,\ldots,u_n\}\), \(B=\{v_1,\ldots,v_n\}\) and matching edges \(u_iv_i\). An ordered bipartition \((S,T)\) is *doubly locating-dominating* if both \(S\) and \(T\) are locating-dominating sets. Let \(\mathcal L_n(z)=\sum_{(S,T)}z^{|S|}\), with the sum over these ordered bipartitions.

**Theorem (complete census and one-vertex reconfiguration).** For every \(n\ge4\),
\[
\mathcal L_n(z)=n(2^{n-1}-2)(z^{n-1}+z^{n+1})+\bigl(2^n+n(n-1)2^{n-2}\bigr)z^n.
\]
Consequently the total number of ordered bipartitions is
\[
L_n=2^{n-2}(n^2+3n+4)-4n,
\]
and every such bipartition is near-balanced: \(|S|\in\{n-1,n,n+1\}\).

Define the *single-transfer reconfiguration graph* \(R_n\) to have these ordered bipartitions as vertices and to join two when one vertex of \(G_n\) transfers between \(S\) and \(T\), preserving both locating-dominating properties. Then \(R_n\) has exactly three connected components: two isolated vertices and one connected component of order \(L_n-2\). Its exact number of edges is
\[
|E(R_n)|=n(n+1)(2^n-4).
\]
The isolated vertices are the two all-split partitions \(S=A,T=B\) and \(S=B,T=A\).

## Assumptions and scope
All graphs are finite, simple and undirected. A set \(D\subseteq V(G)\) is *locating-dominating* when, for every vertex \(w\notin D\), its open-neighborhood trace \(N_G(w)\cap D\) is nonempty, and these traces are distinct for distinct vertices outside \(D\). Vertices inside \(D\) are not required to have distinct traces. The bipartitions are ordered (interchanging \(S\) and \(T\) generally produces a different vertex of \(R_n\)). The indexing of the two cliques is fixed; no quotient by graph automorphisms is taken.

For each matched column \(i\), call its type \(RR\) if \(u_i,v_i\in S\), type \(BB\) if \(u_i,v_i\in T\), type \(RB\) if \(u_i\in S,v_i\in T\), and type \(BR\) if \(u_i\in T,v_i\in S\). Write \(a,b,c,d\) for the respective numbers of these four types, so \(a+b+c+d=n\). This notation concerns membership in the two classes, not graph coloring.

## Proof
**1. Complete local characterization.** We prove that for \(n\ge4\), a column-type word represents a doubly locating-dominating bipartition if and only if
\[
a\le1,\quad b\le1,
\]
and, additionally, when \((a,b)=(1,0)\) or \((0,1)\), both \(c\) and \(d\) are positive. When \((a,b)=(0,0)\) or \((1,1)\), no additional condition is imposed.

First consider locating for \(S\). Two vertices outside \(S\) in the same row of the prism see exactly the same selected vertices from that row, and their only possible additional selected neighbors are their two distinct partners across the matching. Accordingly, two such vertices have identical \(S\)-traces if and only if *neither* of their matched partners is in \(S\). This can happen for a pair in either row exactly when there are at least two columns of type \(BB\). Thus same-row location by \(S\) is equivalent to \(b\le1\). Symmetrically, same-row location by \(T\) is equivalent to \(a\le1\).

For completeness, a vertex outside \(S\) in row \(A\) sees **all** selected vertices of \(A\), possibly together with its single matched partner in \(B\). A vertex outside \(S\) in row \(B\) sees **all** selected vertices of \(B\), possibly together with its single matched partner in \(A\). If their \(S\)-traces were equal, all selected vertices of \(A\) would lie in the one possible matched partner of the \(B\)-vertex, and likewise all selected vertices of \(B\) in one possible matched partner of the \(A\)-vertex. This forces \(|S|\le2\). But under \(a,b\le1\), \(|S|=n+a-b\ge n-1\ge3\). Therefore cross-row traces cannot coincide. The identical argument for \(T\) works since \(|T|=n-a+b\ge3\). Thus \(a,b\le1\) completely guarantees the locating part for both sets.

It remains to check domination. Any vertex outside \(S\) has a selected neighbor in its own row whenever that row contains any selected vertex. When its own row has none, a selected matched partner is its only possible dominating neighbor. Therefore a domination failure for \(S\) occurs precisely if a \(BB\) column exists and one row has no \(S\)-vertex, that is, if \(b=1\) and either \(a+c=0\) or \(a+d=0\). Under \(a\le1,b\le1\), this is precisely the forbidden case \((a,b)=(0,1)\) with \(c=0\) or \(d=0\). Interchanging \(S,T\) gives exactly the forbidden case \((a,b)=(1,0)\) with \(c=0\) or \(d=0\). The characterization follows; it includes the uniform all-split words.

**2. Size-refined enumeration.** For \((a,b)=(0,0)\), each of \(n\) columns independently has type \(RB\) or \(BR\): there are \(2^n\) configurations and \(|S|=n\). For \((a,b)=(1,1)\), choose the distinct \(RR,BB\) columns in \(n(n-1)\) ways and freely choose the remaining \(n-2\) split types: there are \(n(n-1)2^{n-2}\) configurations and again \(|S|=n\). For \((a,b)=(1,0)\), choose the single \(RR\) column, then any nonconstant word over \(RB,BR\) for the remaining \(n-1\) columns. There are \(n(2^{n-1}-2)\) configurations of size \(|S|=n+1\). The symmetric case \((a,b)=(0,1)\) has the same number and size \(|S|=n-1\). These four mutually exclusive cases yield \(\mathcal L_n(z)\) and, at \(z=1\), \(L_n\).

**3. Components of the reconfiguration graph.** Every transfer of one vertex changes a split column into \(RR\) or \(BB\), or changes \(RR\) or \(BB\) into a split column. The two uniform split words \(RB^n\) and \(BR^n\) have no neighbor: any transfer creates exactly one nonsplit column and leaves no column of one of the two split types, violating step 1.

Every other all-split word has \(c,d\ge1\). A valid word with \((a,b)=(1,0)\) has \(c,d\ge1\) and can be transferred at its unique \(RR\) column into an all-split word having both split types; the case \((0,1)\) is symmetric. A valid word with \((a,b)=(1,1)\) has \(c+d=n-2\ge2\). If \(c=0\), transfer one vertex of its \(RR\) column to create an \(RB\) column and retain an existing \(BR\) column. If \(d=0\), similarly create \(BR\). If both counts are positive, either appropriate transfer works. This takes the word into the case \((a,b)=(0,1)\) with \(c,d\ge1\), which was just shown to connect to a mixed all-split word.

The graph of all mixed all-split words is the Boolean cube on \(n\) column orientations with its two opposite uniform vertices deleted, which is connected when \(n\ge3\). Each elementary change between two mixed words can be realized in \(R_n\) by two successive single-vertex transfers: first create \(RR\) (or \(BB\)) in the changing column, then finish with the opposite split orientation. Because both endpoint words are mixed, the intermediate word retains at least one column of each split orientation and is valid by step 1. Hence all mixed all-split words belong to one component. Together with the preceding reductions, exactly one nontrivial component remains. There are precisely two isolated vertices.

**4. Exact edge census.** Classify vertices of \(R_n\) by \(a+b\in\{0,1,2\}\). An edge necessarily joins consecutive levels. There are \(2n(2^{n-1}-2)\) level-one vertices. Each has exactly two edges downward to level zero, obtained by splitting its unique nonsplit column in either way; thus
\[
E_{0,1}=4n(2^{n-1}-2).
\]
At level two, there are \(n(n-1)(2^{n-2}-2)\) configurations with both \(c,d\) positive; each has four edges downward to level one (two ways to split either of its two nonsplit columns). There are \(2n(n-1)\) remaining level-two configurations, with exactly one of \(c,d\) zero; each has exactly two edges downward, namely those introducing its missing split orientation. Hence
\[
E_{1,2}=4n(n-1)(2^{n-2}-2)+4n(n-1)
=4n(n-1)(2^{n-2}-1).
\]
Adding the disjoint edge classes and simplifying gives \(E_{0,1}+E_{1,2}=n(n+1)(2^n-4)\), as asserted.

## Verification
The standalone program `verify.py` constructs both \(n\)-cliques and all \(n\) matching edges, independently tests both locating-dominating conditions on all \(2^{2n}\) ordered assignments for each \(n\in\{4,5,6,7,8\}\), and compares its results with the theorem. It separately reconstructs the entire one-transfer reconfiguration graph and counts components and edges without using the proof characterization as its acceptance oracle. Its output includes:

```
n=4: bipartitions 112; components 110,1,1; edges 240
n=5: bipartitions 332; components 330,1,1; edges 840
n=6: bipartitions 904; components 902,1,1; edges 2520
n=7: bipartitions 2340; components 2338,1,1; edges 6944
n=8: bipartitions 5856; components 5854,1,1; edges 18144
VERIFY_OK oracle_masks=87296 infinite_formula_cases=5
```
These finite computations are independent checks of the instances, **not** a substitute for the preceding proof for every \(n\ge4\). The boundary order \(n=3\) is excluded: the verifier finds twenty valid bipartitions, all isolated under single transfers.

## Relationship to prior work
Foucaud, Maniya, Paul and Pradhan (2025, arXiv:2506.12933) prove the existence of a partition into two locating-dominating sets for the broader class of isolate-free twin-free co-bipartite graphs, which includes \(G_n\). Their statement establishes existence, but does not supply the size-refined census, the near-balance rigidity, the one-transfer component classification or the edge count above. Chakraborty, Foucaud, Henning and Laihonen (2026, arXiv:2610.03131) consider the different asymmetric requirement that only one part locate while the other dominates. Neither existence theorem is asserted here as new. The present graph is also the two-row rook graph \(L(K_{2,n})\); its complement is the crown graph \(K_{n,n}\) with a perfect matching removed. Those graph presentations do not themselves imply the LD partition enumerator or reconfiguration formulas.

## Limitations
The proof concerns ordered partitions into **two** locating-dominating sets of the balanced matched-clique graph \(K_n\square K_2\), for \(n\ge4\), and adjacency by a **single** vertex transfer. It does not classify arbitrary co-bipartite graphs, unordered partitions under graph automorphism, multi-vertex transfer dynamics, or variants requiring code vertices themselves to be located. Computational checks extend only to \(n=8\). Historical priority under alternate locating-code or reconfiguration terminology warrants independent checking; no independent mathematical audit has been performed.

## References
1. F. Foucaud, N. Maniya, S. Paul and S. Pradhan, *Locating-dominating partitions for some classes of graphs*, arXiv:2506.12933 (first posted 2025-06-15). https://arxiv.org/abs/2506.12933
2. A. Chakraborty, F. Foucaud, M. Henning and T. Laihonen, *A note on partitioning the vertex set of a graph into a dominating set and a locating dominating set*, arXiv:2610.03131 (first posted 2026-10-02). https://arxiv.org/abs/2610.03131
