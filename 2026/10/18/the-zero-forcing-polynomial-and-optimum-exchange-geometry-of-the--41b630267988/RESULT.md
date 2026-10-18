# The zero-forcing polynomial and optimum exchange geometry of the Desargues graph

## Finding

Let \(D\) be the bipartite Kneser graph \(H(5,2)\): its vertices are the two-element and three-element subsets of \(\{0,1,2,3,4\}\), and a two-element set is adjacent to a three-element set precisely when it is contained in the latter. Define \(z_k(D)\) to be the number of ordinary zero-forcing vertex sets of cardinality \(k\), and set \(Z_D(t)=\sum_{k=0}^{20}z_k(D)t^k\). The complete enumerator is

\[
\begin{aligned}
Z_D(t)={}&13520t^{8}+53160t^{9}+99652t^{10}+120840t^{11}\\
&+106540t^{12}+71680t^{13}+37540t^{14}+15344t^{15}\\
&+4835t^{16}+1140t^{17}+190t^{18}+20t^{19}+t^{20}.
\end{aligned}
\]

The minimum forcing-set count \(13520\), the minimum size \(8\), their exact four-from-each-shore balance and their \(67\) permutation/duality orbits had already been determined. These prerequisite quantities are not claimed as new here.

Let \(\mathcal J(D)\) have as vertices those \(13520\) minimum ordinary zero-forcing sets, with two joined precisely when one can be obtained from the other by deleting one selected vertex and adding one previously unselected vertex. Then

\[
|E(\mathcal J(D))|=178560,\qquad
\operatorname{rad}(\mathcal J(D))=7,\qquad
\operatorname{diam}(\mathcal J(D))=8.
\]

The graph \(\mathcal J(D)\) is connected, and its exact eccentricity spectrum is \(980\) configurations of eccentricity \(7\) and \(12540\) of eccentricity \(8\). Under the natural \(240\)-element action arising from permutations of the ground set and complementation, the \(980\) central configurations constitute six orbits of sizes \(20,120,120,240,240,240\). This eccentricity result and the complete polynomial are the retained contributions. The known shore balance also implies, as a corollary rather than a new independent result, that the token-sliding reconfiguration graph of minimum sets has no edges.

## Assumptions and scope

All graphs are finite and simple. Ordinary zero forcing starts with a chosen set of blue vertices; a blue vertex having exactly one white neighbor may change that neighbor to blue. A seed set is zero forcing if repeated legal applications can make all vertices blue. Token jumping means exchanging any one selected vertex for any one unselected vertex. Token sliding additionally requires those two vertices to be adjacent in the base graph. Distances, radius, diameter and eccentricities are measured in the minimum-set jumping reconfiguration graph, not in the base graph. All counts refer to labeled subsets of the explicitly defined twenty-vertex graph, not to isomorphism classes.

## Proof

**Exact seed classification and polynomial.** Index the vertices by increasing numerical order of their five-bit incidence masks among those having Hamming weight two or three. Thus the base graph has twenty vertices, thirty edges and degree three. For a black-vertex mask \(B\), define \(T(B)\) by adjoining every white vertex that is the unique white neighbor of some black vertex. This operator is monotone: for \(B\subseteq C\), a force available from \(B\) is either already in \(C\) or remains available from \(C\). Iteration reaches the least fixed point in at most twenty strict increases. That fixed point equals all twenty vertices exactly when the initial set is zero forcing. A sequential rule that repeatedly applies any available force has the same final closure, as can also be deduced from monotonicity.

Enumerating every integer mask from \(0\) through \(2^{20}-1\) with this exact rule, and accumulating the coefficient at the mask's Hamming weight, yields the displayed degree-eight-through-twenty coefficients and zeros at degrees zero through seven. The total number of successful masks is \(524462\); in particular there are \(13520\) successful eight-masks, all with four vertices in each bipartition shore. These outputs are reproduced by two independently programmed implementations: one uses simultaneous closure in Python and one uses one force at a time in C++17. Both enumerate all \(1048576\) masks.

**Exchange graph.** For each successful eight-mask \(B\), examine every one of its eight occupied vertices and every one of its twelve unoccupied vertices. An exchange gives a graph edge if and only if the changed mask is in the complete successful-eight-mask lookup. Retaining each unordered edge once gives exactly \(178560\) edges. The degree-count distribution (degree:number of configurations) is

