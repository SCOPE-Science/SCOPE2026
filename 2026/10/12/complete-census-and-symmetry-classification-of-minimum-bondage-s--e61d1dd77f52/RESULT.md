# Complete census and symmetry classification of minimum bondage sets in the truncated octahedral graph

## Finding

Let \(T\) be the skeleton of the truncated octahedron, with \(24\) vertices and \(36\) edges. For a finite simple graph \(G\), let \(\gamma(G)\) be its domination number and \(b(G)\) the least size of an edge set \(F\) such that \(\gamma(G-F)>\gamma(G)\). Define
\[
\mathcal B_5(T)=\{F\subseteq E(T): |F|=5,\;\gamma(T-F)>\gamma(T)\}.
\]
**Theorem.** The collection \(\mathcal B_5(T)\) has exactly \(276\) members, and every one satisfies \(\gamma(T-F)=9\). Every member contains the full incident edge set \(\delta_T(v)\) of at least one vertex \(v\). Each vertex occurs as such a center in precisely \(13\) members. Exactly \(36\) members contain two complete vertex stars, and the remaining \(240\) contain exactly one. The full graph automorphism group has order \(48\), and its action on \(\mathcal B_5(T)\) has exactly eight orbits of sizes
\[
12,\;24,\;24,\;24,\;48,\;48,\;48,\;48.
\]
Thus \(|\mathcal B_5(T)|=24\cdot13-36=276\). The fact that \(b(T)=5\), without the census or structural classification, was previously established by Srivastava [1].

## Assumptions and scope

All graphs are finite, simple, and undirected. The vertex labels are \(0,\ldots,23\). The following edge list defines \(T\) and establishes the zero-based edge numbering used in the orbit representatives and the verification code. Each pair records an undirected edge.

```
 0:(0,1)    1:(0,2)    2:(0,3)    3:(1,4)    4:(1,5)    5:(2,6)
 6:(2,7)    7:(3,4)    8:(3,8)    9:(4,9)   10:(5,10)  11:(5,11)
12:(6,11)  13:(6,12)  14:(7,12)  15:(7,13)  16:(8,13)  17:(8,14)
18:(9,15)  19:(9,16)  20:(10,16) 21:(10,17) 22:(11,17) 23:(12,18)
24:(13,19) 25:(14,15) 26:(14,19) 27:(15,20) 28:(16,20) 29:(17,21)
30:(18,21) 31:(18,22) 32:(19,22) 33:(20,23) 34:(21,23) 35:(22,23)
```

The eight orbit representatives below are **sets of edge indices** in this list. The second column is the orbit size.

| Edge-index representative | Orbit size |
| --- | ---: |
| \(\{0,1,2,5,6\}\) | 12 |
| \(\{0,1,2,3,4\}\) | 24 |
| \(\{0,1,2,10,17\}\) | 24 |
| \(\{0,1,2,12,15\}\) | 24 |
| \(\{0,1,2,3,9\}\) | 48 |
| \(\{0,1,2,5,17\}\) | 48 |
| \(\{0,1,2,10,11\}\) | 48 |
| \(\{0,1,2,12,13\}\) | 48 |

## Proof

For an edge deletion set \(F\), form the closed neighborhoods \(N_{T-F}[v]\). A set \(D\subseteq V(T)\) dominates \(T-F\) if and only if
\[
\bigcup_{v\in D}N_{T-F}[v]=V(T).
\]
The supplied `verify_bondage.cpp` encodes each neighborhood and set as an exact 24-bit or 36-bit unsigned integer; bitwise union implements this equivalence without approximation. The underlying graph is cubic, so any five or fewer vertices dominate at most \(20\) vertices. The verifier exhausts the \(\binom{24}{6}+\binom{24}{7}=480700\) candidate six- and seven-sets and finds no dominating set. It exhausts all eight-subsets, yielding exactly \(1767\) dominating eight-sets. Consequently \(\gamma(T)=8\).

Deleting edges cannot create a dominating set. Thus \(\gamma(T-F)>8\) holds precisely when **none** of those \(1767\) sets still dominates \(T-F\). Testing all \(\binom{36}{4}=58905\) four-edge subsets shows that each retains at least five dominating eight-sets. By monotonicity, deleting at most four edges never raises \(\gamma\). Exhausting all \(\binom{36}{5}=376992\) five-edge subsets yields precisely \(276\) for which no dominating eight-set survives. This is exhaustive classification, not an inference from samples.

