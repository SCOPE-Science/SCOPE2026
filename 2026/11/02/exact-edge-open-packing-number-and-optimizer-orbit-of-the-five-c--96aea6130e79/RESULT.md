# Exact edge-open-packing number and optimizer orbit of the five-cube

## Finding

Let \(Q_5\) be the graph on the binary words \(\{0,1\}^5\), with two words adjacent precisely when their Hamming distance is one. An **edge-open-packing** is a set \(P\) of edges such that no two distinct edges of \(P\) admit a third, different graph edge joining an endpoint of one to an endpoint of the other. Then

\[
\rho_e^o(Q_5)=12.
\]

Exactly \(80\) distinct labeled edge-open-packings attain cardinality \(12\). All of them form a single orbit under the automorphism group of \(Q_5\). Each is an induced disjoint union of four copies of \(K_{1,3}\), whose four centers lie in one parity class of the cube. Exactly \(40\) of the optimal sets have even-weight centers and \(40\) have odd-weight centers.

More explicitly, every optimum is uniquely determined by its center set

\[
C=\{x,x\oplus a,x\oplus b,x\oplus a\oplus b\},
\qquad
\operatorname{wt}(a)=2,\quad
\operatorname{wt}(b)=4,\quad
\operatorname{wt}(a\mathbin{\&}b)=1,
\]

where \(x,a,b\in\{0,1\}^5\), \(\oplus\) is coordinatewise XOR, \(\operatorname{wt}\) counts one-bits, and \(\&\) is coordinatewise AND. For each \(c\in C\), include precisely the edges from \(c\) to those of its neighbors not adjacent to any other center in \(C\). Different parameter triples can describe the same set.

## Assumptions and scope

All graphs are finite, simple, and undirected. Cube vertices are identified with the integers \(0,\ldots,31\) through binary expansion; an edge is an unordered pair at Hamming distance one. Distinct edge sets, not colorings or ordered tuples, are counted. The assertions concern \(Q_5\) alone, and do not assert a formula for dimensions greater than five.

For an arbitrary graph \(G\), the edge-open-packing number \(\rho_e^o(G)\) is the largest size of an edge-open-packing. In a hypercube, such a set induces disjoint stars on its incident vertices.

## Proof

**1. Lower bound and structural construction.** Fix \(x,a,b\) with the displayed weight conditions. The four members of \(C\) are distinct, have one common parity, and have mutual Hamming-distance multiset \(\{2,2,4,4,4,4\}\). Each center has exactly one other center at distance two and the remaining two at distance four. Two cube vertices at distance two have exactly two common neighbors; two at distance four have none. Consequently, each center has precisely three neighbors adjacent to no other center in \(C\). Select its three incident edges to those private neighbors. No selected leaf is adjacent to another selected center, no two centers are adjacent, and no two leaves are adjacent. Therefore the selected edges induce four disjoint three-edge stars. They constitute a legal edge-open-packing of cardinality \(12\).

For example, in integer notation, take \(C=\{0,3,29,30\}\); its selected edges are

\[
\begin{aligned}
&(0,4),(0,8),(0,16),\\
&(3,7),(3,11),(3,19),\\
&(29,25),(29,21),(29,13),\\
&(30,26),(30,22),(30,14).
\end{aligned}
\]

**2. Complete finite upper-bound certificate.** Form the compatibility graph \(H\) with one vertex for each of the \(80\) cube edges. Two vertices of \(H\) are adjacent exactly when their respective cube edges admit no third cube edge joining their endpoint sets. Then an edge-open-packing of size \(k\) in \(Q_5\) is exactly a \(k\)-clique of \(H\). The graph has \(1120\) conflicting unordered edge pairs.

The accompanying standalone \(\texttt{verify.cpp}\) builds \(H\) directly from the cube adjacency rule and performs exhaustive, duplicate-free clique enumeration. At a search node it keeps a candidate set \(P\) of vertices greater than every previously chosen index. It branches on the least candidate \(v\), and recurses only on larger candidates adjacent to \(v\). Thus every clique of each prescribed size appears once. Its only nontrivial pruning step greedily partitions the candidate-induced compatibility graph into independent color classes. Any clique meets each color class at most once, so a branch with fewer classes than the number of still-needed vertices cannot contain a target clique. This is an exact upper bound, not a heuristic or sampling argument.

The exhaustive search finds **no** clique of size \(13\). A larger clique would contain one of size \(13\). Hence all edge-open-packings have at most \(12\) edges, and the construction in step 1 attains the maximum.

**3. Exhaustive optimizer comparison and symbolic census.** The same search enumerates exactly \(80\) distinct \(12\)-cliques. Each induces four three-edge stars with centers in one parity class, and each center set has distance multiset \(\{2,2,4,4,4,4\}\). The program separately generates all edge sets from the four-center formula in step 1, and checks equality of the two full collections, rather than merely comparing their sizes. This proves the asserted complete optimizer classification.

For an independent symbolic count, choose \(x\) in \(32\) ways, the weight-two mask \(a\) in \(\binom52=10\) ways, and the weight-four mask \(b\) meeting the support of \(a\) once in exactly \(2\) ways. Every resulting four-center set is represented by exactly \(8\) triples: four choices of \(x\) and two choices of the opposite member \(x\oplus b\) of the other distance-two pair. Hence there are \(32\cdot10\cdot2/8=80\) center sets. An even-weight translation preserves center parity, so the two classes each contain \(40\). A coordinate permutation takes any pair of masks with weight pattern \((2,4,1)\) to any other, and XOR translation takes one \(x\) to another; thus the \(80\) optimizers form one cube-automorphism orbit.

## Verification

Compile the supplied self-contained \(\texttt{verify.cpp}\) with a standard C++17 compiler and run it:

```text
g++ -std=c++17 -O2 -Wall -Wextra -Werror verify.cpp -o verify
./verify
```

A successful execution prints \(\texttt{VERIFY_OK}\), together with \(80\) size-twelve cliques, zero size-thirteen cliques, and a \(40+40\) center-parity split. The program also checks the exact equality between the exhaustive optimizer list and the independently generated geometric family. The search, its completeness argument, the explicit witness and the symbolic count together constitute the finite proof; timing or a solver status alone would not do so.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan introduced edge-open-packing and its common-edge convention in 2022. Brešar, Dravec, Hedžet and Samadi studied the parameter on graph products, including hypercubes, in their June 2024 preprint. Their Section 5.1 gives the lower bound \(\rho_e^o(Q_5)\ge10\) in Table 1 and proves exactness for dimensions that are powers of two (Theorem 5.10); it does not give the equality, exact optimizer count or optimizer orbit for dimension five. Brešar and Samadi's March 2024 paper addresses computational complexity, trees, and general extremal bounds, not this dimension-specific count. The present result closes that natural next finite hypercube case. Related material on injective edge colorings provides a partition interpretation of edge-open-packings, but does not imply this upper bound or this census.

## Limitations

The upper bound and complete classification are computer-assisted **finite** assertions about the \(32\)-vertex graph \(Q_5\); no unproved extrapolation to other dimensions is made. The code must be compiled and executed for a reproducibility check. Novelty assessment is limited to the identified sources and mathematical-record searches; equivalent results under other terminology remain possible.

## References

1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776, DOI: 10.1051/ro/2022171, https://www.numdam.org/articles/10.1051/ro/2022171/.
2. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first version 2024-06-06), https://arxiv.org/abs/2406.04020. See Section 5.1, Table 1, and Theorem 5.10.
3. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (2024-03-01), https://arxiv.org/abs/2403.00750.
