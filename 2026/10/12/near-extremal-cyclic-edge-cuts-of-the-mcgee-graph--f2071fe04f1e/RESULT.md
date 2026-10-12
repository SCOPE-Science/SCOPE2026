# Near-extremal cyclic edge cuts of the McGee graph

## Finding

Let \(G\) be the 24-vertex cubic McGee graph (the unique \((3,7)\)-cage). A **cycle-separating edge cut** is a cut \(\delta(S)\) such that both \(G[S]\) and \(G[V(G)\setminus S]\) contain a cycle. Identify \(S\) and its complement, so each cut is counted once.

**Theorem.** Exactly \(362\) cycle-separating edge cuts of size \(8\) exist in \(G\). Each divides the graph into exactly two connected cyclic components. They have the following exhaustive profile, classified by their component of at most twelve vertices:

| Smaller cyclic component | Count | Automorphism orbits |
| --- | ---: | ---: |
| An induced \(8\)-cycle | 34 | 4 |
| A \(7\)-cycle with one pendant vertex | 224 | 8 |
| A theta graph whose three internally disjoint paths have lengths \(3,4,4\) | 80 | 5 |
| Two twelve-vertex subdivisions of \(K_4\) | 24 | 4 |
| **Total** | **362** | **21** |

In the balanced last case, write \(A\) for the subdivision of \(K_4\) obtained by replacing the edges of a \(4\)-cycle by paths of length \(3\) and leaving its complementary matching at length \(1\). Write \(B\) for the subdivision obtained by giving that \(4\)-cycle length \(2\) per edge and its complementary matching length \(3\) per edge. The \(24\) balanced cuts have component-type pairs \(AA,AB,BB\) in exact multiplicities \(6,16,2\), respectively. The four balanced symmetry orbits have sizes \(2,4,16,2\), with \(AA\) forming the first two orbits, \(AB\) the third, and \(BB\) the fourth.

The full automorphism group of \(G\) has order \(32\). Its \(21\) orbits on these eight-edge cuts are listed, with representatives and stabilizer sizes, in `cut_orbits.csv`. The full list of \(362\) cuts is contained in `cut_masks.csv`. The graph also has \(32\) cycle-separating seven-edge cuts, all isolating a shortest \(7\)-cycle; that minimum-cut structural statement is previously covered by the cage connectivity theorem cited below and is not claimed as the new contribution.

## Assumptions and scope

The vertices are \(\mathbb Z/24\mathbb Z\). The edge set is defined by the undirected cycle edges \(\{i,i+1\}\) and LCF chords \(\{i,i+s_i\}\), with indices modulo \(24\) and \(s_{3j}=-12\), \(s_{3j+1}=7\), \(s_{3j+2}=-7\). Duplicate undirected chords are counted once. This is the standard representation with LCF notation `[-12,7,-7]^8`, and yields \(24\) vertices, \(36\) edges, regular degree \(3\), and girth \(7\).

Cuts are **unordered**: \(S\) and \(V(G)\setminus S\) represent the same cut. A cycle-separating cut is counted only when both induced sides contain a cycle. Every candidate accepted in the theorem also has both sides connected, so these are bonds and removing the indicated edges produces exactly two components. No statement is made about cuts with more than eight edges or graphs other than this specified \(G\).

## Proof

For any vertex set \(S\), cubic regularity gives the exact boundary identity
\[
|\delta(S)|=3|S|-2|E(G[S])|.
\]
Choose one representative of every unordered nontrivial partition by demanding \(0\in S\). There are exactly \(2^{23}-1=8{,}388{,}607\) such partitions. For each of them, compute the boundary by scanning the \(36\) undirected edges; for candidates of boundary size at most \(8\), compute connected components of each induced side by graph search. In a connected component having \(v\) vertices and \(e\) edges, a cycle exists if and only if \(e\geq v\). Hence this is an exact decision procedure for *every* candidate cut and makes no statistical inference.

The fully specified enumerator `verify_cuts.cpp` executes that exhaustive test and reproduces the complete mask list in `cut_masks.csv`. It yields \(32\) seven-edge and \(362\) eight-edge cycle-separating cuts, and no cuts of smaller size. In each case the two induced sides are individually connected. For an eight-edge cut, the smaller side must have \(8\), \(10\), or \(12\) vertices: the girth bound gives at least \(7\) vertices on a cyclic side, the smaller side has at most \(12\), and the boundary identity forces its cardinality to be even.

The same exhaustive scan verifies the degree and edge profiles of all small sides. At size \(8\), there are \(8\) induced edges and the side is unicyclic; girth \(7\) makes it an induced \(8\)-cycle or a \(7\)-cycle with one pendant vertex. At size \(10\), there are \(11\) induced edges; all eight other vertices have internal degree \(2\) and precisely two have degree \(3\). Suppressing the degree-two paths gives three parallel connections between the branch vertices, of lengths \(3,4,4\). At size \(12\), there are \(14\) induced edges and four degree-three branch vertices; suppressing the eight degree-two vertices gives a simple \(K_4\) with six weighted edges. The only observed length patterns, verified on every balanced mask in `verify_orbits.py`, are the \(A\) and \(B\) subdivisions defined above. Both sides are checked, yielding the \(AA/AB/BB\) counts.

