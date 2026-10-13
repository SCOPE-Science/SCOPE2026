# All 32,460 metric bases of Tutte's eight-cage in 34 symmetry classes

## Finding

Let \(H\) be the Tutte–Coxeter graph, realized as the incidence graph between the \(15\) edges of the complete graph \(K_6\) and its \(15\) perfect matchings (one-factors). A resolving set is a vertex subset \(S\) for which the distance vectors \((d(v,s):s\in S)\) are different for all distinct vertices \(v\) of \(H\). A *metric basis* is a resolving set of least cardinality.

The graph \(H\) has metric dimension \(6\), and it has **exactly \(32{,}460\) metric bases**. Under the complete automorphism group \(\operatorname{Aut}(H)\) of order \(1{,}440\), the metric bases form exactly \(34\) orbits, with orbit-size distribution
\[
1\cdot180+1\cdot240+1\cdot360+18\cdot720+13\cdot1440=32{,}460.
\]
Here the metric dimension \(6\) was previously established by Bailey; the complete census, bipartition profile, and automorphism-orbit classification are the results recorded here.

Every metric basis contains either \(2\), \(3\), or \(4\) one-factor vertices, with multiplicities \(7{,}470\), \(17{,}520\), and \(7{,}470\), respectively. The joint distribution by number \(a\) of one-factor vertices and the number \(b\) of edges induced by the chosen vertices is
\[
\begin{array}{c|rrr}
a\backslash b&0&1&2\\\hline
2&4230&2880&360\\
3&3840&7920&5760\\
4&4230&2880&360
\end{array}.
\]
All other pairs \((a,b)\) have zero count. The attached `orbits.csv` contains an explicit representative and the stabilizer order for all \(34\) orbits.

## Assumptions and scope

All graphs here are finite, simple, and unweighted. Let the six underlying symbols be \(0,1,2,3,4,5\). Enumerate the edges of \(K_6\) in lexicographic order as \(e_0,\ldots,e_{14}\); enumerate its one-factors lexicographically by their sorted triples of edge indices as \(F_0,\ldots,F_{14}\). Graph vertices \(0,\ldots,14\) represent one-factors; vertices \(15,\ldots,29\) represent edges \(e_0,\ldots,e_{14}\). Adjacency is exactly membership \(e_j\in F_i\). This graph has \(30\) vertices and \(45\) edges. In `orbits.csv`, a vertex subset is encoded as the integer \(\sum_{v\in S}2^v\), and all representative vertex lists use the indexing just given.

## Proof

**Distance lemma.** For distinct edges \(e,f\) of \(K_6\), the corresponding vertices have graph distance \(2\) when \(e\cap f=\varnothing\), and distance \(4\) otherwise. For distinct one-factors \(F,G\), the corresponding vertices have distance \(2\) when \(F\cap G\ne\varnothing\) as sets of edges, and distance \(4\) otherwise. An edge vertex \(e\) and one-factor vertex \(F\) have distance \(1\) when \(e\in F\), and distance \(3\) otherwise. All these claims follow from incidence: two disjoint \(K_6\) edges extend to a common one-factor; two intersecting edges cannot belong to the same one-factor. Distinct one-factors share at most one edge, and when they share none, they can be joined through alternating edge and one-factor vertices in four steps. Every edge lies in exactly three one-factors. A disjoint edge of a given \(F\) lies in some one-factor sharing an edge with \(F\), giving an incidence path of length three. Bipartition parity excludes shorter paths in the remaining cases. Alternatively, `verify.py` reconstructs all \(900\) pairwise distances independently by breadth-first search and checks the formulas entrywise.

**Resolving criterion.** For distinct vertices \(u,v\) from the same bipartition class, define the *distinguishing set* \(\Delta(u,v)=\{w\in V(H):d(w,u)\ne d(w,v)\}\). A subset \(S\) resolves \(H\) if and only if it meets every \(\Delta(u,v)\). If \(u,v\) belong to opposite bipartition classes, their distances to any fixed vertex always have opposite parity; thus *every nonempty landmark set* distinguishes them. There are exactly \(2\binom{15}{2}=210\) same-side pairs; the accompanying program constructs their distinguishing masks using the distance lemma and verifies they are distinct. Consequently it suffices to hit precisely those \(210\) masks.

