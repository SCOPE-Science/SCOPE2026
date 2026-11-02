# The complete five-edge bondage spectrum of the truncated-octahedral graph

## Finding

Let \(T\) be the truncated-octahedral graph, whose vertices are the \(24\) permutations of \((0,1,2,3)\), with two permutations adjacent when one is obtained from the other by swapping two consecutive positions. Its \(36\) edges are indexed \(0,\ldots,35\) in lexicographic order of their sorted vertex-index pairs; the vertices themselves are indexed by lexicographic permutation order.

For \(F\subseteq E(T)\), let \(\gamma(T-F)\) denote the ordinary domination number after deleting \(F\). Exactly \(276\) of the \(\binom{36}{5}=376992\) five-edge subsets satisfy \(\gamma(T-F)>\gamma(T)=8\). No edge subset with fewer than five members has this property. Thus the coefficient at the first nonzero level of the edge-deletion vulnerability spectrum is \(276\), and a uniformly chosen five-edge deletion raises the domination number with probability \(23/31416\).

These \(276\) minimum-cardinality bondage sets fall into exactly **eight orbits under the full graph automorphism group**, whose order is \(48\). Their orbit sizes are \(12,24,24,24,48,48,48,48\). A complete, reproducible list of orbit representatives is given below (five edge indices per row):

| Representative \(F\) | Orbit size |
|:--|--:|
| `(0,1,2,3,4)` | 24 |
| `(0,1,2,4,14)` | 48 |
| `(0,1,2,5,6)` | 12 |
| `(0,1,2,5,15)` | 48 |
| `(0,1,2,7,8)` | 48 |
| `(0,1,2,7,23)` | 24 |
| `(0,1,2,9,10)` | 48 |
| `(0,1,2,10,15)` | 24 |

The edge and vertex numbering is completely defined above and independently reconstructed by the two standalone source files.

## Assumptions and scope

Graphs are finite, simple and undirected. A set \(D\) dominates a graph if every vertex lies in \(D\) or has a neighbor in \(D\). An edge subset \(F\) is a bondage set if deleting its edges strictly increases \(\gamma\). All subsets are subsets of the \(36\) individually distinguished edges: no quotient by automorphisms is applied to the count \(276\). Only the orbit classification uses automorphism equivalence.

The permutation description is the standard order-four permutohedron, isomorphic to the truncated-octahedral graph. As an independent identification check, `verify_independent.py` checks an explicit isomorphism with the published LCF representation \([3,-7,7,-3]^{6}\) of the truncated-octahedral graph.

## Proof

**Exact reduction.** Write \(V=V(T)\), \(E=E(T)\), and \(\mathcal M=\{D\subseteq V:|D|=8,\;D\text{ dominates }T\}\). Direct finite enumeration of all \(\binom{24}{7}=346104\) seven-element vertex sets gives zero dominating sets, and enumeration of all \(\binom{24}{8}=735471\) eight-element vertex sets gives precisely \(1767\) dominating sets. Hence \(\gamma(T)=8\) (smaller dominating sets would extend to dominating seven-element sets).

For every \(D\in\mathcal M\) and \(v\in V\setminus D\), define the nonempty set of incident edges
\[
Q(D,v)=\{\{u,v\}\in E : u\in D\}.
\]
For every \(F\subseteq E\), the set \(D\) remains dominating in \(T-F\) if and only if **no** \(v\in V\setminus D\) has \(Q(D,v)\subseteq F\): a selected vertex dominates itself regardless of deletions, and an unselected vertex loses all its selected neighbors exactly when all its edges in \(Q(D,v)\) are deleted. Since edge deletion cannot reduce the domination number, \(\gamma(T-F)>8\) holds if and only if
\[
\forall D\in\mathcal M\quad\exists v\in V\setminus D:\quad Q(D,v)\subseteq F.
\]
This is a necessary-and-sufficient, finite, integer-set containment criterion, not a heuristic approximation. Because \(T\) is cubic, each \(Q(D,v)\) has between one and three elements.

