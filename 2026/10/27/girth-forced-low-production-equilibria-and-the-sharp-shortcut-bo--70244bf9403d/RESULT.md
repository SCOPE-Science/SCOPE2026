# Girth-forced low-production equilibria and the sharp shortcut boundary

## Finding
Let \(G=(V,E)\) be any finite simple undirected graph with at least one cycle and girth \(g\ge5\). Consider the fully homogeneous strict binary network public-goods game in which each vertex \(v\) chooses \(s_v\in\{0,1\}\) and its unique best response is
\[
s_v=1\quad\Longleftrightarrow\quad\sum_{u\sim v}s_u=2.
\]
Define the producer enumerator and ordinary simple-cycle counts by
\[
E_G(z)=\sum_{s\text{ a pure Nash equilibrium}} z^{\sum_{v\in V}s_v},
\qquad
c_k(G)=\#\{\text{unoriented simple cycles of length }k\text{ in }G\}.
\]
Then the **low-production cycle identity** is
\[
[z^0]E_G(z)=1,\qquad [z^k]E_G(z)=c_k(G)
\quad(1\le k<2g-4).
\]
In particular, the smallest positive producer count in a pure Nash equilibrium is exactly \(g\), and its multiplicity is \(c_g(G)\). The length cutoff is sharp uniformly over girths: for every integer \(g\ge5\), a graph of girth \(g\) has \(c_{2g-4}=1\) but \([z^{2g-4}]E_G=0\).

## Assumptions and scope
The graph is finite, undirected, loopless, and without multiple edges; it need not be connected or regular. It has a finite shortest cycle of length \(g\ge5\), but may also contain trees or isolated vertices. The best-response pattern is \(T(j)=1\) exactly for \(j=2\), and \(T(j)=0\) otherwise, with \(j\) counting **other** producers adjacent to the vertex. This is not the different pattern \(T(0)=T(2)=1\). Equilibrium means every vertex is playing its unique best response simultaneously; no dynamics or welfare interpretation is assumed. Cycle count \(c_k\) counts an undirected simple cycle once (not once per orientation or base point). All exponents are integer producer counts.

## Proof
**1. Structure of an arbitrary equilibrium.** For an equilibrium \(s\) put \(S=\{v\in V:s_v=1\}\). Every vertex of \(S\) has exactly two neighbors within \(S\), so \(G[S]\) is \(2\)-regular, hence is a vertex-disjoint union of cycles if nonempty. Every component contains at least \(g\) vertices. Consequently there is no nonempty equilibrium with fewer than \(g\) producers; and whenever \(0<|S|<2g\), the induced subgraph \(G[S]\) must be one cycle. Conversely, a nonempty set whose induced graph is one cycle yields an equilibrium precisely when no external vertex has exactly two neighbors on that cycle. The empty set is an equilibrium because \(T(0)=0\).

**2. Every sufficiently short cycle yields an equilibrium.** Let \(C\) be a simple cycle of length \(k<2g-4\). It cannot have a chord: a chord divides it into two cycles of lengths \(a+1\) and \(k-a+1\), both at least \(g\), forcing \(k\ge2g-2\), a contradiction. Nor can a vertex outside \(C\) be adjacent to two distinct vertices on \(C\): the two arcs between those attachment vertices, together with the two-edge path through the outside vertex, form cycles of lengths \(a+2\) and \(k-a+2\), both at least \(g\), forcing \(k\ge2g-4\), a contradiction. Thus each vertex of \(C\) has exactly two producing neighbors, and each vertex outside \(C\) has at most one. The strategy with producers exactly \(V(C)\) is an equilibrium.

**3. Bijection below the cutoff.** If an equilibrium has \(1\le k<2g-4\) producers, then \(k<2g\), so by Step 1 its support induces a single simple \(k\)-cycle. Step 2 gives the converse for every such cycle. Distinct cycles in this range cannot share the same entire vertex set, since each is chordless and its induced subgraph is exactly that cycle. Hence support is a bijective correspondence, proving \([z^k]E_G(z)=c_k(G)\). A shortest cycle exists and has length \(g<2g-4\) because \(g>4\), proving the minimum and its multiplicity.

**4. Sharpness.** For each \(g\ge5\), let \(\Theta_g\) consist of three internally vertex-disjoint paths between two terminals, of edge lengths \(g-2\), \(g-2\), and \(2\). Its only simple cycles have lengths \(g,g,2g-4\), so its girth is \(g\) and \(c_{2g-4}(\Theta_g)=1\). The unique length-\(2g-4\) cycle is formed by the two long terminal paths. The internal vertex of the length-\(2\) path lies outside this cycle and has exactly two producing neighbors, so that cycle's vertex set does **not** form an equilibrium. Any equilibrium with \(2g-4<2g\) producers would have to induce a single cycle by Step 1. There is no alternative cycle of that length. Therefore \([z^{2g-4}]E_{\Theta_g}(z)=0\), establishing sharpness.

## Verification
The self-contained program `verify.py` uses two independent finite enumerations: it checks each strategy profile against all local exact-two best responses, and counts undirected simple cycles by vertex-distinct depth-first search with a canonical least starting vertex. It compares the resulting low-support coefficients for cycles of lengths \(5\) through \(13\), the Petersen and Heawood graphs, and five sharpness examples \(\Theta_g\) for \(5\le g\le9\). The program completed with all \(16\) graph instances passing and confirmed \(12\) minimum-producer equilibria on the Petersen graph and \(28\) on the Heawood graph. These are finite consistency checks; the proof above, rather than enumeration, establishes the universal quantified claim.

Run with `python3 verify.py` using only the Python standard library. All input graph constructions are included in that file.

## Relationship to prior work
Gilboa and Nisan (2022) introduce and analyze homogeneous strict binary public-goods best-response patterns and prove complexity results, notably for the exactly-one-neighbor response. Gilboa (2023) gives the broader complexity classification for finite nonmonotone patterns. Klimm and Stahlberg (2023) analyze nonmonotone equilibrium complexity and describe active sets for a different pattern allowing production with zero or a specified positive number of active neighbors. The present result addresses the exact-two-only pattern \(T(j)=\mathbf1_{j=2}\), and determines a **graph-family-wide initial segment of its equilibrium producer-count polynomial**, the least positive count, its multiplicity, and the exact universal cutoff. The general complexity classifications do not themselves state these quantities or imply the cutoff without a separate graph-theoretic argument. The cycle/chord argument uses standard girth facts; no novelty is claimed for those elementary facts in isolation.

## Limitations
The equality is claimed only for \(k<2g-4\); higher producer counts may include unions of cycles and may fail to correspond to simple-cycle counts. The sharpness family shows why the bound cannot be increased for arbitrary graphs of fixed girth. Forests have no nonempty equilibrium for this pattern because the nonempty producer subgraph would have to contain a cycle; they are excluded from the finite-girth statement. The result does not characterize all equilibria at larger supports, welfare, or adjustment dynamics. Equivalent formulations in graph-theoretic fixed-point literature may exist; the originality comparison is not an exhaustive uniqueness proof.

## References
1. Matan Gilboa and Noam Nisan, *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238, first public submission July 9, 2022, https://arxiv.org/abs/2207.04238.
2. Matan Gilboa, *A Characterization of Complexity in Public Goods Games*, arXiv:2301.11580, first public submission January 27, 2023, https://arxiv.org/abs/2301.11580.
3. Max Klimm and Maximilian J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849, first public submission January 27, 2023, https://arxiv.org/abs/2301.11849.