**Minimum and multiplicities.** Every resolving set of size at most \(5\) extends to a resolving set of size \(5\) (monotonicity), and the exact computation checks all \(\binom{30}{5}=142{,}506\) five-subsets against the \(210\) distinguishing masks: none meets all of them. It then checks all \(\binom{30}{6}=593{,}775\) six-subsets, finding exactly \(32{,}460\) that do. Thus the metric dimension is \(6\), and these \(32{,}460\) sets are exactly all metric bases. In the same complete pass, for each set the program calculates its number of one-factor vertices and its number of induced graph edges, yielding the stated joint distribution. No sample-based inference is used.

**Full automorphism group.** Every permutation of the six symbols acts on edges and on one-factors and hence gives a side-preserving automorphism, yielding \(720\) distinct automorphisms. The explicit side-swapping permutation in `verify.py` is checked against every incidence; its composition with the \(720\) permutations gives \(720\) additional, distinct automorphisms. To see these \(1{,}440\) constitute the full group, observe that every automorphism of a connected bipartite graph either preserves or exchanges its two sides. A side-preserving automorphism must preserve graph distance two on the edge-vertices, which is disjointness of the corresponding \(K_6\) edges. The complement of this disjointness graph is the line graph \(L(K_6)\). Its six maximal cliques of size five are exactly the stars through the six symbols, so every automorphism of \(L(K_6)\) arises from a permutation of these symbols. The images of all one-factor vertices are then uniquely determined by their three edge-neighbors. Thus there are at most \(720\) side-preserving automorphisms, and composing with a verified side swap bounds the full group by \(1{,}440\).

**Orbit census.** The program applies all \(1{,}440\) automorphisms to the least unassigned metric-basis bitmask, collects its orbit, and removes that orbit. It repeats until all \(32{,}460\) bases are assigned. It checks that every generated orbit consists entirely of previously unassigned bases and that the complete orbit-size distribution is \(180,240,360,\underbrace{720,\ldots,720}_{18},\underbrace{1440,\ldots,1440}_{13}\). The exact representatives, their induced-edge statistics and orbit stabilizers are provided in `orbits.csv`.

## Verification

The standard-library `verify.py` rederives the graph and distances, checks the full finite candidate universe at sizes five and six, checks the indicated \(S_6\) action and side-switching permutation against every graph edge, and partitions every optimum into the claimed \(34\) orbits. Independently, `verify_independent.cpp` constructs the same graph and breadth-first-search distance matrix using separate code, then enumerates all \(142{,}506+593{,}775\) candidate subsets and decides resolvability by direct distance-vector uniqueness, confirming the same \(32{,}460\) count and all nine joint-profile coefficients. Both verifiers contain exact assertions; source and representative list accompany this result.

Run from a directory containing the files: `python3 verify.py`; `c++ -O3 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`. The C++ binary is compiled locally and not distributed. Verification uses integer operations only and requires no external datasets or Python packages.

## Relationship to prior work

Bailey [1] determined the metric dimension \(6\) of the Tutte eight-cage in a published small distance-regular-graph census. Bailey [2] further analyzes metric dimension in imprimitive distance-regular graphs and cites that value. The later investigation [3] treats incidence-graph metric dimension in generalized quadrangles, deriving bounds for larger classes. These scalar or family-level results do not imply the number or the \(34\) symmetry types of optimum resolving sets established here. No theorem about their absence from all external literature is claimed.

## Limitations

The result concerns only the canonical thirty-vertex Tutte–Coxeter graph and ordinary vertex-distance resolving sets. It does not classify bases of larger generalized quadrangles or other cubic cages. The exact finite counts and orbit representatives depend on the fully specified vertex indexing above; their verification is by exhaustive finite computation, supplemented by the elementary distance and group structure proofs. An earlier unindexed equivalent enumeration is a residual publication-priority risk. No independent mathematical audit has yet been conducted.

## References

[1] Robert F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973v1, public 17 December 2013, https://arxiv.org/abs/1312.4973.

[2] Robert F. Bailey, *On the metric dimension of imprimitive distance-regular graphs*, arXiv:1312.4971, first public 17 December 2013, https://arxiv.org/abs/1312.4971.

[3] Daniele Bartoli, Tamás Héger, György Kiss and Marcella Takáts, *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, arXiv:1706.06583v1, first public 20 June 2017, https://arxiv.org/abs/1706.06583.