For each of these \(276\) subsets, the verifier checks all \(24\) incident three-edge stars and finds at least one full star. It counts exactly \(13\) optimal five-edge subsets containing \(\delta_T(v)\) for each of the \(24\) vertices. Exactly \(36\) subsets contain two full stars, and none contains more than two. Each such double-star subset is the union of the incident stars at two adjacent vertices; conversely each of the \(36\) edges gives such a set. Hence the star-incidence count is \(24\cdot13=312\), and subtracting the \(36\) duplicated members leaves \(276\) distinct subsets.

For a concrete local certificate, the thirteen extra edge-index pairs that can be added to \(\delta_T(0)=\{0,1,2\}\) are
\[
\{3,4\},\{3,9\},\{5,6\},\{5,17\},\{6,10\},\{7,8\},\{7,9\},\{10,11\},\{10,17\},\{12,13\},\{12,15\},\{14,15\},\{16,17\}.
\]
The verifier builds all adjacency-preserving vertex bijections using an exhaustive backtracking algorithm. The search visits vertices in breadth-first order and at every step tests every as-yet-unassigned image against all previously assigned adjacency/nonadjacency relations. Every automorphism appears because any automorphism provides one admissible choice at each level; every completed bijection is an automorphism because all pairs have been checked. Exactly \(48\) bijections are found. Applying all of them to the complete \(276\)-member list produces the eight orbits shown above; their sizes sum to \(276\).

Finally, for each of the eight orbit representatives, the verifier finds an explicit dominating nine-set after deletion. The eight witness sets are printed in `verification_output.txt`. Automorphisms transport these witnesses to every member of their respective orbits. Since no member admits an eight-set, \(\gamma(T-F)=9\) for every \(F\in\mathcal B_5(T)\), completing the proof.

## Verification

The standalone C++17 program `verify_bondage.cpp` implements the complete direct closed-neighborhood census, the automorphism backtracking, the orbit partition, and the nine-vertex witnesses. Its actual run output is `verification_output.txt`. The separate `census.cpp` implements the alternative critical-edge-bundle test; it reproduces the count \(276\), and `bondage_sets.txt` is its complete list of all optimal five-edge sets, written as five zero-based edge indices per line. Both programs use exact integers and the same explicitly stated graph, but their domination-survival algorithms differ.

Compile and run from the folder containing the files:

```
c++ -std=c++17 -O3 verify_bondage.cpp -o verify_bondage
./verify_bondage
c++ -std=c++17 -O3 census.cpp -o census
./census > bondage_sets_replayed.txt
```

The first run must print `ALL CHECKS PASSED`, the size-eight domination count \(1767\), the exact four- and five-edge census sizes, \(276\) optimal subsets, \(48\) automorphisms, and eight orbit sizes as stated. The second prints \(276\) five-index lines, matching `bondage_sets.txt` exactly. No third-party libraries or datasets are needed.

## Relationship to prior work

Srivastava [1], first made public on September 2, 2026, proved \(\gamma(T)=8\) and \(b(T)=5\), exhibited **one** five-edge witness, and exhaustively certified the absence of four-edge bondage sets. It also reports the \(1767\) dominating eight-sets. Those facts and the graph specification are treated as prior work here. Neither the published theorem nor its displayed computations give the total number of optimal five-edge deletion sets, the universal full-star property, the thirteen local extensions, their eight symmetry orbits, or the uniform post-deletion domination value. The finite census here is a separate refinement of the fault structure of a published counterexample to the planar bondage conjecture.

## Limitations

This is a complete finite statement about a specific 24-vertex graph; it does not classify bondage sets of other polyhedral graphs or prove a general theorem for planar cubic graphs. The correctness certificate is an exhaustive reproducible computation, not a formal proof-assistant development. Searches and full-text comparison did not identify an equivalent earlier census, but unindexed or independently developed equivalent work could exist. Independent external audit has not been performed.

## References

[1] Prateek R. Srivastava, *The Truncated Octahedral Graph Has Bondage Number Five*, arXiv:2609.02477v1 (first public September 2, 2026), https://arxiv.org/abs/2609.02477 ; full-text HTML https://arxiv.org/html/2609.02477.

[2] J. F. Fink, M. S. Jacobson, L. F. Kinch, and J. Roberts, *The bondage number of a graph*, Discrete Mathematics **86** (1990), 47–57, doi:10.1016/0012-365X(90)90348-L.