\[
(20:240),(21:120),(22:360),(23:480),(24:1340),(25:1800),
(26:3000),(27:240),(28:4380),(29:480),(30:960),(32:120).
\]

Permuting the five ground elements and optionally complementing every two- or three-element subset induces an explicit group of \(240\) graph automorphisms. Each automorphism carries a forcing mask to another forcing mask and preserves the single-exchange adjacency relation. The action partitions all \(13520\) minima into exactly \(67\) verified orbits: one of size \(20\), one of size \(60\), eighteen of size \(120\), and forty-seven of size \(240\). These previously determined orbit counts are independently reconstructed, but not asserted as a separate discovery.

For the lexicographically first bitmask in every one of the \(67\) orbits, breadth-first search in the complete exchange graph visits all \(13520\) masks. Its eccentricity is either \(7\) or \(8\). Since an automorphism transports shortest paths, eccentricity is constant on each orbit. Exactly six orbit representatives have eccentricity \(7\), with orbit sizes \(20,120,120,240,240,240\); the other sixty-one orbit representatives have eccentricity \(8\). This certifies connectedness, radius \(7\), diameter \(8\), and the full eccentricity spectrum. The supplied finite certificate records every successful minimum mask, every jumping edge and the complete breadth-first distance histogram for each orbit representative.

Finally, any slide in a bipartite base graph removes one occupied vertex from one shore and inserts one in the other shore. It cannot preserve the already established four-plus-four shore balance of all minimum zero-forcing sets. Hence there is no legal minimum token slide. This is a direct consequence of the earlier balance classification.

## Verification

Run `python3 verify_python.py certificate_python.tsv` and compile and run `verify_cpp.cpp` with a C++17 compiler, for example `g++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp` followed by `./verify_cpp certificate_cpp.tsv`. Compare the two ASCII outputs byte for byte with the included `certificate.tsv`. The independent implementations produce exactly the same \(2611589\)-byte certificate, with SHA-256 `5ad851a4887bdc203f66f1e52abd7c8a0fa879ff9273a9382ed373a1c145ef01`. Their recorded standard outputs are included for convenience, but the programs and certificate—not the logs alone—are the verification evidence.

The certificate begins with the full coefficient vector, followed by all successful minimum masks (`S`), all unordered exchange pairs (`E`), and for each orbit its representative mask, orbit size, eccentricity and full distance histogram (`O`). Each mask uses the bit indexing defined above. Regeneration does not depend on any external graph library or other dataset.

## Relationship to prior work

Butler, Grout and Hall (2012) already report the ordinary zero-forcing number \(8\) for the Desargues graph and use it in the inertia-set problem. Their preprint examines several zero-forcing variants but does not state the complete ordinary forcing polynomial or the minimum-set exchange distances. Geneson, Haas and Hogben (2020) define minimum zero-forcing-set token jumping and establish general structural results and examples, but their inspected preprint does not state the present Desargues-graph classification. Separately, the previously known count, four-plus-four balance and \(67\) symmetry orbits for the minimum sets are expressly excluded from the new contribution. In particular, the conclusion that minimum token sliding is frozen follows immediately from that known balance and is not asserted as original. The new information is the full forcing-set size distribution together with the exact jumping exchange graph and its metric center.

## Limitations

This is a theorem about one finite graph, not a statement for all bipartite Kneser graphs or generalized Petersen graphs. It relies on complete finite enumeration and breadth-first distances, with the loops and finite domains given explicitly; it is not a purely symbolic classification valid in arbitrary order. The orbit grouping uses a verified set of \(240\) automorphisms; proving it is the full automorphism group is unnecessary for the metric argument. Searches did not establish publication priority, and unindexed tables, other graph-library computations or supplementary calculations could duplicate some coefficients or distances. Independent external mathematical audit has not been performed.

## References

1. Steve Butler, Jason Grout, H. Tracy Hall, *Zero forcing for inertia sets*, arXiv:1211.4618v1, first posted 2012-11-19. https://arxiv.org/abs/1211.4618
2. Jesse Geneson, Ruth Haas, Leslie Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1, first posted 2020-09-01. https://arxiv.org/abs/2009.00220
3. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648, DOI:10.1016/j.laa.2007.10.009.
