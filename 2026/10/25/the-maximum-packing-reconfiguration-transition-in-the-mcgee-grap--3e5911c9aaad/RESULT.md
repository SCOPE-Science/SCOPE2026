# The maximum-packing reconfiguration transition in the McGee graph

## Finding
Let \(G\) be the canonical 24-vertex McGee graph, the unique cubic graph of girth seven. For \(k\in\{9,10\}\), let \(\mathrm{TJ}_k(G)\) (respectively \(\mathrm{TS}_k(G)\)) be the graph of independent \(k\)-vertex sets, adjacent when exactly one selected vertex can be replaced by an arbitrary unselected vertex (respectively, by a neighboring unselected vertex) while maintaining independence.

The graph has independence number \(\alpha(G)=10\). The two highest nonempty configuration layers have the following **complete connectivity transition**:

* \(\mathrm{TJ}_9(G)\) has exactly 424 vertices and 1,428 edges, is connected, has radius 9 and diameter 11. Its eccentricity counts are 32 vertices of eccentricity 9, 368 of eccentricity 10, and 24 of eccentricity 11.
* \(\mathrm{TS}_9(G)\) has the same 424 vertices and 1,068 edges but splits into a 416-vertex component and four separate two-vertex components. The large component has radius 10 and diameter 11.
* At the maximum packing cardinality, \(\mathrm{TJ}_{10}(G)=\mathrm{TS}_{10}(G)\cong C_4\sqcup C_4\). These have eight vertices and eight edges, with two connected components of four vertices each.

Thus permitting unrestricted token jumps restores connectivity at nine selected vertices, but **even unrestricted jumps cannot connect all maximum independent sets**. The eight maximum configurations are non-rigid individually: each has two legal moves, yet their state space splits into two cycles.

## Assumptions and scope
The vertex set is \(\{0,1,\ldots,23\}\), with arithmetic modulo 24. Include the 24 cycle edges \(\{i,i+1\}\). Also include the unordered chord \(\{i,i+s_i\}\) for every \(i\), where \((s_i)\) is the sequence \((12,7,-7)\) repeated eight times. Repeated representations of one chord are identified. This gives 36 edges and three neighbors at every vertex; it is the standard McGee LCF model. A subset is *independent* if it contains no edge. Configurations in all graphs are vertex-labelled sets (not symmetry classes). A token jump replaces any one chosen vertex with any one unchosen vertex; a token slide further requires those two vertices to be adjacent in \(G\). A legal move must end at another independent set of the same cardinality.

## Proof
**Exhaustive finite certificate with complete search domains.** The program `verify_a.py` recursively processes vertices 0 through 23. At each vertex it first omits that vertex and then includes it precisely when it has no already selected neighbor. By induction on the processed prefix, this binary recursion produces every independent set *exactly once*. Its counts by cardinality zero through ten are
\[
(1,24,240,1304,4212,8328,10024,7072,2668,424,8),
\]
with no independent set of cardinality greater than ten. In particular \(\alpha(G)=10\), and the layers of interest contain precisely 424 and eight configurations.

For each \(k\in\{9,10\}\), the program constructs the full legal move graph by considering, from every independent \(k\)-set, **every ordered pair** consisting of one chosen vertex and one unchosen vertex, checking whether their exchange appears in the complete independent-set lookup table; it additionally tests whether the removed and inserted vertices are adjacent when constructing \(\mathrm{TS}_k\). The reverse move must also appear, and the program asserts graph symmetry. Breadth-first traversal from every configuration identifies connected components and all shortest-path distances. It yields exactly the connected-component sizes and eccentricity distributions stated above. At \(k=10\), every state has degree two, and both components have four vertices. A finite simple connected 2-regular graph on four vertices is \(C_4\), establishing the asserted isomorphism.

The independent program `verify_b.py` enumerates all \(\binom{24}{9}\) and \(\binom{24}{10}\) subsets directly using combinations and checks each of the 36 edge masks for inclusion. It proves maximality by checking that every one of the eight independent ten-sets has a chosen neighbor at each omitted vertex: an independent eleven-set would contain a ten-set that could be extended, which is impossible. Rather than simulating moves from each state, it compares **every unordered pair of configurations**, connecting a pair if its symmetric difference has cardinality two and, for token sliding, if that difference is a graph edge. Its independently constructed graphs reproduce every reported component size and distance distribution. Since both enumerations are exhaustive, the conclusion is a finite proof, not extrapolation from sampled configurations.

## Verification
Run `python3 verify_a.py` and `python3 verify_b.py` using Python 3 and the standard library. Their saved outputs are included as `verify_a.out` and `verify_b.out`. Both programs were executed after the package files were written; the outputs report all assertions passed. In the first checker, the degree distributions provide additional complete edge-incidence verification. In the second, the test of all combinations and all pairs avoids reusing the first checker’s independent-set and adjacency enumeration methods.

## Relationship to prior work
McGee's original 1960 article defines the cubic girth-seven extremal graph; the uniqueness and standard 24-vertex LCF model are classical. The 2014 paper by Bonsma, Kamiński, and Wrochna defines the token-slide and token-jump rules and proves that at maximum independence size these two state graphs coincide for **every** graph. That general proposition explains the equality at cardinality ten, but not the split into two cycles or the connectivity difference at cardinality nine. Their more specialized claw-free connectivity arguments do not apply to this cubic graph: every vertex and its independent three-neighbor set induce a claw, because the girth is seven.

A separately published computation, *The McGee graph independence complex is a five-sphere* (2026), determines the complete independence-set size distribution, including the 424 nine-sets and eight ten-sets. The **counts are not claimed as new here**; that result does not determine either token-move graph, their components, or their diameters. The new assertion concerns the exact structure of the two reconfiguration models at the packing boundary.

## Limitations
The theorem is exact for the specified McGee graph and for token jumping and token sliding at cardinalities 9 and 10. It makes no assertion about arbitrary cages or other cardinalities. The exhaustive argument is feasible because the graph has only 24 vertices; it does not imply a uniform polynomial-time procedure for larger graphs. The literature comparison does not rule out an equivalent unindexed tabulation. The checking and scientific review are not an independent expert audit.

## References
1. W. F. McGee, *A Minimal Cubic Graph of Girth Seven*, Canadian Mathematical Bulletin 3 (1960), 149–152, doi:10.4153/CMB-1960-018-1 (issue date 1960-05-01). https://doi.org/10.4153/CMB-1960-018-1
2. P. Bonsma, M. Kamiński, and M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359 (submitted 2014-03-03), Introduction and Proposition 1. https://arxiv.org/abs/1403.0359
3. *The McGee graph independence complex is a five-sphere*, publicly available mathematical result (2026-10-11), result identifier `5daca7995d97`. This source supplies the previously established independence-set size vector, but no token-move analysis.