**Complete exhaustive certificate.** The standalone `verify_fast.cpp` enumerates all \(\binom{36}{k}\) deleted-edge sets for \(k=0,1,2,3,4,5\), applies the displayed criterion to every candidate, and obtains no bondage sets in the first five levels and exactly \(276\) at level five. The independent `verify_independent.py` enumerates all size-eight dominating sets with a different cover-union calculation. It constructs, for each possible nonempty \(Q(D,v)\), the exact bitset of minimum dominating sets that it destroys, then exhaustively tests each of the \(376992\) five-edge subsets using unions of these bitsets. The count is again \(276\). Thus the enumeration is exhaustive over the full stated universe.

**Automorphism classification.** Each of the \(24\) permutations of the *values* \((0,1,2,3)\), composed optionally with reversal of all four *positions*, preserves adjacent-position swaps. These yield \(48\) distinct graph automorphisms. The full truncated-octahedral graph has no more graph automorphisms: it is the three-connected planar skeleton of the regular truncated octahedron, whose full combinatorial symmetry group is its octahedral group of order \(48\). The verifiers explicitly generate the \(48\) actions on all \(36\) edges, classify each of the \(276\) qualifying sets under these actions, and obtain exactly the eight orbits and representatives in the table. The orbit sizes sum to \(276\), leaving no unclassified case.

## Verification

Both source files require only an ordinary language compiler/interpreter. Run:

```sh
g++ -std=c++17 -O3 verify_fast.cpp -o verify_fast
./verify_fast
python3 verify_independent.py
```

They regenerate the graph, the finite search universes and the answer from their source definitions; no binary datasets, network access, cached outputs or external packages are needed. The independently written Python verifier checks the correspondence to the standard LCF description. The C++ verifier additionally checks every deletion set of sizes zero through four. The exact output includes `bondage_five_sets=276` and orbit-size multiset `[12,24,24,24,48,48,48,48]`. The finite nature of the theorem makes this exhaustive certificate a proof, rather than an extrapolation from small examples.

## Relationship to prior work

Srivastava (2026, arXiv:2609.02477, first submitted 2026-09-02 UTC) proved \(\gamma(T)=8\) and bondage number \(b(T)=5\), thereby refuting the planar bondage conjecture. The new claim **does not** claim those two numerical invariants as original. It refines the first vulnerable edge-deletion level by determining the complete number and automorphism-orbit spectrum of its minimum witnesses. The available primary abstract describes exhaustive verification of four-edge deletions and an existence witness at five edges; it does not itself report this eight-orbit count. The original full manuscript was not available for direct inspection, which remains an explicit historical-priority limitation. The full graph and the computational criterion are reconstructed independently here.

Other inspected records concerning the truncated-octahedral *independence complex*, a general planar bondage conjecture, and a different 18-vertex cubic counterexample address different objects or invariants and do not furnish this exact five-edge vulnerability spectrum.

## Limitations

The result concerns a single natural finite graph, not arbitrary cubic planar graphs or all permutohedra. It counts minimum-size edge-deletion witnesses, not all edge subsets causing an increase in domination number at larger deletion sizes, nor the resulting domination-number distribution after deletion. Complete access to the 2026 source paper was unavailable, so unrecognized previous enumeration in that manuscript cannot be ruled out by its abstract alone. Self-review is not independent mathematical validation.

## References

1. P. R. Srivastava, *The Truncated Octahedral Graph Has Bondage Number Five*, arXiv:2609.02477v1 (2026-09-02), https://arxiv.org/abs/2609.02477 .
2. J. F. Fink, M. S. Jacobson, L. F. Kinch and J. Roberts, *The Bondage Number of a Graph*, Discrete Mathematics 86 (1990), 47–57. DOI: 10.1016/0012-365X(90)90348-L.
3. E. W. Weisstein, *Bondage Number* and *Planar Bondage Conjecture*, MathWorld, https://mathworld.wolfram.com/BondageNumber.html and https://mathworld.wolfram.com/PlanarBondageConjecture.html .
4. *Truncated octahedron*, standard permutohedron representation and LCF form, https://en.wikipedia.org/wiki/Truncated_octahedron .
