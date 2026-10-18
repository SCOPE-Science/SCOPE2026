# Facet and symmetry classification of the triangular graph transportation ball

## Finding
Let \(G=J(5,2)=L(K_5)\) be the triangular graph on the ten unordered pairs of a five-element set, with adjacency when two pairs intersect. Equip \(G\) with unit-edge shortest-path distance, and let \(B\) be the closed unit ball of its nine-dimensional real Lipschitz-free Banach space. **The ball \(B\) has exactly \(1032\) facets, falling into exactly \(17\) orbits under all graph automorphisms and central inversion.** The facets contain respectively \(12,14,16,18,20\) vertices of \(B\), with multiplicities \(110,300,330,280,12\). The orbit sizes, in descending order, are
\[
120,120,120,120,120,60,60,60,60,40,30,30,30,20,20,12,10.
\]
Exactly \(922\) facet-defining normalized potentials have two levels, and \(110\) have three. **The maximum facet-vertex count is \(20\), attained on exactly \(12\) facets.** Its maximizers are precisely the two-valued potentials defined by decomposing the ten edges of \(K_5\) into two complementary Hamiltonian cycles and assigning levels \(0\) and \(1\) to these two cycles.

## Assumptions and scope
All spaces, functionals, and norms are real. The graph is the unweighted triangular graph, not the Petersen graph \(KG(5,2)\), whose edge relation is complementary. Denote its ordered vertex set by
\[
01,02,03,04,12,13,14,23,24,34,
\]
with digits standing for unordered pairs of \(\{0,1,2,3,4\}\). A normalized facet potential is an integer-valued function \(f\) on these ten vertices satisfying \(\min f=0\) and \(|f(u)-f(v)|\le1\) whenever \(u\) and \(v\) are adjacent. A graph edge is *tight* for \(f\) if its endpoint values differ by exactly one. By the vertex-facet correspondence for the polar Lipschitz ball, facet-defining potentials are exactly those with a connected spanning tight-edge graph. A facet then contains precisely one root vertex \(\pm(\delta_u-\delta_v)\) per tight graph edge. The graph contains \(30\) edges and has diameter \(2\).

## Proof
**Facet criterion and exhaustive scope.** The real free unit ball is the symmetric edge polytope
\[
B=\operatorname{conv}\{\delta_u-\delta_v:(u,v)\in E(G)\text{ oriented}\}.
\]
Its polar is the Lipschitz unit ball modulo constants, determined by \(|f(u)-f(v)|\le1\) on edges. The active constraint normals are the oriented edge incidence vectors; their rank is \(10-c\), where \(c\) is the number of connected components of the spanning tight-edge graph. Consequently a normalized Lipschitz potential defines a vertex of the polar (hence a facet of \(B\)) if and only if the tight graph is connected. If so, a tight spanning tree fixes all values by successive \(\pm1\) differences. After subtracting the minimum, all values are integers. Since \(\operatorname{diam}(G)=2\), they lie in \(\{0,1,2\}\). Conversely every admissible nonconstant member of the finite set \(\{0,1,2\}^{10}\) with connected tight graph is a facet potential. This establishes **exhaustiveness** of the finite verification, not a sampling argument. Every oriented graph-edge root is a vertex of \(B\), because adjacent graph vertices are a distance-one pair with no distinct metric point strictly between them. Thus a facet's number of polytope vertices equals its tight-edge count.

**Exact finite classification.** The standalone pure-Python program `verification.py` examines all \(3^{10}=59049\) integer vectors, selecting those with minimum zero, edge differences bounded by one, and connected tight graph. It derives exactly \(1032\) selected vectors with the stated levels and incidence distributions. An independent decomposition separately enumerates the \(1022\) nonconstant binary words and all disjoint nonempty level-zero/level-two sets with no adjacent cross-pair; after the same exact graph test it finds \(922\) and \(110\) facets, respectively, and confirms set equality with the original enumeration. There are no floating-point tolerances or unexamined vectors. The code also checks all \(120\) vertex relabelings of \(K_5\), their actions on potentials, global sign, orbit disjointness, the full list of representatives and orbit sizes, and the fixed-point sum \(4080=240\cdot17\) from Burnside's lemma.

To see that this is the **full** symmetry group of the graph, note that its five cliques of size four are exactly the five stars of edges incident with each vertex of \(K_5\); a triangular clique in \(K_5\)'s line graph has size at most three. Any graph automorphism therefore permutes these five distinguished cliques. Distinct intersections of two of them recover each graph vertex, giving an injection into \(S_5\). Conversely every ground-set permutation induces an automorphism; hence \(\operatorname{Aut}(G)\cong S_5\). The symmetry on \(B\) considered here is \(S_5\times C_2\), with the last factor central inversion. No assertion is made that this is the entire linear isometry group of \(B\).