The enumerated type totals are \(34+224+80+24=362\). Independently, simple-cycle enumeration gives exactly \(32\) seven-cycles and \(34\) eight-cycles. Each seven-cycle has seven distinct external neighbors, since any shared external neighbor would create a cycle of length at most \(5\). Extending it by one such neighbor therefore constructs \(32\cdot7=224\) distinct cycle-with-pendant subgraphs, corroborating the large unicyclic class.

For the symmetry claim, `verify_orbits.py` reconstructs all graph automorphisms as adjacency-preserving vertex permutations; there are exactly \(32\). It applies each permutation to every certified cut mask, normalizes under complementation, and partitions the \(362\) eight-edge masks into \(21\) pairwise-disjoint complete orbits. Their type-by-type numbers are \(4,8,5,4\) and their sizes sum to \(362\). The executable compares the resulting orbit representatives, stabilizers, and types to `cut_orbits.csv`. The same procedure gives two orbits of size \(16\) for the \(32\) previously known seven-edge cuts.

Finally, `verify_independent.cpp` checks all \(2^{24}\) vertex masks using the independent recurrence \(|\delta(S\cup\{v\})|=|\delta(S)|+3-2|N(v)\cap S|\) and disjoint-set component-cycle detection. It reconstructs the *same complete set of canonical cut masks*, not merely the same counts. Agreement of the independently calculated sets confirms all case exhaustiveness claims used above.

## Verification

Requirements: a C++17 compiler and Python 3.10+ with NetworkX 3.x. From a directory containing the embedded files, execute:

```sh
g++ -O3 -std=c++17 verify_cuts.cpp -o verify_cuts
./verify_cuts
g++ -O3 -std=c++17 verify_independent.cpp -o verify_independent
./verify_independent
python3 verify_orbits.py
```

The first program regenerates `cut_masks.csv`; the second tests exact mask equality by an independent enumeration; the third checks all cut shapes, the two cycle counts, the automorphism group, and all orbit-certificate rows. The results are deterministic and use exact integer operations; no random sampling, floating-point thresholds, solver timeouts, or unexamined computational certificates are involved. The two CSVs are supplied in full.

## Relationship to prior work

The McGee graph and its standard LCF form are classical; the girth, regularity, and full automorphism-group order are not new. Dvořák, Kára, Kráľ, and Pangrác (2004) developed general algorithms for cyclic edge connectivity; Steffen (public arXiv version dated 2006-07-04) studied its role in nowhere-zero flows. More recently, Lukoťka, Máčajová, and Rajník (2025), Theorem 11, established for cubic cages up to girth \(15\) both maximal cyclic edge connectivity and the fact that every minimum cycle-separating cut isolates a shortest cycle. Their result entails the seven-edge **structure** quoted here, but neither their statements nor the inspected supporting table give the complete enumeration of eight-edge cuts, their component geometries, or their automorphism orbits.

The claimed new information is precisely the next boundary layer (size eight), not the known minimum size. Exact searches for McGee cut profiles, eight-edge cyclic bonds, cycle-separating subsets, weighted-\(K_4\) components, and possible equivalences to general cage-connectivity theorems did not reveal a stronger covering census. The separately studied cyclic *vertex* connectivity of the McGee graph is eight (the 2020 paper cited below); it removes vertices and does not enumerate edge cuts, so it is not an equivalent result. Search failure is not itself a proof of priority, and earlier unindexed tables or computations may exist.

## Limitations

This is an exact finite result about one named graph. The proof relies on full exhaustive enumeration backed by two independent procedures and complete input/output certificates, not on a general structure theorem valid for all cages. The fact that the first eight-edge-cut layer has the stated geometry should not be extrapolated to other regular graphs. The independently checked computational equality is a finite proof step, not independent human mathematical review. Earlier uncatalogued enumerations remain a priority risk.

## References

1. W. F. McGee, original construction of the \((3,7)\)-cage (1960); convenient representation and classical invariants recorded in Eric Weisstein, *McGee Graph*, MathWorld, https://mathworld.wolfram.com/McGeeGraph.html.
2. Z. Dvořák, J. Kára, D. Kráľ, O. Pangrác, *An Algorithm for Cyclic Edge Connectivity of Cubic Graphs*, SWAT 2004, pp. 236–247, DOI 10.1007/978-3-540-27810-8_21.
3. E. Steffen, *Tutte's 5-Flow Conjecture for Highly Cyclically Connected Cubic Graphs*, first public arXiv version 2006-07-04, https://arxiv.org/abs/math/0607077.
4. R. Lukoťka, E. Máčajová, J. Rajník, *Cages and cyclic connectivity*, Theorem 11, first public arXiv version 2025-03-10, https://arxiv.org/abs/2503.07400.
5. *The cubic graphs with finite cyclic vertex connectivity larger than girth*, Discrete Mathematics (2020), DOI 10.1016/j.disc.2020.112197; its invariant is vertex, not edge, connectivity.
