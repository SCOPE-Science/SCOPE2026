# The pentagonal bipyramid is the unique minimal zero-Euler bold-homology graph

## Finding

Let \(G\) range over **all finite simple connected graphs** with at most seven vertices. Let \(D_c(G;t)=\sum_{S}t^{|S|}\), where the sum runs over nonempty connected dominating vertex subsets. Define \(\mathbb H^k(G;\mathbb F_2)\) by the connected-dominating-set cochain model of bold homology: degree \(k\) has a basis indexed by connected dominating \(k\)-subsets and the coboundary adds one previously absent vertex, with coefficients modulo two.

Then the simultaneous conditions
\[
D_c(G;-1)=0,\qquad \mathbb H^*(G;\mathbb F_2)\ne 0
\]
hold **if and only if** \(|V(G)|=7\) and \(G\cong C_5*\overline{K_2}\), the pentagonal bipyramid (two nonadjacent apices joined to every vertex of a five-cycle). Thus seven is the sharp minimum vertex count, and the minimal witness is unique up to graph isomorphism. There are precisely \(252\) labeled witnesses on a fixed set of seven vertices, forming one isomorphism class.

For that graph the groups are \(\mathbb H^2(G;\mathbb Z)\cong\mathbb Z\) and \(\mathbb H^3(G;\mathbb Z)\cong\mathbb Z\), with all other groups zero. **These two groups and the existence of a witness are not claimed as new**: the suspension formula in Caputi–Celoria–Collari's 2023 follow-up already covers them. The contribution here is the exhaustive sharp minimum and uniqueness statement over arbitrary connected graphs.

## Assumptions and scope

