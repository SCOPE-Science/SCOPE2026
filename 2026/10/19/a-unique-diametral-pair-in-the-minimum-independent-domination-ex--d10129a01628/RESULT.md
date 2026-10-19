# A unique diametral pair in the minimum independent-domination exchange graph of the McGee cage

## Finding
Let \(G\) be the 24-vertex McGee graph, the unique cubic graph of girth seven on the minimum possible number of vertices. Let \(\mathcal I\) be its family of *minimum independent dominating sets*: independent vertex sets that dominate every vertex and have the smallest possible cardinality. Join distinct \(S,T\in\mathcal I\) when \(|S\setminus T|=|T\setminus S|=1\). Then:

1. The independent domination number is \(i(G)=8\), and \(|\mathcal I|=146\). More completely, the numbers of all inclusion-maximal independent sets of sizes eight, nine, and ten are respectively \(146,352,8\), with none at other sizes.
2. The exchange graph \(\mathcal R\) of \(\mathcal I\) is connected, has \(146\) vertices and \(216\) edges, and has degree multiplicities \(2:64,\ 3:48,\ 4:16,\ 5:16,\ 8:2\). It has no triangles.
3. Its radius is \(11\), its diameter is \(12\), and exactly two vertices have eccentricity \(12\); all other \(144\) vertices have eccentricity \(11\). There is **exactly one unordered pair of vertices at distance twelve**.
4. Under the full automorphism group of the McGee graph (of order \(32\)), these \(146\) optima form seven orbits of sizes \(2,16,16,16,32,32,32\). The two exceptional optima are precisely the orbit of size two.

Under the Hamiltonian LCF vertex numbering specified below, the unique diametral pair is
\[
A=\{1,4,7,10,13,16,19,22\},\qquad
B=\{2,5,8,11,14,17,20,23\}.
\]
Thus \(d_{\mathcal R}(A,B)=12\), and every other unordered pair of minimum independent dominating sets is at distance at most eleven. Whether exchanges are defined as token jumps or token slides makes no difference here.

## Assumptions and scope
The labelled graph has vertices \(\{0,1,\ldots,23\}\) and the 24 cyclic edges \(\{j,j+1\pmod {24}\}\), plus chords \(\{j,j+s_j\pmod {24}\}\), where the integer sequence \((s_j)\) consists of eight repetitions of \((-12,7,-7)\). Duplicate undirected chords are counted once. This is the standard LCF representation of the McGee graph. The explicit adjacency has \(36\) edges, degree three at every vertex, and girth seven.

A subset \(S\) is independent if no edge has both endpoints in \(S\), and dominating if for each vertex \(v\), either \(v\in S\) or \(v\) is adjacent to some member of \(S\). Independent dominating sets are exactly the inclusion-maximal independent sets. The exchange graph in the finding retains only minimum-cardinality independent dominating sets and does not permit intermediate non-optimal states. All counts refer to individually labelled vertex subsets, not graph-symmetry classes.

## Proof
For each vertex \(v\), let \(N(v)\) be its three-neighbor bit mask, and represent every subset by a 24-bit integer \(m\). The following exact predicates decide the defining conditions:
\[
\operatorname{ind}(m)\iff \bigwedge_{v\in m}\bigl(N(v)\cap m=\varnothing\bigr),
\qquad
\operatorname{dom}(m)\iff m\cup\bigcup_{v\in m}N(v)=V(G).
\]

There are two independent, exhaustive paths to the numerical certificate. In `enumerate_mcgee.py`, a binary include/exclude recursion processes every vertex, discarding a branch that would place adjacent vertices in the chosen set. By induction on the processed prefix, the leaves are **all** independent sets without repetition. This gives the complete independent-set size sequence, for sizes zero through ten,
\[
(1,24,240,1304,4212,8328,10024,7072,2668,424,8).
\]
Applying the domination predicate to every leaf gives precisely \(146\) maximal independent sets of size eight, \(352\) of size nine, and \(8\) of size ten. In `verify_mcgee.cpp`, a separate C++17 program tests every integer mask in \(\{0,\ldots,2^{24}-1\}\) directly using adjacency-bit tests and a union-of-closed-neighborhoods test, rather than the independent-set recursion. Its exact totals agree, and it finds no independent dominating set of size below eight. The Python and C++ searches are exhaustive finite proofs of the assertions about \(i(G)\) and all minimum sets, not randomized tests or incomplete searches.

Order the 146 minimum-set bit masks increasingly. Two such masks give an exchange edge exactly when their symmetric difference has two vertices, one removed and one added. An elementary observation shows that an exchange preserving *independent domination* is necessarily a slide along an edge: for \(S'=(S\setminus\{a\})\cup\{b\}\), domination of \(S\) gives \(N(b)\cap S\ne\varnothing\) because \(b\notin S\); independence of \(S'\) forces \(N(b)\cap(S\setminus\{a\})=\varnothing\). Therefore \(ab\in E(G)\). Conversely every such admissible slide is a jump. Consequently the two exchange rules define exactly the same edge set. Both implementations construct all \(216\) edges and the degree distribution stated in the finding.

