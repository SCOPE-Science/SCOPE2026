# Complete labeled vertex-switching metric for eight-team one-factorizations

## Finding

Let \(V=\{0,1,\ldots,7\}\). A *one-factorization* is an unordered partition of the \(28\) edges of \(K_8\) into seven perfect matchings; vertex labels remain fixed, while permuting matchings has no effect. Define \(\mathcal R\) on all such one-factorizations by one nontrivial *vertex-switch*, defined precisely below. Then \(\mathcal R\) has \(6{,}240\) vertices, is connected, has \(66{,}360\) edges, and has radius \(5\) and diameter \(6\). Its degree distribution is

\[
\#\{F:\deg_{\mathcal R}(F)=d\}=
\begin{cases}
420&d=9,\\960&d=14,\\30&d=21,\\4200&d=23,\\630&d=29,\\0&\text{otherwise.}
\end{cases}
\]

Moreover, the eccentricity distribution is \(5^{5790},6^{450}\), and all distance distributions are determined by the six isomorphism orbits in the following table. Each vector lists counts at distances \(0,1,\ldots,\operatorname{ecc}\) from any vertex in that orbit.

| Orbit size | Degree | Eccentricity | Distance distribution |
| ---: | ---: | ---: | --- |
| 30 | 21 | 6 | (1,21,203,959,3164,1828,64) |
| 420 | 9 | 6 | (1,9,155,1499,3880,680,16) |
| 630 | 29 | 5 | (1,29,303,2607,3112,188) |
| 960 | 14 | 5 | (1,14,280,2548,3353,44) |
| 1,680 | 23 | 5 | (1,23,355,3000,2800,61) |
| 2,520 | 23 | 5 | (1,23,369,2787,2978,82) |

In particular, \(960\) vertex-labeled perfect one-factorizations, which permit no nontrivial *factor*-switch, each admit exactly fourteen distinct *vertex*-switch neighbors.

## Assumptions and scope

All objects are finite and simple; factors are unordered and the eight vertices are labeled. For \(F\) and an unordered pair \(\{a,b\}\subset V\), let \(f\) denote the unique matching containing \(ab\). Form a bipartite graph \(B(F;a,b)\) whose parts are \(V\setminus\{a,b\}\) and the six matchings \(F\setminus\{f\}\). Connect \(z\) to the two matchings containing \(az\) and \(bz\). This is a \(2\)-regular bipartite graph. If it has at least two connected components, choose a **single** component \(C\) and, for every \(z\in C\cap V\), interchange the factor membership of edges \(az\) and \(bz\). These simultaneous swaps preserve the one-factorization property. Join \(F\) to the result if it is distinct. Choosing a component when \(B\) is connected is **excluded**, following the nontrivial-vertex-switch convention of Kaski et al. Repeated choices producing the same unordered resulting factorization create only one graph edge. No permutation of vertex labels is quotiented out when deciding equality of states.

A proper seven-edge-coloring of \(K_8\) modulo global color permutation is equivalently an unordered one-factorization, but is **not** the same as a one-factorization up to vertex relabeling.

## Proof

The following finite algorithm exhausts the entire domain and constitutes a reproducible exhaustive proof of the displayed numerical claims. Its two independently implemented forms are attached as `check_matching.py` and `check_coloring.py`; each uses exact integer operations and no sampling.

**Exhaustive state generation.** There are \(105\) perfect matchings of \(K_8\). The first algorithm constructs each recursively by pairing the least remaining vertex with every possible partner. Represent matchings as \(28\)-bit masks. To generate an unordered partition into seven matchings, take the first uncovered edge and recurse over **every** perfect matching containing that edge and disjoint from previously chosen factors. This creates every factorization: the factor containing the first uncovered edge is forced, so at each stage the search loses no possibilities and cannot generate a second ordering of the same set of factors. Sorting the resulting seven mask indices canonicalizes the state. The algorithm yields exactly \(6{,}240\) different states. The second implementation independently backtracks through proper color assignments while fixing the seven colors incident to vertex zero, which canonically removes global color renamings, and also yields \(6{,}240\) states.

