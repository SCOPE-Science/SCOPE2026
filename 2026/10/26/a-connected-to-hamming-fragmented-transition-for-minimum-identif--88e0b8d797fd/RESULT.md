# A connected-to-Hamming-fragmented transition for minimum identifying codes of adjacent Kneser graphs

## Finding
For \(n\in\{8,9\}\), define the Kneser graph \(K(n,2)\) with vertex set \(\binom{[n]}2\), where two vertices are adjacent exactly when the corresponding pairs are disjoint. An *identifying code* \(C\) is a vertex subset for which all intersections \(C\cap N[v]\) with closed vertex neighborhoods are nonempty and pairwise different. Write \(\mathcal X_n\) for the graph whose vertices are minimum identifying codes of \(K(n,2)\), with edges between codes differing by exactly one selected vertex.

Both graphs have minimum identifying-code size six. Nevertheless:

* \(\mathcal X_8\) is connected with exactly \(141120\) vertices and \(4730880\) edges. Its exact degree distribution is \(56:3360\), \(58:10080\), \(64:20160\), \(66:67200\), \(72:10080\), \(74:30240\), where each entry is degree: multiplicity.
* \(\mathcal X_9\) has \(7560\) vertices and \(22680\) edges, and is isomorphic to a disjoint union of \(280\) copies of the Cartesian graph product \(K_3\square K_3\square K_3\). Every minimum code corresponds to a spanning \(3P_3\) (three vertex-disjoint three-point paths) in the complete graph on nine labeled points, with the six path edges serving as code vertices.

This is a finite, exact comparison of the complete optimum-configuration spaces for two neighboring Kneser graphs of the same code size, not a statement about general \(n\).

## Assumptions and scope
All graphs are finite, simple, undirected. The identifying-code neighborhoods are **closed**, so \(N[v]\) includes \(v\). A codeword is an unordered pair of ground elements. An exchange removes exactly one codeword and adds one formerly absent codeword; no intermediate nonoptimal code is admitted. The assertion concerns \(n=8\) and \(n=9\) only. Vertex labels are \(0,1,\ldots,n-1\); the enumeration treats all labeled configurations separately.

## Proof
**Finite exhaustive part.** The companion `verify.cpp` is a finite constructive certificate for the following facts. It enumerates all \(k\)-subsets of the \(\binom n2\) Kneser vertices, for each integer \(1\le k\le6\), in strictly increasing bitmask order. For each candidate \(C\), it constructs every signature \(N[v]\cap C\) directly from disjointness of the two underlying pairs and checks that all signatures are nonempty and distinct. For each \(k<6\), no code passes. At \(k=6\), exactly \(141120\) and \(7560\) pass for \(n=8\) and \(n=9\), respectively. Thus both minima equal six, independently of existing numerical theorems.

The same program forms the entire exchange graph by replacing each of six selected vertices with each unselected vertex, testing membership against the entire exhaustively enumerated optimum set. A breadth-first search over that exact finite adjacency list proves that \(\mathcal X_8\) is connected, counts its \(4730880\) edges, and obtains the stated degree multiplicities. For \(n=9\) the same procedure yields \(280\) connected components, each of size \(27\), each degree six, and exactly \(22680\) exchange edges. These computations are exhaustive (not sampled), use integer operations only, and their precise reproducibility instructions appear below.

**Structural identification for \(n=9\).** Independently of finding optimum codes by brute-force search, `verify.cpp` enumerates all partitions of \([9]\) into three unordered triples and all choices of center in each triple. For each triple, include the two edges from its chosen center to the other two points. These six edges define a spanning disjoint union of three paths \(P_3\). There are exactly \(9!/((3!)^3 3!)=280\) partitions, with \(3^3=27\) center choices each; the code constructs \(7560\) distinct six-edge sets, directly verifies that each is an identifying code, and checks that **every** one of the \(7560\) independently enumerated minimum codes belongs to this family. This proves the full minimum-set characterization, using exhaustive finite verification without assuming an unproved classification theorem.

To characterize exchanges, remove one edge from any such spanning \(3P_3\): two complete three-vertex paths remain, together with one edge of the third path and an isolated vertex in its three-point block. If adding one edge produces another spanning \(3P_3\), the two complete components cannot change (they already account for six vertices), and the remaining edge must be joined to the isolated third vertex. Thus the partition into triples is unchanged; only one path center changes. Conversely, each different choice of center in that triple is achieved by exchanging exactly one path edge, giving a triangle \(K_3\) on its three center choices. Three independent blocks give \(K_3\square K_3\square K_3\). Distinct partitions cannot be connected by an exchange, hence \(280\) such components. Each component has \(27\) vertices of degree \(6\), hence \(27\cdot6/2=81\) edges, for \(280\cdot81=22680\) edges total.

## Verification
Compile on any C++17 compiler with `c++ -O2 -std=c++17 verify.cpp -o verify` and run `./verify`. The code exits with a nonzero status if any enumerated structural or numeric assertion fails. Its terminal output is:

```text
LOWER_BOUND_OK n=8
LOWER_BOUND_OK n=9
K8_OK codes=141120 edges=4730880 components=1
K9_OK codes=7560 edges=22680 components=280 Hamming_factors=K3xK3xK3
ALL_VERIFY_OK
```

The enumeration loops through every relevant subset, not just representative subsets or a sample. The finite nature of the two cases, the bitmask upper limits, and the explicit adjacency and signature rules make the check independently replayable. The purely combinatorial edge-swap argument separately identifies the components as ternary Cartesian cubes.

## Relationship to prior work
Foucaud, Gravier, Naserasr, Parreau and Valicov study identifying codes in **line graphs**; note that \(K(n,2)\) is the complement of the line graph of \(K_n\), so those code characterizations do not transfer directly. Roozbayani and Maimani's paper concerns precisely identifying codes in Kneser graphs and establishes the **numerical** minimum-size formula covering both orders here. Those scalar minimum values are prior work, not claimed as a new general discovery. The added conclusions here are an exact census, degree spectrum and connectivity for \(K(8,2)\), plus the full minimum-code configuration space and its \(280\) ternary-Hamming-component exchange geometry for \(K(9,2)\). The identified earlier abstracts and available primary passages did not establish this *combined* exchange classification, but the full Roozbayani–Maimani article could not be inspected; it therefore remains a substantive originality risk.

## Limitations
The result is restricted to the two stated finite graphs. The enumeration is an exhaustive proof for those sizes only, not evidence for a general pattern. Full-text access to the most directly relevant numerical Kneser-code paper was unavailable, so equivalent earlier structural characterizations cannot be excluded. A literature search is not a priority certificate, and no independent external audit is claimed.

## References
1. F. Foucaud, S. Gravier, R. Naserasr, A. Parreau, P. Valicov, *Identifying codes in line graphs*, arXiv:1107.0207 (first public version 2011-07-01), https://arxiv.org/abs/1107.0207 .
2. M. Roozbayani and H. R. Maimani, *Identifying codes and watching systems in Kneser graphs*, *Discrete Mathematics, Algorithms and Applications* 9 (2017), article 1750007, https://doi.org/10.1142/S1793830917500070 (first published online 2016-12-16).