For every one of the 146 exchange vertices, run breadth-first search in the finite unweighted exchange graph. Each BFS computes shortest-path distance to every other vertex. In both independently implemented distance calculations every vertex is reached, establishing connectivity. The largest row maximum is twelve and the smallest is eleven. Exactly two rows have maximum twelve; the only unordered pair at distance twelve is \((A,B)\). Checking all pairs of adjacent exchange vertices shows there is no common neighbor, establishing triangle-freeness. All these complete finite distance and incidence checks are reproduced in `mcgee_certificate.json` and verified by `check_mcgee_certificate.py`.

Finally, enumerate every graph automorphism without assuming a precomputed group. An automorphism maps vertex zero to one of 24 vertices and permutes its three neighbors, giving at most 144 initial choices. Recursively extend each partial assignment by trying every as-yet-unassigned image that preserves its distance to *every already assigned vertex*, pruning impossible branches. Every genuine automorphism preserves graph distances and is therefore visited. Every complete distance-preserving permutation is also adjacency-preserving and hence is a graph automorphism. The recursion produces exactly \(32\) distinct permutations. Acting on the 146 minimum sets with these permutations yields seven disjoint orbits of the displayed sizes; the orbit of size two is precisely \(\{A,B\}\). `check_mcgee_certificate.py` separately checks the stored permutations and all orbit assertions against the explicit graph.

## Verification
The package contains `enumerate_mcgee.py`, `verify_mcgee.cpp`, `check_mcgee_certificate.py`, and `mcgee_certificate.json`, together with exact output records `primary_output.txt`, `cxx_output.txt`, and `checker_output.txt`. To reproduce the evidence using Python 3 and a C++17 compiler, in one directory run:

```sh
python3 enumerate_mcgee.py > primary_output.txt
g++ -std=c++17 -O2 -Wall -Wextra verify_mcgee.cpp -o verify_mcgee
./verify_mcgee > cxx_output.txt
python3 check_mcgee_certificate.py > checker_output.txt
```

The executable is built afresh and need not be provided. The Python code uses only the standard library. The independently obtained cardinality, component, eccentricity, degree, diameter-pair, and edge counts agree. The certificate records the exact sorted minimum sets and all exchange edges, rather than relying solely on summary counts. The manifest in its containing archive supplies byte lengths and SHA-256 values for every artifact.

## Relationship to prior work
Independent domination (the minimum size of an inclusion-maximal independent set) and its general cubic-graph bounds are classical. Duckworth and Wormald treat independent domination in random cubic graphs, and Dorbec, Henning, Montassier, and Southey prove general cubic-graph bounds. Their general bounds do not enumerate optimal sets, certify all exchanges, or determine distances in the particular McGee cage. The author-uploaded full text of the latter paper was checked for the graph name and its relevant general statements.

Bonsma, Kamiński, and Wrochna develop independent-set token-reconfiguration methods on claw-free graphs; their Proposition 1 explicitly notes that jumps and slides coincide for *maximum* independent sets. The present optima are *minimum-cardinality maximal* independent sets, in a graph with induced claws, so the claw-free reachability theorems are inapplicable. The elementary one-step jump-to-slide argument above is not claimed as novel; the graph-specific full configuration and distance classification is the retained contribution. Suzuki, Mouawad, and Nishimura study a different dominating-set addition/removal reconfiguration graph.

An existing exact McGee independence-complex calculation establishes its homotopy type and face-size distribution. It therefore agrees with the independent-set face counts here. Its asserted homotopy and face counts do not specify which faces are maximal, how the 146 minimum maximal faces exchange, or the sharp eccentricity and orbit data. This distinction was checked against the full published mathematical statement. Related published calculations for identifying codes and 2-factors of the same cage concern different families of configurations.

## Limitations
This is an exact theorem for the single, specified 24-vertex graph, not a claim about arbitrary cubic graphs or cages of other girths. The finite exhaustive proof makes no infinite-family assertion. Some broader historical literature was available only as abstracts and unindexed equivalent computations remain a bibliographic risk. No independent external scientific audit or publication-priority certification has been performed.

## References
- W. Duckworth and N. C. Wormald, *Minimum independent dominating sets of random cubic graphs*, Random Structures & Algorithms 21 (2002), 147–161, doi:10.1002/rsa.10047 (first online 2002-07-25). https://doi.org/10.1002/rsa.10047
- P. Dorbec, M. A. Henning, M. Montassier, and J. Southey, *Independent Domination in Cubic Graphs*, J. Graph Theory 80 (2015), 329–349, doi:10.1002/jgt.21855 (first online 2015-02-04). https://doi.org/10.1002/jgt.21855
- P. Bonsma, M. Kamiński, and M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1 (2014-03-03), Proposition 1 and Sections 1–3. https://arxiv.org/html/1403.0359v1
- A. Suzuki, A. E. Mouawad, and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714v1 (2014-01-22). https://arxiv.org/html/1401.5714v2
- E. W. Weisstein, *McGee Graph*, MathWorld (LCF graph representation). https://mathworld.wolfram.com/McGeeGraph.html
- *The McGee graph independence complex is a five-sphere*, published mathematical record and proof. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-mcgee-graph-independence-complex-is-a-five-sphere--5daca7995d97