Every graph is finite, simple, undirected, and connected. A nonempty subset \(S\subseteq V(G)\) is connected dominating if the induced subgraph \(G[S]\) is connected and \(S\cup N_G(S)=V(G)\). For \(k\ge 1\), let \(C^k(G;R)\) be the free \(R\)-module on connected dominating subsets of cardinality \(k\). Its coboundary is
\[
\delta^k(S)=\sum_{v\notin S}(-1)^{\#\{w\in S:w<v\}}(S\cup\{v\}),
\]
using a fixed vertex order. A connected superset of a connected dominating set remains connected dominating, so this is a cochain complex. Its cohomology is the established connected-domination model of bold homology (not the graph-theoretic domination complex \(D_{n,k}\)). Over \(\mathbb F_2\) the signs disappear.

The classification theorem is a finite, exhaustive statement for \(1\le|V(G)|\le7\), with no assertion about all larger graphs. The exact modular computations prove the lower bound and uniqueness, while a separate simplicial collapse identifies integral homology for the witness.

## Proof

**1. Complete finite classification.** Fix \(n\in\{1,\ldots,7\}\). Index unordered vertex pairs lexicographically, represent an edge set by an integer \(g\in[0,2^{\binom n2})\), and visit every such integer exactly once. Connectivity is tested by iteratively adjoining neighbors from a seed vertex. For each connected graph and each nonempty vertex bitmask \(s\), the verifier tests the two defining conditions for being connected dominating, using an exact integer bitmask traversal. The Boolean array of all such subsets completely determines each cochain differential.

For each \(k\), the matrix of \(\delta^k\) over \(\mathbb F_2\) has its rows indexed by connected dominating \((k+1)\)-subsets, its columns by connected dominating \(k\)-subsets, and an entry one exactly for an inclusion differing by one vertex. Gaussian elimination on exact bit vectors yields its rank \(r_k\). The verified Betti number is
\[
\dim_{\mathbb F_2}\mathbb H^k(G;\mathbb F_2)
=c_k-r_k-r_{k-1},
\]
where \(c_k\) counts degree-\(k\) basis elements and \(r_0=r_n=0\). The Euler value is evaluated independently as \(\sum_k(-1)^k c_k\). These operations enumerate **every labeled graph and every possible connected dominating set** in the asserted range, not a sample.

The complete results are:

| \(n\) | Connected labeled graphs | Graphs with \(D_c(G;-1)=0\) | Among those, graphs with nonzero bold homology |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 |
| 2 | 1 | 0 | 0 |
| 3 | 4 | 3 | 0 |
| 4 | 38 | 34 | 0 |
| 5 | 728 | 660 | 0 |
| 6 | 26,704 | 24,401 | 0 |
| 7 | 1,866,256 | 1,691,767 | 252 |

For **each** of the \(252\) positive labeled candidates, the verifier also tests these graph-theoretic statements: exactly two vertices have degree five; they are nonadjacent and adjacent to all five other vertices; the remaining vertices each have exactly two neighbors among themselves. A simple two-regular graph on five vertices is necessarily \(C_5\), proving every candidate has the claimed graph isomorphism type. Conversely, an explicit witness is verified below. The number of labelings is independently \(7!/|\operatorname{Aut}(C_5*\overline{K_2})|=7!/(10\cdot2)=252\), in agreement with the exhaustive census. Each positive case also has the exact mod-two cohomology dimensions one in degrees two and three and zero elsewhere.

**2. Integral witness and vanishing Euler characteristic.** Write the rim cyclically as \(0,1,2,3,4\), and denote the apices by \(a,b\). Let \(F\) be the upper order ideal of connected dominating subsets, and let \(K\) be its complementary downward-closed simplicial complex. All mixed subsets containing at least one apex and one rim vertex belong to \(F\); neither \(\{a\}\), \(\{b\}\), nor \(\{a,b\}\) does. A rim-only set belongs to \(F\) precisely when it consists of three consecutive rim vertices or at least four rim vertices. Consequently \(K\) is the disjoint union of an edge \(\{a,b\}\) and a complex \(L\) on the rim, with complete one-skeleton and exactly five triangles:
\[
(0,1,3),\ (0,2,3),\ (0,2,4),\ (1,2,4),\ (1,3,4).
\]
These triangles have distinct free perimeter edges \((0,1),(2,3),(0,4),(1,2),(3,4)\), respectively. Collapsing each triangle across its free edge leaves precisely the five diagonals of the pentagon, themselves a five-cycle. Hence \(L\simeq S^1\), while \(K\simeq S^1\sqcup\mathrm{pt}\). Its reduced integral cohomology is \(\mathbb Z\) in dimensions zero and one, and zero otherwise.

The full simplex relative cochain complex \(C^*(\Delta^{6},K;R)\), shifted by one degree, is exactly the connected-domination cochain complex. Because \(\Delta^6\) is contractible, the long exact sequence gives \(\mathbb H^k(G;R)\cong\widetilde H^{k-2}(K;R)\) in the relevant degrees \(k\ge2\); in degree one, a direct check gives zero. Taking \(R=\mathbb Z\) proves the integral groups claimed above.

Finally, mixed connected dominating sets contribute \(((1+t)^2-1)((1+t)^5-1)\), and rim-only connected dominating sets contribute \(5t^3+5t^4+t^5\). Thus
\[
D_c(G;t)=10t^2+30t^3+35t^4+21t^5+7t^6+t^7,
\qquad D_c(G;-1)=0.
\]
This finishes the sharp existence, lower-bound, and uniqueness proof.

## Verification

The self-contained C++17 verifier is embedded at `checks/bold_census.cpp`; it requires only a conforming C++17 compiler. From a directory containing the extracted files, run:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -pedantic checks/bold_census.cpp -o bold_census
./bold_census
```

Its exact observed standard output is preserved in `checks/bold_census_output.txt`. It reports `ALL_GRAPHS_EXHAUSTED connected=1893732 chi_zero=1716865 positive=252`, checks the full mod-two Betti vector of every positive case, and exits nonzero if any candidate fails the claimed pentagonal-bipyramid structure. The relevant codomain of every boundary matrix has at most \(\binom 73=35\) basis elements, so 64-bit exact row vectors suffice. Every graph is represented by an edge bitmask with at most \(21\) bits; no approximate arithmetic or truncated search is used.

The witness collapse supplies an independent mathematical explanation of its cohomology and Euler characteristic. The finite enumeration is a complete exhaustive proof of the finite bound, not an experiment extrapolated to larger orders.

## Relationship to prior work

Caputi, Celoria, and Collari's 2022 work introduces the connected-dominating-set cochain description and the equality \(\chi(\mathbb H)=D_c(-1)\), and asks in Question 5.11 whether zero Euler characteristic can coexist with nonzero bold homology. Their 2023 follow-up, especially Theorem 5.8, gives a **general simplicial-suspension theorem that already entails this pentagonal-bipyramid example and its nonzero groups**. Therefore neither the affirmative answer to Question 5.11 nor the homology groups of this particular suspension are original contributions here.

What those general theorems do **not** establish is that no smaller connected graph works, or that **every** minimal witness is isomorphic to the same graph. The present exhaustive all-graph calculation proves exactly these two extremal statements. Other graph-domination complexes, conventional neighborhood complexes, and matching complexes are different objects; similarly named results for them do not imply this classification.

## Limitations

The vertex bound is exactly seven: nothing is asserted about uniqueness or classification at eight or more vertices. The global classification uses coefficients in \(\mathbb F_2\); the integral homology conclusion applies to the unique minimal witness only. The extremal uniqueness rests on the provided exhaustive finite verifier, with structural recognition of all positive cases, not on a uniform human-only classification by graph families. The literature comparison covers the most directly relevant primary works and indexed records but cannot exclude all unindexed equivalent results. No independent external validation is claimed.

## References

1. L. Caputi, D. Celoria, C. Collari, *Categorifying connected domination via graph überhomology*, arXiv:2201.00721v1 (first public 2022-01-03), especially Sections 4–5 and Question 5.11. https://arxiv.org/abs/2201.00721
2. L. Caputi, D. Celoria, C. Collari, *From the Mayer–Vietoris spectral sequence to überhomology*, arXiv:2304.10134v1 (first public 2023-04-20), especially Section 5 and Theorem 5.8. https://arxiv.org/abs/2304.10134