**Exhaustive edges.** For every state and all \(\binom82=28\) unordered pairs \(\{a,b\}\), each implementation builds the described \(2\)-regular bipartite auxiliary graph. The partition of its six non-anchor vertices has precisely the following patterns, counted over all state–anchor-pair choices:

| Component sizes on the non-anchor side | Count |
| --- | ---: |
| (2,2,2) | 23,520 |
| (2,4) | 70,560 |
| (3,3) | 13,440 |
| (6) | 67,200 |

The counts sum to \(6{,}240\cdot28=174{,}720\). Every proper connected component is individually switched; every result is canonicalized as an unordered set of matchings, and duplicate targets are removed. The adjacency relation is verified symmetric. The resulting degree histogram gives \(2|E|=132{,}720\), hence \(|E|=66{,}360\).

**All-pairs metric from symmetry.** Every permutation of the eight vertex labels preserves the defined move and hence acts by graph automorphisms. The matching-based checker explicitly enumerates all \(8!=40{,}320\) permutations of the edge coordinates. Applying all of them to representatives, with canonical matching and factor sorting, partitions the \(6{,}240\) states into exactly six orbits, with sizes \(30,420,630,960,1680,2520\). They sum to the entire state space, and no unassigned states remain. Breadth-first search from one representative of **each** orbit visits all \(6{,}240\) vertices and yields the six exact distance distributions displayed above. Vertex-label permutations preserve every distance, so the distributions apply to every state. Connectedness follows from the first such complete BFS; the largest representative eccentricity is \(6\), the smallest is \(5\), giving diameter \(6\) and radius \(5\). The second, edge-coloring-based checker reconstructs the adjacency graph independently and obtains the same six distance distributions by its own invariant grouping.

**Frozen factor-switch distinction.** In the 960-state orbit of degree fourteen, every pair of factors has a single alternating eight-cycle, hence a factor-switch cannot act nontrivially. Nevertheless, the independently computed vertex-switch degree there is fourteen. Thus the extra mobility is not a consequence of mere factor switching.

## Verification

Run `python3 check_matching.py` and `python3 check_coloring.py` using Python 3 with the standard library. Expected complete transcripts appear in `matching_output.txt` and `coloring_output.txt`. Both scripts end in `VERIFY_OK`, enumerate all \(6{,}240\) configurations and \(66{,}360\) undirected edges, report one connected component, and independently reproduce the degree histogram, six representative eccentricities, and distance vectors. The matching-based checker additionally computes the complete permutation-orbit partition rather than assuming a historical classification. Its finite exhaustive enumeration is the basis for the theorem; merely inspecting the recorded output without running or reading the algorithms is insufficient.

## Relationship to prior work

Kaski, de Souza Medeiros, Östergård and Wanless [1] introduced the precise vertex-switch operation and tabulated switching graphs **whose vertices are isomorphism classes under vertex relabeling**, including the connected six-class quotient for \(K_8\) (Sections 1, 3, 5, 6 and Table 1). Their quotient has six vertices, not the \(6{,}240\) fixed-label states studied here. A connected quotient graph does not imply that its labeled covering/reconfiguration graph is connected, nor does it determine the labeled degrees or distances. The already known six-isomorphism-class census is credited, not asserted as a new contribution. Factor-switching is another operation from [1]; its subgraph is insufficient to prove this theorem, as it leaves the 960 perfect factorizations isolated. The contribution here is the **full fixed-label vertex-switching metric**, not the existence or definition of vertex switching and not a recount of the isomorphism classes.

## Limitations

This is an exact finite classification for \(K_8\) only. It does not prove a bounded diameter or connectivity at higher orders, nor address multi-component simultaneous switches. The numerical proof relies on exhaustive executable enumeration and is not an independent formal-machine or externally audited certificate. Exhaustive checks distinguish this precisely defined labeled graph from the earlier isomorphism quotient, but cannot exclude an equivalent result hidden in unpublished or differently indexed computations.

## References

[1] P. Kaski, A. de Souza Medeiros, P. R. J. Östergård, I. M. Wanless, *Switching in One-Factorisations of Complete Graphs*, Electronic Journal of Combinatorics 21(2) (2014), #P2.49, first published 2014-06-09, doi:10.37236/3606. Public full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p49/pdf/ .