**Maximum and equality classification without enumeration.** Every graph edge of \(G\) belongs to exactly one of five four-vertex cliques \(Q_v\) indexed by \(v\in V(K_5)\), comprising all original \(K_5\) edges through \(v\). On each clique the Lipschitz potential has range at most one. Tight pairs can occur only across its minimum and maximum levels, so at most \(\lfloor4^2/4\rfloor=4\) among its six edges can be tight. This yields at most \(5\cdot4=20\) tight edges globally. Equality forces every clique \(Q_v\) to split \(2\)-versus-\(2\) into values separated by one. For a normalized integral facet potential, values \(0\) and \(2\) cannot occur among the same four edges through any \(v\). At equality the edges of \(K_5\) carrying extreme level \(0\) or \(2\) therefore form a degree-two spanning union of cycles, with the \(0\)-edge cycles vertex-disjoint from the \(2\)-edge cycles. If both extreme levels occurred, each class would require at least three ground-set vertices, impossible on five. Hence equality forces a two-level potential. The five edges at each level form complementary two-regular spanning subgraphs of \(K_5\), necessarily Hamiltonian five-cycles. There are exactly \((5-1)!/2=12\) such choices; every choice yields an admissible potential with a connected tight graph and \(20\) tight edges. This proves the sharp maximum and characterizes all equality cases.

**Explicit orbit representatives.** Read each ten-digit word in the vertex order fixed above. Each row is the tuple (orbit size, facet vertices, number of height levels, normalized potential):

| Orbit size | Facet vertices | Levels | Potential |
|---:|---:|---:|---|
| 120 | 14 | 2 | `0000001101` |
| 120 | 14 | 2 | `0000001111` |
| 120 | 16 | 2 | `0001001101` |
| 120 | 18 | 2 | `0001010110` |
| 120 | 18 | 2 | `0001011110` |
| 60 | 14 | 2 | `0000011111` |
| 60 | 16 | 2 | `0001001100` |
| 60 | 16 | 2 | `0001010111` |
| 60 | 16 | 3 | `0011111112` |
| 40 | 12 | 2 | `0000001011` |
| 30 | 12 | 2 | `0000001100` |
| 30 | 12 | 3 | `0111111112` |
| 30 | 16 | 2 | `0000011110` |
| 20 | 18 | 2 | `0001110100` |
| 20 | 18 | 3 | `0011011112` |
| 12 | 20 | 2 | `0011101100` |
| 10 | 12 | 2 | `0000111111` |

## Verification
Run `python3 verification.py` using Python 3.9 or newer and the standard library. The program recomputes the edge set and checks the complete normalized ternary grid, independently reconstructs binary and ternary subfamilies, verifies every symmetry orbit and Burnside sum, and checks the Hamiltonian-cycle equality classification. Successful execution prints `ALL EXACT CHECKS PASSED` and detailed data. All computations are finite and exact, and their exhaustiveness follows from the preceding integer-height proof. The analytic sharp \(20\)-vertex upper bound does not depend on the enumeration.

## Relationship to prior work
D'Alì–Delucchi–Michałek (arXiv:1910.05193, 2019) identify symmetric edge polytopes with graph transportation balls and give the connected-tight-subgraph facet criterion as Theorem 3.1; that **criterion is prior work**, not a new claim here. Chen–Davis–Korchevskaia (arXiv:2107.12315, 2021) further describe facet-subgraph fibers for general connected graphs. Their statements do not enumerate the exact \(17\) signed automorphism orbits, the \(1032\) specific facets, the incidence spectrum, or the sharp complementary-Hamiltonian-cycle equality classification for \(J(5,2)\). Aliaga (arXiv:2102.01219, 2021) treats the extreme-point structure of Lipschitz-free spaces at a general level, rather than this finite graph's facets. The present contribution is an **evaluated exact classification** and a sharp explicit extremal characterization, not a claimed invention of the general facet criterion. An unpublished or unindexed database could contain the numerical count without the orbit theorem.

## Limitations
The result concerns exactly the real free space over the ten-vertex graph \(J(5,2)\). It gives no closed formula for the corresponding invariants of \(J(n,2)\) for arbitrary \(n\), no classification of all face dimensions, and no assertion about the full Banach-space linear isometry group. The combinatorial enumeration is exhaustive for this finite input but not evidence of an infinite-family theorem. No external independent audit is asserted.

## References
- A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first posted 2019-10-11), especially Theorem 3.1 and §2.3. https://arxiv.org/abs/1910.05193
- T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first posted 2021-07-26), especially Theorems 3 and 9. https://arxiv.org/abs/2107.12315
- R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first posted 2021-02-01), primary MSC 46B20. https://arxiv.org/abs/2102.01219
